/* ═══════════════════════════════════════════════════════════════════════
   DION — shared script for every page.
   Edit the DION object below and the change appears on all six pages.
   ═══════════════════════════════════════════════════════════════════════ */

const DION = {
  phone: "+30 000 000 0000",
  address: ["Street name 00", "Town, Greece"],
  hours: ["Every day · 18:00 until late", "The courtyard fills up after 21:00"],
  mapUrl: "https://www.google.com/maps",
  instagram: { handle: "@yourhandle", url: "https://instagram.com/" },
  cta: "Reserve a table",

  drinks: [
    { name: "Mastiha Spritz",   of: "mastiha, sparkling, soda, lemon",   price: "" },
    { name: "Olive Oil Sour",   of: "tsipouro, lemon, honey, olive oil", price: "" },
    { name: "Aegean Negroni",   of: "Greek gin, sweet vermouth, bitter", price: "" },
    { name: "Frozen Rakomelo",  of: "raki, thyme honey, clove",          price: "" },
    { name: "Cypress & Tonic",  of: "Greek gin, rosemary, grapefruit",   price: "" },
    { name: "Kalimera",         of: "vodka, sour cherry, mint",          price: "" }
  ],
  drinksFootnote: "The list moves with the season — ask what's good tonight.",

  introOncePerSession: true,   // entrance plays once per browser session
  doorsAt: 2850,
  doorsDur: 1150,
  maxHold: 2200
};

/* ═══ 1. CONFIG → PAGE ═════════════════════════════════════════════════ */
(function(){
  const set = (id, v) => { const el = document.getElementById(id); if (el && v) el.textContent = v; };
  document.querySelectorAll("[data-cta]").forEach(el => el.textContent = DION.cta);
  document.querySelectorAll("[data-phone]").forEach(el => {
    el.setAttribute("href", "tel:" + DION.phone.replace(/\s/g, ""));
  });
  set("cAddr1", DION.address[0]);  set("cAddr2", DION.address[1]);
  set("cHours1", DION.hours[0]);   set("cHours2", DION.hours[1]);
  set("cPhone", DION.phone);       set("fPhone", DION.phone);
  set("fAddr", DION.address.join(", "));
  set("cIgHandle", DION.instagram.handle);
  ["cIg", "fIg"].forEach(id => { const el = document.getElementById(id); if (el) el.href = DION.instagram.url; });
  const map = document.getElementById("cMap"); if (map) map.href = DION.mapUrl;
  document.querySelectorAll("#year").forEach(el => el.textContent = new Date().getFullYear());

  const list = document.getElementById("drinkList");
  if (list && DION.drinks.length) {
    list.innerHTML = DION.drinks.map(d =>
      `<li><b>${d.name}</b>${d.price ? `<i>${d.price}</i>` : ""}<em>${d.of}</em></li>`
    ).join("");
    set("drinkFoot", DION.drinksFootnote);
  }
})();

/* ═══ 2. THE ENTRANCE (home page only) ═════════════════════════════════ */
(function(){
  const root = document.documentElement;
  const ent  = document.getElementById("entrance");
  const skip = document.getElementById("skip");
  const hero = document.getElementById("heroImg");
  if (!ent) return;                       // every page but the home page

  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  let finished = false;

  function finish(){
    if (finished) return;
    finished = true;
    root.classList.remove("intro-lock");
    root.classList.add("intro-over");
    root.style.setProperty("--intro-play","running");
    ent.classList.add("is-done");
    if (skip) skip.remove();
    setTimeout(() => ent.remove(), 500);
  }

  if (DION.introOncePerSession) {
    try {
      if (sessionStorage.getItem("dion-entered")) { ent.remove(); if (skip) skip.remove(); }
      else sessionStorage.setItem("dion-entered", "1");
    } catch(e){}
  }
  if (!document.getElementById("entrance")) {
    root.classList.add("intro-over");
    if (hero) hero.complete ? hero.classList.add("is-loaded")
      : hero.addEventListener("load", () => hero.classList.add("is-loaded"), { once:true });
    return;
  }

  root.classList.add("intro-lock");
  setTimeout(() => root.classList.remove("intro-lock"), 9000);

  /* Declared before the hero handlers: a cached hero completes synchronously
     and calls release() immediately, which would otherwise hit the TDZ. */
  let holding = false;
  function hold(){ if (heroReady || finished) return; holding = true; root.style.setProperty("--intro-play","paused"); }
  function release(){ if (!holding) return; holding = false; root.style.setProperty("--intro-play","running"); }

  let heroReady = false;
  function heroDone(){ heroReady = true; if (hero) hero.classList.add("is-loaded"); release(); }
  function heroFailed(){ heroReady = true; if (hero) hero.classList.add("is-failed"); release(); }
  if (hero) {
    if (hero.complete && hero.naturalWidth) heroDone();
    else if (hero.complete) heroFailed();
    else {
      hero.addEventListener("load", heroDone, { once:true });
      hero.addEventListener("error", heroFailed, { once:true });
    }
  }

  if (!reduce) {
    const wait = Math.max(0, DION.doorsAt - 120 - performance.now());
    setTimeout(() => { hold(); setTimeout(release, DION.maxHold); }, wait);
  }

  const doorR = ent.querySelector(".door--r");
  if (doorR) doorR.addEventListener("animationend", e => { if (e.animationName === "doorR") finish(); });
  setTimeout(finish, DION.doorsAt + DION.doorsDur + DION.maxHold + 900);
  if (reduce) setTimeout(finish, 1900);
  if (skip) skip.addEventListener("click", finish);
})();

/* ═══ 3. NO BROKEN PICTURES ════════════════════════════════════════════ */
addEventListener("error", e => {
  const el = e.target;
  if (el && el.tagName === "IMG") el.classList.add("is-failed");
}, true);

/* ═══ 4. NAVIGATION ════════════════════════════════════════════════════ */
(function(){
  const nav = document.getElementById("nav");
  const burger = document.getElementById("burger");
  const menu = document.getElementById("menu");
  if (!nav || !burger || !menu) return;

  if (nav.classList.contains("nav--overlay")) {
    const onScroll = () => nav.classList.toggle("is-stuck", scrollY > 40);
    addEventListener("scroll", onScroll, { passive:true }); onScroll();
  }

  const close = () => { document.body.classList.remove("menu-open"); burger.setAttribute("aria-expanded","false"); };
  burger.addEventListener("click", () => {
    const open = !document.body.classList.contains("menu-open");
    document.body.classList.toggle("menu-open", open);
    burger.setAttribute("aria-expanded", String(open));
  });
  menu.addEventListener("click", e => { if (e.target.closest("a")) close(); });
  addEventListener("keydown", e => { if (e.key === "Escape") close(); });
})();

/* ═══ 5. REVEALS ═══════════════════════════════════════════════════════ */
(function(){
  const items = document.querySelectorAll(".rv, .rv-fade");
  if (!items.length) return;
  if (!("IntersectionObserver" in window)) { items.forEach(el => el.classList.add("in")); return; }
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add("in"); obs.unobserve(en.target); } });
  }, { rootMargin: "0px 0px -10% 0px", threshold: .06 });
  items.forEach(el => io.observe(el));
})();

/* ═══ 6. GALLERY LIGHTBOX ══════════════════════════════════════════════ */
(function(){
  const box = document.getElementById("lightbox");
  const img = document.getElementById("lbImg");
  const closeBtn = document.getElementById("lbClose");
  if (!box || !img || !closeBtn) return;
  let last = null;
  document.querySelectorAll(".gal button").forEach(b => b.addEventListener("click", () => {
    last = b;
    img.src = b.dataset.full;
    img.alt = b.querySelector("img").alt;
    box.classList.add("is-open");
    closeBtn.focus();
  }));
  const shut = () => { box.classList.remove("is-open"); if (last) last.focus(); };
  closeBtn.addEventListener("click", shut);
  box.addEventListener("click", e => { if (e.target === box) shut(); });
  addEventListener("keydown", e => { if (e.key === "Escape" && box.classList.contains("is-open")) shut(); });
})();
