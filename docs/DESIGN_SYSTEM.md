# PEIAN.LAB interface system

The visual direction is a precise engineering portfolio: deep space blue, readable
technical typography, quiet surfaces and source-backed project explanations. This
iteration preserves the portrait, sixteen project entries, bilingual case studies
and research archive. It does not change research claims or repository visibility.

## Four complementary tools

| Tool | Applied responsibility |
| --- | --- |
| Lumen UI | Real Web Components: Card, Badge and Button. Contracts retrieved from the connected catalog, then checked against installed public exports. |
| emil-design-eng | Short press feedback, pointer-only transforms, no motion on keyboard navigation, visible focus, Escape focus return and honest copy failure feedback. |
| ui-ux-pro-max | Content-first portfolio hierarchy, responsive layout, readable metadata, touch targets and independent light/dark checks. |
| design-system | Primitive, semantic and component-token layers, shared typography/spacing/radii, documented component states. |

The UI/UX search suggested a modular editorial grid. The existing Space Grotesk,
Noto Sans TC and IBM Plex Mono fonts were preserved instead of adopting its generic
academic serif suggestion. Existing blue branding takes precedence over a generated
palette suggestion. Components are not a reason to migrate the static site to React.

## Versioned Lumen boundary

- `@santi020k/lumen-elements`: 4.2.0.
- Resolved `@santi020k/lumen-core`: 4.1.0; umbrella styles: 4.2.0.
- MCP catalog hash: `7113faa8466fe24529069b1918abbbfdf18c101d00341b2824cba2149c416e77`.
- Catalog diagnostics passed; installed Elements/Core versions matched the contracts.
- `site/ui-entry.js` registers only Card, Badge and Button, once.
- `tools/build-ui.mjs` bundles the official stylesheet once and emits local CSS/JS
  plus the packages' license notices. No runtime component CDN is required.
- Native filter/copy controls are progressively upgraded before the application
  attaches listeners. Navigation, search inputs and disclosures keep native semantics.
- Without JavaScript, project content and links remain readable and the mobile
  navigation is visible. Search/filter/theme/copy enhancement requires JavaScript.

## Tokens and ownership

`site/design-tokens.css` owns primitive HSL values, semantic Lumen roles and portfolio
aliases. Lumen semantic variables remain HSL channel values, consumed as
`hsl(var(--surface))`; older product aliases use complete CSS colors. This prevents
collisions with Lumen's `surface`, `ink` and `line` contracts.

| Layer | Examples | Purpose |
| --- | --- | --- |
| Primitive | `--navy-950`, `--blue-400`, `--space-6`, `--radius-lg` | Base design values |
| Semantic | `--canvas`, `--surface`, `--ink-soft`, `--brand`, `--on-brand` | Meaning, remapped for each theme |
| Component | `--card-inset`, `--control-height`, `--section-space` | Reusable layout relationships |

Use a single border/radius owner: the featured Lumen card owns the outside edge,
the inner anchor owns navigation and focus, and only the artwork clips at its corners.
Long-form content stays unboxed except where grouping or limitations need emphasis.

## Interaction review

| Before | After | Why |
| --- | --- | --- |
| Card hover lifts and strong shadows | Stable surfaces with a border emphasis | Avoid moving a reading surface or confusing touch hover |
| 600ms scroll reveals with long stagger | 280ms entry, 40/80ms stagger, 8px travel | Keep first entry legible and brief |
| Keyboard actions inherit motion | Keyboard input disables transitions and reveals hidden content | Preserve immediate, visible navigation |
| Escape only closes mobile menu | Close and return focus to its trigger | Avoid focus remaining in a hidden menu |
| Clipboard denial navigates away | Localized status with the address retained | Failure should not interrupt reading |
| Small labels and mixed surface colors | Shared label scale and semantic color aliases | Consistent hierarchy across both languages/themes |

Pointer press uses 120ms feedback; ordinary state transitions use 180ms. Motion is
disabled for reduced-motion and keyboard paths. Touch screens do not inherit hover
translation. The palette does not use green to indicate a successful copy.

## Build and verification

```sh
npm ci --ignore-scripts
npm run build:ui
python tools/build_case_studies.py
python tools/check_site.py
python tools/check_design.py
npm test
```

Commit generated `site/assets/` and case pages with their source. CI rebuilds the
bundle and rejects a difference from committed assets before deployment.

The design check verifies text/action/focus contrast token pairs in both themes,
one component entry per page, all cards/badges, and motion/fallback rules. It is not
a full WCAG conformance audit. Browser QA covers rendered component registration,
responsive layouts, Enter/Space activation, search, theme switching, language links
and Escape focus return. Physical phone and assistive-technology testing remain
separate from browser viewport checks.
