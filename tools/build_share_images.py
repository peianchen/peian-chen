"""Render typography-based social cards from the same public project metadata."""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT = Path('C:/Windows/Fonts/consola.ttf')
if not FONT.is_file():
    FONT = Path('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf')
projects = json.loads((ROOT / 'content/case_studies.json').read_text(encoding='utf-8'))
items = [(p['name'],p['domain'],p['nodes'],ROOT/'site/img/projects'/f"{p['slug']}-share.png") for p in projects]
items.append(('PEI AN CHEN','RESEARCH + ENGINEERING',['SENSING','FIRMWARE','APPLICATIONS','DIGITAL SYSTEMS'],ROOT/'site/img/portfolio-share.png'))
for name,domain,nodes,path in items:
    canvas = Image.new('RGB',(1200,630),'#060d1c')
    d = ImageDraw.Draw(canvas)
    for x in range(0,1200,40): d.line((x,0,x,630),fill='#10213a')
    for y in range(0,630,40): d.line((0,y,1200,y),fill='#10213a')
    def text(x,y,value,size,fill):
        d.text((x,y),value,font=ImageFont.truetype(str(FONT),size),fill=fill)
    text(50,55,'PEIAN.LAB / ENGINEERING SYSTEMS',22,'#69b7ff')
    text(50,180,name,62,'#eff6ff')
    text(50,280,domain,24,'#a4b9d6')
    for i,node in enumerate(nodes):
        x=50+i*280
        d.rectangle((x,390,x+255,480),fill='#102846',outline='#69b7ff',width=2)
        text(x+12,423,node,18,'#eff6ff')
    text(50,555,'peianchen.github.io/peian-chen',22,'#a4b9d6')
    path.parent.mkdir(parents=True,exist_ok=True)
    canvas.save(path,optimize=True)
print('Rendered four 1200 x 630 social preview cards.')
