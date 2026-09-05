#!/usr/bin/env python3
"""Builds the seven DION pages from one shared shell so the nav, head and
footer can never drift apart.

Every visible string exists twice — Greek and English — and both ship in the
page. The language toggle in the nav flips which set is shown, so there is no
second copy of the site to keep in sync and no redirect on first load.

Run:  python3 build.py
"""
import pathlib

OUT = pathlib.Path(__file__).parent

U = "https://images.unsplash.com/photo-"
def img(pid, w, h, q=72):
    return f"{U}{pid}?auto=format&amp;fit=crop&amp;w={w}&amp;h={h}&amp;q={q}"


# ── bilingual helpers ──────────────────────────────────────────────────
def t(el, en):
    """Inline pair — both languages inside one element."""
    return f'<span class="l-el">{el}</span><span class="l-en">{en}</span>'


def dual(tag, el, en, cls=""):
    """Emits the element twice, once per language, so the surrounding
    layout rules (.col spacing, .rv reveals) still see flat siblings."""
    c = f'{cls} l-el'.strip()
    d = f'{cls} l-en'.strip()
    return (f'<{tag} class="{c}">{el}</{tag}>\n'
            f'<{tag} class="{d}">{en}</{tag}>')


def paras(items, cls="lede rv"):
    """A run of paragraphs given as (greek, english) pairs."""
    return "\n".join(dual("p", el, en, cls) for el, en in items)


# ── pages ──────────────────────────────────────────────────────────────
# filename, nav label (el, en), <title> (el, en), meta description (el)
PAGES = [
    ("index.html",   ("Αρχική", "Home"),
     ("DION — Λίγη νησιώτικη ενέργεια", "DION — A little island energy"),
     "Το DION είναι ένα bar στην Παλαιά Φώκαια. Καλά ποτά, μουσική και βραδιές που κρατούν λίγο περισσότερο."),
    ("drinks.html",  ("Ποτά", "Drinks"),
     ("Ποτά · DION", "Drinks · DION"),
     "Signature cocktails, κλασικές επιλογές, ελληνικές ετικέτες και αποστάγματα που αγαπάμε πραγματικά."),
    ("vibe.html",    ("Η Ατμόσφαιρα", "The Vibe"),
     ("Η Ατμόσφαιρα · DION", "The Vibe · DION"),
     "Το DION αλλάζει όσο πέφτει ο ήλιος. Έλα για ένα ποτό, μείνε για δεύτερο."),
    ("gallery.html", ("Φωτογραφίες", "Gallery"),
     ("Φωτογραφίες · DION", "Gallery · DION"),
     "Οι βραδιές στο DION δείχνουν καλύτερα απ' όσο περιγράφονται."),
    ("events.html",  ("Events", "Events"),
     ("Events · DION", "Events · DION"),
     "Τι συμβαίνει στο DION — events, DJ sets και live βραδιές."),
    ("about.html",   ("Το DION", "About"),
     ("Το DION", "About · DION"),
     "Το DION ξεκίνησε από μια απλή ιδέα: να φτιάξουμε το bar στο οποίο θα θέλαμε να περνάμε τα δικά μας βράδια."),
    ("contact.html", ("Επικοινωνία", "Contact"),
     ("Επικοινωνία · DION", "Contact · DION"),
     "Βρες το DION — διεύθυνση, ώρες λειτουργίας και κρατήσεις."),
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

ARROW = ('<svg width="16" height="9" viewBox="0 0 16 9" fill="none" stroke="currentColor" '
         'stroke-width="1.3" aria-hidden="true"><path d="M0 4.5h14M10.5 1l3.6 3.5-3.6 3.5"/></svg>')

# site.js is the one place these are edited; the values below are only
# what shows if the script fails to load, so keep them matching DION in
# assets/site.js. Nothing here is read at runtime.
FALLBACK = {
    "phone":  "+30 694 822 2527",
    "tel":    "tel:+306948222527",
    "addr":   ("28is Oktovriou 22", "Palea Fokea 190 13, Greece"),
    "hours":  (("Ανοιχτά από τις 20:30 · Παρασκευή από τις 21:00", "Open from 20:30 · Friday from 21:00"),
               ("Κλειστά τις Κυριακές", "Closed Sundays")),
    "cta":    ("Κλείσε τραπέζι", "Book a table"),
}

# Every booking button dials the bar. site.js rewrites the label and the
# number, so the wording and the phone live in exactly one place.
CTA_BTN = ('<a class="btn{{extra}}" href="{tel}" data-cta data-phone>'
           '<span data-cta-label>{label}</span></a>').format(
    tel=FALLBACK["tel"], label=t(*FALLBACK["cta"]))

ANNOUNCE = """<!-- Filled in by site.js from DION.announcement — stays hidden when inactive. -->
<div class="announce" id="announce" hidden>
  <p id="annText"></p>
  <button type="button" id="annClose" aria-label="Close">&times;</button>
</div>"""

LIGHTBOX = """<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo">
  <div class="lb__stage">
    <img id="lbImg" src="" alt="">
  </div>
  <button type="button" class="lb__close" aria-label="Close">&times;</button>
  <button type="button" class="lb__nav lb__nav--prev" aria-label="Previous photo">&#8249;</button>
  <button type="button" class="lb__nav lb__nav--next" aria-label="Next photo">&#8250;</button>
  <p class="lb__hint">{hint}</p>
</div>""".format(hint=t("Pinch ή διπλό tap για zoom", "Pinch or double-tap to zoom"))


def nav(active_file, overlay):
    cls = "nav nav--overlay" if overlay else "nav nav--solid"
    links = ""
    for href, (lab_el, lab_en), _, _ in PAGES:
        cur = ' aria-current="page"' if href == active_file else ""
        # The Events link is removed by site.js when nothing is scheduled.
        flag = ' data-nav="events"' if href == "events.html" else ""
        links += f'      <li{flag}><a href="{href}"{cur}>{t(lab_el, lab_en)}</a></li>\n'
    return f"""<header class="{cls}" id="nav">
  <a class="nav__brand" href="index.html" aria-label="DION">
    <svg viewBox="0 0 100 190" aria-hidden="true"><use href="#dion-mark"/></svg>
    <span>DION<small>Mainland Soul</small></span>
  </a>
  <button class="lang" id="lang" type="button" aria-label="Change language">
    <span class="l-el">EN</span><span class="l-en">ΕΛ</span>
  </button>
  <button class="nav__burger" id="burger" type="button" aria-label="Menu" aria-expanded="false"><span></span></button>
  <ul class="nav__links" id="menu">
{links}      <li>{CTA_BTN.format(extra=" nav__cta")}</li>
  </ul>
  {CTA_BTN.format(extra=" nav__cta")}
</header>"""


def footer(active_file):
    parts = []
    for h, (el, en), _, _ in PAGES:
        cur = ' aria-current="page"' if h == active_file else ""
        flag = ' data-nav="events"' if h == "events.html" else ""
        parts.append(f'<a href="{h}"{cur}{flag}>{t(el, en)}</a>')
    links = "".join(parts)
    tagline = t("Λίγη νησιώτικη ενέργεια, χωρίς να φύγεις από τη στεριά.",
                "A little island energy, without leaving the mainland.")
    base = t("Ελληνικό στο ποτήρι, ελληνικό στην ψυχή.",
             "Greek in the glass, Greek at heart.")
    return f"""<footer class="foot">
  <div class="wrap">
    <a class="foot__brand" href="index.html" aria-label="DION">
      <svg viewBox="0 0 100 190" aria-hidden="true"><use href="#dion-mark"/></svg>
      <span><b>DION</b><small>Mainland Soul</small></span>
    </a>
    <p class="foot__line">{tagline}</p>
    <nav aria-label="Footer">{links}</nav>
    <div class="foot__col">
      <span id="fAddr">{", ".join(FALLBACK["addr"])}</span>
      <span id="fHours">{t(*FALLBACK["hours"][0])}</span>
      <a id="fPhone" href="{FALLBACK["tel"]}" data-phone>{FALLBACK["phone"]}</a>
      <a id="fIg" href="https://instagram.com/" target="_blank" rel="noopener">Instagram</a>
    </div>
    <div class="foot__base">
      <span>© <span id="year">2026</span> DION · Mainland Soul</span>
      <span>{base}</span>
    </div>
  </div>
</footer>"""


def shell(filename, title_el, title_en, desc, body, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="el" data-lang="el" data-title-el="{title_el}" data-title-en="{title_en}">
<head>
<meta charset="utf-8">
<script>
/* Language is settled before first paint so the wrong one never flashes. */
document.documentElement.className="js";
(function(){{var l="el";try{{if(localStorage.getItem("dion-lang")==="en")l="en"}}catch(e){{}}
var r=document.documentElement;r.lang=l;r.setAttribute("data-lang",l);}})();
</script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title_el}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B0B0A">
<meta property="og:title" content="{title_el}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="hero-wide.jpeg">
<meta property="og:type" content="website">
<meta property="og:locale" content="el_GR">
<meta property="og:locale:alternate" content="en_GB">
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
{ANNOUNCE}
{nav(filename, overlay=(filename == "index.html"))}

<main>
{body}
</main>

{LIGHTBOX}

{footer(filename)}
<script src="assets/site.js"></script>
</body>
</html>
"""


def pagehead(eyebrow, heading, lede=None, hand=None):
    """Each argument is a (greek, english) pair."""
    out = ['<section class="pagehead">', '  <div class="wrap">',
           dual("p", eyebrow[0], eyebrow[1], "eyebrow rv"),
           dual("h1", heading[0], heading[1], "rv")]
    if lede:
        out.append(dual("p", lede[0], lede[1], "lede rv"))
    if hand:
        out.append(dual("p", hand[0], hand[1], "hand rv"))
    out += ["  </div>", "</section>"]
    return "\n".join(out)


def plate(slot_prefix, a, b, c=None):
    """The overlapping composition: a tall plate, a square riding over its
    bottom-right corner, and an optional small accent at bottom-left."""
    def cell(cls, slot, spec):
        pid, w, h, alt = spec
        return (f'    <!-- photo slot: {slot} — swap src for img/{slot}.jpg -->\n'
                f'    <button type="button" class="fig {cls} rv" '
                f'data-full="{img(pid, 1600, int(1600*h/w), 80)}" '
                f'aria-label="{alt}">\n'
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


# ── page bodies ────────────────────────────────────────────────────────
HERO = f"""<section class="hero">
  <picture class="hero__media" id="heroMedia">
    <img id="heroImg" src="hero-wide.jpeg" width="2000" height="1330" fetchpriority="high"
         decoding="async" alt="DION">
  </picture>
  <div class="hero__inner">
    <h1 class="l-el">Λίγη νησιώτικη ενέργεια,<em>χωρίς να φύγεις από τη στεριά.</em></h1>
    <h1 class="l-en">A little island energy,<em>without leaving the mainland.</em></h1>
    <svg class="squiggle" viewBox="0 0 74 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true">
      <path d="M1 8C7 1 12 1 18 7c6 6 11 6 17 0 6-6 11-6 17 0 6 6 11 6 17-1"/>
    </svg>
    <p class="l-el">Καλό ποτό, καλή μουσική και βραδιές που δεν χρειάζονται ιδιαίτερο σχέδιο.</p>
    <p class="l-en">Great drinks, good music and the kind of nights that don't need much of a plan.</p>
    <div class="hero__cta">
      <a class="btn" href="drinks.html">{t("Δες τα ποτά", "Explore the drinks")} {ARROW}</a>
      {CTA_BTN.format(extra="")}
    </div>
  </div>
  <a class="scroll-cue" href="#intro" aria-hidden="true" tabindex="-1">Scroll</a>
</section>"""

INTRO = f"""{CURVE.format(c="cream")}
<section class="section section--cream" id="intro">
  <div class="wrap col">
{paras([
    ("Το DION είναι το μέρος για εκείνες τις βραδιές που ξεκινούν με ένα ποτό και καταλήγουν λίγο αργότερα απ' όσο είχες υπολογίσει.",
     "DION is made for the kind of evening that starts with one drink and somehow ends a little later than planned."),
    ("Cocktails φτιαγμένα σωστά, ελληνικές ετικέτες που αξίζει να δοκιμάσεις, μουσική που κρατάει την ενέργεια ψηλά και μια χαλαρή ατμόσφαιρα που θυμίζει καλοκαιρινή απόδραση.",
     "Proper cocktails, Greek bottles worth discovering, music that keeps the mood moving and a relaxed atmosphere with just enough summer energy to feel like an escape."),
])}
{dual("p", "Χωρίς υπερβολές. Χωρίς στημένο ύφος. Απλώς ένα μέρος που θέλεις να ξαναέρθεις.",
      "No unnecessary fuss. No trying too hard. Just somewhere you'll want to come back to.", "hand rv")}
  </div>
</section>"""

PILLARS = f"""<section class="strip" id="strip">
  <div class="wrap strip__grid strip__grid--3">
    <div class="feat rv">
      <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M9 13h30L24 29 9 13Z"/><path d="M24 29v9M17 39h14"/><path d="M31.5 9c-1.5 1.5-3 3-4.5 4.5"/><circle cx="33" cy="7" r="2.6"/>
      </svg>
      <h3>{t("Ποτά που αξίζουν", "Drinks worth staying for")}</h3>
      <p>{t("Cocktails με χαρακτήρα, κλασικές επιλογές που γίνονται όπως πρέπει και ελληνικά κρασιά και αποστάγματα που αγαπάμε πραγματικά.", "Cocktails with character, classics made properly and Greek wines and spirits we genuinely enjoy.")}</p>
    </div>
    <div class="feat rv">
      <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M12 27a12 12 0 0 1 24 0"/><path d="M24 7v-4M9.5 12.5 7 10M38.5 12.5 41 10M7 27H3M45 27h-4"/>
        <path d="M5 34c4-3 7 3 11 0s7 3 11 0 7 3 11 0"/><path d="M5 41c4-3 7 3 11 0s7 3 11 0 7 3 11 0"/>
      </svg>
      <h3>{t("Η σωστή ατμόσφαιρα", "The right atmosphere")}</h3>
      <p>{t("Ζεστά βράδια, μουσική, παρέες και ένας χώρος φτιαγμένος για να κάθεσαι λίγο περισσότερο.", "Warm evenings, good music, good people and a space designed to make you stay a little longer.")}</p>
    </div>
    <div class="feat rv">
      <svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M24 41c0-11 2-21 7-30"/><path d="M27 30c-6-1-10-6-9-11 6 0 10 5 9 11Z"/>
        <path d="M28.5 21c5-2 8-7 7-12-6 1-9 7-7 12Z"/><path d="M25 37c-5 0-9-4-9-8 5 0 9 4 9 8Z"/>
      </svg>
      <h3>{t("Ελληνική ψυχή", "Greek at heart")}</h3>
      <p>{t("Το DION έχει Ελλάδα μέσα του χωρίς να προσπαθεί να γίνει καρτ ποστάλ. Απλό, σύγχρονο και ανεπιτήδευτο.", "DION carries Greece in its character without trying to turn it into a postcard. Simple, modern and effortless.")}</p>
    </div>
  </div>
</section>"""

CARDS = f"""<section class="section section--cream">
  <div class="wrap">
    <div class="col">
{dual("p", "Ρίξε μια ματιά", "Have a look", "eyebrow rv")}
    </div>
    <div class="cards">
      <a class="card rv" href="drinks.html">
        <span class="card__img"><img src="{img('1597075687490-8f673c6c17f6',900,675)}" width="900" height="675" loading="lazy" decoding="async" alt=""></span>
        <h3>{t("Ποτά", "Drinks")}</h3>
        <p>{t("Signature cocktails, κλασικά και ελληνικές ετικέτες που αξίζουν.", "Signature cocktails, classics and Greek bottles worth discovering.")}</p>
        <span>{t("Δες τον κατάλογο →", "See the list →")}</span>
      </a>
      <a class="card rv" href="vibe.html">
        <span class="card__img"><img src="{img('1714381633320-e5c3fd0f14db',900,675)}" width="900" height="675" loading="lazy" decoding="async" alt=""></span>
        <h3>{t("Η Ατμόσφαιρα", "The Vibe")}</h3>
        <p>{t("Έλα για ένα ποτό. Μείνε για δεύτερο. Η βραδιά βρίσκει τον ρυθμό της.", "Come for a drink. Stay for another. The evening finds its own rhythm.")}</p>
        <span>{t("Ρίξε μια ματιά →", "Have a look →")}</span>
      </a>
      <a class="card rv" href="gallery.html">
        <span class="card__img"><img src="{img('1568644396922-5c3bfae12521',900,675)}" width="900" height="675" loading="lazy" decoding="async" alt=""></span>
        <h3>{t("Φωτογραφίες", "Gallery")}</h3>
        <p>{t("Οι βραδιές στο DION δείχνουν καλύτερα απ' όσο περιγράφονται.", "Nights at DION are easier to show than explain.")}</p>
        <span>{t("Άνοιξε τη gallery →", "Open the gallery →")}</span>
      </a>
    </div>
  </div>
</section>"""

# The reservation call to action, reused on several pages.
RESERVE = f"""{CURVE.format(c="olive")}
<section class="section section--olive">
  <div class="wrap col">
{dual("h2", "Το τραπέζι σου σε περιμένει.", "Your table is waiting.", "rv")}
{dual("p", "Εσύ απλώς αποφάσισε με ποιον έρχεσαι.", "You just need to decide who you're bringing.", "lede rv")}
    <p class="rv">{CTA_BTN.format(extra="")}</p>
  </div>
</section>"""

DRINKS_BODY = f"""{pagehead(
    ("Ποτά", "Drinks"),
    ("Το ποτήρι είναι καλό σημείο <em>για να ξεκινήσεις.</em>",
     "The glass is a pretty good <em>place to start.</em>"),
    ("Στο DION αγαπάμε τα ποτά που έχουν χαρακτήρα χωρίς να χρειάζονται εξήγηση δέκα λεπτών.",
     "At DION, we like drinks with personality that don't need a ten-minute explanation."))}
{CURVE.format(c="cream")}
<section class="section section--cream">
  <div class="wrap">
{plate("drinks",
  ("1597075687490-8f673c6c17f6", 900, 1125, "DION"),
  ("1470337458703-46ad1756a187", 900, 900,  "DION"),
  ("1574879948818-1cfda7aa5b1a", 900, 900,  "DION"))}
    <div class="col" style="margin-top:clamp(38px,5vw,60px)">
{paras([
    ("Θα βρεις signature cocktails, κλασικές επιλογές, κρασιά από την Ελλάδα και τον υπόλοιπο κόσμο, μπύρες και αποστάγματα που έχουμε διαλέξει επειδή μας αρέσουν — όχι επειδή απλώς έπρεπε να υπάρχουν σε έναν κατάλογο.",
     "Expect signature cocktails, properly made classics, Greek and international wines, beer and spirits we've chosen because we actually like them — not because they simply needed to appear on a menu."),
    ("Αν δεν ξέρεις τι θέλεις, πες μας τι σου αρέσει. Θα βρούμε κάτι.",
     "If you're not sure what you want, tell us what you normally enjoy. We'll take it from there."),
])}
    </div>

    <!-- Categories and items come from DION.drinks in assets/site.js.
         A category with no items is skipped entirely. -->
    <div class="menu" id="drinkMenu"></div>
    <p class="list__foot" id="drinkFoot"></p>

    <div class="col" style="margin-top:clamp(38px,5vw,60px)">
{dual("p", "Ελληνικό στο ποτήρι, ελληνικό στην ψυχή.", "Greek in the glass, Greek at heart.", "hand rv")}
      <p class="rv">{CTA_BTN.format(extra=" btn--dark")}</p>
    </div>
  </div>
</section>"""

VIBE_BODY = f"""{pagehead(
    ("Η Ατμόσφαιρα", "The Vibe"),
    ("Το DION αλλάζει <em>όσο πέφτει ο ήλιος.</em>",
     "DION changes <em>as the sun goes down.</em>"),
    ("Νωρίς, είναι το μέρος για ένα χαλαρό ποτό και κουβέντα. Αργότερα, η μουσική δυναμώνει λίγο, τα τραπέζια γεμίζουν και η βραδιά αποκτά τον δικό της ρυθμό.",
     "Early on, it's somewhere to settle in for a relaxed drink and a conversation. Later, the music comes up, the tables fill and the evening finds its own rhythm."))}
<section class="section section--olive">
  <div class="wrap">
{plate("vibe",
  ("1485872299829-c673f5194813", 900, 1125, "DION"),
  ("1714381633320-e5c3fd0f14db", 900, 900,  "DION"),
  ("1694659589047-64e59133764a", 900, 900,  "DION"))}
    <div class="col" style="margin-top:clamp(38px,5vw,60px)">
{paras([
    ("Δεν προσπαθούμε να γίνουμε club και δεν χρειάζεται να φωνάζεις για να ακούσεις την παρέα σου. Η ιδέα είναι πιο απλή:",
     "We're not trying to be a club, and you shouldn't need to shout to hear the person sitting next to you. The idea is simpler:"),
])}
{dual("p", "Να έρθεις για ένα ποτό.<br>Να μείνεις για δεύτερο.<br>Και να φύγεις έχοντας ήδη αποφασίσει ότι θα ξανάρθεις.",
      "Come for a drink.<br>Stay for another.<br>Leave already knowing you'll be back.", "hand rv")}
    </div>
  </div>
</section>
{CURVE.format(c="cream")}
<section class="section section--cream">
  <div class="wrap col">
{dual("p", "Καλοκαίρι, λίγο πιο κοντά", "Summer, a little closer", "eyebrow rv")}
{dual("h2", "Ζεστός αέρας, μουσική στο βάθος, <em style=\"font-style:italic;color:var(--olive-400)\">ένα κρύο ποτό στο τραπέζι.</em>",
      "Warm air, music in the background, <em style=\"font-style:italic;color:var(--olive-400)\">a cold drink on the table.</em>", "rv")}
{paras([
    ("Υπάρχει κάτι στις ελληνικές καλοκαιρινές βραδιές που είναι δύσκολο να περιγράψεις, και καμία ιδιαίτερη βιασύνη να πας κάπου αλλού. Αυτό είναι το συναίσθημα που θέλαμε να φέρουμε στο DION.",
     "There's something about Greek summer evenings that's difficult to put into words, and absolutely no rush to be somewhere else. That's the feeling we wanted to bring to DION."),
])}
    <p class="rv"><a class="btn btn--dark" href="gallery.html">{t("Δες τις φωτογραφίες", "See the gallery")} {ARROW}</a></p>
  </div>
</section>"""

GAL = ["1568644396922-5c3bfae12521", "1527359443443-84a48aec73d2",
       "1566417713940-fe7c737a9ef2", "1569924995012-c4c706bfcd51",
       "1591243315780-978fd00ff9db", "1623408859815-22534357b3db",
       "1546373702-eb3e6f769df2",    "1604601638534-8cc3198794e2"]
GAL_HTML = "\n".join(
    f'      <!-- photo slot: gallery-{n} — swap src for img/gallery-{n}.jpg -->\n'
    f'      <button type="button" data-full="{img(pid,1500,1500,80)}" aria-label="DION">'
    f'<img src="{img(pid,800,800)}" width="800" height="800" loading="lazy" '
    f'decoding="async" alt="DION"></button>'
    for n, pid in enumerate(GAL, 1))

GALLERY_BODY = f"""{pagehead(
    ("Φωτογραφίες", "Gallery"),
    ("Οι βραδιές στο DION δείχνουν <em>καλύτερα απ' όσο περιγράφονται.</em>",
     "Nights at DION are easier <em>to show than explain.</em>"),
    ("Ποτά, μουσική, φίλοι και εκείνες οι μικρές στιγμές που κάνουν μια απλή έξοδο να κρατήσει λίγο περισσότερο.",
     "Drinks, music, friends and all the little moments that turn a quick evening out into something that lasts a little longer."))}
<section class="section section--dark">
  <div class="wrap">
    <div class="gal">
{GAL_HTML}
    </div>
  </div>
</section>
{RESERVE}"""

EVENTS_BODY = f"""{pagehead(
    ("Events", "Events"),
    ("Τι συμβαίνει <em>στο DION</em>", "What's happening <em>at DION</em>"),
    ("Κάποιες βραδιές θέλουν απλώς ένα καλό soundtrack. Άλλες αξίζουν λίγο περισσότερο. Εδώ θα βρίσκεις τα επόμενα events, DJ sets, live βραδιές και οτιδήποτε διαφορετικό έχουμε προγραμματίσει.",
     "Some nights only need a good soundtrack. Others deserve a little more. This is where you'll find upcoming events, DJ sets, live nights and anything else we've got planned."))}
<section class="section section--olive">
  <div class="wrap">
    <!-- Events come from DION.events in assets/site.js. Anything dated
         before today drops off the page on its own. -->
    <ul class="events" id="eventList"></ul>

    <div class="col" id="eventEmpty" hidden>
{dual("h2", "Τίποτα προγραμματισμένο αυτή τη στιγμή.", "Nothing special on the calendar right now.", "rv")}
{paras([
    ("Αλλά αυτό δεν σημαίνει ότι πρέπει να περιμένεις. Το bar είναι ανοιχτό, τα ποτά είναι κρύα και η μουσική παίζει.",
     "That doesn't mean you need to wait. The bar is open, the drinks are cold and the music is on."),
])}
      <p class="rv">{CTA_BTN.format(extra="")}</p>
    </div>
  </div>
</section>"""

ABOUT_BODY = f"""{pagehead(
    ("Το DION", "About"),
    ("Το bar στο οποίο θα θέλαμε <em>να περνάμε τα δικά μας βράδια.</em>",
     "The kind of bar we'd actually want <em>to spend our own evenings in.</em>"))}
{CURVE.format(c="cream")}
<section class="section section--cream">
  <div class="wrap">
    <!-- photo slot: about — swap src for img/about.jpg -->
    <button type="button" class="fig fig--full rv" data-full="hero-wide.jpeg" aria-label="DION">
      <img src="hero-wide.jpeg" width="2000" height="1330" loading="lazy" decoding="async" alt="DION">
    </button>
    <div class="col" style="margin-top:clamp(38px,5vw,60px)">
{dual("p", "Όχι υπερβολικά επίσημο.<br>Όχι υπερβολικά δυνατό.<br>Όχι ένα μέρος που προσπαθεί υπερβολικά να εντυπωσιάσει.",
      "Not overly formal.<br>Not unnecessarily loud.<br>Not somewhere trying too hard to impress you.", "hand rv")}
{paras([
    ("Ένα όμορφο bar με καλά ποτά, ελληνικό χαρακτήρα, μουσική και ανθρώπους που σε κάνουν να νιώθεις άνετα από την πρώτη στιγμή.",
     "Just a beautiful bar with good drinks, Greek character, music and people who make you feel comfortable from the moment you arrive."),
    ("Η Ελλάδα είναι μέρος της ταυτότητάς μας — από τα κρασιά και τα αποστάγματα μέχρι τις γεύσεις και τη διάθεση — αλλά το DION δεν δημιουργήθηκε για να αντιγράψει κάποιο νησί. Δημιουργήθηκε για να σου δώσει λίγο από εκείνο το συναίσθημα.",
     "Greece is part of our identity — from the wines and spirits to the flavours and the mood — but DION was never created to imitate an island. It was created to give you a little of that feeling."),
    ("Εκείνη τη στιγμή του καλοκαιριού που κάθεσαι έξω, έχεις ένα ποτό μπροστά σου και δεν σε ενδιαφέρει ιδιαίτερα τι ώρα είναι. Αυτό είναι το DION.",
     "That moment on a Greek summer evening when you're sitting outside, there's a drink in front of you and you've completely stopped caring what time it is. That's DION."),
])}
      <p class="rv">{CTA_BTN.format(extra=" btn--dark")}</p>
    </div>
  </div>
</section>"""

CONTACT_BODY = f"""{pagehead(
    ("Επικοινωνία", "Contact"),
    ("Έλα να <em>μας βρεις.</em>", "Come and <em>find us.</em>"),
    ("Για ένα γρήγορο ποτό, για ολόκληρο το βράδυ ή απλώς επειδή πέρασες από τη γειτονιά.",
     "For one quick drink, the whole evening or simply because you happened to be nearby."))}
<section class="section section--olive">
  <div class="wrap">
    <ul class="facts">
      <li class="rv"><h3>{t("Διεύθυνση", "Address")}</h3>
        <p id="cAddr1">{FALLBACK["addr"][0]}</p><p id="cAddr2">{FALLBACK["addr"][1]}</p></li>
      <li class="rv"><h3>{t("Ώρες λειτουργίας", "Opening hours")}</h3>
        <p id="cHours1">{t(*FALLBACK["hours"][0])}</p>
        <p id="cHours2">{t(*FALLBACK["hours"][1])}</p></li>
      <li class="rv"><h3>{t("Τηλέφωνο", "Phone")}</h3>
        <a id="cPhone" href="{FALLBACK["tel"]}" data-phone>{FALLBACK["phone"]}</a></li>
    </ul>

    <div class="col" style="margin-top:clamp(38px,5vw,58px)">
{dual("h2", "Κρατήσεις", "Reservations", "rv")}
{dual("p", "Θέλεις να είσαι σίγουρος ότι θα έχεις τραπέζι; Κάνε κράτηση ή επικοινώνησε μαζί μας.",
      "Want to make sure there's a table waiting? Book ahead or get in touch with us.", "lede rv")}
      <div class="cta-row rv">
        {CTA_BTN.format(extra="")}
        <a class="btn" id="cWa" href="https://wa.me/" target="_blank" rel="noopener" hidden>WhatsApp</a>
      </div>
    </div>

    <a class="ig rv" id="cIg" href="https://instagram.com/" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true">
        <rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/>
        <circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/>
      </svg>
      <span><b id="cIgHandle">@yourhandle</b><span>{t("Ακολούθησε τις βραδιές μας στο Instagram.", "Follow the nights at DION.")}</span></span>
    </a>

    <a class="map rv" id="cMap" href="https://www.google.com/maps" target="_blank" rel="noopener">
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
      <span class="map__label"><em>DION</em><span>{t("Άνοιγμα στους Χάρτες →", "Open in Maps →")}</span></span>
    </a>
  </div>
</section>"""

BODIES = {
    "index.html":   HERO + "\n" + INTRO + "\n" + PILLARS + "\n" + CARDS + "\n" + RESERVE,
    "drinks.html":  DRINKS_BODY,
    "vibe.html":    VIBE_BODY,
    "gallery.html": GALLERY_BODY,
    "events.html":  EVENTS_BODY,
    "about.html":   ABOUT_BODY,
    "contact.html": CONTACT_BODY,
}

HOME_HEAD = '<link rel="preload" as="image" href="hero-wide.jpeg" fetchpriority="high">\n'

for filename, _labels, (title_el, title_en), desc in PAGES:
    html = shell(filename, title_el, title_en, desc, BODIES[filename],
                 extra_head=HOME_HEAD if filename == "index.html" else "")
    (OUT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename, len(html), "bytes")
