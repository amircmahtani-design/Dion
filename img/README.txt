Drop your real DION photos in this folder, then point the pages at them.

The site expects these slots. Any size works — the CSS crops them — but
shoot for at least 1200px on the long edge.

  drinks-a.jpg    tall,   portrait-ish   (the big plate on the Drinks page)
  drinks-b.jpg    square                 (the one riding over its corner)
  drinks-c.jpg    square                 (the small accent, bottom left)

  vibe-a.jpg      tall,   portrait-ish   (same three slots on The Vibe)
  vibe-b.jpg      square
  vibe-c.jpg      square

  gallery-1.jpg .. gallery-8.jpg         square-ish, the gallery grid

  about.jpg       wide, landscape        (the plate on the About page)

To use one: open the page, find the <img src="https://images.unsplash.com/...">
for that slot and replace the whole src with  img/drinks-a.jpg
The width= and height= attributes can stay; the CSS handles the crop.

Every slot is labelled with an HTML comment naming it, so search the page
for "drinks-a" and you will land on the right line.
