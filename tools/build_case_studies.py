"""Build the complete bilingual project collection from reviewed source content."""
from html import escape as e
import json
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
BASE = 'https://peianchen.github.io/peian-chen/'
PROJECTS = json.loads((ROOT / 'content/case_studies.json').read_text(encoding='utf-8'))


def svg_text(text, x, y, size=20, fill='#eff6ff', width=22):
    lines = textwrap.wrap(text, width=width, break_long_words=False)
    return ''.join(f'<text x="{x}" y="{y+i*(size+8)}" fill="{fill}" font-size="{size}">{e(line)}</text>' for i,line in enumerate(lines))


def diagram(p):
    blocks = []
    for i,label in enumerate(p['nodes']):
        x = 38+i*292
        blocks.append(f'<rect x="{x}" y="225" width="250" height="120" rx="12" fill="#102846" stroke="#69b7ff"/>{svg_text(f"0{i+1}",x+20,256,15,"#a4b9d6")}{svg_text(label,x+20,293,18,width=18)}')
        if i<3:
            blocks.append(f'<path d="M{x+250} 285h40l-9 -7m9 7l-9 7" fill="none" stroke="#69b7ff" stroke-width="2"/>')
    title_size=42 if len(p['name'])<28 else 32
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 450" role="img" aria-labelledby="title desc">
<title id="title">{e(p['name'])} architecture</title><desc id="desc">{e(' to '.join(p['nodes']))}. Source-derived explanatory diagram.</desc>
<defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#1a3352"/></pattern></defs><rect width="1200" height="450" fill="#060d1c"/><rect width="1200" height="450" fill="url(#grid)"/>
<g font-family="monospace">{svg_text(p['domain'],38,60,17,'#69b7ff',70)}{svg_text(p['name'],38,126,title_size,width=60)}{svg_text(p['tags'],38,175,17,'#a4b9d6',100)}{''.join(blocks)}{svg_text('ARCHITECTURE / EXPLANATORY DIAGRAM',38,406,15,'#a4b9d6',80)}</g></svg>'''


def notes(entries):
    return ''.join(f'<article class="case-note"><h3>{e(title)}</h3><p>{e(text)}</p></article>' for title,text in entries)


def render(p,lang):
    en=lang=='en'
    c=p[lang]
    prefix='../../../' if en else '../../'
    home='../../'
    route=('en/' if en else '')+f"projects/{p['slug']}/"
    other=prefix+('' if en else 'en/')+f"projects/{p['slug']}/"
    labels={
        'purpose': 'Purpose and use' if en else '目的與用途',
        'architecture':'System architecture' if en else '系統架構',
        'workflow':'Operating workflow' if en else '操作流程',
        'decisions':'Design decisions' if en else '設計選擇',
        'evidence':'Results and images' if en else '成果與圖像',
        'analysis':'Analysis and interpretation' if en else '分析與判讀',
        'reproduce':'Explore and reproduce' if en else '閱讀與重現',
        'limits':'Scope and limitations' if en else '範圍與限制',
        'sources':'Sources' if en else '資料來源'
    }
    sections=[]
    toc=[]
    def section(anchor,body,classes=''):
        toc.append((anchor,labels[anchor]))
        sections.append(f'<section class="case-section {classes}" id="{anchor}"><p class="section-index">{len(toc):02} / {anchor.upper()}</p><h2>{labels[anchor]}</h2>{body}</section>')

    section('purpose',f'<p class="case-context">{e(c["purpose"])}</p>')
    architecture=''.join(f'<lumen-card class="architecture-part" variant="muted"><small>0{i+1}</small><h3>{e(title)}</h3><p>{e(text)}</p></lumen-card>' for i,(title,text) in enumerate(c['architecture']))
    section('architecture',f'<div class="architecture-parts">{architecture}</div>')
    flow=''.join(f'<details class="flow-step" {"open" if i==0 else ""}><summary><span>0{i+1}</span>{e(title)}</summary><p>{e(text)}</p></details>' for i,(title,text) in enumerate(c['steps']))
    section('workflow',f'<div class="flow-explorer">{flow}</div>')
    if c.get('decisions'):
        section('decisions',f'<div class="case-note-grid">{notes(c["decisions"])}</div>')

    gallery=[]
    kinds={
        'prototype':('原型照片','Prototype photograph'),
        'simulation':('模擬結果','Simulation result'),
        'analysis':('分析輸出','Analysis output'),
        'historical':('歷史紀錄','Archived result')
    }
    for im in p.get('gallery',[]):
        text=im[lang]
        kind=kinds[im['kind']][1 if en else 0]
        path=prefix+im['src']
        gallery.append(f'''<figure class="result-figure"><a class="result-image" href="{path}" target="_blank" rel="noreferrer" aria-label="{e(text['title'])} — {'open full size' if en else '開啟原圖'}"><img src="{path}" width="{im['width']}" height="{im['height']}" loading="lazy" decoding="async" alt="{e(text['title'])}"></a><figcaption><lumen-badge variant="outline">{kind}</lumen-badge><h3>{e(text['title'])}</h3><p>{e(text['caption'])}</p><a href="{path}" target="_blank" rel="noreferrer">{'Open full size' if en else '查看原圖'} ↗</a></figcaption></figure>''')
    results=f'<div class="case-note-grid">{notes(c["results"])}</div>'
    if p.get('validation'):
        v=p['validation']
        label=f"{v['date']} / {v['tool']}: {v['checks']} checks, 0 failures." if en else f"{v['date']} / {v['tool']}：{v['checks']} 項檢查通過。"
        results=f'<div class="validation-record"><strong>{e(label)}</strong><p>{"Functional simulation. " if en else "功能模擬。"}<a href="https://github.com/peianchen/{p["repo"]}/blob/{p["branch"]}/{v["report"]}">{"Run record" if en else "執行紀錄"} ↗</a></p></div>'+results
    if gallery:
        results+='<div class="result-gallery">'+''.join(gallery)+'</div>'
    else:
        results+=f'<p class="media-availability">{e(c["media_note"])}</p>'
    section('evidence',results)
    section('analysis',f'<div class="analysis-grid">{notes(c["analysis"])}</div>')
    section('reproduce','<ol class="case-checklist">'+''.join(f'<li>{e(step)}</li>' for step in c['reproduce'])+'</ol>')
    section('limits',f'<p>{e(c["limits"])}</p>','case-limits')
    source_links=''.join(f'<li><a href="{e(s["url"])}">{e(s["label"])} ↗</a></li>' for s in p['sources'])
    provenance='Selected photographs and plots retain their original content. Captions identify prototype, archived, analysis or simulation material.' if en else '入選照片與圖表保留原始內容，圖說分別註明原型、歷史紀錄、分析輸出或模擬。'
    section('sources',f'<ul class="case-sources">{source_links}</ul><p>{provenance}</p>')

    candidates=[q for q in PROJECTS if q!=p and q['group']==p['group']]
    candidates+=(q for q in PROJECTS if q!=p and q not in candidates)
    related=''.join(f'<a class="related-project" href="../{q["slug"]}/"><small>{e(q["domain"])}</small><strong>{e(q["name"])}</strong><span>{"Explore project" if en else "閱讀專案介紹"} →</span></a>' for q in candidates[:2])
    tags=''.join(f'<lumen-badge variant="outline">{e(tag.strip())}</lumen-badge>' for tag in p['tags'].split('/'))
    repo_url=f'https://github.com/peianchen/{p["repo"]}' if p['repo'] else home+'#contact'
    action=('Explore source code' if en else '查看公開原始碼') if p['repo'] else ('Discuss this project' if en else '聯絡討論專案')
    status={'engineering':('工程實作','Engineering project'),'research':('研究專案','Research project'),'coursework':('課程實作','Coursework')}[p['group']][1 if en else 0]
    section_links=''.join(f'<a href="#{anchor}">{label}</a>' for anchor,label in toc)
    fonts='https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=Noto+Sans+TC:wght@400;500;700;900&amp;family=Space+Grotesk:wght@500;600;700&amp;display=swap'
    return f'''<!doctype html>
<html lang="{'en' if en else 'zh-Hant'}" data-theme="midnight"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p['name'])} | Pei An Chen</title><meta name="description" content="{e(c['summary'])}"><meta name="theme-color" content="#060d1c">
<link rel="canonical" href="{BASE+route}"><link rel="alternate" hreflang="zh-Hant" href="{BASE}projects/{p['slug']}/"><link rel="alternate" hreflang="en" href="{BASE}en/projects/{p['slug']}/">
<meta property="og:type" content="article"><meta property="og:title" content="{e(p['name'])} | Pei An Chen"><meta property="og:description" content="{e(c['summary'])}"><meta property="og:url" content="{BASE+route}"><meta property="og:image" content="{BASE}img/projects/{p['slug']}-share.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml"><link href="{fonts}" rel="stylesheet"><link rel="stylesheet" href="{prefix}assets/ui.css"><link rel="stylesheet" href="{prefix}design-tokens.css"><link rel="stylesheet" href="{prefix}style.css"><link rel="stylesheet" href="{prefix}case-studies.css"><link rel="stylesheet" href="{prefix}portfolio-ui.css"><script type="module" src="{prefix}assets/ui.js"></script></head>
<body class="case-page"><a class="skip-link" href="#main">{'Skip to content' if en else '跳到主要內容'}</a><div class="scroll-meter" aria-hidden="true"><span id="scroll-progress"></span></div>
<header class="site-header" id="top"><a class="brand" href="{home}"><span class="brand-mark">PA</span><span class="brand-copy"><strong>PEIAN.LAB</strong><small>ENGINEERING SYSTEMS</small></span></a>
<nav class="case-header-nav" aria-label="{'Navigation' if en else '導覽'}"><a href="{home}#projects">{'All projects' if en else '全部專案'}</a><a href="{home}#contact">{'Contact' if en else '聯絡'}</a></nav>
<div class="header-actions"><a class="language-switch" href="{other}" lang="{'zh-Hant' if en else 'en'}" aria-label="{'切換至中文' if en else 'Switch to English'}">{'中文' if en else 'EN'}</a><button class="theme-toggle" aria-label="{'Toggle theme' if en else '切換明暗主題'}" aria-pressed="false"><span class="theme-toggle__track"><span class="theme-toggle__knob"></span></span><span class="theme-toggle__label">MODE</span></button></div></header>
<main id="main" class="section-shell"><div class="case-hero"><a class="case-back" href="{home}#projects">← {'All projects' if en else '返回專案列表'}</a><div class="case-meta"><span class="section-index">{e(p['domain'])}</span><lumen-badge variant="outline">{status}</lumen-badge></div><p class="case-name">{e(p['name'])}</p><h1>{e(c['title'])}</h1><p class="case-lead">{e(c['summary'])}</p><div class="case-tags">{tags}</div><div class="case-actions"><a class="button button--primary" href="#evidence">{'Explore results' if en else '查看成果與圖像'} ↓</a><a class="button button--ghost" href="{repo_url}">{action} ↗</a></div></div>
<figure class="case-figure"><img src="{prefix}img/projects/{p['slug']}.svg" width="1200" height="450" alt="{e(' → '.join(p['nodes']))}"><figcaption>{e(c['caption'])} <a href="{prefix}img/projects/{p['slug']}.svg" target="_blank" rel="noreferrer">{'Open architecture diagram' if en else '查看架構圖原尺寸'} ↗</a></figcaption></figure>
<div class="case-layout"><nav class="case-toc" aria-label="{'On this page' if en else '頁面目錄'}">{section_links}</nav><div class="case-body">{''.join(sections)}</div></div>
<section class="case-related"><h2>{'Continue exploring' if en else '繼續探索'}</h2><div>{related}</div></section></main>
<footer class="site-footer"><span>© 2026 PEI AN CHEN</span><a href="{home}#projects">{'All 16 projects' if en else '查看全部 16 個專案'} ↗</a></footer></body></html>'''


def update_home():
    import re
    for lang,relative,prefix in [('zh','index.html','./'),('en','en/index.html','./')]:
        path=SITE/relative
        text=path.read_text(encoding='utf-8')
        index=0
        def update(match):
            nonlocal index
            card=match[0]
            p=PROJECTS[index]
            index+=1
            existing_link = re.compile(r'<a\b[^>]*href="'+re.escape(prefix+'projects/'+p['slug']+'/')+r'"[^>]*>.*?</a>', re.S)
            matches = list(existing_link.finditer(card))
            if matches:
                # Rebuilding must preserve one detail link per card.
                for duplicate in reversed(matches[1:]):
                    card=card[:duplicate.start()]+card[duplicate.end():]
                return card
            label='Explore the complete project' if lang=='en' else '完整專案介紹'
            return card.replace('</article>',f'<a class="project-link project-link--case" href="{prefix}projects/{p["slug"]}/">{label} →</a>\n        </article>')
        text=re.sub(r'<article class="project-card\b.*?</article>',update,text,flags=re.S)
        assert index==len(PROJECTS)
        text='\n'.join(line.rstrip() for line in text.splitlines())+'\n'
        path.write_text(text,encoding='utf-8')


def main():
    assets=SITE/'img/projects'
    assets.mkdir(parents=True,exist_ok=True)
    for p in PROJECTS:
        (assets/f"{p['slug']}.svg").write_text(diagram(p),encoding='utf-8')
        for lang in ('zh','en'):
            path=SITE/('en' if lang=='en' else '')/'projects'/p['slug']
            path.mkdir(parents=True,exist_ok=True)
            (path/'index.html').write_text(render(p,lang),encoding='utf-8')
    update_home()
    print(f'Rendered {len(PROJECTS)*2} project pages and {len(PROJECTS)} architecture diagrams.')


if __name__=='__main__':
    main()
