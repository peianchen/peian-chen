"""Check bilingual content, project scope, and local static references."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.cards = 0
        self.details = 0
        self.filters = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == "article" and "project-card" in classes:
            self.cards += 1
        if tag == "details" and "project-details" in classes:
            self.details += 1
        if tag == "button" and attrs.get("data-filter"):
            self.filters.append(attrs["data-filter"])


def main():
    root = Path(__file__).resolve().parents[1] / "site"
    parsed = {}
    for relative in ("index.html", "en/index.html"):
        path = root / relative
        source = path.read_text(encoding="utf-8")
        page = Page()
        page.feed(source)
        assert not [key for key, count in Counter(page.ids).items() if count > 1]
        assert page.cards == page.details == 16, relative
        assert {"medical-imaging", "data-structures", "taipei-bus", "project-search", "pressible", "space-payload", "bioimage-analysis", "pva-pump"} <= set(page.ids)
        assert "early-work-title" not in page.ids
        assert not re.search(r"Rice-Variety|稻米品種|Wireless Robotic-Arm Carrier|無線機械手臂搬運載具", source)
        assert {"all", "imaging", "algorithms", "web", "research"} <= set(page.filters)
        assert len(page.filters) == len(set(page.filters))
        assert re.search(r'id="visible-count">16<', source)
        assert not re.search(r"INTERVIEW_GUIDE|面試|展現能力|REPOSITORIES MAPPED", source)
        assert any("NYCU-AFPGA-Labs" in link for link in page.links)
        assert {"featured", "coursework", "engineering-work"} <= set(page.ids)
        assert source.count('class="featured-card"') == 3
        assert "mailto:chen861019@gmail.com" in page.links
        assert any("NYCU-Data-Structures-Graph-Algorithms" in link for link in page.links)
        assert "https://github.com/peianchen/taipei-bus-live" in page.links
        assert "Ph.D. Student" in source and "Ph.D. Candidate" not in source
        assert "KiCad" in source and "Zephyr RTOS" in source
        assert source.count('class="capability-row"') == 10
        assert all(term in source for term in ("ECsnap", "SolidWorks", "COMSOL", "Embedded Linux", "2027", "PVA"))
        assert not re.search(r"resumeList|vno=|研發替代役|薪資|士林|tel:|salary", source, re.IGNORECASE)
        assert "Recovery FSM" in source and "System ON idle" in source
        assert not re.search(r"recovery-boundary verification|監測與恢復流程", source)
        assert source.count("<h1 ") == 1
        assert "2019" in source and "Biosensors &amp; Bioelectronics" in source
        parsed[path.resolve()] = page
    for path in root.glob('**/projects/*/index.html'):
        source = path.read_text(encoding='utf-8')
        page = Page()
        page.feed(source)
        assert not [key for key, count in Counter(page.ids).items() if count > 1]
        assert {'purpose', 'workflow', 'decisions', 'evidence', 'reproduce', 'limits', 'sources'} <= set(page.ids)
        assert source.count('<h1>') == 1
        assert 'og:image' in source and 'hreflang="en"' in source
        assert not re.search(r'INTERVIEW_GUIDE|面試|展現能力|C:/Users|vno=', source)
        parsed[path.resolve()] = page
    assert len(parsed) == 8
    for path, page in parsed.items():
        checked = 0
        for link in page.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if target.is_dir():
                target /= "index.html"
            assert target.is_relative_to(root.resolve()) and target.is_file(), link
            if parts.fragment:
                assert unquote(parts.fragment) in parsed[target].ids, link
            checked += 1
        print(f"{path.relative_to(root)}: {page.cards} cards, {page.details} details, {checked} local links OK")


if __name__ == "__main__":
    main()
