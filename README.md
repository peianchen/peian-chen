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
- `site/ui-entry.js`: selective Lumen Web Component registration; bundles the shared application script
- `site/design-tokens.css`: primitive, semantic and component tokens for both themes
- `site/portfolio-ui.css`: portfolio-specific layout, component states and motion rules
- `.github/workflows/deploy.yml`: static GitHub Pages deployment

The interface uses Lumen Elements 4.2.0 with a small local bundle, refined with
`emil-design-eng`, `ui-ux-pro-max` and `design-system` practices. See the
[design system and component contracts](docs/DESIGN_SYSTEM.md).

After editing JavaScript, run `npm ci --ignore-scripts` and `npm run build:ui`.
The committed static assets keep a fresh checkout directly previewable.

Live site: <https://peianchen.github.io/peian-chen/>

## Featured case studies

Three systems have independent Chinese and English pages, with architecture diagrams, purpose, workflows, design decisions, results, reproduction notes and limitations:

- [ThermoPatch](https://peianchen.github.io/peian-chen/en/projects/thermopatch/)
- [SpaceCellCam](https://peianchen.github.io/peian-chen/en/projects/spacecellcam/)
- [Space BMC Core](https://peianchen.github.io/peian-chen/en/projects/space-bmc/)

Their editable source is `content/case_studies.json`. Run `python tools/build_case_studies.py` after editing it. See [maintenance instructions](docs/PORTFOLIO_MAINTENANCE.md).

## Content

The bilingual pages cover sixteen engineering, research, and graduate-course
projects. Undergraduate project summaries are omitted by the owner's preference.
Each project includes an expandable purpose, implementation approach, and scope.
Public repositories have direct links; private research/code is described without
exposing private research source. AFPGA now links to a curated public edition with clean history. Historical results are not presented as fresh
validation or clinical evidence.

Copy is cross-checked against the public GitHub profile, implementation READMEs,
and professional sections of the owner's 104 resume. See
[content sources](docs/CONTENT_SOURCES.md) for the reference scope.

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
