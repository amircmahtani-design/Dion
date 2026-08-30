/* ═══════════════════════════════════════════════════════════════════════
   DION — shared script for every page.
   Edit the DION object below and the change appears on all six pages.
   ═══════════════════════════════════════════════════════════════════════ */

const DION = {
  phone: "+30 694 822 2527",
  address: ["28is Oktovriou 22", "Palea Fokea 190 13, Greece"],
  /* Google lists a Tuesday 08:30–15:00 slot too, which looks like a stale
     entry rather than a real morning shift — worth checking your listing. */
  hours: ["Open from 20:30 · Friday from 21:00", "Closed Sundays"],
  mapUrl: "https://www.google.com/maps/search/?api=1&query=Dion&query_place_id=ChIJa93n6GrtoRQRnKa6rMdH4ck",
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

/* ═══ 6. LIGHTBOX — tap any picture, then pinch, wheel or drag to zoom ══
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
