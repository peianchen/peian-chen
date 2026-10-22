# Portfolio content and publication

The website introduces projects and their engineering decisions. GitHub repositories preserve implementation details, reproducible procedures and evidence. Use public-reader language; avoid interview-specific framing.

## Editing content

- `site/index.html` and `site/en/index.html`: the bilingual home pages, complete project index, research archive and profile.
- `content/case_studies.json`: paired Chinese/English case-study content, source repository and optional verification record.
- `tools/build_case_studies.py`: generates 32 static project pages for all sixteen projects, their explanatory SVG architecture diagrams and homepage detail links.
- `tools/build_share_images.py`: generates PNG social previews from project names and system stages. Requires Pillow and a monospace font.
- `site/style.css` and `site/case-studies.css`: shared space-blue design, accessible reading layouts and responsive components.
- `site/design-tokens.css` and `site/portfolio-ui.css`: three-layer Lumen theme and product styling; see [Design system](DESIGN_SYSTEM.md).
- `site/ui-entry.js`: selective Lumen registration and progressive control enhancement. Rebuild with `npm ci --ignore-scripts` and `npm run build:ui` after editing this entry or `site/site.js`.

After editing the case-study source:

```sh
python tools/build_case_studies.py
python tools/check_site.py
python tools/check_design.py
node tools/check_interactions.cjs
```

Commit generated pages and `site/assets/` alongside their source. The deployment workflow rebuilds pinned Lumen assets and checks HTML references, token contrast and interactions before uploading `site/`. Visitors do not need a package installation; project content remains readable without browser JavaScript.

## Evidence rules

Every result needs an identified source and scope. Distinguish a configured target, a calculation, an archived test, a new simulation and a hardware measurement. Diagrams explain system behavior and must not look like fabricated screenshots or measured waveforms.

See [project media selection](PROJECT_MEDIA.md) for accepted images, exclusions and source revisions. Prefer a small useful gallery over repeated or unreadable figures. A project without an appropriate result image can keep its architecture and analysis complete without adding decorative evidence.

Keep public ThermoPatch separate from private V2 research. The BMC case covers the heartbeat monitor, not a complete recovery controller. SpaceCellCam configuration and the project name do not establish optical, thermal or orbital qualification.

AFPGA's public edition uses a clean history; its old repository and original reports remain private backups. Do not merge old branches into the new public repository.

## Before publishing

1. Check both languages, every case-study route, local links and social images.
2. Check desktop and mobile, light and dark themes, keyboard navigation, filtering and an empty search.
3. Verify the filtered URL can be refreshed and language switching preserves section and search state.
4. Review only intended staged paths; confirm source references and repository visibility.
5. After the Pages workflow succeeds, read the live pages and verify the published revision.
