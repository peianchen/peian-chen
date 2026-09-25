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
    theme === "blueprint" ? "#eaf2ee" : "#07110f",
  );
};

const savedTheme = localStorage.getItem("portfolio-theme");
setTheme(savedTheme === "blueprint" ? "blueprint" : "midnight");

themeButton?.addEventListener("click", () => {
  const nextTheme = root.dataset.theme === "midnight" ? "blueprint" : "midnight";
  setTheme(nextTheme);
  localStorage.setItem("portfolio-theme", nextTheme);
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

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const filter = button.dataset.filter;
    filterButtons.forEach((item) => {
      const active = item === button;
      item.classList.toggle("is-active", active);
      item.setAttribute("aria-pressed", String(active));
    });

    let count = 0;
    projectCards.forEach((card) => {
      const matches = filter === "all" || card.dataset.category.split(" ").includes(filter);
      card.classList.toggle("is-hidden", !matches);
      if (matches) count += 1;
    });
    if (visibleCount) visibleCount.textContent = String(count);
  });
});

const revealItems = document.querySelectorAll(".reveal");
if (reduceMotion || !("IntersectionObserver" in window)) {
  revealItems.forEach((item) => item.classList.add("is-visible"));
} else {
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
    window.location.href = "https://github.com/chen861019";
  }
});
