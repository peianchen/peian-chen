const root = document.documentElement;
const themeButton = document.querySelector(".theme-toggle");
const menuButton = document.querySelector(".menu-toggle");
const navigation = document.querySelector(".primary-nav");
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

const setTheme = (theme) => {
  root.dataset.theme = theme;
  themeButton?.setAttribute("aria-pressed", String(theme === "blueprint"));
  document.querySelector('meta[name="theme-color"]')?.setAttribute(
    "content",
    theme === "blueprint" ? "#edf3fc" : "#060d1c",
  );
};

let savedTheme;
try {
  savedTheme = localStorage.getItem("portfolio-theme");
} catch {
  // Theme switching remains usable when browser storage is unavailable.
}
setTheme(savedTheme === "blueprint" ? "blueprint" : "midnight");

themeButton?.addEventListener("click", () => {
  const nextTheme = root.dataset.theme === "midnight" ? "blueprint" : "midnight";
  setTheme(nextTheme);
  try {
    localStorage.setItem("portfolio-theme", nextTheme);
  } catch {
    // Persisting a preference is optional.
  }
});

const setMenu = (open) => {
  menuButton?.setAttribute("aria-expanded", String(open));
  navigation?.classList.toggle("is-open", open);
};

menuButton?.addEventListener("click", () => {
  setMenu(menuButton.getAttribute("aria-expanded") !== "true");
});

navigation?.addEventListener("click", (event) => {
  if (event.target.closest("a")) setMenu(false);
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") setMenu(false);
});

const filterButtons = [...document.querySelectorAll(".filter-button")];
const projectCards = [...document.querySelectorAll(".project-card")];
const visibleCount = document.querySelector("#visible-count");
const searchInput = document.querySelector("#project-search");
const clearSearch = document.querySelector(".search-clear");
const emptyResult = document.querySelector(".search-empty");
const projectGrid = document.querySelector("#project-grid");
const searchIndex = projectCards.map((card) => ({
  card,
  text: card.textContent.normalize("NFKC").toLocaleLowerCase(),
}));
let activeFilter = "all";
const languageLink = document.querySelector('.language-switch');
const initialUrl = window.location ? new URL(window.location.href) : null;
if (initialUrl && searchInput) {
  searchInput.value = initialUrl.searchParams.get('q') || '';
  const requestedFilter = initialUrl.searchParams.get('filter');
  if (filterButtons.some(button => button.dataset.filter === requestedFilter)) activeFilter = requestedFilter;
}

const syncLanguageLink = () => {
  if (!languageLink || !window.location) return;
  const target = new URL(languageLink.getAttribute('href'), window.location.href);
  target.hash = window.location.hash;
  target.search = window.location.search;
  languageLink.setAttribute('href', target.href);
};

const updateProjects = () => {
  const query = (searchInput?.value || "").normalize("NFKC").trim().toLocaleLowerCase();
  const terms = query.split(/\s+/).filter(Boolean);
  let count = 0;
  searchIndex.forEach(({ card, text }) => {
    const categoryMatches = activeFilter === "all" || card.dataset.category.split(" ").includes(activeFilter);
    const matches = categoryMatches && terms.every((term) => text.includes(term));
    card.classList.toggle("is-hidden", !matches);
    if (matches) count += 1;
  });
  if (visibleCount) visibleCount.textContent = String(count);
  projectGrid?.classList.toggle("is-single-result", count === 1);
  if (emptyResult) emptyResult.hidden = count !== 0;
  if (clearSearch) clearSearch.hidden = !searchInput?.value;
  document.querySelectorAll('.catalog-heading').forEach(heading => {
    let next = heading.nextElementSibling;
    let anyVisible = false;
    while (next && !next.classList.contains('catalog-heading')) {
      if (next.classList.contains('project-card') && !next.classList.contains('is-hidden')) anyVisible = true;
      next = next.nextElementSibling;
    }
    heading.hidden = !anyVisible;
  });
  filterButtons.forEach(button => {
    const selected = button.dataset.filter === activeFilter;
    button.setAttribute('aria-pressed', String(selected));
    button.classList.toggle('is-active', selected);
  });
  if (window.location && window.history && searchInput) {
    const url = new URL(window.location.href);
    query ? url.searchParams.set('q', searchInput.value) : url.searchParams.delete('q');
    activeFilter === 'all' ? url.searchParams.delete('filter') : url.searchParams.set('filter', activeFilter);
    window.history.replaceState(null, '', url);
  }
  syncLanguageLink();
};

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    activeFilter = button.dataset.filter;
    filterButtons.forEach((item) => {
      const active = item === button;
      item.classList.toggle("is-active", active);
      item.setAttribute("aria-pressed", String(active));
    });

    updateProjects();
  });
});
searchInput?.addEventListener("input", updateProjects);
clearSearch?.addEventListener("click", () => {
  if (searchInput) searchInput.value = "";
  updateProjects();
  searchInput?.focus();
});
updateProjects();
window.addEventListener('hashchange', syncLanguageLink);
// A course deep link should stay visible even after a previous filtered view.
const courseLink = document.querySelector('.primary-nav a[href="#coursework"]');
courseLink?.addEventListener('click', () => {
  activeFilter = 'all';
  if (searchInput) searchInput.value = '';
  updateProjects();
});

const revealItems = document.querySelectorAll(".reveal");
if (reduceMotion || !("IntersectionObserver" in window)) {
  revealItems.forEach((item) => item.classList.add("is-visible"));
} else {
  root.classList.add('js-motion');
  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.12 },
  );
  revealItems.forEach((item) => revealObserver.observe(item));
}

const navLinks = [...document.querySelectorAll('.primary-nav a[href^="#"]')];
const sections = navLinks
  .map((link) => document.querySelector(link.getAttribute("href")))
  .filter(Boolean);

if ("IntersectionObserver" in window) {
  const sectionObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        navLinks.forEach((link) => {
          link.classList.toggle("is-active", link.getAttribute("href") === `#${entry.target.id}`);
        });
      });
    },
    { rootMargin: "-35% 0px -55%", threshold: 0 },
  );
  sections.forEach((section) => sectionObserver.observe(section));
}

const progressBar = document.querySelector("#scroll-progress");
let scrollFrame = null;
const updateProgress = () => {
  const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
  const ratio = maxScroll > 0 ? window.scrollY / maxScroll : 0;
  if (progressBar) progressBar.style.transform = `scaleX(${Math.min(1, ratio)})`;
  scrollFrame = null;
};

window.addEventListener(
  "scroll",
  () => {
    if (!scrollFrame) scrollFrame = requestAnimationFrame(updateProgress);
  },
  { passive: true },
);
updateProgress();

const timeNode = document.querySelector("#taipei-time");
const timeFormatter = new Intl.DateTimeFormat("en-GB", {
  timeZone: "Asia/Taipei",
  hour: "2-digit",
  minute: "2-digit",
  second: "2-digit",
  hour12: false,
});
const updateTime = () => {
  if (timeNode) timeNode.textContent = `TPE ${timeFormatter.format(new Date())}`;
};
updateTime();
setInterval(updateTime, 1000);

const copyButton = document.querySelector(".copy-handle");
const toast = document.querySelector(".toast");
let toastTimer;
copyButton?.addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(copyButton.dataset.copy);
    toast?.classList.add("is-visible");
    copyButton.textContent = "COPIED";
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast?.classList.remove("is-visible");
      copyButton.textContent = "COPY HANDLE";
    }, 1800);
  } catch {
    window.location.href = "https://github.com/peianchen";
  }
});
