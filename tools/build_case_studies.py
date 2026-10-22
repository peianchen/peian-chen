"""Render bilingual, source-backed case studies without a client-side framework."""
from html import escape as e
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
BASE = 'https://peianchen.github.io/peian-chen/'
PROJECTS = json.loads((ROOT / 'content/case_studies.json').read_text(encoding='utf-8'))


def diagram(p):
    blocks = []
    for i, label in enumerate(p['nodes']):
        x = 38 + i * 292
        blocks.append(f'<rect x="{x}" y="225" width="250" height="110" rx="8" fill="#102846" stroke="#69b7ff"/><text x="{x+20}" y="258" fill="#a4b9d6" font-size="16">0{i+1}</text><text x="{x+20}" y="300" fill="#eff6ff" font-size="20">{e(label)}</text>')
        if i < 3:
            blocks.append(f'<path d="M{x+250} 280 h40 l-9 -7 m9 7 l-9 7" fill="none" stroke="#69b7ff" stroke-width="2"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 450" role="img" aria-labelledby="title desc">
<title id="title">{e(p['name'])} architecture</title><desc id="desc">{' to '.join(p['nodes'])}. Explanatory diagram, not measured data.</desc>
<defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#1a3352" stroke-width="1"/></pattern></defs>
<rect width="1200" height="450" fill="#060d1c"/><rect width="1200" height="450" fill="url(#grid)"/>
<g font-family="monospace"><text x="38" y="65" fill="#69b7ff" font-size="18">{e(p['domain'])}</text><text x="38" y="135" fill="#eff6ff" font-size="48">{e(p['name'])}</text><text x="38" y="178" fill="#a4b9d6" font-size="20">{e(p['tags'])}</text>{''.join(blocks)}<text x="38" y="405" fill="#a4b9d6" font-size="16">ARCHITECTURE / SOURCE-DERIVED EXPLANATION</text></g></svg>'''


def render(p, lang):
    en = lang == 'en'
    c = p[lang]
    prefix = '../../../' if en else '../../'
    home = '../../'
    route = ('en/' if en else '') + f"projects/{p['slug']}/"
    other = prefix + ('' if en else 'en/') + f"projects/{p['slug']}/"
    headings = ['Purpose', 'How it works', 'Design decisions', 'Results and evidence', 'Reproduce the workflow', 'Scope and limitations', 'Source material'] if en else ['目的與用途', '系統如何運作', '設計選擇與取捨', '結果與證據', '如何重現', '範圍與限制', '資料來源']
    sections = []
    sections.append(f'<section id="purpose"><p class="section-index">01 / CONTEXT</p><h2>{headings[0]}</h2><p>{e(c["purpose"])}</p></section>')
    steps = ''.join(f'<details class="flow-step" {"open" if i==0 else ""}><summary><span>0{i+1}</span>{e(title)}</summary><p>{e(text)}</p></details>' for i,(title,text) in enumerate(c['steps']))
    sections.append(f'<section id="workflow"><p class="section-index">02 / WORKFLOW</p><h2>{headings[1]}</h2><p class="muted">{"Select a stage to explore its role." if en else "點選階段，查看資料與控制如何往下傳遞。"}</p><div class="flow-explorer">{steps}</div></section>')
    for idx,key,anchor in [(2,'decisions','decisions'), (3,'results','evidence')]:
        entries = ''.join(f'<article class="case-note"><h3>{e(title)}</h3><p>{e(text)}</p></article>' for title,text in c[key])
        if key == 'results' and p.get('validation'):
            v = p['validation']
            result = f"{v['date']} / {v['tool']}: {v['checks']} checks passed; 0 errors, 0 warnings. Functional simulation only." if en else f"{v['date']} 使用 {v['tool']} 重新執行：{v['checks']} 項檢查通過，0 errors、0 warnings。範圍為功能模擬。"
            entries = f'<article class="case-note"><h3>{"Verified regression" if en else "本次回歸驗證"}</h3><p>{result} <a href="https://github.com/peianchen/{p["repo"]}/blob/main/{v["report"]}">{"Run record" if en else "執行紀錄"}</a></p></article>' + entries
        sections.append(f'<section id="{anchor}"><p class="section-index">0{idx+1} / {anchor.upper()}</p><h2>{headings[idx]}</h2><div class="case-note-grid">{entries}</div></section>')
    sections.append(f'<section id="reproduce"><p class="section-index">05 / REPRODUCE</p><h2>{headings[4]}</h2><ol class="case-checklist">'+''.join(f'<li>{e(step)}</li>' for step in c['reproduce'])+'</ol></section>')
    sections.append(f'<section id="limits" class="case-limits"><h2>{headings[5]}</h2><p>{e(c["limits"])}</p></section>')
    sources = f'https://github.com/peianchen/{p["repo"]}'
    sections.append(f'<section id="sources"><h2>{headings[6]}</h2><p><a href="{sources}/blob/main/README.md">README</a> · <a href="{sources}">{"Source code and technical documentation" if en else "原始碼與技術文件"}</a></p><p>{"Reviewed on 22 October 2026. See the repository for subsequent changes." if en else "內容核對日期：2026 年 10 月 22 日；後續更新以 repository 為準。"}</p></section>')
    related = ''.join(f'<a class="related-project" href="../{q["slug"]}/"><small>{e(q["domain"])}</small><strong>{e(q["name"])}</strong><span>{"Read case study" if en else "閱讀專案介紹"} →</span></a>' for q in PROJECTS if q!=p)
    tags = ''.join(f'<lumen-badge variant="outline">{e(tag.strip())}</lumen-badge>' for tag in p['tags'].split('/'))
    fonts = 'https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=Noto+Sans+TC:wght@400;500;700;900&amp;family=Space+Grotesk:wght@500;600;700&amp;display=swap'
    return f'''<!doctype html>
<html lang="{'en' if en else 'zh-Hant'}" data-theme="midnight"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p['name'])} | Pei An Chen</title><meta name="description" content="{e(c['summary'])}"><meta name="theme-color" content="#060d1c">
<link rel="canonical" href="{BASE+route}"><link rel="alternate" hreflang="zh-Hant" href="{BASE}projects/{p['slug']}/"><link rel="alternate" hreflang="en" href="{BASE}en/projects/{p['slug']}/">
<meta property="og:type" content="article"><meta property="og:title" content="{e(p['name'])} | Pei An Chen"><meta property="og:description" content="{e(c['summary'])}"><meta property="og:url" content="{BASE+route}"><meta property="og:image" content="{BASE}img/projects/{p['slug']}-share.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml"><link href="{fonts}" rel="stylesheet"><link rel="stylesheet" href="{prefix}assets/ui.css"><link rel="stylesheet" href="{prefix}design-tokens.css"><link rel="stylesheet" href="{prefix}style.css"><link rel="stylesheet" href="{prefix}case-studies.css"><link rel="stylesheet" href="{prefix}portfolio-ui.css"><script type="module" src="{prefix}assets/ui.js"></script></head>
<body class="case-page"><a class="skip-link" href="#main">{'Skip to content' if en else '跳到主要內容'}</a>
<header class="site-header" id="top"><a class="brand" href="{home}"><span class="brand-mark">PA</span><span class="brand-copy"><strong>PEIAN.LAB</strong><small>ENGINEERING SYSTEMS</small></span></a>
<nav class="case-header-nav" aria-label="{'Navigation' if en else '導覽'}"><a href="{home}#projects">{'All projects' if en else '全部專案'}</a><a href="{sources}">GitHub</a></nav>
<div class="header-actions"><a class="language-switch" href="{other}" lang="{'zh-Hant' if en else 'en'}">{'中文' if en else 'EN'}</a><button class="theme-toggle" aria-label="{'Toggle theme' if en else '切換明暗主題'}" aria-pressed="false"><span class="theme-toggle__track"><span class="theme-toggle__knob"></span></span><span class="theme-toggle__label">MODE</span></button></div></header>
<main id="main" class="section-shell"><div class="case-hero"><p class="section-index">{e(p['domain'])}</p><p class="case-name">{e(p['name'])}</p><h1>{e(c['title'])}</h1><p class="case-lead">{e(c['summary'])}</p><div class="case-tags">{tags}</div><a class="button button--primary" href="{sources}">{'Explore source code' if en else '查看公開原始碼'} ↗</a></div>
<figure class="case-figure"><img src="{prefix}img/projects/{p['slug']}.svg" width="1200" height="450" alt="{e(' → '.join(p['nodes']))}"><figcaption>{e(c['caption'])}</figcaption></figure>
<div class="case-layout"><nav class="case-toc" aria-label="{'On this page' if en else '頁面目錄'}">{''.join(f'<a href="#{anchor}">{label}</a>' for anchor,label in zip(['purpose','workflow','decisions','evidence','reproduce','limits','sources'],headings))}</nav><div class="case-body">{''.join(sections)}</div></div>
<section class="case-related"><h2>{'Explore another system' if en else '繼續探索其他系統'}</h2><div>{related}</div></section></main>
<footer class="site-footer"><span>© 2026 PEI AN CHEN</span><a href="{home}#contact">{'Contact' if en else '聯絡'} ↗</a></footer></body></html>'''


def main():
    assets = SITE / 'img/projects'
    assets.mkdir(parents=True, exist_ok=True)
    for p in PROJECTS:
        (assets / f"{p['slug']}.svg").write_text(diagram(p), encoding='utf-8')
        for lang in ('zh','en'):
            path = SITE / ('en' if lang == 'en' else '') / 'projects' / p['slug']
            path.mkdir(parents=True, exist_ok=True)
            (path / 'index.html').write_text(render(p,lang), encoding='utf-8')
    print('Rendered 6 case studies and 3 architecture diagrams.')


if __name__ == '__main__':
    main()
