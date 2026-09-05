/* ═══════════════════════════════════════════════════════════════════════
   DION — shared script for every page.
   Edit the DION object below and the change appears on all seven pages.

   Anything written as { el: "...", en: "..." } is Greek first, English
   second. Greek is what a visitor sees unless they flip the EN switch.
   ═══════════════════════════════════════════════════════════════════════ */

const DION = {

  /* ── the basics ──────────────────────────────────────────────────── */
  phone: "+30 694 822 2527",
  address: ["28is Oktovriou 22", "Palea Fokea 190 13, Greece"],
  /* Google lists a Tuesday 08:30–15:00 slot too, which looks like a stale
     entry rather than a real morning shift — worth checking your listing. */
  hours: {
    el: ["Ανοιχτά από τις 20:30 · Παρασκευή από τις 21:00", "Κλειστά τις Κυριακές"],
    en: ["Open from 20:30 · Friday from 21:00", "Closed Sundays"]
  },
  mapUrl: "https://www.google.com/maps/search/?api=1&query=Dion&query_place_id=ChIJa93n6GrtoRQRnKa6rMdH4ck",
  instagram: { handle: "@yourhandle", url: "https://instagram.com/" },

  /* Every "book a table" button dials this number. */
  cta: { el: "Κλείσε τραπέζι", en: "Book a table" },

  /* WhatsApp button on the Contact page. Set active:false to hide it.
     Leave number empty to reuse the phone number above. */
  whatsapp: { active: true, number: "" },

  /* ── the announcement bar ────────────────────────────────────────── */
  /* Set active:true to show a strip across the top of every page.
     A visitor can dismiss it, and it stays dismissed for that visit. */
  announcement: {
    active: false,
    el: "Απόψε στο DION — DJ set από τις 21:30.",
    en: "Tonight at DION — DJ set from 21:30."
  },

  /* ── events ──────────────────────────────────────────────────────── */
  /* Leave the list empty and the Events page drops out of the menu
     entirely — nobody lands on an empty page. Set showEventsWhenEmpty
     to true if you would rather keep the link and show the "nothing
     scheduled" message instead.

     Dates are yyyy-mm-dd for sorting only; the page prints them
     day-first in whichever language is showing. Anything dated before
     today disappears on its own, so old nights never need deleting.

     To add one, copy this shape:

     { date: "2026-09-19", time: "21:30",
       title: { el: "DJ set", en: "DJ set" },
       text:  { el: "Λίγα λόγια για τη βραδιά.",
                en: "A line or two about the night." } },
  */
  showEventsWhenEmpty: false,
  events: [],

  /* ── the drinks list ─────────────────────────────────────────────── */
  /* Categories print in this order. A category with no items is skipped,
     so you can fill them in one at a time. Prices are optional — leave
     "" and nothing is printed. */
  drinks: [
    {
      name: { el: "Signature Cocktails", en: "Signature Cocktails" },
      items: [
        { name: "Mastiha Spritz",  price: "",
          of: { el: "μαστίχα, αφρώδες, σόδα, λεμόνι",       en: "mastiha, sparkling, soda, lemon" } },
        { name: "Olive Oil Sour",  price: "",
          of: { el: "τσίπουρο, λεμόνι, μέλι, ελαιόλαδο",    en: "tsipouro, lemon, honey, olive oil" } },
        { name: "Aegean Negroni",  price: "",
          of: { el: "ελληνικό τζιν, γλυκό βερμούτ, bitter", en: "Greek gin, sweet vermouth, bitter" } },
        { name: "Frozen Rakomelo", price: "",
          of: { el: "ρακή, θυμαρίσιο μέλι, γαρύφαλλο",      en: "raki, thyme honey, clove" } },
        { name: "Cypress & Tonic", price: "",
          of: { el: "ελληνικό τζιν, δεντρολίβανο, γκρέιπφρουτ", en: "Greek gin, rosemary, grapefruit" } },
        { name: "Kalimera",        price: "",
          of: { el: "βότκα, βύσσινο, δυόσμος",              en: "vodka, sour cherry, mint" } }
      ]
    },
    { name: { el: "Κλασικά Cocktails", en: "Classics" },       items: [] },
    { name: { el: "Κρασί",             en: "Wine" },           items: [] },
    { name: { el: "Ελληνικές Ετικέτες", en: "Greek Bottles" },  items: [] },
    { name: { el: "Μπύρα",             en: "Beer" },           items: [] },
    { name: { el: "Αποστάγματα",       en: "Spirits" },        items: [] },
    { name: { el: "Χωρίς Αλκοόλ",      en: "Alcohol-Free" },   items: [] }
  ],
  drinksFootnote: {
    el: "Ο κατάλογος αλλάζει με την εποχή — ρώτησέ μας τι είναι καλό απόψε.",
    en: "The list moves with the season — ask what's good tonight."
  },

  /* ── the entrance animation (home page only) ─────────────────────── */
  introOncePerSession: true,
  doorsAt: 2850,
  doorsDur: 1150,
  maxHold: 2200
};


/* ═══ 0. LANGUAGE ══════════════════════════════════════════════════════
   Both languages ship inside every page; CSS shows one set and hides the
   other. The head script has already picked one before first paint, so
   all this does is handle the toggle and keep the <title> in step.     */
const LANG = (function(){
  const root = document.documentElement;
  const get  = () => root.getAttribute("data-lang") === "en" ? "en" : "el";

  function set(l){
    l = (l === "en") ? "en" : "el";
    root.lang = l;
    root.setAttribute("data-lang", l);
    const title = root.getAttribute("data-title-" + l);
    if (title) document.title = title;
    try { localStorage.setItem("dion-lang", l); } catch(e){}
    dispatchEvent(new CustomEvent("dion:lang", { detail: l }));
  }

  set(get());                                   // sync the title on load

  const btn = document.getElementById("lang");
  if (btn) btn.addEventListener("click", () => set(get() === "el" ? "en" : "el"));

  return { get, set };
})();

/* Picks the right half of an { el, en } pair. Plain strings pass through
   untouched, so a value that is the same in both languages can stay one
   string in the config above. */
function pick(v){
  if (v && typeof v === "object" && !Array.isArray(v)) return v[LANG.get()] || v.el || "";
  return v || "";
}

/* Builds the two-language markup for anything written into the page by
   this script, so switching language never needs a reload. */
function both(v){
  if (v && typeof v === "object" && !Array.isArray(v)) {
    return `<span class="l-el">${v.el || ""}</span><span class="l-en">${v.en || v.el || ""}</span>`;
  }
  return v || "";
}


/* ═══ 1. CONFIG → PAGE ═════════════════════════════════════════════════ */
(function(){
  const set  = (id, v) => { const el = document.getElementById(id); if (el && v) el.innerHTML = v; };
  const tel  = "tel:" + DION.phone.replace(/[^\d+]/g, "");

  document.querySelectorAll("[data-phone]").forEach(el => el.setAttribute("href", tel));
  document.querySelectorAll("[data-cta-label]").forEach(el => el.innerHTML = both(DION.cta));

  set("cAddr1", DION.address[0]);
  set("cAddr2", DION.address[1]);
  set("fAddr",  DION.address.join(", "));
  set("cHours1", both({ el: DION.hours.el[0], en: DION.hours.en[0] }));
  set("cHours2", both({ el: DION.hours.el[1], en: DION.hours.en[1] }));
  set("fHours",  both({ el: DION.hours.el[0], en: DION.hours.en[0] }));
  set("cPhone",  DION.phone);
  set("fPhone",  DION.phone);
  set("cIgHandle", DION.instagram.handle);

  ["cIg", "fIg"].forEach(id => { const el = document.getElementById(id); if (el) el.href = DION.instagram.url; });
  const map = document.getElementById("cMap"); if (map) map.href = DION.mapUrl;
  document.querySelectorAll("#year").forEach(el => el.textContent = new Date().getFullYear());

  const wa = document.getElementById("cWa");
  if (wa && DION.whatsapp && DION.whatsapp.active) {
    const num = (DION.whatsapp.number || DION.phone).replace(/[^\d]/g, "");
    if (num) { wa.href = "https://wa.me/" + num; wa.hidden = false; }
  }
})();


/* ═══ 2. THE DRINKS MENU ═══════════════════════════════════════════════ */
(function(){
  const host = document.getElementById("drinkMenu");
  if (!host) return;

  const groups = (DION.drinks || []).filter(g => g.items && g.items.length);
  host.innerHTML = groups.map(g => `
    <div class="menu__group rv">
      <h2 class="menu__head">${both(g.name)}</h2>
      <ul class="list">
        ${g.items.map(d => `<li><b>${d.name}</b>${d.price ? `<i>${d.price}</i>` : ""}<em>${both(d.of)}</em></li>`).join("")}
      </ul>
    </div>`).join("");

  const foot = document.getElementById("drinkFoot");
  if (foot) foot.innerHTML = both(DION.drinksFootnote);
})();


/* ═══ 3. EVENTS ════════════════════════════════════════════════════════
   Anything dated before today is dropped, so the page tidies itself. If
   nothing is left, the Events link is pulled out of the menu and the
   footer unless showEventsWhenEmpty is on.                             */
(function(){
  const MONTHS = {
    el: ["Ιανουαρίου","Φεβρουαρίου","Μαρτίου","Απριλίου","Μαΐου","Ιουνίου",
         "Ιουλίου","Αυγούστου","Σεπτεμβρίου","Οκτωβρίου","Νοεμβρίου","Δεκεμβρίου"],
    en: ["January","February","March","April","May","June",
         "July","August","September","October","November","December"]
  };
  const DAYS = {
    el: ["Κυριακή","Δευτέρα","Τρίτη","Τετάρτη","Πέμπτη","Παρασκευή","Σάββατο"],
    en: ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
  };

  /* Day-first, spelled out, in both languages. */
  function when(iso, time){
    const p = String(iso).split("-");
    const d = new Date(+p[0], +p[1] - 1, +p[2]);
    if (isNaN(d)) return { el: iso, en: iso };
    const out = {};
    ["el", "en"].forEach(l => {
      out[l] = `${DAYS[l][d.getDay()]} ${d.getDate()} ${MONTHS[l][d.getMonth()]}`
             + (time ? ` · ${time}` : "");
    });
    return out;
  }

  const today = new Date(); today.setHours(0, 0, 0, 0);
  const live = (DION.events || [])
    .filter(e => { const d = new Date(e.date); return !isNaN(d) && d >= today; })
    .sort((a, b) => String(a.date).localeCompare(String(b.date)));

  const empty = !live.length;

  if (empty && !DION.showEventsWhenEmpty) {
    document.querySelectorAll('[data-nav="events"]').forEach(el => el.remove());
  }

  const list = document.getElementById("eventList");
  if (!list) return;                                  // not the Events page

  const blank = document.getElementById("eventEmpty");
  if (empty) {
    list.hidden = true;
    if (blank) blank.hidden = false;
    return;
  }

  list.innerHTML = live.map(e => {
    const w = when(e.date, e.time);
    return `<li class="rv">
      <p class="events__when">${both(w)}</p>
      <h2 class="events__title">${both(e.title)}</h2>
      ${e.text ? `<p class="events__text">${both(e.text)}</p>` : ""}
    </li>`;
  }).join("");
})();


/* ═══ 4. THE ANNOUNCEMENT BAR ══════════════════════════════════════════
   Sits above the header. The nav is pushed down by its exact height, so
   nothing overlaps whether the header is the transparent home version or
   the solid one on every other page.                                   */
(function(){
  const bar = document.getElementById("announce");
  const a   = DION.announcement;
  if (!bar || !a || !a.active || !(a.el || a.en)) return;

  const key = "dion-ann-" + (a.el || a.en).slice(0, 40);
  try { if (sessionStorage.getItem(key)) return; } catch(e){}

  const text = document.getElementById("annText");
  if (text) text.innerHTML = both({ el: a.el, en: a.en });
  bar.hidden = false;
  document.body.classList.add("has-announce");

  const measure = () =>
    document.documentElement.style.setProperty("--ann-h", bar.offsetHeight + "px");
  measure();
  addEventListener("resize", measure, { passive: true });
  addEventListener("dion:lang", measure);            // Greek and English differ in length

  const close = document.getElementById("annClose");
  if (close) close.addEventListener("click", () => {
    bar.remove();
    document.body.classList.remove("has-announce");
    document.documentElement.style.setProperty("--ann-h", "0px");
    try { sessionStorage.setItem(key, "1"); } catch(e){}
  });
})();


/* ═══ 5. THE ENTRANCE (home page only) ═════════════════════════════════ */
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


/* ═══ 6. NO BROKEN PICTURES ════════════════════════════════════════════ */
addEventListener("error", e => {
  const el = e.target;
  if (el && el.tagName === "IMG") el.classList.add("is-failed");
}, true);


/* ═══ 7. NAVIGATION ════════════════════════════════════════════════════ */
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


/* ═══ 8. REVEALS ═══════════════════════════════════════════════════════ */
(function(){
  const items = document.querySelectorAll(".rv, .rv-fade");
  if (!items.length) return;
  if (!("IntersectionObserver" in window)) { items.forEach(el => el.classList.add("in")); return; }
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add("in"); obs.unobserve(en.target); } });
  }, { rootMargin: "0px 0px -10% 0px", threshold: .06 });
  items.forEach(el => io.observe(el));
})();


/* ═══ 9. LIGHTBOX — tap any picture, then pinch, wheel or drag to zoom ══
   Works for the gallery grid and for the overlapping plates on the other
   pages: anything with [data-full] joins the same set, so the arrows step
   through every picture on the page.                                    */
(function(){
  const box = document.getElementById("lightbox");
  if (!box) return;
  const img      = box.querySelector("#lbImg");
  const stage    = box.querySelector(".lb__stage");
  const closeBtn = box.querySelector(".lb__close");
  const prevBtn  = box.querySelector(".lb__nav--prev");
  const nextBtn  = box.querySelector(".lb__nav--next");
  const shots = [...document.querySelectorAll("[data-full]")];
  if (!shots.length) return;

  const MIN = 1, MAX = 5;
  let i = 0, scale = 1, tx = 0, ty = 0, last = null;

  const apply = ease => {
    img.classList.toggle("is-eased", !!ease);
    img.style.transform = `translate(${tx}px, ${ty}px) scale(${scale})`;
    const z = scale > 1.01;
    box.classList.toggle("is-zoomed", z);
    stage.classList.toggle("is-zoomed", z);
    if (ease) setTimeout(() => img.classList.remove("is-eased"), 300);
  };
  const reset = ease => { scale = 1; tx = ty = 0; apply(ease); };

  /* Keep the picture from being dragged off screen entirely. */
  function clamp(){
    const r = img.getBoundingClientRect();
    const ox = Math.max(0, (r.width  - stage.clientWidth)  / 2);
    const oy = Math.max(0, (r.height - stage.clientHeight) / 2);
    tx = Math.min(ox, Math.max(-ox, tx));
    ty = Math.min(oy, Math.max(-oy, ty));
  }
  function zoomTo(next, cx, cy){
    next = Math.min(MAX, Math.max(MIN, next));
    const r = img.getBoundingClientRect();
    const px = cx - (r.left + r.width / 2);
    const py = cy - (r.top  + r.height / 2);
    const k = next / scale;
    tx = tx - px * (k - 1);
    ty = ty - py * (k - 1);
    scale = next;
    if (scale === 1) { tx = ty = 0; } else clamp();
  }

  function show(n, ease){
    i = (n + shots.length) % shots.length;
    const b = shots[i];
    img.src = b.dataset.full;
    const inner = b.querySelector("img");
    img.alt = inner ? inner.alt : "";
    reset(ease);
  }
  function open(n){
    show(n, false);
    box.classList.add("is-open");
    document.body.classList.add("menu-open");   // reuses the scroll lock
    closeBtn.focus();
  }
  function shut(){
    box.classList.remove("is-open");
    document.body.classList.remove("menu-open");
    reset(false);
    if (shots[i]) shots[i].focus();
  }

  shots.forEach((b, n) => b.addEventListener("click", () => open(n)));
  closeBtn.addEventListener("click", shut);
  if (prevBtn) prevBtn.addEventListener("click", e => { e.stopPropagation(); show(i - 1, true); });
  if (nextBtn) nextBtn.addEventListener("click", e => { e.stopPropagation(); show(i + 1, true); });

  addEventListener("keydown", e => {
    if (!box.classList.contains("is-open")) return;
    if (e.key === "Escape")      { e.preventDefault(); shut(); }
    if (e.key === "ArrowLeft")   show(i - 1, true);
    if (e.key === "ArrowRight")  show(i + 1, true);
    if (e.key === "+" || e.key === "=") { zoomTo(scale * 1.4, innerWidth / 2, innerHeight / 2); apply(true); }
    if (e.key === "-")           { zoomTo(scale / 1.4, innerWidth / 2, innerHeight / 2); apply(true); }
    if (e.key === "0")           reset(true);
  });

  /* Desktop: wheel or trackpad pinch. */
  stage.addEventListener("wheel", e => {
    e.preventDefault();
    zoomTo(scale * (e.deltaY < 0 ? 1.18 : 1 / 1.18), e.clientX, e.clientY);
    apply(false);
  }, { passive:false });

  /* Double click / double tap toggles between fit and 2.5x. Handled purely
     in the pointer logic below so mouse and touch take the same path — a
     separate dblclick listener would fire alongside it and cancel itself. */
  let lastTap = 0;
  function toggleZoom(x, y){
    if (scale > 1.01) reset(true);
    else { zoomTo(2.5, x, y); apply(true); }
  }

  /* Touch and mouse: one finger pans, two fingers pinch. */
  const pts = new Map();
  let startDist = 0, startScale = 1, startMid = null, moved = false;

  const dist = a => Math.hypot(a[0].x - a[1].x, a[0].y - a[1].y);
  const mid  = a => ({ x:(a[0].x + a[1].x) / 2, y:(a[0].y + a[1].y) / 2 });

  stage.addEventListener("pointerdown", e => {
    stage.setPointerCapture(e.pointerId);
    pts.set(e.pointerId, { x:e.clientX, y:e.clientY });
    moved = false;
    const a = [...pts.values()];
    if (a.length === 2) { startDist = dist(a); startScale = scale; startMid = mid(a); }
    else { last = { x:e.clientX, y:e.clientY }; }
    if (a.length === 1) stage.classList.add("is-panning");
  });

  stage.addEventListener("pointermove", e => {
    if (!pts.has(e.pointerId)) return;
    pts.set(e.pointerId, { x:e.clientX, y:e.clientY });
    const a = [...pts.values()];
    if (a.length === 2) {
      const d = dist(a);
      if (startDist) { zoomTo(startScale * (d / startDist), startMid.x, startMid.y); apply(false); }
      moved = true;
    } else if (a.length === 1 && last && scale > 1.01) {
      tx += e.clientX - last.x;
      ty += e.clientY - last.y;
      last = { x:e.clientX, y:e.clientY };
      clamp(); apply(false);
      moved = true;
    }
  });

  function release(e){
    pts.delete(e.pointerId);
    if (pts.size < 2) startDist = 0;
    if (pts.size === 0) {
      last = null;
      stage.classList.remove("is-panning");
      /* A clean tap: double tap zooms, single tap on the backdrop closes. */
      if (!moved) {
        const now = Date.now();
        if (now - lastTap < 300) { toggleZoom(e.clientX, e.clientY); lastTap = 0; }
        else {
          lastTap = now;
          setTimeout(() => {
            if (lastTap && Date.now() - lastTap >= 290 && scale <= 1.01
                && e.target === stage) shut();
          }, 300);
        }
      }
    }
  }
  stage.addEventListener("pointerup", release);
  stage.addEventListener("pointercancel", release);
  addEventListener("resize", () => { if (scale > 1.01) { clamp(); apply(false); } });
})();
