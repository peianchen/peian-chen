# Project content guide

The portfolio contains 16 projects, with a Chinese and English page for each.
The catalogue is not a list of equally mature products: research prototypes,
focused firmware/RTL modules, applications and coursework are labelled separately.

## Content sources

- `content/case_studies.json` contains the existing architecture, workflow,
  results, analysis, scope and reviewed image captions.
- `content/project_briefs.json` adds a concise output/evidence brief, a specific
  three-step implementation walkthrough, direct implementation-reading links and
  two manually selected related projects. Every entry has both languages.
- `content/media-sources.json` records the selected media and hashes.
- `tools/build_case_studies.py` renders both languages and updates homepage card
  summaries and evidence lines without replacing the surrounding homepage.

The 2026-10-23 content pass cross-checked the public project READMEs and relevant
release, source and verification records. It did not rerun sensor experiments,
train models, flash devices or repeat course hardware tests. Historical figures
remain attached to their original scope or revision.

## Reading order

1. Identify what was built and what evidence is available.
2. Show the selected result, photograph or existing check record.
3. Explain a concrete technical case with inputs, processing and interpretation.
4. Provide architecture, operating workflow, analysis and reproduction guidance.
5. State limitations and link the sources.

Architecture illustrations are explanatory, not measured results. They appear
inside the architecture section rather than standing in for a project result.
Projects without suitable photographs use verifiable interfaces and code
descriptions; no unrelated screenshot or decorative image substitutes for proof.

## Publication boundaries

- Do not publish theses, defense decks, or images extracted from those materials.
- Keep research source code, mission parameters and unpublished raw data private.
- Distinguish photographs, UI captures, model output and hardware measurements.
- Do not merge evidence from different board or application generations.
- Never imply that compilation or a limited test suite establishes full system,
  sensor, clinical, environmental or flight qualification.
- Keep Chinese and English meanings aligned, including limitations and dates.

## Checks

```text
python tools/build_case_studies.py
python tools/check_site.py
python tools/check_design.py
node tools/check_interactions.cjs
```

The static checks cover all 16 brief entries, bilingual rendering, walkthroughs,
related-project links, one evidence line per card, image hashes and local links.
The deployment workflow also checks that generation does not change the committed
site. Inspect desktop and mobile layouts before publication.
