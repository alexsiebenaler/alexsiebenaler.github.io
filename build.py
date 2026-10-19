"""Builds the static portfolio pages. Edit content here, then run: python3 build.py"""
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).parent

PROFILE_IMG = "https://static.wixstatic.com/media/487fb0_4a9c69a3c9184f11ae457a221ec77599~mv2.jpg/v1/fill/w_726,h_1080,al_c,q_85/IMG_2065.jpg"
ABOUT_IMG = "https://static.wixstatic.com/media/487fb0_ee73f05dbf134b839bee34d99ba84827~mv2.jpg/v1/fill/w_840,h_800,al_c,q_85/IMG_2680.jpg"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About me"),
    ("honors.html", "Honors Program"),
    ("leadership.html", "Leadership"),
    ("research.html", "Research"),
    ("intercultural.html", "Intercultural"),
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
                "id": "business-owner",
                "name": "Business owner, MN Apex Solutions",
                "level": "Application", "when": "Ongoing", "status": "progress",
                "summary": "Running a Minnesota floor coating company, handling both the technical side of polyurea and polyaspartic systems and business development.",
                "reflection": None, "reflection_due": "HONR 475",
                "artifacts": [],
            },
            {
                "id": "mav-fund",
                "name": "Mav Fund",
                "level": "Application", "when": "Planned", "status": "planned",
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
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;700;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%2349306e'/%3E%3Ctext x='16' y='22' font-family='Arial' font-weight='700' font-size='15' fill='%23febd11' text-anchor='middle'%3EAS%3C/text%3E%3C/svg%3E">
</head>
"""


def header(active):
    links = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{e(t)}</a></li>' for h, t in NAV
    )
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html">Alex Siebenaler</a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav id="nav" aria-label="Main"><ul>{links}<li><a href="#contact">Contact</a></li></ul></nav>
  </div>
</header>
<main id="main">
"""


FOOTER = """</main>
<footer class="site-footer" id="contact">
  <div class="wrap footer-inner">
    <div>
      <h2>Contact</h2>
      <p>Questions about my portfolio? I'm glad to talk through any of it.</p>
    </div>
    <dl class="contact-list">
      <dt>Email</dt><dd><a href="mailto:alex.siebenaler@mnsu.edu">alex.siebenaler@mnsu.edu</a></dd>
      <dt>Personal</dt><dd><a href="mailto:ahsiebenaler@gmail.com">ahsiebenaler@gmail.com</a></dd>
      <dt>Phone</dt><dd><a href="tel:+16512336082">651-233-6082</a></dd>
      <dt>LinkedIn</dt><dd><a href="https://www.linkedin.com/in/alex-siebenaler" target="_blank" rel="noopener">alex-siebenaler</a></dd>
    </dl>
  </div>
  <div class="wrap fine">Minnesota State University, Mankato Honors Program portfolio</div>
</footer>
<script>
const t=document.querySelector('.nav-toggle'),n=document.getElementById('nav');
t.addEventListener('click',()=>{const o=t.getAttribute('aria-expanded')==='true';t.setAttribute('aria-expanded',String(!o));n.classList.toggle('open',!o);});
</script>
</body>
</html>
"""


def doc_button(label, path, pending_label=None):
    if path:
        return f'<a class="btn" href="{e(path)}" target="_blank" rel="noopener">{e(label)}</a>'
    return f'<span class="btn btn-pending" aria-disabled="true">{e(pending_label or label)}<small>Coming soon</small></span>'


def page_header(title, intro):
    return f"""<section class="page-head"><div class="wrap"><h1>{e(title)}</h1><p class="lede">{e(intro)}</p></div></section>"""


def write(name, title, desc, body):
    (ROOT / name).write_text(head(title, desc) + header(name) + body + FOOTER)


# ---------------- Home
def experience_map():
    cols = []
    for key, c in COMPETENCIES.items():
        items = "".join(
            f'<li class="s-{x["status"]}"><a href="{key}.html#{x["id"]}"><span class="dot" aria-hidden="true"></span>'
            f'<span class="xname">{e(x["name"])}</span><span class="xmeta">{e(x["level"])}, {e(STATUS_LABEL[x["status"]].lower())}</span></a></li>'
            for x in c["experiences"]
        )
        short = {"research": "Research, Scholarly & Creative"}.get(key, c["title"])
        cols.append(f'<div class="map-col"><h3><a href="{key}.html">{e(short)}</a></h3><ul>{items}</ul></div>')
    done = sum(x["status"] == "complete" for c in COMPETENCIES.values() for x in c["experiences"])
    return f"""<div class="map" aria-label="Honors experience map">
  <div class="map-top"><p><strong>{done} of 8</strong> required honors experiences complete</p>
  <ul class="legend"><li class="s-complete"><span class="dot"></span>Complete</li><li class="s-progress"><span class="dot"></span>In progress</li><li class="s-planned"><span class="dot"></span>Planned</li></ul></div>
  <div class="map-cols">{''.join(cols)}</div>
</div>"""


home = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-text">
      <h1>Alex<br>Siebenaler</h1>
      <p class="subtitle">Honors Portfolio, Minnesota State University, Mankato</p>
      <p class="welcome">Welcome. This portfolio collects the experiences that have shaped me as a leader, a researcher, and a person who works across cultures, along with my reflections on what each one taught me.</p>
    </div>
    <figure class="hero-photo"><img src="{PROFILE_IMG}" alt="Portrait of Alex Siebenaler" width="363" height="540"></figure>
  </div>
</section>
<section class="band">
  <div class="wrap mission">
    <h2>Mission</h2>
    <div>
      <p class="big-serif">To graduate, build a career in accounting and finance, and eventually start businesses of my own, while staying grounded in four values: growth and development, individualism, personal well-being, and belonging.</p>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>My honors experiences</h2><p>The Honors Program asks for eight experiences across three competencies. Select any experience to read about it.</p></div>
    {experience_map()}
  </div>
</section>
<section class="section section-tight">
  <div class="wrap explore">
    <a href="about.html"><h3>About me</h3><p>My majors, goals, and what I do outside class.</p></a>
    <a href="honors.html"><h3>Honors Program</h3><p>Why I chose Honors, in my own essays.</p></a>
    <a href="leadership.html"><h3>Leadership</h3><p>Strengths results and leadership experiences.</p></a>
  </div>
</section>
"""
write("index.html", "Alex Siebenaler | Honors Portfolio", "Alex Siebenaler's Minnesota State Mankato Honors Program portfolio.", home)

# ---------------- About
about = f"""{page_header("About me", "Junior at Minnesota State University, Mankato, studying quantitative finance and accounting.")}
<section class="section">
  <div class="wrap about-grid">
    <figure class="about-photo"><img src="{ABOUT_IMG}" alt="Alex Siebenaler" width="420" height="400"></figure>
    <div class="prose">
      <dl class="facts">
        <dt>Majors</dt><dd>Quantitative Finance and Accounting</dd>
        <dt>Minor</dt><dd>Business Analytics</dd>
        <dt>Graduation</dt><dd>Spring 2028</dd>
        <dt>Involvement</dt><dd>Honors Program; President, Maverick Entrepreneurship Club; Beta Alpha Psi; Student Executive Team</dd>
      </dl>
      <h2>Where I'm headed</h2>
      <p>I plan to work in accounting and finance after graduation. Longer term, I want to keep building businesses. I already run MN Apex Solutions, a Minnesota floor coating company, and the experience of owning a business has shaped how I think about leadership, risk, and responsibility.</p>
      <h2>Outside of class</h2>
      <p>I enjoy spending time with friends, playing and watching sports, working out, and games. I'm driven and competitive, and I like having something to work toward.</p>
    </div>
  </div>
</section>
"""
write("about.html", "About me | Alex Siebenaler", "About Alex Siebenaler: majors, goals and interests.", about)

# ---------------- Honors Program
honors = f"""{page_header("Honors Program", "The Minnesota State Mankato Honors Program develops students in three competencies: leadership, research, scholarly and creative activity, and intercultural engagement.")}
<section class="section">
  <div class="wrap prose">
    <p>Honors students complete eight experiences across these competencies, at both a development level (building the skill) and an application level (putting it to use), and reflect on each one. This portfolio is where those experiences and reflections live, and it's what I'll defend at the end of the program.</p>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <div class="section-head"><h2>Why Honors</h2><p>Why I joined the program, why I've stayed, and the synthesis essay that ties it all together.</p></div>
    <div class="essays">
      <article class="essay"><h3>HONR 201 essay</h3><p>Written in Fall 2024, my first semester in the program.</p>{doc_button("Read essay (PDF)", None, "Read essay")}</article>
      <article class="essay"><h3>HONR 375 essay</h3><p>Written in Fall 2026, looking back on what Honors has meant so far.</p>{doc_button("Read essay (PDF)", None, "Read essay")}</article>
      <article class="essay"><h3>Synthesis essay</h3><p>My final reflection tying all eight experiences together, written in HONR 475.</p>{doc_button("Read essay (PDF)", None, "Read essay")}</article>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap prose">
    <h2>Honors with Distinction</h2>
    <p>I'm working toward Honors with Distinction, which requires three language courses beyond my level before college. I've completed SPAN 201 and SPAN 202.</p>
  </div>
</section>
"""
write("honors.html", "Honors Program | Alex Siebenaler", "Alex Siebenaler's Why Honors essays.", honors)


# ---------------- Competency pages
def experience_block(x):
    meta = (f'<dl class="xfacts"><div><dt>Level</dt><dd>{e(x["level"])}</dd></div>'
            + (f'<div><dt>When</dt><dd>{e(x["when"])}</dd></div>' if x["when"] else "")
            + f'<div><dt>Status</dt><dd class="s-{x["status"]}"><span class="dot"></span>{STATUS_LABEL[x["status"]]}</dd></div></dl>')
    if x["reflection"]:
        refl = f'<div class="actions">{doc_button("Read reflection (PDF)", x["reflection"])}'
    else:
        refl = (f'<div class="placeholder"><h4>Reflection</h4><p>This will be reflection text. My reflection on this experience is being written for {e(x["reflection_due"])} and will be posted here.</p></div>'
                f'<div class="actions">')
    arts = "".join(doc_button(f"{label} (PDF)", path, label) for label, path in x["artifacts"])
    if not x["artifacts"]:
        arts = '<p class="muted small">Artifacts will be added as this experience is documented.</p>'
    return f"""<article class="experience" id="{x['id']}">
  <div class="x-main">
    <h2>{e(x['name'])}</h2>
    {meta}
    <p>{e(x['summary'])}</p>
    {refl}{arts}</div>
  </div>
</article>"""


def competency_page(key, extra=""):
    c = COMPETENCIES[key]
    body = page_header(c["title"], c["intro"]) + extra + '<section class="section"><div class="wrap experiences">' + \
        "".join(experience_block(x) for x in c["experiences"]) + "</div></section>"
    write(f"{key}.html", f"{c['title']} | Alex Siebenaler", f"Alex Siebenaler's {c['title']} experiences.", body)


strengths = f"""<section class="section section-alt">
  <div class="wrap strengths">
    <div><h2>StrengthsFinder results</h2><p>My top five CliftonStrengths themes, and the reports that explain how they show up in my work.</p></div>
    <div class="actions">{doc_button("Signature Themes report (PDF)", None, "Signature Themes report")}{doc_button("Strengths Insight Guide (PDF)", None, "Strengths Insight Guide")}</div>
  </div>
</section>"""

competency_page("leadership", strengths)
competency_page("research")
competency_page("intercultural")
print("built")
