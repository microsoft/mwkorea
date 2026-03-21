import zipfile, xml.etree.ElementTree as ET
import os
os.chdir(r'c:\Users\jechoi\koreamw\koreamw\mwkorea')

docx_path = '코파일럿 스튜디오에서 엑셀파일을 참조할 때 도움이 될 팁.docx'
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

with zipfile.ZipFile(docx_path) as z:
    with z.open('word/document.xml') as f:
        tree = ET.parse(f)
        root = tree.getroot()

body = root.find('.//w:body', ns)
for elem in body:
    tag = elem.tag.split('}')[-1]
    if tag == 'p':
        pPr = elem.find('w:pPr', ns)
        style = ''
        if pPr is not None:
            pStyle = pPr.find('w:pStyle', ns)
            if pStyle is not None:
                style = pStyle.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val','')
        texts = []
        for r in elem.findall('.//w:r', ns):
            t = r.find('w:t', ns)
            if t is not None and t.text:
                texts.append(t.text)
        text = ''.join(texts)
        if text.strip():
            print(f'[{style}] {text}')
    elif tag == 'tbl':
        for row in elem.findall('.//w:tr', ns):
            cells = []
            for cell in row.findall('w:tc', ns):
                cell_texts = []
                for t in cell.findall('.//w:t', ns):
                    if t.text:
                        cell_texts.append(t.text)
                cells.append(''.join(cell_texts))
            if any(c.strip() for c in cells):
                print('[TABLE] ' + ' | '.join(cells))
