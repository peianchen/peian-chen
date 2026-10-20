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
    dispatch(name) { events[name]?.({ target: this }); },
    focus() { this.focused = true; },
    ...properties,
  };
}

for (const storageBlocked of [false, true]) {
  const root = element({ scrollHeight: 1200 });
  const input = element({ value: "" });
  const clear = element();
  const count = element();
  const empty = element();
  const grid = element();
  const theme = element();
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
  };
  vm.runInNewContext(source, {
    document: {
      documentElement: root,
      querySelector: (selector) => selectors[selector] || null,
      querySelectorAll: (selector) => ({ ".filter-button": filters, ".project-card": cards }[selector] || []),
      addEventListener() {},
    },
    window: { matchMedia: () => ({ matches: true }), innerHeight: 800, scrollY: 0, addEventListener() {} },
    localStorage: {
      getItem() { if (storageBlocked) throw new Error("blocked"); return null; },
      setItem() { if (storageBlocked) throw new Error("blocked"); },
    },
    Intl, Date, setInterval() {}, requestAnimationFrame() {},
  });
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
  console.log(`Search, filter, clear, count, theme: OK (storageBlocked=${storageBlocked})`);
}
