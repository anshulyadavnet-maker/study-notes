#!/usr/bin/env python3
"""StudyHub Point PET Markdown -> PDF renderer.

Semantic PET boxes are rendered as Markdown first, then wrapped in stable
HTML. This preserves bold/italic text, lists, tables, code and blockquotes.
Both multiline and single-line ::: box syntax are supported.
"""
import argparse, html, re, sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import md2pdf as pipeline
try:
    from watermark import auto_watermark_pdf
except Exception:
    auto_watermark_pdf=None

SOCIAL_LINKS=[
("Instagram","@studyhub.point","https://www.instagram.com/studyhub.point/"),
("YouTube","@studyhub.points","https://www.youtube.com/@studyhub.points"),
("Telegram","studyhub_point","https://t.me/studyhub_point"),
("Website","studyhubpoint","https://studyhubpoint.anshulyadav.net/"),
]

PET_CSS=r'''
body.pet-document{background:#fffdf8;color:#20242b}
.pet-cover{page-break-after:always;min-height:92vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:15mm 10mm;box-sizing:border-box}
.pet-cover .kicker{font-size:11pt;font-weight:800;letter-spacing:.12em;color:#1769aa;text-transform:uppercase;margin-bottom:4mm}
.pet-cover h1{font-size:26pt;line-height:1.2;color:#12385a;margin:2mm 0 4mm}.pet-cover .rule{width:32mm;height:3pt;background:#1769aa;margin:3mm auto 5mm}.pet-cover .sub{font-size:14pt;color:#4b5563;margin-bottom:6mm}.pet-cover .meta{font-size:10pt;color:#6b7280;margin-bottom:6mm}.pet-cover .badge{display:inline-block;background:#eef6ff;color:#1769aa;border:1pt solid #1769aa;padding:2mm 5mm;border-radius:3mm;font-weight:700;font-size:11pt}
.cover-social{display:flex;flex-wrap:wrap;justify-content:center;gap:2.5mm;margin-top:7mm}.social-pill{display:inline-block;padding:1.5mm 3.5mm;border:1pt solid #d1d5db;border-radius:20mm;background:#fff;color:#374151;font-size:8.5pt;font-weight:600;text-decoration:none}
body.pet-document h1.pet-heading{margin-top:7mm;padding:4mm 5mm;border-radius:3mm;border-left:7pt solid #1769aa;background:#eef6ff;color:#12385a;box-shadow:0 .8mm 0 rgba(23,105,170,.12)}
body.pet-document h2.pet-heading{margin-top:5mm;padding:2.8mm 3.5mm;border:1pt solid #d4dbe4;border-left:5pt solid #1769aa;border-radius:2mm;background:#f7faff;color:#18324b}
body.pet-document h3.pet-heading{margin-top:3.5mm;padding:2mm 3mm;border-left:4pt solid #0b7377;border-bottom:1pt solid #d4e5e5;background:#f3fbfb;border-radius:0 1.5mm 1.5mm 0}
body.pet-document h4.pet-heading{padding:1.5mm 2.5mm;border-left:3pt solid #9a6500;background:#fff9ec;border-radius:0 1.5mm 1.5mm 0}
.pet-box{margin:3.5mm 0;padding:3.2mm 4mm;border:1pt solid #cfd6de;border-left:5pt solid #64748b;border-radius:2.2mm;page-break-inside:avoid;box-shadow:0 .6mm 0 rgba(30,41,59,.035)}
.pet-box .pet-box-title{margin:0 0 1.5mm;font-weight:800;font-size:10.5pt}.pet-box p:last-child{margin-bottom:0}
.pet-concept{border-left-color:#1769aa;background:#f1f7fd}.pet-trick{border-left-color:#a45c00;background:#fff7e8}.pet-tip{border-left-color:#0b7377;background:#effafa}.pet-warning{border-left-color:#b52e3c;background:#fff1f2}.pet-example{border-left-color:#5667a8;background:#f4f5ff}.pet-formula{border-left-color:#1769aa;background:#edf5ff}.pet-remember{border-left-color:#157347;background:#effaf3}.pet-pyq{border-left-color:#7a4e9e;background:#f8f2fc}.pet-practice{border-left-color:#236a8b;background:#f0f8fb}.pet-fact{border-left-color:#8a6100;background:#fff9ed}.pet-trap{border-left-color:#c27a16;background:#fff6df}
.pet-box strong,.pet-box b{font-weight:800}.pet-box em,.pet-box i{font-style:italic}.pet-box table{width:100%;margin:2mm 0}.pet-box ul,.pet-box ol{margin-top:1.5mm;margin-bottom:1.5mm}
body.pet-document table{page-break-inside:avoid}.pet-back-cover{page-break-before:always;min-height:85vh;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:15mm 10mm;box-sizing:border-box}.bc-card{width:100%;max-width:160mm;border:1.5pt solid #d4dbe4;border-radius:4mm;padding:8mm;background:#fff;text-align:center}.bc-logo{font-size:18pt;font-weight:800;color:#12385a}.bc-tagline{font-size:10pt;color:#4b5563;margin:2mm 0 4mm}.bc-grid{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm;margin:4mm 0}.bc-item{display:block;padding:2mm 3mm;border:1pt solid #e5e7eb;border-radius:2mm;background:#f9fafb;text-decoration:none;color:#1f2937;text-align:left}.bc-platform{font-size:9.5pt;font-weight:700}.bc-handle{font-size:8pt;color:#4b5563}
'''

ALLOWED={"concept":"Core Concept","trick":"⚡ Trick","tip":"💡 Exam Tip","warning":"⚠ Warning","example":"Example","formula":"Formula","remember":"🔑 Remember","pyq":"PYQ Focus","practice":"Practice","fact":"Important Fact","trap":"⚠ Trap"}
PET_RULES=[("pet-history",("भारतीय इतिहास","History")),("pet-movement",("राष्ट्रीय आंदोलन","National Movement")),("pet-geography",("भूगोल","Geography")),("pet-economy",("भारतीय अर्थव्यवस्था","Indian Economy")),("pet-polity",("संविधान","लोक प्रशासन","Indian Constitution","Public Administration")),("pet-science",("सामान्य विज्ञान","General Science")),("pet-maths",("प्रारम्भिक अंकगणित","Arithmetic")),("pet-hindi",("सामान्य हिन्दी","Hindi")),("pet-english",("General English","English")),("pet-reasoning",("तर्क एवं तर्कशक्ति","Reasoning")),("pet-current",("सामयिकी","Current Affairs")),("pet-awareness",("सामान्य जागरूकता","General Awareness")),("pet-passage",("अपठित हिन्दी गद्यांश","Hindi Passage"))]

def _markdown_html(md):
    import markdown
    md=pipeline.convert_icons(md); md=pipeline.convert_figures(md); md=pipeline.split_adjacent_blockquotes(md)
    return markdown.markdown(md,extensions=["tables","fenced_code","sane_lists","attr_list"],output_format="html5")

def _render_box(kind,title,body):
    rendered=_markdown_html(body.strip()) if body.strip() else ""
    return f'<div class="pet-box pet-{kind}"><p class="pet-box-title">{html.escape(title)}</p>{rendered}</div>'

def convert_pet_boxes(md):
    """Parse multiline and single-line ::: semantic boxes safely."""
    lines=md.splitlines(); out=[]; i=0
    opener=re.compile(r'^:::\s*(\w+)(?:\s+(.*?))?\s*$')
    single=re.compile(r'^:::\s*(\w+)\s+(.*?)\s*:::\s*$')
    while i<len(lines):
        line=lines[i]
        m=single.match(line.strip())
        if m and m.group(1).lower() in ALLOWED:
            kind=m.group(1).lower(); rest=m.group(2).strip(); out.append(_render_box(kind,ALLOWED[kind],rest)); i+=1; continue
        m=opener.match(line.strip())
        if m and m.group(1).lower() in ALLOWED:
            kind=m.group(1).lower(); title=m.group(2).strip() if m.group(2) else ALLOWED[kind]; body=[]; i+=1
            while i<len(lines) and lines[i].strip()!=':::': body.append(lines[i]); i+=1
            if i<len(lines) and lines[i].strip()==':::': i+=1
            out.append(_render_box(kind,title,'\n'.join(body))); continue
        out.append(line); i+=1
    return '\n'.join(out)

HEADING_RE=re.compile(r'<h([1-4])([^>]*)>(.*?)</h\1>',re.S); TAG_RE=re.compile(r'<[^>]+>')
def heading_class(text):
    low=html.unescape(TAG_RE.sub('',text)).casefold()
    for cls,keys in PET_RULES:
        if any(k.casefold() in low for k in keys): return cls
    return 'pet-general'
def decorate_headings(h):
    def repl(m):
        level,attrs,inner=m.groups(); cls='pet-heading '+heading_class(inner); cm=re.search(r'\bclass="([^"]*)"',attrs)
        attrs=(attrs[:cm.start(1)]+cm.group(1)+' '+cls+attrs[cm.end(1):]) if cm else attrs+f' class="{cls}"'
        return f'<h{level}{attrs}>{inner}</h{level}>'
    return HEADING_RE.sub(repl,h)

def render_markdown(md,prefix=''):
    md=convert_pet_boxes(md); rendered=_markdown_html(md); rendered=pipeline.colour_blockquotes(rendered); rendered=pipeline.convert_tasks(rendered); rendered=decorate_headings(rendered)
    return pipeline.prefix_ids(rendered,prefix) if prefix else rendered

def social_pills(): return ''.join(f'<a href="{u}" class="social-pill" target="_blank">{html.escape(p)} · {html.escape(h)}</a>' for p,h,u in SOCIAL_LINKS)
def build_cover(title,subtitle,meta,badge):
    mh=''.join(f'<div>{html.escape(x)}</div>' for x in meta if x)
    return f'<section class="pet-cover"><div class="kicker">Study Notes · UPSSSC PET 2026</div><h1>{html.escape(title)}</h1><div class="rule"></div><div class="sub">{html.escape(subtitle)}</div><div class="meta">{mh}</div><div class="badge">{html.escape(badge)}</div><div class="cover-social">{social_pills()}</div></section>'
def build_back_cover():
    cards=''.join(f'<a href="{u}" target="_blank" class="bc-item"><span class="bc-platform">{html.escape(p)}</span><br><span class="bc-handle">{html.escape(h)}</span></a>' for p,h,u in SOCIAL_LINKS)
    return f'<section class="pet-back-cover"><div class="bc-card"><div class="bc-logo">StudyHub Point</div><div class="bc-tagline">आपकी सफलता, हमारा संकल्प · Best Wishes for Your UPSSSC PET Preparation!</div><div class="bc-grid">{cards}</div></div></section>'

def render_pet_pdf(files,output,title,subtitle='',author='',badge='PET 2026',show_toc=True,show_cover=True,show_back_cover=True,flow=False,extra_css=None,watermark=True,watermark_scale=1.0,watermark_opacity=.08):
    pipeline._OPTS['qcols']=False; body=[]
    for i,f in enumerate(files,1): body.append(render_markdown(f.read_text(encoding='utf-8'),f'ch{i:02d}' if len(files)>1 else ''))
    content='\n'.join(body); parts=[]
    if show_cover: parts.append(build_cover(title,subtitle,[author,f'{len(files)} अध्याय-फ़ाइल' if len(files)>1 else '',date.today().strftime('%d %B %Y')],badge))
    if show_toc:
        t=pipeline.build_toc(content)
        if t: parts.append(t)
    parts.append(content)
    if show_back_cover: parts.append(build_back_cover())
    document=f'<!DOCTYPE html><html lang="hi"><head><meta charset="utf-8"><style>{PET_CSS}</style><title>{html.escape(title)}</title></head><body class="pet-document">{"".join(parts)}</body></html>'
    output=Path(output); output.parent.mkdir(parents=True,exist_ok=True); rendered=False
    if getattr(pipeline,'WEASYPRINT_AVAILABLE',False):
        try:
            from weasyprint import HTML,CSS
            from weasyprint.text.fonts import FontConfiguration
            fc=FontConfiguration(); sheets=[CSS(filename=str(pipeline.CSS_FILE),font_config=fc),CSS(string=PET_CSS,font_config=fc)]
            if flow: sheets.append(CSS(string='h1{page-break-before:auto;margin-top:9mm}h1:first-of-type{margin-top:0}',font_config=fc))
            if extra_css: sheets.append(CSS(filename=str(extra_css),font_config=fc))
            HTML(string=document,base_url=str(pipeline.HERE)).write_pdf(str(output),stylesheets=sheets,font_config=fc); rendered=True
        except Exception as e: print(f'! WeasyPrint failed: {e}; using browser fallback')
    if not rendered: pipeline.render_pdf_with_browser(document,output,pipeline.CSS_FILE,extra_css=extra_css,flow=flow)
    if watermark and auto_watermark_pdf: auto_watermark_pdf(output,scale=watermark_scale,opacity=watermark_opacity)
    mb = output.stat().st_size / 1024 / 1024
    try:
        print(f'✔ {output} ({mb:.2f} MB)')
    except UnicodeEncodeError:
        print(f'[OK] {output} ({mb:.2f} MB)')
    return output

def main():
    p=argparse.ArgumentParser(description='PET Markdown notes to styled PDF'); p.add_argument('inputs',nargs='+'); p.add_argument('-o','--output'); p.add_argument('--title'); p.add_argument('--subtitle',default=''); p.add_argument('--author',default=''); p.add_argument('--badge',default='PET 2026'); p.add_argument('--toc',action='store_true'); p.add_argument('--no-toc',action='store_true'); p.add_argument('--no-cover',action='store_true'); p.add_argument('--no-back-cover',action='store_true'); p.add_argument('--flow',action='store_true'); p.add_argument('--css'); p.add_argument('--no-watermark',action='store_true'); p.add_argument('--watermark-scale',type=float,default=1.0); p.add_argument('--watermark-opacity',type=float,default=.08); a=p.parse_args()
    files=pipeline.collect(a.inputs)
    if not files: raise SystemExit('No Markdown files found.')
    title=a.title or files[0].stem.replace('-',' ').replace('_',' '); output=a.output or str(files[0].with_suffix('.pdf'))
    render_pet_pdf(files,output,title,a.subtitle,a.author,a.badge,a.toc or (len(files)>1 and not a.no_toc),not a.no_cover,not a.no_back_cover,a.flow,a.css,not a.no_watermark,a.watermark_scale,a.watermark_opacity)
if __name__=='__main__': main()
