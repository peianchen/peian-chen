# Pei An Chen - Engineering Portfolio

Personal engineering portfolio for embedded biomedical sensing, FPGA, medical image analysis, research instrumentation, and cross-layer system integration.

## Local preview

```powershell
python -m http.server 8000 --directory site
```

Then open `http://localhost:8000`.

## Architecture

- `site/index.html`: semantic single-page content
- `site/style.css`: responsive engineering-console visual system
- `site/en/index.html`: complete English version with shared assets
- `site/site.js`: theme, combined search/filtering, navigation, reveal, clock, and clipboard interactions
- `.github/workflows/deploy.yml`: static GitHub Pages deployment

Live site: <https://peianchen.github.io/peian-chen/>

## Content

The bilingual pages cover twelve engineering, research, and course projects.
Each project includes an expandable purpose, implementation approach, and scope.
Public repositories have direct links; private research/code is described without
changing repository permissions. Historical results are not presented as fresh
validation or clinical evidence.

Copy is cross-checked against the public GitHub profile and implementation
READMEs. See [content sources](docs/CONTENT_SOURCES.md) for the reference scope.

The current portrait is the owner-supplied `site/img/peian-chen-campus-2026.jpg`.
Both languages use CSS framing to focus on the person and link to the full photo.
The image itself is unchanged; the previous `site/img/peian-chen.jpg` is retained.

## Checks

```powershell
python tools/check_site.py
node tools/check_interactions.cjs
node --check site/site.js
git diff --check
```

The dependency-free interaction checks cover combined category/keyword search,
multiple keywords, full-width input normalization, empty results, clear/focus,
counts, and theme operation when browser storage is blocked. Browser layout and
keyboard checks remain separate from these source-level checks.
