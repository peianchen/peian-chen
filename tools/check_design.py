"""Validate the Lumen boundary, token contrast and progressive enhancement."""
import colorsys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
source = (SITE / 'design-tokens.css').read_text(encoding='utf-8')
declaration = re.compile(r'--([\w-]+):\s*([^;]+);')
base, light = source.split('html[data-theme="blueprint"]', 1)
base = dict(declaration.findall(base))


def resolve(name, tokens):
    value = tokens[name]
    reference = re.fullmatch(r'var\(--([\w-]+)\)', value)
    return resolve(reference[1], tokens) if reference else value


def luminance(name, tokens):
    h, s, l = map(float, resolve(name, tokens).replace('%', '').split())
    rgb = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    linear = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in rgb]
    return sum(c * w for c, w in zip(linear, (.2126, .7152, .0722)))


for theme, tokens in [('midnight', base), ('blueprint', base | dict(declaration.findall(light)))]:
    pairs = [(ink, bg, 4.5) for ink in ('ink', 'ink-soft', 'ink-muted', 'brand') for bg in ('canvas', 'surface')]
    pairs += [('on-brand', 'brand-solid', 4.5), ('focus-ring', 'surface', 3)]
    for fg, bg, minimum in pairs:
        a, b = sorted((luminance(fg, tokens), luminance(bg, tokens)))
        ratio = (b + .05) / (a + .05)
        assert ratio >= minimum, (theme, fg, bg, ratio)
    print(f'{theme}: {len(pairs)} text/action/focus token pairs pass contrast targets')

for path in [SITE / 'index.html', SITE / 'en/index.html', *SITE.glob('**/projects/*/index.html')]:
    html = path.read_text(encoding='utf-8')
    for asset in ('assets/ui.css', 'assets/ui.js', 'design-tokens.css', 'portfolio-ui.css'):
        assert html.count(asset) == 1, (path, asset)
    assert '<script src="./site.js"' not in html
    assert '<lumen-badge' in html
    if path.parent == SITE or path.parent == SITE / 'en':
        assert html.count('<lumen-card') == 3
        assert html.count('class="project-state"') == 16

css = (SITE / 'portfolio-ui.css').read_text(encoding='utf-8')
assert 'prefers-reduced-motion' in css and 'hover: hover' in css
assert 'html:not(.js-ready) .primary-nav' in css
assert 'data-input="keyboard"' in css
for path in ('style.css', 'case-studies.css', 'portfolio-ui.css'):
    assert not re.search(r'#[\da-fA-F]{3,8}\b|rgba?\(', (SITE / path).read_text(encoding='utf-8')), path
assert (SITE / 'assets/ui.js').stat().st_size < 25000
assert (SITE / 'assets/LICENSES.txt').is_file()
print('Eight pages: one local Lumen entry, preserved badges/cards, motion/fallback rules, token-only product CSS')
