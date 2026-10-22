# -*- coding: utf-8 -*-
"""GODLY MUST — build lecture pages from Notion markdown dumps"""
import re, html, os

SRC = "src-lectures"
OUT = "lectures"
os.makedirs(OUT, exist_ok=True)

LECTURES = [
    ("electronics", "el-t1", "نظري 01", "نظري", "د. أكرم محمد حاتم"),
    ("electronics", "el-t2", "نظري 02", "نظري", "د. أكرم محمد حاتم"),
    ("electronics", "el-t3", "نظري 03", "نظري", "د. أكرم محمد حاتم"),
    ("electronics", "el-p1", "عملي 01", "مختبر", "م. زهراء عبد المهدي + م. عقيل علي"),
    ("electronics", "el-p2", "عملي 02", "مختبر", "م. زهراء عبد المهدي + م. عقيل علي"),
    ("electronics", "el-p3", "عملي 03", "مختبر", "م. زهراء عبد المهدي + م. عقيل علي"),
    ("ds", "ds-t1", "نظري 01", "نظري", "م.م عباس كامل"),
    ("ds", "ds-t2", "نظري 02", "نظري", "م.م عباس كامل"),
    ("ds", "ds-t3", "نظري 03", "نظري", "م.م عباس كامل"),
    ("ds", "ds-p1", "عملي 01", "مختبر", "م.م عباس كامل + ب. صبا صباح"),
    ("ds", "ds-p2", "عملي 02", "مختبر", "م.م عباس كامل + ب. صبا صباح"),
    ("ca", "ca-t1", "نظري 01", "نظري", "م. رسل العبيدي"),
    ("ca", "ca-t2", "نظري 02", "نظري", "م. رسل العبيدي"),
    ("ca", "ca-t3", "نظري 03", "نظري", "مرجع شامل — مبني على مخططات المحاضرة"),
    ("ca", "ca-p1", "عملي 01", "مختبر", "مختبر تركيب الحاسوب"),
    ("ca", "ca-p2", "عملي 02", "مختبر", "مختبر تركيب الحاسوب"),
]
SUBJ_AR = {"electronics": "أسس الإلكترونيك", "ds": "هياكل البيانات", "ca": "تركيب ومعمارية الحاسوب"}
SUBJ_EN = {"electronics": "ELECTRONICS FUNDAMENTALS", "ds": "DATA STRUCTURES & ALGORITHMS", "ca": "COMPUTER ORGANIZATION & ARCHITECTURE"}

def fmt_math(s):
    s = re.sub(r'_\{?([A-Za-z0-9]+)\}?', r'<sub>\1</sub>', s)
    s = re.sub(r'\^\{?([A-Za-z0-9]+)\}?', r'<sup>\1</sup>', s)
    for a, b in [('\\approx','≈'), ('\\times','×'), ('\\Omega','Ω'), ('\\mu','μ'), ('\\pi','π'), ('\\rightarrow','←'), ('\\cdot','·')]:
        s = s.replace(a, b)
    return s

def inline(t):
    t = t.strip()
    t = html.escape(t)
    for tag in ['b', 'i', 'u', 'code', 's']:
        t = t.replace(f'&lt;{tag}&gt;', f'<{tag}>').replace(f'&lt;/{tag}&gt;', f'</{tag}>')
    t = re.sub(r'&lt;span color="[^"]*"&gt;(.*?)&lt;/span&gt;', r'<b>\1</b>', t)
    t = re.sub(r'\$`([^`]+)`\$', lambda m: '<span class="math-tex">' + m.group(1) + '</span>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<i>\1</i>', t)
    return t

BLOCK_START = re.compile(r'^(```|<callout|<details|<table|<hr|!\[|#{1,4}\s|-\s|\d+\.\s|---$|<br|\$\$)')

def collect_until_close(lines, i, tag):
    first = lines[i].strip()
    after = re.sub(rf'^<{tag}[^>]*>', '', first)
    depth, buf = 1, ([after] if after.strip() else [])
    i += 1
    while i < len(lines):
        l = lines[i].strip()
        if re.match(rf'<{tag}\b', l):
            depth += 1
        if f'</{tag}>' in l:
            depth -= 1
            if depth == 0:
                before = l.replace(f'</{tag}>', '')
                if before.strip():
                    buf.append(before)
                i += 1
                break
        buf.append(l)
        i += 1
    return '\n'.join(buf), i

def render_table(inner):
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', inner, re.S)
    out = ['<div class="tbl-wrap"><table class="tbl">']
    for ri, r in enumerate(rows):
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)
        tag = 'th' if ri == 0 else 'td'
        out.append('<tr>' + ''.join(f'<{tag}>{inline(c)}</{tag}>' for c in cells) + '</tr>')
    out.append('</table></div>')
    return '\n'.join(out)

def parse_blocks(text):
    lines = text.split('\n')
    out, i = [], 0
    while i < len(lines):
        s = lines[i].strip()
        if not s:
            i += 1; continue
        if s == '$$':
            buf = []
            i += 1
            while i < len(lines) and lines[i].strip() != '$$':
                buf.append(lines[i].strip()); i += 1
            i += 1
            out.append('<div class="math-tex math-tex--display">' + html.escape(' '.join(buf)) + '</div>')
            continue
        if s.startswith('```'):
            lang = s[3:].strip() or 'code'
            buf, i = [], i + 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                buf.append(lines[i]); i += 1
            i += 1
            out.append(f'<pre class="code" dir="ltr"><code class="lang-{html.escape(lang)}">{html.escape(chr(10).join(buf))}</code></pre>')
            continue
        m = re.match(r'<callout(?:\s+icon="([^"]*)")?(?:\s+color="([^"]*)")?\s*>', s)
        if m:
            inner, i = collect_until_close(lines, i, 'callout')
            out.append(f'<div class="callout"><span class="callout__icon">{m.group(1) or "💡"}</span><div class="callout__body">{parse_blocks(inner)}</div></div>')
            continue
        if re.match(r'<details\b', s):
            inner, i = collect_until_close(lines, i, 'details')
            sm = re.search(r'<summary>(.*?)</summary>', inner, re.S)
            title = inline(sm.group(1)) if sm else ''
            body = inner[sm.end():] if sm else inner
            out.append(f'<details class="tg"><summary><span>{title}</span><span class="tg__plus" aria-hidden="true">+</span></summary><div class="tg__body">{parse_blocks(body)}</div></details>')
            continue
        if re.match(r'<table\b', s):
            inner, i = collect_until_close(lines, i, 'table')
            out.append(render_table(inner))
            continue
        m = re.match(r'!\[[^\]]*\]\((\S+)\)', s)
        if m:
            fname = m.group(1).split('/')[-1].split('?')[0].split('#')[0]
            cap = ''
            if i + 1 < len(lines) and lines[i+1].strip() and not BLOCK_START.match(lines[i+1].strip()):
                cap = lines[i+1].strip(); i += 1
            fig = f'<figure class="fig"><img src="assets/{html.escape(fname)}" alt="{html.escape(cap)}" loading="lazy">'
            if cap:
                fig += f'<figcaption>{inline(cap)}</figcaption>'
            out.append(fig + '</figure>')
            i += 1; continue
        if s == '---':
            out.append('<hr class="rule">'); i += 1; continue
        m = re.match(r'(#{1,4})\s+(.*)', s)
        if m:
            lvl = len(m.group(1))
            out.append(f'<h{lvl} class="doc-h{lvl}">{inline(m.group(2))}</h{lvl}>')
            i += 1; continue
        if re.match(r'-\s+', s):
            items = []
            while i < len(lines) and re.match(r'-\s+', lines[i].strip()):
                items.append(re.sub(r'^-\s+', '', lines[i].strip())); i += 1
            out.append('<ul class="lst">' + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ul>')
            continue
        if re.match(r'\d+\.\s+', s):
            items = []
            while i < len(lines) and re.match(r'\d+\.\s+', lines[i].strip()):
                items.append(re.sub(r'^\d+\.\s+', '', lines[i].strip())); i += 1
            out.append('<ol class="lst lst--num">' + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ol>')
            continue
        buf = [s]; i += 1
        while i < len(lines) and lines[i].strip() and not BLOCK_START.match(lines[i].strip()):
            buf.append(lines[i].strip()); i += 1
        out.append('<p class="para">' + '<br>'.join(inline(x) for x in buf) + '</p>')
    return '\n'.join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{code} — {title_ar} | GODLY MUST</title>
<meta name="description" content="{title_ar} — {title_en} · {subj_ar}">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<link rel="stylesheet" href="../styles.css">
</head>
<body class="docpage">
<div class="noise" aria-hidden="true"></div>
<header class="nav">
  <a class="nav__logo mono" href="../index.html" dir="ltr">GODLY&nbsp;MUST<sup>®</sup></a>
  <nav class="nav__links"><a href="../index.html#subjects">← الأرشيف</a></nav>
  <span class="nav__cta mono docpage__subj" dir="ltr">{subj_en}</span>
</header>
<main>
  <header class="doc__head">
    <div class="doc__meta mono"><span class="doc__code">{code}</span><span class="doc__type doc__type--{typecls}">{type_ar}</span></div>
    <h1 class="doc__title">{title_ar}</h1>
    <div class="doc__en mono" dir="ltr">{title_en}</div>
    <div class="doc__teach">👤 {teach} · {subj_ar}</div>
  </header>
  <article class="doc">
{content}
  </article>
  <nav class="doc__pager">
    {prev_html}
    <a class="btn" href="../index.html#subjects">كل المحاضرات</a>
    {next_html}
  </nav>
</main>
<footer class="footer footer--mini">
  <div class="footer__bar mono">
    <span>© 2026 GODLY MUST</span>
    <span>صُنع بحب في العراق 🇮🇶</span>
  </div>
</footer>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function () {{
  document.querySelectorAll('.math-tex').forEach(function (el) {{
    katex.render(el.textContent, el, {{ displayMode: el.classList.contains('math-tex--display'), throwOnError: false }});
  }});
}});
</script>
</body>
</html>
"""

def split_title(raw):
    # "المحاضرة 1 نظري: أشباه الموصلات ومستويات الطاقة — Semiconductors & Energy Levels"
    # "عملي 1: مدخل إلى البرمجة كائنية التوجه — OOP Lab 1"
    ar, en = raw, ""
    if ' — ' in raw:
        ar, en = raw.split(' — ', 1)
    if ': ' in ar:
        ar = ar.split(': ', 1)[1]
    elif ':' in ar:
        ar = ar.split(':', 1)[1]
    return ar.strip(), en.strip()

pages = []
for subj, slug, code, type_ar, teach in LECTURES:
    raw = open(f"{SRC}/{slug}.md", encoding='utf-8').read()
    fm = re.match(r"---\ntitle: '(.*?)'\n---\n", raw, re.S)
    title_raw = fm.group(1) if fm else slug
    body = raw[fm.end():] if fm else raw
    title_ar, title_en = split_title(title_raw)
    pages.append({"subj": subj, "slug": slug, "code": code, "type_ar": type_ar,
                  "teach": teach, "title_ar": title_ar, "title_en": title_en, "body": body})

for idx, p in enumerate(pages):
    content = parse_blocks(p["body"])
    # prev / next within same subject
    same = [x for x in pages if x["subj"] == p["subj"]]
    pos = [i for i, x in enumerate(same) if x["slug"] == p["slug"]][0]
    prev_html = (f'<a class="btn btn--solid" href="{same[pos-1]["slug"]}.html">→ السابقة: {same[pos-1]["code"]}</a>' if pos > 0
                 else '<span></span>')
    next_html = (f'<a class="btn btn--solid" href="{same[pos+1]["slug"]}.html">التالية: {same[pos+1]["code"]} ←</a>' if pos < len(same)-1
                 else '<span></span>')
    html_out = TEMPLATE.format(
        code=p["code"], title_ar=p["title_ar"], title_en=p["title_en"],
        subj_ar=SUBJ_AR[p["subj"]], subj_en=SUBJ_EN[p["subj"]],
        teach=p["teach"], type_ar=p["type_ar"],
        typecls="lab" if p["type_ar"] == "مختبر" else "theory",
        content=content, prev_html=prev_html, next_html=next_html)
    open(f"{OUT}/{p['slug']}.html", "w", encoding='utf-8').write(html_out)
    print(f"✅ {p['slug']}.html — {p['title_ar'][:40]} ({len(html_out)//1024}KB)")

print("DONE —", len(pages), "lecture pages")
