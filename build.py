"""Builds the static portfolio pages. Edit content here, then run: python3 build.py

To add a PDF: put it in docs/ and set its path, e.g. "reflection": "docs/eide-bailly-reflection.pdf".
To add a photo: put it in images/ and set "photo": "images/eide-bailly.jpg" on that experience.
"""
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).parent

PROFILE_IMG = "https://static.wixstatic.com/media/487fb0_4a9c69a3c9184f11ae457a221ec77599~mv2.jpg/v1/fill/w_800,h_800,al_t,q_85/IMG_2065.jpg"
ABOUT_IMG = "https://static.wixstatic.com/media/487fb0_ee73f05dbf134b839bee34d99ba84827~mv2.jpg/v1/fill/w_840,h_800,al_c,q_85/IMG_2680.jpg"

HONORS_PAGES = [
    ("honors.html", "Honors Program"),
    ("leadership.html", "Leadership"),
    ("research.html", "Research"),
    ("intercultural.html", "Intercultural Engagement"),
]

# ---- Experiences. status: complete | progress | planned. doc: path to a PDF in /docs, or None until uploaded.
COMPETENCIES = {
    "leadership": {
        "title": "Leadership",
        "intro": "How I've learned to lead, from structured development programs to running an organization myself.",
        "experiences": [
            {
                "id": "eide-bailly-internship",
                "name": "Eide Bailly internship",
                "level": "Application", "when": "Spring 2026", "status": "complete",
                "summary": "A spring internship with Eide Bailly, a regional accounting and advisory firm, applying what I learned in the classroom on real client work as part of a team.",
                "reflection": None, "reflection_due": "HONR 375",
                "artifacts": [("Internship credit reflection", None), ("Internship description", None)],
            },
            {
                "id": "eide-bailly-slp",
                "name": "Eide Bailly SLP",
                "level": "Development", "when": "Summer 2025", "status": "complete",
                "summary": "Eide Bailly's student program that introduced me to the firm, its people, and the professional skills expected in public accounting.",
                "reflection": None, "reflection_due": "HONR 475",
                "artifacts": [],
            },
            {
                "id": "mec-president",
                "name": "President, Maverick Entrepreneurship Club",
                "level": "Application", "when": "Spring 2026 to present", "status": "progress",
                "summary": "Leading Minnesota State Mankato's entrepreneurship club: running the officer team, planning meetings and events, and updating the club constitution.",
                "reflection": None, "reflection_due": "HONR 475",
                "artifacts": [],
            },
        ],
    },
    "research": {
        "title": "Research, Scholarly & Creative Activity",
        "intro": "Projects where I gathered information, tested ideas, and built something original that others could use.",
        "experiences": [
            {
                "id": "ibe",
                "name": "Integrated Business Experience (IBE)",
                "level": "Application", "when": "", "status": "complete",
                "summary": "The College of Business course where students build and run a real company, from researching a product idea through selling it and presenting results.",
                "reflection": None, "reflection_due": "HONR 375",
                "artifacts": [("Presentation slides", None), ("Product and photos", None)],
            },
            {
                "id": "mn-apex-solutions",
                "name": "Owner, MN Apex Solutions",
                "level": "Application", "when": "Ongoing", "status": "progress",
                "summary": "As owner of a Minnesota floor coating company, I manage the financial side of the business: keeping the books, pricing jobs and preparing bids, and tracking the company's financial performance.",
                "reflection": None, "reflection_due": "HONR 475",
                "artifacts": [],
            },
            {
                "id": "mav-fund",
                "name": "Mav Fund",
                "level": "Application", "when": "", "status": "planned",
                "summary": "Planned participation in the Mav Fund.",
                "reflection": None, "reflection_due": "HONR 475",
                "artifacts": [],
            },
        ],
    },
    "intercultural": {
        "title": "Intercultural Engagement",
        "intro": "Experiences that have shaped how I understand my own culture and connect with people from others.",
        "experiences": [
            {
                "id": "exchange-student",
                "name": "Foreign exchange student experience",
                "level": "Application", "when": "2020 to present", "status": "complete",
                "summary": "A relationship with a foreign exchange student that started in 2020 and continues today, documented through photos over the years and letters.",
                "reflection": None, "reflection_due": "HONR 375",
                "artifacts": [("Letters", None), ("Photos over time", None)],
            },
            {
                "id": "study-abroad",
                "name": "Study abroad, KEDGE Business School",
                "level": "Application", "when": "Spring 2027", "status": "planned",
                "summary": "A planned semester at KEDGE Business School in Marseille, France.",
                "reflection": None, "reflection_due": "HONR 475",
                "artifacts": [],
            },
        ],
    },
}

STATUS_LABEL = {"complete": "Complete", "progress": "In progress", "planned": "Planned"}

# Simple shapes in the site palette, used where a photo hasn't been added yet.
ART = {
    "leadership": """<svg viewBox="0 0 300 340" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="300" height="340" fill="#8b6f90"/><path d="M40 260 L150 150 L260 260" fill="none" stroke="#febd11" stroke-width="18" stroke-linejoin="round"/><path d="M40 200 L150 90 L260 200" fill="none" stroke="#dcd8d9" stroke-width="18" stroke-linejoin="round" opacity=".55"/><path d="M40 320 L150 210 L260 320" fill="none" stroke="#49306e" stroke-width="18" stroke-linejoin="round"/></svg>""",
    "research": """<svg viewBox="0 0 300 340" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="300" height="340" fill="#3e375a"/><rect x="48" y="210" width="34" height="90" rx="3" fill="#8b6f90"/><rect x="104" y="160" width="34" height="140" rx="3" fill="#bbb7b9"/><rect x="160" y="120" width="34" height="180" rx="3" fill="#8b6f90"/><rect x="216" y="70" width="34" height="230" rx="3" fill="#febd11"/></svg>""",
    "intercultural": """<svg viewBox="0 0 300 340" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="300" height="340" fill="#dcd8d9"/><circle cx="115" cy="170" r="78" fill="#49306e" opacity=".9"/><circle cx="185" cy="170" r="78" fill="#febd11" opacity=".8"/><circle cx="150" cy="110" r="52" fill="#8b6f90" opacity=".75"/></svg>""",
    "honors": """<svg viewBox="0 0 300 340" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="300" height="340" fill="#49306e"/><circle cx="150" cy="170" r="90" fill="none" stroke="#febd11" stroke-width="14"/><circle cx="150" cy="170" r="50" fill="#8b6f90"/></svg>""",
}


def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='14' fill='%238b6f90'/%3E%3C/svg%3E">
</head>
"""


def header(active):
    def link(href, text):
        cur = ' aria-current="page"' if href == active else ""
        return f'<a href="{href}"{cur}>{e(text)}</a>'
    honors_active = active in [h for h, _ in HONORS_PAGES]
    sub = "".join(f"<li>{link(h, t)}</li>" for h, t in HONORS_PAGES)
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html">
      <span class="brand-dot" aria-hidden="true"></span>
      <span class="brand-name">Alex<br>Siebenaler</span>
      <span class="brand-sub">Quantitative Finance &amp; Accounting<br>Honors Student</span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav id="nav" aria-label="Main">
      <ul class="nav-list">
        <li>{link("index.html", "Home")}</li>
        <li class="has-sub{' is-active' if honors_active else ''}">
          <a href="honors.html"{' aria-current="true"' if honors_active else ''}>Honors</a>
          <ul class="sub">{sub}</ul>
        </li>
        <li>{link("about.html", "About Me")}</li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </div>
</header>
<main id="main">
"""


FOOTER = """</main>
<footer class="site-footer" id="contact">
  <div class="wrap footer-grid">
    <div><h2>Phone</h2><p><a href="tel:+16512336082">651-233-6082</a></p></div>
    <div><h2>Email</h2><p><a href="mailto:alex.siebenaler@mnsu.edu">alex.siebenaler@mnsu.edu</a><br><a href="mailto:ahsiebenaler@gmail.com">ahsiebenaler@gmail.com</a></p></div>
    <div><h2>Connect</h2><p><a href="https://www.linkedin.com/in/alex-siebenaler" target="_blank" rel="noopener">LinkedIn</a></p></div>
    <div class="fine"><p>Minnesota State University, Mankato<br>Honors Program portfolio</p></div>
  </div>
</footer>
<script>
const t=document.querySelector('.nav-toggle'),n=document.getElementById('nav');
t.addEventListener('click',()=>{const o=t.getAttribute('aria-expanded')==='true';t.setAttribute('aria-expanded',String(!o));n.classList.toggle('open',!o);});
</script>
</body>
</html>
"""


def doc_button(label, path, cls="btn"):
    if path:
        return f'<a class="{cls}" href="{e(path)}" target="_blank" rel="noopener">{e(label)}</a>'
    return f'<span class="{cls} is-pending" aria-disabled="true" title="Coming soon">{e(label)}<span class="soon">Coming soon</span></span>'


def page_title(title, intro):
    return f"""<section class="page-title"><div class="wrap"><h1>{e(title)}</h1><p>{e(intro)}</p></div></section>"""


def media(photo, alt, art_key):
    if photo:
        return f'<img src="{e(photo)}" alt="{e(alt)}" loading="lazy">'
    return ART[art_key]


def write(name, title, desc, body, active=None):
    (ROOT / name).write_text(head(title, desc) + header(active or name) + body + FOOTER)


# ---------------- Home
DIRECTORY = [
    ("leadership", "Leadership", "Eide Bailly internship; Eide Bailly SLP; Maverick Entrepreneurship Club"),
    ("research", "Research", "Integrated Business Experience; MN Apex Solutions; Mav Fund"),
    ("intercultural", "Intercultural Engagement", "Foreign exchange student experience; study abroad in Marseille"),
]

cards = "".join(f"""<a class="dir-card" href="{k}.html">
  <div class="dir-media">{ART[k]}</div>
  <div class="dir-box"><h3>{e(t)}</h3><p>{e(d)}</p><span class="pill pill-olive">Read</span></div>
</a>""" for k, t, d in DIRECTORY)

home = f"""<section class="hello">
  <div class="wrap hello-grid">
    <figure class="hello-photo"><img src="{PROFILE_IMG}" alt="Alex Siebenaler" width="420" height="420"></figure>
    <div class="hello-text">
      <h1>Hello</h1>
      <h2>A bit about me</h2>
      <p>I'm Alex Siebenaler, an Honors student at Minnesota State University, Mankato, studying quantitative finance and accounting. I expect to graduate in Spring 2028. This portfolio collects the experiences that have shaped me and my reflections on what each one taught me.</p>
      <p>Mission statement: to graduate and build a career in quantitative finance and accounting, while staying grounded in four values: growth and development, individualism, personal well-being, and belonging.</p>
      <div class="pill-row"><a class="pill pill-mauve" href="honors.html">Honors</a><a class="pill pill-gold" href="about.html">About Me</a></div>
    </div>
  </div>
</section>
<section class="directory">
  <div class="wrap">
    <h2 class="display">Directory</h2>
    <div class="dir-grid">{cards}</div>
  </div>
</section>
"""
write("index.html", "Home | Alex Siebenaler Honors Portfolio", "Alex Siebenaler's Minnesota State Mankato Honors Program portfolio.", home)

# ---------------- About
about = f"""{page_title("About Me", "A junior at Minnesota State University, Mankato, studying quantitative finance and accounting.")}
<section class="band">
  <div class="wrap">
    <article class="feature">
      <div class="feature-media">{media(ABOUT_IMG, "Alex Siebenaler", "honors")}</div>
      <div class="feature-card">
        <h2>Alex Siebenaler</h2>
        <h3>Honors Student, Class of 2028</h3>
        <dl class="facts">
          <dt>Majors</dt><dd>Quantitative Finance and Accounting</dd>
          <dt>Certificate</dt><dd>Business Analytics</dd>
          <dt>Graduation</dt><dd>Spring 2028</dd>
          <dt>Involvement</dt><dd>President, Maverick Entrepreneurship Club; Beta Alpha Psi; Student Executive Team</dd>
        </dl>
        <h4>Future goals</h4>
        <p>After graduation, I plan to start my career in quantitative finance and accounting, where I can pair analytical, data-driven work with a strong foundation in financial reporting. My Business Analytics certificate builds the data skills to support that path.</p>
        <h4>Hobbies and interests</h4>
        <p>I enjoy spending time with friends, playing and watching sports, working out, and games. I'm driven and competitive, and I like having something to work toward.</p>
      </div>
    </article>
  </div>
</section>
"""
write("about.html", "About Me | Alex Siebenaler", "About Alex Siebenaler: majors, goals and interests.", about)

# ---------------- Honors Program
essays = [
    ("HONR 201 Why Honors essay", "Written in Fall 2024, my first semester in the program.", None),
    ("HONR 375 Why Honors essay", "Written in Fall 2026, looking back on what Honors has meant so far.", None),
    ("Honors synthesis essay", "My final reflection tying all eight experiences together, written in HONR 475.", None),
]
essay_cards = "".join(f'<article class="essay-card"><h3>{e(t)}</h3><p>{e(d)}</p>{doc_button("Read essay", p)}</article>' for t, d, p in essays)

honors = f"""{page_title("Honors Program", "The Minnesota State Mankato Honors Program develops students in three competencies: leadership; research, scholarly and creative activity; and intercultural engagement.")}
<section class="band">
  <div class="wrap">
    <div class="band-intro">
      <h2>Why Honors</h2>
      <p>Honors students complete eight experiences across these competencies, at a development level (building the skill) and an application level (putting it to use), and reflect on each one. These essays explain why I joined the program and what it has meant to me.</p>
    </div>
    <div class="essay-grid">{essay_cards}</div>
  </div>
</section>
"""
write("honors.html", "Honors Program | Alex Siebenaler", "Alex Siebenaler's Why Honors essays.", honors)


# ---------------- Competency pages
LEVEL_LABEL = {"leadership": "Leadership", "research": "Research", "intercultural": "Intercultural"}
for k in COMPETENCIES:
    COMPETENCIES[k]["level_label"] = LEVEL_LABEL[k]


def meta_line(x):
    when = f" · {e(x['when'])}" if x["when"] else ""
    return f'<p class="meta"><span class="status s-{x["status"]}">{STATUS_LABEL[x["status"]]}</span>{when}</p>'


def experience_card(key, x):
    """Summary card on the competency page, linking to the experience's own page."""
    return f"""<article class="feature" id="{x['id']}">
  <div class="feature-media">{media(x.get('photo'), x['name'], key)}</div>
  <div class="feature-card">
    <h2>{e(x['name'])}</h2>
    <h3>{e(COMPETENCIES[key]['level_label'])} {e(x['level'])}</h3>
    {meta_line(x)}
    <p>{e(x['summary'])}</p>
    <div class="btn-row"><a class="btn" href="{x['id']}.html">View experience</a></div>
  </div>
</article>"""


def experience_page(key, x):
    c = COMPETENCIES[key]
    if x["reflection"]:
        reflection = f'<p>Read my full reflection on this experience.</p><div class="btn-row">{doc_button("Read reflection", x["reflection"])}</div>'
    else:
        reflection = (f'<p class="placeholder">This will be reflection text. My reflection on this experience '
                      f'is being written for {e(x["reflection_due"])} and will be posted here.</p>'
                      f'<div class="btn-row">{doc_button("Read reflection", None)}</div>')
    if x["artifacts"]:
        arts = "".join(f'<li><span>{e(label)}</span>{doc_button("Open", path)}</li>' for label, path in x["artifacts"])
        artifacts = f'<ul class="artifact-list">{arts}</ul>'
    else:
        artifacts = '<p class="muted">Artifacts for this experience will be added here.</p>'
    body = f"""<section class="page-title">
  <div class="wrap">
    <a class="back" href="{key}.html">Back to {e(c['title'])}</a>
    <h1>{e(x['name'])}</h1>
    <p class="kind">{e(c['level_label'])} {e(x['level'])}</p>
    {meta_line(x)}
  </div>
</section>
<section class="band">
  <div class="wrap">
    <article class="feature">
      <div class="feature-media">{media(x.get('photo'), x['name'], key)}</div>
      <div class="feature-card">
        <h2>About this experience</h2>
        <p>{e(x['summary'])}</p>
        <h4>Reflection</h4>
        {reflection}
      </div>
    </article>
  </div>
</section>
<section class="plain">
  <div class="wrap narrow">
    <h2>Artifacts</h2>
    {artifacts}
  </div>
</section>
"""
    write(f"{x['id']}.html", f"{x['name']} | Alex Siebenaler", f"{x['name']}: Alex Siebenaler's honors experience.", body, active=f"{key}.html")


def competency_page(key, extra=""):
    c = COMPETENCIES[key]
    body = (page_title(c["title"], c["intro"]) + extra
            + '<section class="band"><div class="wrap features">'
            + "".join(experience_card(key, x) for x in c["experiences"])
            + "</div></section>")
    write(f"{key}.html", f"{c['title']} | Alex Siebenaler", f"Alex Siebenaler's {c['title']} experiences.", body)
    for x in c["experiences"]:
        experience_page(key, x)


strengths = f"""<section class="plain plain-tight">
  <div class="wrap strengths">
    <div><h2>StrengthsFinder results</h2><p>My top five CliftonStrengths themes and the reports that explain them.</p></div>
    <div class="btn-row">{doc_button("Signature Themes report", None)}{doc_button("Strengths Insight Guide", None)}</div>
  </div>
</section>"""

competency_page("leadership", strengths)
competency_page("research")
competency_page("intercultural")
print("built")
