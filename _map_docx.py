import zipfile, xml.etree.ElementTree as ET

docx_path = r'c:\Users\jechoi\koreamw\koreamw\mwkorea\코파일럿 스튜디오에서 엑셀파일을 참조할 때 도움이 될 팁.docx'
ns = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
}

# Build rId -> image mapping
with zipfile.ZipFile(docx_path) as z:
    with z.open('word/_rels/document.xml.rels') as f:
        rels = ET.parse(f).getroot()
    rId_map = {}
    for rel in rels:
        rId = rel.get('Id')
        target = rel.get('Target','')
        if 'media' in target:
            rId_map[rId] = target.split('/')[-1]

    with z.open('word/document.xml') as f:
        tree = ET.parse(f)
        root = tree.getroot()

body = root.find('.//w:body', ns)

for elem in body:
    tag = elem.tag.split('}')[-1]
    if tag == 'p':
        texts = []
        for r in elem.findall('.//w:r', ns):
            t = r.find('w:t', ns)
            if t is not None and t.text:
                texts.append(t.text)
        text = ''.join(texts).strip()

        blips = elem.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip')
        imgs = []
        for blip in blips:
            rId = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
            if rId and rId in rId_map:
                imgs.append(rId_map[rId])

        if imgs:
            print('[IMG: ' + str(imgs) + '] ' + text[:50])
        elif text:
            print('[TEXT] ' + text[:80])
