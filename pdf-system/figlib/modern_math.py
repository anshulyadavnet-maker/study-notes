"""
modern_math.py — visual figures for Chapter 46.

di-table          : table-based data interpretation
di-bars           : comparative bar chart for DI
di-line           : line trend for DI
 di-pie           : pie-chart percentages and angles
caselet-flow      : convert a caselet into counts step by step
sufficiency-flow  : statement sufficiency decision flow
counting-tree     : fundamental counting principle tree
arrangement       : permutation/combination distinction
probability-tree  : sequential probability branches
probability-box   : sample space, favourable outcomes and complement
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=4600):
    value=spec.get("seed",default)
    try:return int(value)
    except Exception:return sum(ord(ch) for ch in str(value))


def _card(cv,x,y,w,h,col,bg,r=5,sw=1.3):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _fmt(v):
    v=float(v)
    if abs(v-round(v))<1e-9:return str(int(round(v)))
    return f"{v:.2f}".rstrip("0").rstrip(".")


# ───────────────────────────── DI table ─────────────────────────────────────
def di_table(spec):
    years=["21","22","23","24"];a=[120,150,180,200];b=[100,140,160,220]
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4601))
    cv.text(W/2,20,"read the table first; calculate only what the question asks",size=9.8,weight=700,color=C["soft"])
    x0,y0,cw=42,52,78
    headers=["year"]+years
    for j,v in enumerate(headers):
        _card(cv,x0+j*cw,y0,cw-4,28,C["blue"],C["blue_bg"],r=4,sw=1.1);cv.text(x0+j*cw+(cw-4)/2,y0+19,v,size=8.8,weight=700,color=C["blue"])
    for i,(lab,vals,col,bg) in enumerate((("A",a,C["green"],C["green_bg"]),("B",b,C["purple"],C["purple_bg"]))):
        y=y0+(i+1)*36;allv=[lab]+[str(v) for v in vals]
        for j,v in enumerate(allv):
            _card(cv,x0+j*cw,y,cw-4,28,col,bg if j==0 else "#ffffff",r=4,sw=1.1);cv.text(x0+j*cw+(cw-4)/2,y+19,v,size=8.8,weight=700 if j==0 else 400,color=col)
    _card(cv,48,174,356,32,C["amber"],C["amber_bg"],sw=1.5);cv.text(226,195,"A total=650; B total=620; compare, ratio, average",size=9.1,weight=700,color=C["amber"])
    cv.text(W/2,H-8,"label rows and columns before doing arithmetic",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── DI bars ──────────────────────────────────────
def di_bars(spec):
    cats=["A","B","C","D"];v1=[12,18,15,22];v2=[10,14,20,16]
    W,H=452,260;cv=Canvas(W,H,seed=_seed(spec,4602));cv.text(W/2,20,"grouped bars make category comparisons visual",size=9.9,weight=700,color=C["soft"])
    x0,y0,bw,gap,scale=42,205,24,28,6
    for i,cat in enumerate(cats):
        x=x0+i*(2*bw+gap+16)
        for j,(val,col,bg) in enumerate(((v1[i],C["blue"],C["blue_bg"]),(v2[i],C["green"],C["green_bg"]))):
            xx=x+j*(bw+4);hh=val*scale;cv.raw(f'<rect x="{xx}" y="{y0-hh}" width="{bw}" height="{hh}" fill="{bg}" stroke="{col}" stroke-width="1.1"/>');cv.text(xx+bw/2,y0-hh-7,str(val),size=7.5,weight=700,color=col)
        cv.text(x+bw+2,y0+17,cat,size=8.5,weight=700,color=C["soft"])
    cv.line(x0,y0,x0+4*(2*bw+gap+16)-gap-16,y0,color=C["ink"],w=1.2)
    cv.text(80,50,"series A",size=8.5,color=C["blue"],weight=700);cv.text(160,50,"series B",size=8.5,color=C["green"],weight=700)
    cv.text(W/2,H-8,"compare absolute difference or percentage difference as asked",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── DI line ──────────────────────────────────────
def di_line(spec):
    vals=[20,35,30,50,45];W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4603));cv.text(W/2,20,"line graph shows change and trend over ordered periods",size=9.8,weight=700,color=C["soft"])
    x0,y0,sx,sy=50,200,78,3
    pts=[]
    for i,v in enumerate(vals):
        p=(x0+i*sx,y0-v*sy);pts.append(p);cv.dot(*p,r=4,color=C["red"]);cv.text(p[0],p[1]-9,str(v),size=8,color=C["red"],weight=700);cv.text(p[0],y0+17,str(i+1),size=8,color=C["soft"])
    for p,q in zip(pts,pts[1:]):cv.line(*p,*q,color=C["blue"],w=1.8)
    cv.line(x0,y0,x0+4*sx,y0,color=C["ink"],w=1.1);cv.line(x0,y0-170,x0,y0,color=C["ink"],w=1.1)
    _card(cv,60,48,330,28,C["purple"],C["purple_bg"],sw=1.4);cv.text(225,67,"read increase, decrease, maximum and average",size=9,weight=700,color=C["purple"])
    return cv.svg()


# ───────────────────────────── pie DI ──────────────────────────────────────
def di_pie(spec):
    vals=[40,30,20,10];labels=["A","B","C","D"];cols=[C["blue"],C["green"],C["amber"],C["red"]];cx,cy,r=120,116,76;W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4604));cv.text(W/2,20,"pie sectors convert proportion into angle",size=9.8,weight=700,color=C["soft"])
    start=-math.pi/2;total=sum(vals)
    for v,lab,col in zip(vals,labels,cols):
        end=start+2*math.pi*v/total;steps=8;arc=[(cx+r*math.cos(start+(end-start)*i/steps),cy+r*math.sin(start+(end-start)*i/steps)) for i in range(steps+1)];d=f"M{cx},{cy} L"+" L".join(f"{x:.1f},{y:.1f}" for x,y in arc)+" Z";cv.raw(f'<path d="{d}" fill="{col}" opacity="0.75" stroke="#ffffff" stroke-width="1.2"/>');mid=(start+end)/2;cv.text(cx+48*math.cos(mid),cy+48*math.sin(mid),lab,size=9,weight=700,color=C["ink"]);start=end
    for i,(lab,v,col) in enumerate(zip(labels,vals,cols)):
        y=54+i*34;_card(cv,270,y,140,26,col,"#ffffff",r=5,sw=1.1);cv.text(340,y+17,f"{lab}: {v}% = {v*3.6:.0f} deg",size=8.4,weight=700,color=col)
    cv.text(W/2,H-8,"one percent corresponds to 3.6 degrees",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── caselet flow ─────────────────────────────────
def caselet_flow(spec):
    W,H=452,270;cv=Canvas(W,H,seed=_seed(spec,4605));cv.text(W/2,20,"caselet: translate words into counts before answering",size=9.8,weight=700,color=C["soft"])
    boxes=[("total students","720",C["blue"],C["blue_bg"]),("boys:girls","5:4",C["green"],C["green_bg"]),("boys / girls","400 / 320",C["purple"],C["purple_bg"]),("playing","240 + 160 = 400",C["amber"],C["amber_bg"])]
    for i,(lab,val,col,bg) in enumerate(boxes):
        y=48+i*44;_card(cv,42,y,368,30,col,bg,r=5,sw=1.3);cv.text(56,y+19,lab,size=8.8,anchor="start",weight=700,color=col);cv.text(396,y+19,val,size=8.8,anchor="end",color=col)
        if i<3:cv.arrow(226,y+32,226,y+40,color=C["grey"],w=1.0)
    cv.text(W/2,H-8,"each sentence produces one usable number or ratio",size=8.8,color=C["ink"])
    return cv.svg()


# ───────────────────────────── sufficiency flow ─────────────────────────────
def sufficiency_flow(spec):
    W,H=452,260;cv=Canvas(W,H,seed=_seed(spec,4606));cv.text(W/2,20,"data sufficiency asks whether information is enough",size=9.8,weight=700,color=C["soft"])
    _card(cv,44,50,364,34,C["blue"],C["blue_bg"],sw=1.5);cv.text(226,72,"Question: what is x?",size=11,weight=700,color=C["blue"])
    _card(cv,48,104,158,42,C["green"],C["green_bg"],sw=1.5);cv.text(127,124,"Statement I",size=9.5,weight=700,color=C["green"]);cv.text(127,140,"x+y=10",size=9,color=C["green"])
    _card(cv,246,104,158,42,C["purple"],C["purple_bg"],sw=1.5);cv.text(325,124,"Statement II",size=9.5,weight=700,color=C["purple"]);cv.text(325,140,"x-y=4",size=9,color=C["purple"])
    cv.arrow(206,125,242,125,color=C["grey"],w=1.2)
    _card(cv,88,184,276,34,C["amber"],C["amber_bg"],sw=1.6);cv.text(226,206,"both together -> x=7: sufficient",size=9.2,weight=700,color=C["amber"])
    cv.text(W/2,H-8,"do not solve more than the question requires",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── counting tree ────────────────────────────────
def counting_tree(spec):
    W,H=452,260;cv=Canvas(W,H,seed=_seed(spec,4607));cv.text(W/2,20,"fundamental counting principle multiplies independent choices",size=9.5,weight=700,color=C["soft"])
    cv.text(54,56,"shirt",size=9,weight=700,color=C["blue"]);cv.text(54,112,"trouser",size=9,weight=700,color=C["green"]);cv.text(54,168,"outfits",size=9,weight=700,color=C["purple"])
    for i in range(3):
        x=110+i*38;cv.dot(x,62,r=3,color=C["blue"]);cv.line(x,66,x,102,color=C["grey"],w=1.0)
        for j in range(2):
            xx=x-8+j*16;cv.dot(xx,120,r=3,color=C["green"]);cv.line(xx,124,xx,158,color=C["grey"],w=1.0)
            for k in range(2):cv.dot(xx-5+k*10,178,r=2.5,color=C["purple"])
    _card(cv,252,70,156,40,C["amber"],C["amber_bg"],sw=1.5);cv.text(330,94,"3 x 2 = 6 outfits",size=10,weight=700,color=C["amber"])
    cv.text(W/2,H-8,"choices at each stage multiply",size=8.8,color=C["ink"])
    return cv.svg()


# ───────────────────────────── arrangement ──────────────────────────────────
def arrangement(spec):
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4608));cv.text(W/2,20,"permutation arranges; combination selects",size=10,weight=700,color=C["soft"])
    _card(cv,42,52,170,74,C["blue"],C["blue_bg"],sw=1.5);cv.text(127,74,"arrange 3 of 5",size=10,weight=700,color=C["blue"]);cv.text(127,96,"order matters",size=9,color=C["blue"]);cv.text(127,115,"5P3 = 5x4x3",size=9.5,weight=700,color=C["blue"])
    _card(cv,240,52,170,74,C["green"],C["green_bg"],sw=1.5);cv.text(325,74,"select 3 of 5",size=10,weight=700,color=C["green"]);cv.text(325,96,"order ignored",size=9,color=C["green"]);cv.text(325,115,"5C3 = 10",size=9.5,weight=700,color=C["green"])
    _card(cv,80,164,292,32,C["purple"],C["purple_bg"],sw=1.5);cv.text(226,185,"nPr = nCr x r!",size=10,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"same people, different question: order or selection?",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── probability tree ─────────────────────────────
def probability_tree(spec):
    W,H=452,270;cv=Canvas(W,H,seed=_seed(spec,4609));cv.text(W/2,20,"sequential probability: multiply along a branch, add branches",size=9.5,weight=700,color=C["soft"])
    cv.text(42,64,"start",size=8.5,weight=700,color=C["blue"]);cv.dot(70,66,r=3,color=C["blue"])
    cv.line(73,66,170,48,color=C["grey"],w=1.1);cv.line(73,66,170,92,color=C["grey"],w=1.1)
    cv.text(112,52,"red 5/8",size=8.5,color=C["red"]);cv.text(112,88,"blue 3/8",size=8.5,color=C["blue"])
    cv.dot(174,48,r=3,color=C["red"]);cv.dot(174,92,r=3,color=C["blue"])
    cv.line(177,48,286,32,color=C["grey"],w=1.0);cv.line(177,48,286,64,color=C["grey"],w=1.0);cv.line(177,92,286,78,color=C["grey"],w=1.0);cv.line(177,92,286,108,color=C["grey"],w=1.0)
    cv.text(224,34,"red 4/7",size=8,color=C["red"]);cv.text(224,62,"blue 3/7",size=8,color=C["blue"]);cv.text(224,80,"red 5/7",size=8,color=C["red"]);cv.text(224,106,"blue 2/7",size=8,color=C["blue"])
    _card(cv,306,42,110,50,C["purple"],C["purple_bg"],sw=1.5);cv.text(361,63,"P(2 red)",size=9,weight=700,color=C["purple"]);cv.text(361,82,"=5/8 x 4/7",size=8.6,color=C["purple"])
    cv.text(W/2,H-8,"without replacement: denominator changes after each draw",size=8.5,color=C["ink"])
    return cv.svg()


# ───────────────────────────── probability box ──────────────────────────────
def probability_box(spec):
    W,H=452,248;cv=Canvas(W,H,seed=_seed(spec,4610));cv.text(W/2,20,"probability = favourable outcomes / total outcomes",size=9.9,weight=700,color=C["soft"])
    _card(cv,42,54,164,68,C["blue"],C["blue_bg"],sw=1.5);cv.text(124,76,"sample space S",size=10,weight=700,color=C["blue"]);cv.text(124,99,"total outcomes = 8",size=9,color=C["blue"])
    _card(cv,246,54,164,68,C["green"],C["green_bg"],sw=1.5);cv.text(328,76,"event E",size=10,weight=700,color=C["green"]);cv.text(328,99,"favourable = 3",size=9,color=C["green"])
    _card(cv,74,152,304,36,C["purple"],C["purple_bg"],sw=1.6);cv.text(226,175,"P(E)=3/8; P(not E)=1−3/8=5/8",size=9.3,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"probability lies from 0 to 1",size=8.8,color=C["ink"])
    return cv.svg()


REGISTRY={
    "di-table":di_table,
    "di-bars":di_bars,
    "di-line":di_line,
    "di-pie":di_pie,
    "caselet-flow":caselet_flow,
    "sufficiency-flow":sufficiency_flow,
    "counting-tree":counting_tree,
    "arrangement":arrangement,
    "probability-tree":probability_tree,
    "probability-box":probability_box,
}
