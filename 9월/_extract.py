import os, sys, json
from docx import Document
from docx.oxml.ns import qn

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SRC, "_out")
os.makedirs(OUT, exist_ok=True)


def rels_map(doc):
    m = {}
    try:
        for rid, rel in doc.part.rels.items():
            if rel.reltype.endswith("/hyperlink"):
                m[rid] = rel.target_ref
    except Exception:
        pass
    return m


def para_text(p, doc, hmap, imgs, name):
    el = p._p
    parts = []
    for child in el.iter():
        tag = child.tag
        if tag == qn('w:t'):
            parts.append(child.text or "")
        elif tag == qn('w:tab'):
            parts.append("\t")
        elif tag == qn('w:br'):
            parts.append("\n")
        elif tag == qn('a:blip'):
            rid = child.get(qn('r:embed'))
            if rid:
                try:
                    part = doc.part.related_parts[rid]
                    ext = os.path.splitext(part.partname)[1] or ".png"
                    fn = f"{name}_img{len(imgs):02d}{ext}"
                    with open(os.path.join(OUT, fn), "wb") as f:
                        f.write(part.blob)
                    imgs.append(fn)
                    parts.append(f"[[IMAGE:{fn}]]")
                except Exception as e:
                    parts.append(f"[[IMAGE_ERR:{rid}:{e}]]")
    txt = "".join(parts)
    # hyperlinks
    links = []
    for h in el.findall(qn('w:hyperlink')):
        rid = h.get(qn('r:id'))
        t = "".join(n.text or "" for n in h.iter(qn('w:t')))
        if rid and rid in hmap:
            links.append(f"{t} -> {hmap[rid]}")
    style = p.style.name if p.style is not None else ""
    return txt, style, links


def dump(path):
    name = os.path.splitext(os.path.basename(path))[0]
    safe = "".join(c if c.isalnum() else "_" for c in name)[:30]
    doc = Document(path)
    hmap = rels_map(doc)
    imgs = []
    lines = [f"===== FILE: {os.path.basename(path)} ====="]
    body = doc.element.body
    from docx.text.paragraph import Paragraph
    from docx.table import Table
    for child in body.iterchildren():
        if child.tag == qn('w:p'):
            p = Paragraph(child, doc)
            txt, style, links = para_text(p, doc, hmap, imgs, safe)
            if txt.strip() or links:
                pref = f"[{style}] " if style and style != "Normal" else ""
                lines.append(pref + txt)
                for l in links:
                    lines.append(f"    LINK: {l}")
        elif child.tag == qn('w:tbl'):
            t = Table(child, doc)
            lines.append("--- TABLE ---")
            for r in t.rows:
                cells = []
                for c in r.cells:
                    ct = []
                    for p in c.paragraphs:
                        txt, style, links = para_text(p, doc, hmap, imgs, safe)
                        if txt.strip():
                            ct.append(txt)
                        for l in links:
                            ct.append(f"LINK: {l}")
                    cells.append(" / ".join(ct))
                lines.append(" | ".join(cells))
            lines.append("--- /TABLE ---")
    lines.append(f"===== IMAGES: {len(imgs)} =====")
    with open(os.path.join(OUT, safe + ".txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(safe, len(lines), len(imgs))


for f in sorted(os.listdir(SRC)):
    if f.lower().endswith(".docx") and not f.startswith("~"):
        dump(os.path.join(SRC, f))
