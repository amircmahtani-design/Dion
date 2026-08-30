#!/usr/bin/env python3
"""Builds the six DION pages from one shared shell so the nav, head and
footer can never drift apart. Run:  python3 build.py"""
import pathlib

OUT = pathlib.Path(__file__).parent

U = "https://images.unsplash.com/photo-"
def img(pid, w, h, q=72):
    return f"{U}{pid}?auto=format&amp;fit=crop&amp;w={w}&amp;h={h}&amp;q={q}"

PAGES = [
    ("index.html",   "Home",      "DION — Mainland Soul"),
    ("drinks.html",  "Drinks",    "Drinks · DION"),
    ("vibe.html",    "The Vibe",  "The Vibe · DION"),
    ("gallery.html", "Gallery",   "Gallery · DION"),
    ("about.html",   "About",     "About · DION"),
    ("contact.html", "Contact",   "Contact · DION"),
]

MARK_PATHS = """    <path d="M17 13 H83"/><path d="M83 13 V23 H17 V13"/>
    <path d="M30 24 C22 24 17 29 17 36 C17 43 22 48 29 48 C34 48 38 44 38 39 C38 35 35 32 31 32 C28 32 26 34 26 37"/>
    <path d="M70 24 C78 24 83 29 83 36 C83 43 78 48 71 48 C66 48 62 44 62 39 C62 35 65 32 69 32 C72 32 74 34 74 37"/>
    <path d="M31 47 L69 26"/><path d="M35 52 H65"/>
    <path d="M36 52 C35 76 35 112 36 138"/><path d="M64 52 C65 76 65 112 64 138"/>
    <path d="M43 57 V133 M50 57 V133 M57 57 V133 M40 61 V129 M60 61 V129"/>
    <path d="M35 138 C33 143 31 146 28 149 H72 C69 146 67 143 65 138"/>
    <path d="M28 149 V157 H72 V149"/><path d="M28 157 C27 159 26 161 24 162 M72 157 C73 159 74 161 76 162"/>
    <path d="M24 162 H76 M24 162 V174 H76 V162"/>
    <path d="M36 146 C50 150 64 138 68 118 C72 98 71 70 70 50"/>
    <path d="M68 118 C73 111 79 110 82 114 C78 120 72 122 68 118 Z"/>
    <path d="M70 96 C75 89 81 88 84 92 C80 98 74 100 70 96 Z"/>
    <path d="M70 72 C75 65 81 64 84 68 C80 74 74 76 70 72 Z"/>
    <path d="M70 52 C75 45 81 44 84 48 C80 54 74 56 70 52 Z"/>
    <path d="M36 146 C31 149 27 154 26 159"/>
    <path d="M33 148 C29 144 24 145 22 149 C26 153 31 152 33 148 Z"/>
    <path d="M28 155 C24 152 19 153 17 157 C21 161 26 160 28 155 Z"/>"""

DOOR_ART = """      <svg class="mark draw" viewBox="0 0 100 190" aria-hidden="true">
        <path class="seed" pathLength="100" d="M17 13 H83"/>
        <path class="seed" pathLength="100" d="M70 24 C78 24 83 29 83 36"/>
        <path class="s1" pathLength="100" d="M83 13 V23 H17 V13"/>
        <path class="s1" pathLength="100" d="M83 36 C83 43 78 48 71 48 C66 48 62 44 62 39 C62 35 65 32 69 32 C72 32 74 34 74 37"/>
        <path class="s1" pathLength="100" d="M30 24 C22 24 17 29 17 36 C17 43 22 48 29 48 C34 48 38 44 38 39 C38 35 35 32 31 32 C28 32 26 34 26 37"/>
        <path class="s2" pathLength="100" d="M31 47 L69 26"/>
        <path class="s2" pathLength="100" d="M35 52 H65"/>
        <path class="s2" pathLength="100" d="M36 52 C35 76 35 112 36 138"/>
        <path class="s2" pathLength="100" d="M64 52 C65 76 65 112 64 138"/>
        <path class="s3" pathLength="100" d="M43 57 V133 M50 57 V133 M57 57 V133 M40 61 V129 M60 61 V129"/>
        <path class="s4" pathLength="100" d="M35 138 C33 143 31 146 28 149 H72 C69 146 67 143 65 138"/>
        <path class="s4" pathLength="100" d="M28 149 V157 H72 V149"/>
        <path class="s4" pathLength="100" d="M28 157 C27 159 26 161 24 162 M72 157 C73 159 74 161 76 162"/>
        <path class="s4" pathLength="100" d="M24 162 H76 M24 162 V174 H76 V162"/>
        <path class="s5" pathLength="100" d="M36 146 C50 150 64 138 68 118 C72 98 71 70 70 50"/>
        <path class="s5" pathLength="100" d="M36 146 C31 149 27 154 26 159"/>
        <path class="s6" pathLength="100" d="M68 118 C73 111 79 110 82 114 C78 120 72 122 68 118 Z"/>
        <path class="s6" pathLength="100" d="M70 96 C75 89 81 88 84 92 C80 98 74 100 70 96 Z"/>
        <path class="s6" pathLength="100" d="M70 72 C75 65 81 64 84 68 C80 74 74 76 70 72 Z"/>
        <path class="s6" pathLength="100" d="M70 52 C75 45 81 44 84 48 C80 54 74 56 70 52 Z"/>
        <path class="s6" pathLength="100" d="M33 148 C29 144 24 145 22 149 C26 153 31 152 33 148 Z"/>
        <path class="s6" pathLength="100" d="M28 155 C24 152 19 153 17 157 C21 161 26 160 28 155 Z"/>
      </svg>
      <div class="intro-word"><b>DION</b><i>Mainland Soul</i></div>"""

ENTRANCE = f"""
<!-- ═══ THE ENTRANCE — home page only ═════════════════════════════════ -->
<div class="entrance" id="entrance" role="presentation">
  <div class="door door--l"><div class="door__art">
{DOOR_ART}
  </div></div>
  <div class="door door--r"><div class="door__art">
{DOOR_ART}
  </div></div>
</div>
<button class="skip" id="skip" type="button">Skip</button>
"""

CURVE = ('<svg class="curve curve--{c}" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true">'
         '<path fill="currentColor" d="M0 62C240 18 480 4 720 22s480 62 720 34v34H0V62Z"/></svg>')


def nav(active, overlay):
    cls = "nav nav--overlay" if overlay else "nav nav--solid"
    links = ""
    for href, label, _ in [(p[0], p[1], 0) for p in PAGES]:
        cur = ' aria-current="page"' if label == active else ""
        links += f'      <li><a href="{href}"{cur}>{label}</a></li>\n'
    return f"""<header class="{cls}" id="nav">
  <a class="nav__brand" href="index.html" aria-label="DION, home">
    <svg viewBox="0 0 100 190" aria-hidden="true"><use href="#dion-mark"/></svg>
    <span>DION<small>Mainland Soul</small></span>
  </a>
  <button class="nav__burger" id="burger" type="button" aria-label="Menu" aria-expanded="false"><span></span></button>
  <ul class="nav__links" id="menu">
{links}      <li><a class="btn nav__cta" href="contact.html" data-cta>Reserve a table</a></li>
  </ul>
  <a class="btn nav__cta" href="contact.html" data-cta>Reserve a table</a>
</header>"""


def footer(active):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if l == active else ""}>{l}</a>'
        for h, l, _ in PAGES)
    return f"""<footer class="foot">
  <div class="wrap">
    <a class="foot__brand" href="index.html" aria-label="DION, home">
      <svg viewBox="0 0 100 190" aria-hidden="true"><use href="#dion-mark"/></svg>
      <span><b>DION</b><small>Mainland Soul</small></span>
    </a>
    <nav aria-label="Footer">{links}</nav>
    <div class="foot__col">
      <span id="fAddr">Street name 00, Town, Greece</span>
      <a id="fPhone" href="tel:+300000000000" data-phone>+30 000 000 0000</a>
      <a id="fIg" href="https://instagram.com/" target="_blank" rel="noopener">Instagram</a>
    </div>
    <div class="foot__base">
      <span>© <span id="year">2026</span> DION · Mainland Soul</span>
      <span>Greek in the glass, Greek at heart.</span>
    </div>
  </div>
</footer>"""


def shell(filename, active, title, desc, body, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<script>document.documentElement.className="js"</script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B0B0A">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="hero-wide.jpeg">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com" crossorigin>
<link rel="stylesheet" media="print" onload="this.media='all'"
      href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..600&family=Jost:wght@300;400;500&family=Caveat:wght@500&display=swap">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..600&family=Jost:wght@300;400;500&family=Caveat:wght@500&display=swap"></noscript>
{extra_head}<link rel="stylesheet" href="assets/site.css">
</head>
<body>

<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="dion-mark" viewBox="0 0 100 190">
  <g fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
{MARK_PATHS}
  </g>
</symbol></svg>
{ENTRANCE if filename == "index.html" else ""}
{nav(active, overlay=(filename == "index.html"))}

<main>
{body}
</main>

{LIGHTBOX}

{footer(active)}
<script src="assets/site.js"></script>
</body>
</html>
"""


def pagehead(eyebrow, heading, lede="", hand=""):
    out = f"""<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow rv">{eyebrow}</p>
    <h1 class="rv">{heading}</h1>"""
    if lede:
        out += f'\n    <p class="lede rv">{lede}</p>'
    if hand:
        out += f'\n    <p class="hand rv">{hand}</p>'
    return out + "\n  </div>\n</section>"


def plate(slot_prefix, a, b, c=None):
    """The overlapping composition: a tall plate, a square riding over its
    bottom-right corner, and an optional small accent at bottom-left.
    Each figure is a button so it opens in the zoomable lightbox."""
    def cell(cls, slot, spec):
        pid, w, h, alt = spec
        return (f'    <!-- photo slot: {slot} — swap src for img/{slot}.jpg -->\n'
                f'    <button type="button" class="fig {cls} rv" '
                f'data-full="{img(pid, 1600, int(1600*h/w), 80)}" '
                f'aria-label="Open photo: {alt}">\n'
                f'      <img src="{img(pid, w, h)}" width="{w}" height="{h}" '
                f'loading="lazy" decoding="async" alt="{alt}">\n    </button>')
    cls = "overlap has-c" if c else "overlap"
    out = [f'  <div class="{cls}">']
    out.append(cell("fig--a", slot_prefix + "-a", a))
    out.append(cell("fig--b", slot_prefix + "-b", b))
    if c:
        out.append(cell("fig--c", slot_prefix + "-c", c))
    out.append("  </div>")
    return "\n".join(out)


LIGHTBOX = """<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo">
  <div class="lb__stage">
    <img id="lbImg" src="" alt="">
  </div>
  <button type="button" class="lb__close" aria-label="Close">&times;</button>
  <button type="button" class="lb__nav lb__nav--prev" aria-label="Previous photo">&#8249;</button>
  <button type="button" class="lb__nav lb__nav--next" aria-label="Next photo">&#8250;</button>
  <p class="lb__hint">Pinch, scroll or double-tap to zoom</p>
</div>"""


# ── page bodies ────────────────────────────────────────────────────────
HERO = f"""<section class="hero">
  <picture class="hero__media" id="heroMedia">
    <img id="heroImg" src="hero-wide.jpeg" width="2000" height="1330" fetchpriority="high"
         decoding="async" alt="The DION courtyard on a summer night — string lights over full tables and the bar glowing through open shutters">
  </picture>
  <div class="hero__inner">
    <h1>Good vibes.<em>Mainland soul.</em></h1>
    <svg class="squiggle" viewBox="0 0 74 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true">
      <path d="M1 8C7 1 12 1 18 7c6 6 11 6 17 0 6-6 11-6 17 0 6 6 11 6 17-1"/>
    </svg>
    <p>Incredible drinks, feel-good energy and unforgettable nights.</p>
    <p class="hand">Greek in the glass, Greek at heart.
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">
        <path d="M12 21C4 15 2 11 3.6 7.7 5.2 4.4 9.6 4.6 12 8.4c2.4-3.8 6.8-4 8.4-.7C22 11 20 15 12 21Z"/>
      </svg>
    </p>
    <a class="btn" href="drinks.html">See what's inside
      <svg width="16" height="9" viewBox="0 0 16 9" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true">
        <path d="M0 4.5h14M10.5 1l3.6 3.5-3.6 3.5"/></svg>
    </a>
  </div>
  <a class="scroll-cue" href="#strip" aria-hidden="true" tabindex="-1">Scroll</a>
</section>"""

STRIP = """<svg class="curve curve--cream" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true">
  <path fill="currentColor" d="M0 62C240 18 480 4 720 22s480 62 720 34v34H0V62Z"/>
</svg>
<section class="strip" id="strip">
  <div class="wrap strip__grid">
    <div class="feat rv">
      <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M9 13h30L24 29 9 13Z"/><path d="M24 29v9M17 39h14"/><path d="M31.5 9c-1.5 1.5-3 3-4.5 4.5"/><circle cx="33" cy="7" r="2.6"/>
      </svg>
      <h3>Incredible drinks</h3><p>Cocktails worth coming back for.</p>
    </div>
    <div class="feat rv">
      <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M24 41c0-11 2-21 7-30"/><path d="M27 30c-6-1-10-6-9-11 6 0 10 5 9 11Z"/>
        <path d="M28.5 21c5-2 8-7 7-12-6 1-9 7-7 12Z"/><path d="M25 37c-5 0-9-4-9-8 5 0 9 4 9 8Z"/>
      </svg>
      <h3>Greek at heart</h3><p>Greek ingredients. Greek bottles. No fuss.</p>
    </div>
    <div class="feat rv">
      <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M12 27a12 12 0 0 1 24 0"/><path d="M24 7v-4M9.5 12.5 7 10M38.5 12.5 41 10M7 27H3M45 27h-4"/>
        <path d="M5 34c4-3 7 3 11 0s7 3 11 0 7 3 11 0"/><path d="M5 41c4-3 7 3 11 0s7 3 11 0 7 3 11 0"/>
      </svg>
      <h3>Real atmosphere</h3><p>Music, people and warm nights.</p>
    </div>
    <div class="feat rv">
      <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M24 40C10 30 6 22 9 16c3-6 11-6 15 1 4-7 12-7 15-1 3 6-1 14-15 24Z"/>
      </svg>
      <h3>Young at heart</h3><p>Fancy without the fuss.</p>
    </div>
  </div>
</section>"""

CARDS = f"""<section class="section section--cream">
  <div class="wrap">
    <div class="col">
      <p class="eyebrow rv">Have a look</p>
      <h2 class="rv">A little island energy, <em style="font-style:italic;color:var(--olive-400)">without leaving the mainland.</em></h2>
      <p class="lede rv">No dress code, no island mark-up — just somewhere you end up staying longer than you planned.</p>
    </div>
    <div class="cards">
      <a class="card rv" href="drinks.html">
        <span class="card__img"><img src="{img('1597075687490-8f673c6c17f6',900,675)}" width="900" height="675" loading="lazy" decoding="async" alt="A cocktail on a wooden table"></span>
        <h3>Drinks</h3><p>Greek ingredients, Greek bottles, zero unnecessary theatre.</p><span>See the list →</span>
      </a>
      <a class="card rv" href="vibe.html">
        <span class="card__img"><img src="{img('1714381633320-e5c3fd0f14db',900,675)}" width="900" height="675" loading="lazy" decoding="async" alt="Tables and chairs under strung lights"></span>
        <h3>The Vibe</h3><p>Come for one, stay for three. Music, people and warm nights.</p><span>Have a look →</span>
      </a>
      <a class="card rv" href="gallery.html">
        <span class="card__img"><img src="{img('1568644396922-5c3bfae12521',900,675)}" width="900" height="675" loading="lazy" decoding="async" alt="Three people raising glasses"></span>
        <h3>Gallery</h3><p>Nights that ran long, and the people who stayed for them.</p><span>Open the gallery →</span>
      </a>
    </div>
  </div>
</section>"""

HOME_CTA = f"""{CURVE.format(c="olive")}
<section class="section section--olive">
  <div class="wrap col">
    <h2 class="rv">Come by. Stay a while.</h2>
    <p class="lede rv">Every day · 18:00 until late. The courtyard fills up after 21:00.</p>
    <p class="rv"><a class="btn" href="contact.html" data-cta>Reserve a table</a></p>
  </div>
</section>"""

DRINKS_BODY = f"""{pagehead("Drinks", "Drinks we actually <em style='font-style:italic;color:var(--sage)'>want</em> to drink.",
  "Good ingredients. Greek character. Zero unnecessary theatre. What goes into the glass stays close to home.")}
{CURVE.format(c="cream")}
<section class="section section--cream">
  <div class="wrap">
{plate("drinks",
  ("1597075687490-8f673c6c17f6", 900, 1125, "A cocktail resting on a wooden table"),
  ("1470337458703-46ad1756a187", 900, 900,  "Amber cocktail poured over a single large cube of ice"),
  ("1574879948818-1cfda7aa5b1a", 900, 900,  "A drink being poured behind the bar"))}
    <ul class="list" id="drinkList"></ul>
    <p class="list__foot" id="drinkFoot"></p>
    <div class="col" style="margin-top:clamp(38px,5vw,60px)">
      <p class="hand rv">Greek in the glass, Greek at heart.</p>
      <p class="rv"><a class="btn btn--dark" href="contact.html" data-cta>Reserve a table</a></p>
    </div>
  </div>
</section>"""

VIBE_BODY = f"""{pagehead("The Vibe", "Come for one. Stay for three.",
  "It starts with one drink and a table for two. Then someone pulls up a chair, the music finds its stride, and nobody's looking at their phone any more.",
  "Fancy without the fuss.")}
<section class="section section--olive">
  <div class="wrap">
{plate("vibe",
  ("1485872299829-c673f5194813", 900, 1125, "Two friends talking over drinks"),
  ("1714381633320-e5c3fd0f14db", 900, 900,  "Tables and chairs under strung lights"),
  ("1694659589047-64e59133764a", 900, 900,  "A bulb glowing in the branches overhead"))}
    <div class="col" style="margin-top:clamp(38px,5vw,60px)">
      <p class="lede rv">No dress code, no island mark-up. Music that suits the hour, and the people who turn up.</p>
      <p class="rv"><a class="btn" href="gallery.html">See the gallery
        <svg width="16" height="9" viewBox="0 0 16 9" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true">
          <path d="M0 4.5h14M10.5 1l3.6 3.5-3.6 3.5"/></svg></a></p>
    </div>
  </div>
</section>"""

GAL = [
    ("1568644396922-5c3bfae12521", "Three people raising glasses together"),
    ("1527359443443-84a48aec73d2", "A lit terrace after dark"),
    ("1566417713940-fe7c737a9ef2", "A drink being poured at the bar"),
    ("1569924995012-c4c706bfcd51", "The bar on a busy night"),
    ("1591243315780-978fd00ff9db", "A glass raised across the table"),
    ("1623408859815-22534357b3db", "Pouring into a chilled glass"),
    ("1546373702-eb3e6f769df2", "Bulbs strung through the branches"),
    ("1604601638534-8cc3198794e2", "A quiet corner under the trees"),
]
GAL_HTML = "\n".join(
    f'      <!-- photo slot: gallery-{n} — swap src for img/gallery-{n}.jpg -->\n'
    f'      <button type="button" data-full="{img(pid,1500,1500,80)}" '
    f'aria-label="Open photo: {alt}">'
    f'<img src="{img(pid,800,800)}" width="800" height="800" loading="lazy" '
    f'decoding="async" alt="{alt}"></button>'
    for n, (pid, alt) in enumerate(GAL, 1))

GALLERY_BODY = f"""{pagehead("Gallery", "Nights that ran long.",
  "Eight from the courtyard. Tap any of them to see it full size.")}
<section class="section section--dark">
  <div class="wrap">
    <div class="gal">
{GAL_HTML}
    </div>
  </div>
</section>"""

ABOUT_BODY = f"""{pagehead("About", "A little island energy, <em>without leaving the mainland.</em>")}
{CURVE.format(c="cream")}
<section class="section section--cream">
  <div class="wrap">
    <!-- photo slot: about — swap src for img/about.jpg -->
    <button type="button" class="fig fig--full rv" data-full="hero-wide.jpeg"
            aria-label="Open photo: the DION courtyard at night">
      <img src="hero-wide.jpeg" width="2000" height="1330" loading="lazy" decoding="async"
           alt="The DION courtyard on a summer night">
    </button>
    <div class="col" style="margin-top:clamp(38px,5vw,60px)">
      <p class="lede rv">DION is a bar. Good drinks made properly, Greek bottles and ingredients we
        actually like, music that suits the hour, and the people who turn up.</p>
      <p class="lede rv">No dress code, no island mark-up — just somewhere you end up staying longer
        than you planned.</p>
      <p class="hand rv">Fancy without the fuss.</p>
      <p class="rv"><a class="btn btn--dark" href="contact.html" data-cta>Reserve a table</a></p>
    </div>
  </div>
</section>"""

CONTACT_BODY = f"""{pagehead("Find us", "Come by. Stay a while.",
  "Most people just turn up — but if you'd rather have a table waiting, call ahead.")}
<section class="section section--olive">
  <div class="wrap">
    <ul class="facts">
      <li class="rv"><h3>Where</h3>
        <p id="cAddr1">Street name 00</p><p id="cAddr2">Town, Greece</p></li>
      <li class="rv"><h3>Open</h3>
        <p id="cHours1">Every day · 18:00 until late</p>
        <p id="cHours2">The courtyard fills up after 21:00</p></li>
      <li class="rv"><h3>Talk to us</h3>
        <a id="cPhone" href="tel:+300000000000" data-phone>+30 000 000 0000</a></li>
    </ul>

    <a class="ig rv" id="cIg" href="https://instagram.com/" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true">
        <rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/>
        <circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/>
      </svg>
      <span><b id="cIgHandle">@yourhandle</b><span>Tonight's music, tomorrow's plans, everything in between.</span></span>
    </a>

    <a class="map rv" id="cMap" href="https://www.google.com/maps" target="_blank" rel="noopener" aria-label="Open DION in Google Maps">
      <span class="map__grid"></span>
      <svg class="map__road" viewBox="0 0 400 300" fill="none" stroke="currentColor" stroke-width="7" aria-hidden="true">
        <path d="M-10 210C70 200 120 176 190 150s150-40 230-72"/>
        <path d="M150 320V180l110-70V-10" stroke-width="4"/>
        <path d="M-10 96c90 22 150 10 230-30" stroke-width="3"/>
      </svg>
      <span class="map__pin">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">
          <path d="M12 22s7-7.2 7-12A7 7 0 0 0 5 10c0 4.8 7 12 7 12Z"/><circle cx="12" cy="10" r="2.4"/>
        </svg>
      </span>
      <span class="map__label"><em>DION</em><span>Open in Maps →</span></span>
    </a>

    <div class="cta-row">
      <a class="btn" href="tel:+300000000000" data-cta data-phone>Reserve a table</a>
      <span>or just turn up — most people do.</span>
    </div>
  </div>
</section>"""

BODIES = {
    "index.html":   (HERO + "\n" + STRIP + "\n" + CARDS + "\n" + HOME_CTA,
                     "DION is a bar. Greek drinks, warm nights and good people. Island soul, without leaving the mainland."),
    "drinks.html":  (DRINKS_BODY,  "Greek ingredients, Greek bottles and flavours we actually love. The DION drinks list."),
    "vibe.html":    (VIBE_BODY,    "Come for one, stay for three. Music, people and warm nights at DION."),
    "gallery.html": (GALLERY_BODY, "Nights that ran long — photographs from the DION courtyard."),
    "about.html":   (ABOUT_BODY,   "DION is a bar. A little island energy, without leaving the mainland."),
    "contact.html": (CONTACT_BODY, "Find DION — address, opening hours and how to reserve a table."),
}

HOME_HEAD = ('<link rel="preload" as="image" href="hero-wide.jpeg" fetchpriority="high">\n')

for filename, active, title in PAGES:
    body, desc = BODIES[filename]
    html = shell(filename, active, title, desc, body,
                 extra_head=HOME_HEAD if filename == "index.html" else "")
    (OUT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename, len(html), "bytes")
