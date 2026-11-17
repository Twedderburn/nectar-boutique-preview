"""Builds the Nectar Boutique concept pages from shared partials.
Each block maps to a standard Shopify OS 2.0 section so the design ports to a theme.
Run: python build.py  (writes the .html files next to this script)"""
import html, os

BOOK = "https://www.vagaro.com/nectarboutique/book-now"
STORE = "https://nectarboutiquebdn.myshopify.com"
OUT = os.path.dirname(os.path.abspath(__file__))
e = html.escape

PAGES = [("index.html", "Home"), ("services.html", "Services"), ("shop.html", "Shop"),
         ("about.html", "About"), ("visit.html", "Visit")]

SERVICES = {
 "Skin": [("Custom Facial",125,"Includes a free skin consultation"),("iS Clinical Fire & Ice Facial",140,""),("Anti-Age Facial",140,""),("Dermaplaning Facial",140,""),("Express Facial",85,""),("Dermaplaning",85,""),("Microneedling",300,""),("BioRepeel",175,""),("LED Light Therapy",25,"Add-on")],
 "Hair": [("Women's Haircut",50,""),("Men's Haircut",35,""),("Girls Haircut",40,"Ages 11 to 13"),("Boys Haircut",30,"Ages 11 to 13"),("Child's Haircut",25,"10 and under"),("Women's Blowout",35,"Includes wash"),("Styling with Flat or Curling Iron",35,"Includes wash"),("Curls",60,"No wash"),("Curls & Half Up",75,"No wash"),("Special Occasions / Up-Dos","from 100","Arrive with dry hair"),("Bang Trim","Free","For Dawn's regular clients")],
 "Colour": [("Colour and Haircut","from 115",""),("Colour and Blow-Dry","from 100",""),("Colour, Partial Highlight and Haircut","from 130",""),("Colour, Partial Highlight and Blow-Dry","from 120",""),("Partial Highlight and Haircut","from 130",""),("Partial Highlight and Blow-Dry","from 120","")],
 "Nails": [("Signature Manicure",35,""),("Signature Manicure with Permanent Polish",45,""),("Permanent Polish on Hands",45,""),("Signature Pedicure",60,""),("Signature Pedicure with Permanent Polish",75,""),("Men's Pedicure",50,"")],
 "Brows & Lashes": [("Korean Lash Lift & Tint",100,""),("Lash Lift & Tint",90,""),("Full Brow Shaping",25,""),("Brow Maintenance",20,""),("Eyebrow Tinting",20,""),("Eyelash Tint",30,""),("Eyebrow Wax and Tint",35,""),("Eyelash and Eyebrow Tinting",48,"")],
 "Waxing": [("Lip",18,""),("Chin",18,""),("Lip and Chin",35,""),("Brow and Lip Wax",35,""),("Full Face",60,""),("Underarms",25,""),("Half Arms",35,""),("Full Arms",45,""),("Bikini",35,""),("Brazilian",60,""),("Half Legs",45,""),("Full Legs",70,""),("Upper Leg and Bikini",75,""),("Full Leg and Bikini",100,""),("Back","from 50",""),("Chest","from 50","")],
 "Teeth & Makeup": [("Cosmetic Teeth Whitening",100,""),("Special Event Makeup",125,"")],
}

PRODUCTS = [
 ("is-clinical-super-serum-advance","iS Clinical","Super Serum Advance+","272.40","p1.jpg"),
 ("glymed-oxygen-cream","GlyMed Plus","Oxygen Cream","94.50","p2.png"),
 ("../collections/sun-protection","Colorescience","Face Shield Glow SPF 50","74.99","p3.png"),
 ("epicutis-lipid-serum","Epicutis","Lipid Serum","290.00","p4.jpg"),
 ("glymed-chocolate-masque","GlyMed Plus","Chocolate Masque","82.50","p7.jpg"),
 ("paul-mitchell-bond-rx-shampoo","Paul Mitchell","Bond RX Shampoo","33.00","p5.jpg"),
 ("kit-sch-pistachio-latte-hair-perfume","Kitsch","Pistachio Latte Hair Perfume","28.99","p6.jpg"),
 ("coconut-brown-sugar-body-scrub","Happy Hippo Bath Co.","Coconut & Brown Sugar Body Scrub","19.99","p8.jpg"),
]
COLLECTIONS = [
 ("nectar-country-club","Nectar Country Club","Our own line","c1.png"),
 ("happy-hippo-bath-co","Happy Hippo Bath Co.","Bath and body","c2.jpg"),
 ("hair-products","Hair","Care, styling and accessories","c3.jpg"),
 ("spa-essentials","Spa Essentials","Wraps, headbands and more","c4.jpg"),
]
REVIEWS = [
 ("Kate helped heal and clear my skin. Every facial is relaxing and effective, and the consultations are tailored to me.","Mackenzie B.","Google"),
 ("Top tier. Kate built a skincare routine that fit my budget and never pushed products on me.","Sara C.","Google"),
 ("Shelby shaped my brows perfectly. I'm so happy with how they turned out.","Kristy","Vagaro"),
 ("Calm, bright and welcoming. Dawn always gives a great haircut, and my pedicure with Shelby was gentle and down to earth.","Carl","Vagaro"),
]
HOURS = [("Tuesday","9:00 am to 5:30 pm"),("Wednesday","10:00 am to 8:00 pm"),("Thursday","9:00 am to 5:00 pm"),
         ("Friday","9:00 am to 4:00 pm"),("Saturday","9:00 am to 3:00 pm"),("Sunday",None),("Monday",None)]

def ext(url, text, cls="button"):
    return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener">{text}</a>'

def head(title, desc):
    return f"""<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300&family=Jost:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/theme.css">
</head>
<body>"""

def header(current):
    links = "".join(f'<a href="{f}"{" aria-current=\"page\"" if f==current else ""}>{n}</a>' for f,n in PAGES[1:])
    return f"""
<div class="announcement">Concept preview by Tyler Wedderburn, not the official Nectar Boutique site.</div>
<header class="header"><div class="page-width">
  <a class="header__logo" href="index.html"><img src="assets/img/logo.png" alt="Nectar Boutique" width="100" height="34"></a>
  <nav aria-label="Main">{links}</nav>
  <details class="menu-drawer"><summary aria-label="Menu">Menu</summary><nav aria-label="Mobile">{links}</nav></details>
  {ext(BOOK,"Book now","button button--primary")}
</div></header>
<main>"""

def footer():
    return f"""</main>
<footer class="footer"><div class="page-width">
  <div class="grid">
    <div><img src="assets/img/logo.png" alt="Nectar Boutique" width="77" height="26"><p style="margin:0">Facials, hair, nails, brows and lashes in Brandon, Manitoba.</p></div>
    <div><h4>Explore</h4><ul>{''.join(f'<li><a href="{f}">{n}</a></li>' for f,n in PAGES[1:])}</ul></div>
    <div><h4>Visit</h4><ul><li>1431 Princess Avenue<br>Brandon, MB R7A 0R6</li><li>204-922-0862</li><li><a href="https://www.instagram.com/nectarboutique_bdn" target="_blank" rel="noopener">Instagram</a></li></ul></div>
  </div>
  <p class="legal">Concept preview prepared for Nectar Boutique by Tyler Wedderburn, November 2026. Prices and products as listed on Vagaro and Shopify on November 17, 2026.</p>
</div></footer>
<div class="sticky-cta">{ext(BOOK,"Book","button button--primary")}<a class="button" href="shop.html">Shop</a></div>
</body></html>
"""

def money(p):
    if isinstance(p,int): return f"${p}"
    if p.startswith("from "): return f"<i>from</i>${p[5:]}"
    return e(p)

def product_grid(items):
    return '<div class="product-grid">' + "".join(
        f'<a class="card" href="{STORE}/products/{h}" target="_blank" rel="noopener"><div class="card__media"><img src="assets/img/{img}" alt="{e(v+" "+t)}" loading="lazy" width="600" height="600"></div><span class="card__vendor">{e(v)}</span><span class="card__title">{e(t)}</span><span class="card__price">${pr}</span></a>'
        for h,v,t,pr,img in items) + '</div>'

def collection_list():
    return '<div class="collection-list">' + "".join(
        f'<a class="collection-card" href="{STORE}/collections/{h}" target="_blank" rel="noopener"><div class="card__media"><img src="assets/img/{img}" alt="" loading="lazy"></div><h3>{e(t)}</h3><span class="subtle">{e(s)}</span></a>'
        for h,t,s,img in COLLECTIONS) + '</div>'

def testimonials():
    cards = "".join(f'<figure class="testimonial"><span class="stars" aria-label="5 stars">★★★★★</span><blockquote>{e(q)}</blockquote><figcaption><b>{e(n)}</b> · {src}</figcaption></figure>' for q,n,src in REVIEWS)
    return f"""<section class="section scheme-2"><div class="page-width">
  <div class="title-row"><div><p class="caption">Kind words</p><h2>Brandon's <em>calmest</em> hour.</h2></div>
  <div class="score"><b>4.8</b><span><span class="stars">★★★★★</span><br><span class="subtle">171 Google reviews</span></span></div></div>
  <div class="testimonials">{cards}</div>
  <p class="note">Preview note: quotes are condensed from public Google and Vagaro reviews and would use the reviewers' exact words on the live site. <a href="https://www.google.com/maps/search/?api=1&amp;query=Nectar+Boutique+1431+Princess+Ave+Brandon" target="_blank" rel="noopener">Read all reviews on Google</a></p>
</div></section>"""

def cta():
    return f"""<section class="section scheme-ink center"><div class="page-width">
  <h2>Your hour is <em>waiting.</em></h2>
  <p class="rte subtle">Choose a service, pick a time, done. Most bookings take under a minute.</p>
  <div class="buttons">{ext(BOOK,"Book an appointment","button button--primary")}<a class="button" href="shop.html">Shop skincare</a></div>
</div></section>"""

def page(fn, title, desc, body):
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(head(title, desc) + header(fn) + body + footer())

# ---------- Home ----------
page("index.html", "Nectar Boutique | Salon, Spa & Skin Studio in Brandon, MB",
 "Facials, hair, nails, brows and lashes on Princess Avenue in Brandon, plus professional skincare to take home.",
 f"""
<section class="section"><div class="page-width banner">
  <div>
    <p class="caption">Salon · Spa · Skin studio in Brandon, MB</p>
    <h1>Feel your best, <em>every day.</em></h1>
    <p class="rte subtle">Facials, hair, nails, brows and lashes on Princess Avenue, plus the professional skincare our estheticians use in the treatment room. Book a visit, or shop the shelf from home.</p>
    <div class="buttons">{ext(BOOK,"Book an appointment","button button--primary")}<a class="button" href="services.html">See the menu</a></div>
    <div class="rating"><span class="stars" aria-hidden="true">★★★★★</span><span><b>4.8</b> from 171 Google reviews</span></div>
  </div>
  <div class="banner__media"><img src="assets/img/c4.jpg" alt="Client in a checkered hair towel wrap" width="900" height="900"></div>
</div></section>

<section class="section scheme-2"><div class="page-width">
  <p class="caption">Signature treatments</p><h2>Where to <em>start.</em></h2>
  <div class="multicolumn">
    <div class="column"><p class="caption">Skin</p><h3>Custom Facial</h3><span class="price">$125</span><p class="subtle">A free skin consultation, then a facial built for what your skin needs that day.</p>{ext(BOOK,"Book a facial →","link")}</div>
    <div class="column"><p class="caption">Lashes</p><h3>Korean Lash Lift &amp; Tint</h3><span class="price">$100</span><p class="subtle">A soft, lasting curl with a tint to finish. No extensions and no mascara needed for weeks.</p>{ext(BOOK,"Book a lash lift →","link")}</div>
    <div class="column"><p class="caption">Nails</p><h3>Signature Pedicure</h3><span class="price">$60</span><p class="subtle">An hour in our calm pedicure room. Add permanent polish for $15 and walk out chip-free.</p>{ext(BOOK,"Book a pedicure →","link")}</div>
  </div>
</div></section>

<section class="section"><div class="page-width">
  <div class="title-row"><div><p class="caption">The shelf</p><h2>Take the <em>treatment</em> home.</h2></div><a class="button" href="shop.html">Shop all</a></div>
  {product_grid(PRODUCTS[:4])}
</div></section>
{testimonials()}
{cta()}""")

# ---------- Services ----------
blocks = "".join(
    f'<details{" open" if i==0 else ""}><summary>{e(cat)}<small>{len(items)} services</small></summary><div class="service-list">' +
    "".join(f'<div class="service"><div>{e(n)}{f"<small>{e(note)}</small>" if note else ""}</div><span class="price">{money(p)}</span>{ext(BOOK,"Book","")}</div>' for n,p,note in items) +
    '</div></details>'
    for i,(cat,items) in enumerate(SERVICES.items()))
count = sum(len(v) for v in SERVICES.values())
page("services.html", "Services & Prices | Nectar Boutique",
 "The full Nectar Boutique service menu with prices: facials, hair, colour, nails, brows, lashes, waxing, teeth whitening and makeup.",
 f"""
<section class="section"><div class="page-width">
  <p class="caption">The menu</p><h1>Services <em>&amp; prices.</em></h1>
  <p class="rte subtle">{count} services across seven categories. Prices are in Canadian dollars. Tap Book on any service to go straight to our booking calendar.</p>
  <div class="collapsible">{blocks}</div>
  <p class="note">Walk-ins are welcome when we have space. Please give 24 hours' notice to cancel: late cancellations are charged 50% of the service, and no-shows 100%.</p>
</div></section>
{cta()}""")

# ---------- Shop ----------
page("shop.html", "Shop Skincare & Spa Products | Nectar Boutique",
 "Professional skincare from iS Clinical, GlyMed Plus, Epicutis and Colorescience, plus hair care and bath products. Free pickup in Brandon.",
 f"""
<section class="section"><div class="page-width">
  <p class="caption">The shelf</p><h1>Professional skincare, <em>picked by our estheticians.</em></h1>
  <p class="rte subtle">The same lines we use in the treatment room. Not sure what suits your skin? Ask for a free consultation at your next visit. Pickup at the studio is always free.</p>
  {product_grid(PRODUCTS)}
  <div class="buttons">{ext(STORE+"/collections/all","Shop all products","button button--primary")}</div>
</div></section>
<section class="section scheme-2"><div class="page-width">
  <p class="caption">Collections</p><h2>Shop by <em>collection.</em></h2>
  {collection_list()}
</div></section>
<section class="section"><div class="page-width">
  <div class="multicolumn">
    <div class="column column--plain"><h3>Free pickup</h3><p class="subtle">Order online and collect at 1431 Princess Avenue during opening hours.</p></div>
    <div class="column column--plain"><h3>Free consultation</h3><p class="subtle">Our estheticians will help you build a routine that fits your skin and your budget.</p></div>
    <div class="column column--plain"><h3>Gift certificates</h3><p class="subtle">Treat someone to a facial, a pedicure or a shelf favourite.</p></div>
  </div>
</div></section>""")

# ---------- About ----------
team = [("Diane Finley","Owner and founder"),("Dawn Dolloff","Hair stylist"),("Shelby Mabon","Brows and nails"),("Kate","Esthetician")]
page("about.html", "About Us | Nectar Boutique",
 "Meet Diane, Dawn, Shelby and Kate, the team at Nectar Boutique in Brandon, Manitoba.",
 f"""
<section class="section"><div class="page-width image-with-text">
  <div class="image-with-text__media placeholder"><div><b>Your studio, here.</b><br>Placeholder for a photo of the treatment room or the team</div></div>
  <div>
    <p class="caption">About Nectar</p><h1>A small studio with a <em>big menu.</em></h1>
    <p class="rte subtle">Nectar Boutique was founded by Diane Finley to give Brandon one place to look after skin, hair and nails without rushing. Our team takes time with every client, starting with a conversation about what you want and what your skin needs.</p>
    <p class="rte subtle">We stock the professional lines we trust in the treatment room, so your results keep going after you leave.</p>
    <div class="buttons">{ext(BOOK,"Book a visit","button button--primary")}</div>
  </div>
</div></section>
<section class="section scheme-2"><div class="page-width">
  <p class="caption">The team</p><h2>Meet the <em>people</em> behind Nectar.</h2>
  <div class="multicolumn multicolumn--4">{''.join(f'<div class="column column--plain"><div class="initial">{n[0]}</div><h3>{e(n)}</h3><p class="subtle">{e(r)}</p></div>' for n,r in team)}</div>
</div></section>
{testimonials()}""")

# ---------- Visit ----------
hours = "".join(f'<span{" class=\"closed\"" if not h else ""}>{d}</span><span{" class=\"closed\"" if not h else ""}>{h or "Closed"}</span>' for d,h in HOURS)
page("visit.html", "Visit Us | Nectar Boutique, 1431 Princess Ave, Brandon",
 "Hours, address, parking and policies for Nectar Boutique at 1431 Princess Avenue, Brandon, Manitoba.",
 f"""
<section class="section"><div class="page-width">
  <p class="caption">Visit</p><h1>Find us on <em>Princess Avenue.</em></h1>
  <div class="contact">
    <div><h3>Studio</h3><p>1431 Princess Avenue<br>Brandon, MB R7A 0R6</p><p>204-922-0862</p>{ext("https://www.google.com/maps/search/?api=1&amp;query=1431+Princess+Ave+Brandon+MB","Get directions")}</div>
    <div><h3>Hours</h3><div class="hours">{hours}</div></div>
    <div><h3>Good to know</h3><ul class="list"><li>Free parking</li><li>Walk-ins welcome</li><li>LGBTQIA+ friendly</li><li>Kid friendly</li><li>Free WiFi</li><li>Cash, debit, Visa and Mastercard</li></ul></div>
  </div>
</div></section>
<section class="section scheme-2"><div class="page-width rte">
  <p class="caption">Policies</p><h2>Booking <em>&amp; cancellations.</em></h2>
  <p class="subtle">Please give at least 24 hours' notice if you need to cancel or move your appointment. Late cancellations are charged 50% of the service fee, and missed appointments are charged in full.</p>
  <p class="subtle">Questions? Call us at 204-922-0862 or message us on <a href="https://www.instagram.com/nectarboutique_bdn" target="_blank" rel="noopener">Instagram</a>.</p>
</div></section>
{cta()}""")
print("built", len(PAGES), "pages")
