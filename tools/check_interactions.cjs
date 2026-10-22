const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const source = fs.readFileSync(path.join(__dirname, "../site/site.js"), "utf8");

function element(properties = {}) {
  const classes = new Set();
  const events = {};
  return {
    dataset: {},
    textContent: "",
    hidden: false,
    style: {},
    classList: {
      toggle(name, active) { active ? classes.add(name) : classes.delete(name); },
      add(name) { classes.add(name); },
      remove(name) { classes.delete(name); },
      contains(name) { return classes.has(name); },
    },
    setAttribute(name, value) { this[name] = value; },
    getAttribute(name) { return this[name]; },
    addEventListener(name, handler) { events[name] = handler; },
    dispatch(name, extra = {}) { return events[name]?.({ target: this, ...extra }); },
    focus() { this.focused = true; },
    ...properties,
  };
}

(async () => {
for (const storageBlocked of [false, true]) {
  const root = element({ scrollHeight: 1200 });
  const input = element({ value: "" });
  const clear = element();
  const count = element();
  const empty = element();
  const grid = element();
  const theme = element();
  const menu = element({ 'aria-expanded': 'false' });
  const navigation = element();
  const copy = element({ dataset: { copy: 'github.com/peianchen' }, textContent: 'COPY HANDLE' });
  const toast = element();
  const course = element();
  const language = element({ href: './en/' });
  const documentEvents = {};
  let clipboardFails = false;
  let copiedValue;
  const location = { href: 'https://peianchen.github.io/peian-chen/?q=MRI&filter=imaging#projects', hash: '#projects', search: '?q=MRI&filter=imaging' };
  const cards = [
    element({ dataset: { category: "research imaging" }, textContent: "MRI SPECT PyTorch" }),
    element({ dataset: { category: "algorithms" }, textContent: "C BFS Huffman" }),
    element({ dataset: { category: "bio embedded" }, textContent: "BLE ThermoPatch" }),
  ];
  const filters = ["all", "imaging", "algorithms"].map((filter) => element({ dataset: { filter } }));
  const selectors = {
    ".theme-toggle": theme,
    "#project-search": input,
    ".search-clear": clear,
    "#visible-count": count,
    ".search-empty": empty,
    "#project-grid": grid,
    '.menu-toggle': menu,
    '.primary-nav': navigation,
    '.copy-handle': copy,
    '.toast': toast,
    '.language-switch': language,
    '.primary-nav a[href="#coursework"]': course,
  };
  vm.runInNewContext(source, {
    document: {
      documentElement: root,
      querySelector: (selector) => selectors[selector] || null,
      querySelectorAll: (selector) => ({ ".filter-button": filters, ".project-card": cards }[selector] || []),
      addEventListener(name, handler) { (documentEvents[name] ||= []).push(handler); },
    },
    window: {
      location, history: { replaceState(_state, _title, url) {
        location.href = url.href; location.hash = url.hash; location.search = url.search;
      } },
      matchMedia: () => ({ matches: true }), innerHeight: 800, scrollY: 0, addEventListener() {},
    },
    navigator: { clipboard: { async writeText(value) {
      if (clipboardFails) throw new Error('denied');
      copiedValue = value;
    } } },
    localStorage: {
      getItem() { if (storageBlocked) throw new Error("blocked"); return null; },
      setItem() { if (storageBlocked) throw new Error("blocked"); },
    },
    URL, Intl, Date, setInterval() {}, setTimeout() {}, clearTimeout() {}, requestAnimationFrame() {},
  });
  assert.equal(count.textContent, '1');
  assert.equal(input.value, 'MRI');
  assert.match(language.href, /en\/\?q=MRI&filter=imaging#projects/);
  course.dispatch('click');
  assert.equal(count.textContent, "3");
  input.value = "ＭＲＩ spect";
  input.dispatch("input");
  assert.equal(count.textContent, "1");
  assert.equal(grid.classList.contains("is-single-result"), true);
  filters[2].dispatch("click");
  assert.equal(count.textContent, "0");
  assert.equal(empty.hidden, false);
  clear.dispatch("click");
  assert.equal(count.textContent, "1");
  assert.equal(clear.hidden, true);
  assert.equal(input.focused, true);
  filters[0].dispatch("click");
  assert.equal(count.textContent, "3");
  assert.equal(empty.hidden, true);
  assert.equal(grid.classList.contains("is-single-result"), false);
  theme.dispatch("click");
  assert.equal(root.dataset.theme, "blueprint");
  assert.equal(root.dataset.lumenScheme, 'light');
  menu.dispatch('click');
  assert.equal(menu['aria-expanded'], 'true');
  for (const handler of documentEvents.keydown) handler({ key: 'Escape' });
  assert.equal(menu['aria-expanded'], 'false');
  assert.equal(menu.focused, true);
  assert.equal(root.dataset.input, 'keyboard');
  await copy.dispatch('click');
  assert.equal(copiedValue, 'github.com/peianchen');
  assert.equal(toast.textContent, '已複製 GitHub 網址。');
  clipboardFails = true;
  const beforeCopyFailure = location.href;
  await copy.dispatch('click');
  assert.match(toast.textContent, /github.com\/peianchen/);
  assert.equal(location.href, beforeCopyFailure, 'Clipboard denial must not navigate away');
  console.log(`Search, URL restoration, course reset, theme, Escape focus, clipboard: OK (storageBlocked=${storageBlocked})`);
}
})().catch(error => { console.error(error); process.exitCode = 1; });
