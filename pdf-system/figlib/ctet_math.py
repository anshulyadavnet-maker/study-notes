"""
ctet_math.py — figures for CTET Paper I Mathematics MCQs.

place-value-ctet : hundreds/tens/ones place-value model
number-line-ctet : number line and comparison
fraction-model   : shaded fraction bar
shape-symmetry   : 2-D shapes and a reflection line
solid-net-ctet   : cube net
measurement-scale: ruler and unit marks
clock-ctet       : analog clock time
math-data-ctet   : simple bar/data display
pattern-ctet     : repeating/growing pattern
money-ctet       : rupee notes/coins model
strategy-ctet    : multiple child strategies
assessment-cycle : formative assessment loop
error-analysis-ctet: child error to diagnosis
remedial-cycle   : diagnostic-remedial-follow-up cycle
community-math   : mathematics in daily/community context
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=5200):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def _card(cv, x, y, w, h, col, bg, r=5, sw=1.3):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _fmt(value):
    value = float(value)
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.2f}".rstrip("0").rstrip(".")


# ───────────────────────────── place value ──────────────────────────────────
def place_value(spec):
    number = int(spec.get("number", 342))
    h, t, o = number // 100, (number // 10) % 10, number % 10
    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 5201))
    cv.text(W / 2, 20, "place value: hundreds, tens and ones", size=10.2, weight=700, color=C["soft"])
    vals = [("hundreds", h, 100, C["blue"], C["blue_bg"]), ("tens", t, 10, C["green"], C["green_bg"]), ("ones", o, 1, C["amber"], C["amber_bg"])]
    for i, (lab, digit, mult, col, bg) in enumerate(vals):
        x = 34 + i * 140
        _card(cv, x, 48, 124, 66, col, bg, sw=1.5)
        cv.text(x + 62, 69, lab, size=8.7, weight=700, color=col)
        cv.text(x + 62, 96, str(digit), size=17, weight=700, color=col)
        cv.text(x + 62, 132, f"{digit} x {mult} = {digit * mult}", size=8.6, color=col)
    _card(cv, 56, 168, 340, 32, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(226, 189, f"{number} = {h*100} + {t*10} + {o}", size=10.3, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "the same digit has a different value in a different place", size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── number line ──────────────────────────────────
def number_line(spec):
    W, H = 452, 190
    cv = Canvas(W, H, seed=_seed(spec, 5202))
    cv.text(W / 2, 20, "number line: numbers grow from left to right", size=10.2, weight=700, color=C["soft"])
    x0, x1, y = 48, 404, 100
    cv.line(x0, y, x1, y, color=C["ink"], w=1.6)
    cv.arrow(x1 - 12, y, x1 + 8, y, color=C["ink"], w=1.3)
    for n in range(0, 11):
        x = x0 + n * (x1 - x0) / 10
        cv.line(x, y - 6, x, y + 6, color=C["ink"], w=1.1)
        cv.text(x, y + 22, str(n), size=9, color=C["soft"])
    for n, lab, col, yy in ((3, "A", C["blue"], y - 28), (7, "B", C["red"], y - 28)):
        x = x0 + n * (x1 - x0) / 10
        cv.dot(x, y, r=4.3, color=col)
        cv.text(x, yy, f"{lab}={n}", size=8.9, weight=700, color=col)
    cv.text(W / 2, H - 8, "B is to the right of A, so 7 > 3", size=9, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── fraction model ───────────────────────────────
def fraction_model(spec):
    num = int(spec.get("num", 3)); den = int(spec.get("den", 4))
    num = max(0, min(num, den)); W, H = 452, 190
    cv = Canvas(W, H, seed=_seed(spec, 5203))
    cv.text(W / 2, 20, "fraction model: numerator shaded out of denominator equal parts", size=9.7, weight=700, color=C["soft"])
    x0, y0, bw, bh = 58, 54, 320, 50
    seg = bw / den
    for i in range(den):
        fill = C["blue_bg"] if i < num else "#ffffff"
        cv.raw(f'<rect x="{x0 + i * seg:.2f}" y="{y0}" width="{seg:.2f}" height="{bh}" fill="{fill}" stroke="{C["blue"]}" stroke-width="1.3"/>')
    _card(cv, 164, 132, 124, 28, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(226, 151, f"fraction = {num}/{den}", size=11, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "denominator counts equal parts; numerator counts selected parts", size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── shapes and symmetry ──────────────────────────
def shape_symmetry(spec):
    W, H = 452, 230
    cv = Canvas(W, H, seed=_seed(spec, 5204))
    cv.text(W / 2, 20, "shape and reflection: both halves match across the mirror line", size=9.8, weight=700, color=C["soft"])
    # square
    cv.rect(44, 68, 94, 94, color=C["blue"], w=1.7, fill=C["blue_bg"])
    cv.line(91, 58, 91, 172, color=C["red"], w=1.5, dash="4 3")
    cv.text(91, 191, "square: 4 lines", size=8.8, color=C["blue"], weight=700)
    # triangle
    tri = [(188, 162), (276, 162), (232, 70)]
    cv.polygon(tri, color=C["green"], w=1.7, fill=C["green_bg"])
    cv.line(232, 70, 232, 162, color=C["red"], w=1.5, dash="4 3")
    cv.text(232, 191, "equilateral: 3 lines", size=8.8, color=C["green"], weight=700)
    # circle
    cv.circle(370, 116, 48, color=C["purple"], w=1.7, fill=C["purple_bg"])
    cv.line(322, 116, 418, 116, color=C["red"], w=1.3, dash="4 3")
    cv.line(370, 68, 370, 164, color=C["red"], w=1.3, dash="4 3")
    cv.text(370, 191, "circle: many lines", size=8.8, color=C["purple"], weight=700)
    return cv.svg()


# ───────────────────────────── cube net ─────────────────────────────────────
def solid_net(spec):
    W, H = 320, 235
    cv = Canvas(W, H, seed=_seed(spec, 5205))
    cv.text(W / 2, 20, "cube net: six square faces fold into a solid", size=10, weight=700, color=C["soft"])
    x0, y0, s = 112, 72, 42
    cells = [(x0, y0), (x0+s, y0), (x0+2*s, y0), (x0+3*s, y0), (x0+s, y0-s), (x0+s, y0+s)]
    for i, (x, y) in enumerate(cells):
        col = [C["blue"], C["green"], C["amber"], C["purple"], C["red"], C["teal"]][i]
        bg = [C["blue_bg"], C["green_bg"], C["amber_bg"], C["purple_bg"], C["red_bg"], C["teal_bg"]][i]
        cv.rect(x, y, s, s, color=col, w=1.4, fill=bg)
        cv.text(x+s/2, y+s/2+4, str(i+1), size=10, weight=700, color=col)
    cv.text(W / 2, 208, "6 faces, 12 edges, 8 vertices", size=9.5, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── ruler ───────────────────────────────────────
def measurement_scale(spec):
    W, H = 452, 210
    cv = Canvas(W, H, seed=_seed(spec, 5206))
    cv.text(W / 2, 20, "measure from zero, not from the edge of the ruler", size=9.8, weight=700, color=C["soft"])
    x0, y, unit = 44, 100, 42
    cv.line(x0, y, x0+8*unit, y, color=C["blue"], w=2)
    for i in range(9):
        x=x0+i*unit;cv.line(x,y-12,x,y+12,color=C["ink"],w=1.1);cv.text(x,y+28,str(i),size=8.5,color=C["soft"])
    cv.line(x0+5*unit,y-24,x0+5*unit,y+7,color=C["red"],w=1.6)
    cv.text(x0+5*unit,y-34,"5 cm",size=9,weight=700,color=C["red"])
    _card(cv, 100, 158, 252, 26, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 176, "1 m = 100 cm; 1 cm = 10 mm", size=9.2, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── clock ────────────────────────────────────────
def clock_ctet(spec):
    hour=int(spec.get("hour",3));minute=int(spec.get("minute",30));W,H=260,220;cx,cy,r=110,105,68
    cv=Canvas(W,H,seed=_seed(spec,5207));cv.text(W/2,20,"read the minute hand first: each number = 5 minutes",size=9.5,weight=700,color=C["soft"])
    cv.circle(cx,cy,r,color=C["blue"],w=1.7,fill=C["blue_bg"])
    for i in range(12):
        a=2*math.pi*i/12-math.pi/2;px,py=cx+(r-10)*math.cos(a),cy+(r-10)*math.sin(a);cv.text(px,py+3,str(i+1),size=8,color=C["soft"])
    ma=2*math.pi*minute/60-math.pi/2;ha=2*math.pi*((hour%12)+minute/60)/12-math.pi/2
    cv.line(cx,cy,cx+(r-16)*math.cos(ma),cy+(r-16)*math.sin(ma),color=C["red"],w=1.6);cv.line(cx,cy,cx+(r-28)*math.cos(ha),cy+(r-28)*math.sin(ha),color=C["green"],w=2.4);cv.dot(cx,cy,r=3,color=C["ink"])
    _card(cv,190,72,54,44,C["purple"],C["purple_bg"],sw=1.4);cv.text(217,93,f"{hour}:{minute:02d}",size=10,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"minute hand at 6 -> 30 minutes",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── bar/data ─────────────────────────────────────
def math_data(spec):
    vals=[4,7,5,9];labels=["Mon","Tue","Wed","Thu"];W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,5208));cv.text(W/2,20,"bar height represents the value in each category",size=9.8,weight=700,color=C["soft"])
    x0,y0,bw,gap,scale=52,194,46,38,12
    for i,(lab,val) in enumerate(zip(labels,vals)):
        x=x0+i*(bw+gap);hh=val*scale;cv.raw(f'<rect x="{x}" y="{y0-hh}" width="{bw}" height="{hh}" fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.3"/>');cv.text(x+bw/2,y0+17,lab,size=8,color=C["soft"]);cv.text(x+bw/2,y0-hh-8,str(val),size=8.5,weight=700,color=C["blue"])
    cv.line(x0,y0,x0+4*(bw+gap)-gap,y0,color=C["ink"],w=1.2);cv.text(W/2,H-8,"compare bars, add values, or find maximum as asked",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── pattern ──────────────────────────────────────
def pattern_ctet(spec):
    vals=[2,4,6,8,10];W,H=452,190;cv=Canvas(W,H,seed=_seed(spec,5209));cv.text(W/2,20,"growing pattern: the same change repeats",size=10,weight=700,color=C["soft"])
    for i,v in enumerate(vals):
        x=54+i*76;cv.circle(x,92,14,color=C["blue"],w=1.2,fill=C["blue_bg"]);cv.text(x,97,str(v),size=8.8,weight=700,color=C["blue"])
        if i<len(vals)-1:cv.arrow(x+18,92,x+56,92,color=C["grey"],w=1.0)
    _card(cv,82,138,288,26,C["purple"],C["purple_bg"],sw=1.4);cv.text(226,156,"add 2 each time -> next = 12",size=9.5,weight=700,color=C["purple"])
    return cv.svg()


# ───────────────────────────── money ────────────────────────────────────────
def money_ctet(spec):
    W,H=452,210;cv=Canvas(W,H,seed=_seed(spec,5210));cv.text(W/2,20,"money: combine notes and coins, then check the total",size=9.8,weight=700,color=C["soft"])
    items=[("₹100",C["blue"],C["blue_bg"]),("₹20",C["green"],C["green_bg"]),("₹5",C["amber"],C["amber_bg"]),("₹2",C["purple"],C["purple_bg"])]
    for i,(lab,col,bg) in enumerate(items):
        x=38+i*100;_card(cv,x,54,76,46,col,bg,sw=1.5);cv.text(x+38,82,lab,size=10,weight=700,color=col);cv.text(x+38,114,"1 each",size=8,color=col)
    _card(cv,98,150,256,28,C["red"],C["red_bg"],sw=1.5);cv.text(226,169,"total = ₹127",size=10,weight=700,color=C["red"])
    return cv.svg()


# ───────────────────────────── child strategies ────────────────────────────
def strategy_ctet(spec):
    W,H=452,256;cv=Canvas(W,H,seed=_seed(spec,5211));cv.text(W/2,20,"different correct strategies show mathematical thinking",size=9.7,weight=700,color=C["soft"])
    rows=[("Riya","split 25+25+25+25",C["blue"],C["blue_bg"]),("Aman","5 x 20",C["green"],C["green_bg"]),("Sara","100 - 4 x 25",C["purple"],C["purple_bg"])]
    for i,(lab,method,col,bg) in enumerate(rows):
        y=52+i*48;_card(cv,38,y,376,34,col,bg,sw=1.4);cv.text(52,y+22,lab,size=8.8,anchor="start",weight=700,color=col);cv.text(402,y+22,method,size=8.7,anchor="end",color=col)
    _card(cv,84,204,284,26,C["amber"],C["amber_bg"],sw=1.4);cv.text(226,222,"all reach 100; compare reasoning",size=9.1,weight=700,color=C["amber"])
    return cv.svg()


# ───────────────────────────── assessment cycle ─────────────────────────────
def assessment_cycle(spec):
    W,H=452,230;cv=Canvas(W,H,seed=_seed(spec,5212));cv.text(W/2,20,"formative assessment creates a teaching feedback loop",size=9.7,weight=700,color=C["soft"])
    nodes=[("teach",C["blue"],C["blue_bg"]),("observe",C["green"],C["green_bg"]),("diagnose",C["amber"],C["amber_bg"]),("adapt",C["purple"],C["purple_bg"])]
    xs=[60,170,280,390];y=96
    for i,(lab,col,bg) in enumerate(nodes):
        _card(cv,xs[i]-42,y-20,84,40,col,bg,sw=1.5);cv.text(xs[i],y+5,lab,size=9,weight=700,color=col)
        if i<len(nodes)-1:cv.arrow(xs[i]+46,y,xs[i+1]-46,y,color=C["grey"],w=1.1)
    cv.arrow(xs[-1],y+26,xs[0],y+26,color=C["red"],w=1.1)
    cv.text(W/2,160,"use evidence to change the next instruction",size=9,color=C["red"],weight=700)
    cv.text(W/2,H-8,"assessment is part of teaching, not only a final score",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── error analysis ───────────────────────────────
def error_analysis_ctet(spec):
    W,H=452,238;cv=Canvas(W,H,seed=_seed(spec,5213));cv.text(W/2,20,"a wrong answer is evidence about the child's current thinking",size=9.5,weight=700,color=C["soft"])
    _card(cv,38,52,126,40,C["red"],C["red_bg"],sw=1.5);cv.text(101,76,"child answer",size=9,weight=700,color=C["red"])
    cv.arrow(168,72,208,72,color=C["grey"],w=1.2)
    _card(cv,216,52,126,40,C["amber"],C["amber_bg"],sw=1.5);cv.text(279,76,"analyse error",size=9,weight=700,color=C["amber"])
    cv.arrow(346,72,386,72,color=C["grey"],w=1.2)
    _card(cv,106,132,240,40,C["green"],C["green_bg"],sw=1.5);cv.text(226,156,"diagnose misconception -> plan support",size=8.9,weight=700,color=C["green"])
    cv.text(W/2,H-8,"do not label the child; investigate the strategy",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── remedial cycle ───────────────────────────────
def remedial_cycle(spec):
    W,H=452,230;cv=Canvas(W,H,seed=_seed(spec,5214));cv.text(W/2,20,"remedial teaching follows diagnosis and ends with re-assessment",size=9.4,weight=700,color=C["soft"])
    nodes=[("diagnose",C["red"],C["red_bg"]),("targeted task",C["blue"],C["blue_bg"]),("guided practice",C["green"],C["green_bg"]),("re-check",C["purple"],C["purple_bg"])]
    xs=[58,170,282,394];y=100
    for i,(lab,col,bg) in enumerate(nodes):
        _card(cv,xs[i]-45,y-21,90,42,col,bg,sw=1.4);cv.text(xs[i],y+5,lab,size=8.3,weight=700,color=col)
        if i<len(nodes)-1:cv.arrow(xs[i]+48,y,xs[i+1]-48,y,color=C["grey"],w=1.1)
    cv.text(W/2,164,"if gap remains, adjust the support and repeat",size=9,color=C["red"],weight=700)
    cv.text(W/2,H-8,"remedial does not mean less learning; it means better-matched support",size=8.4,color=C["ink"])
    return cv.svg()


# ───────────────────────────── community math ───────────────────────────────
def community_math(spec):
    W,H=452,230;cv=Canvas(W,H,seed=_seed(spec,5215));cv.text(W/2,20,"community mathematics connects classroom numbers to daily life",size=9.5,weight=700,color=C["soft"])
    items=[("market","money",C["blue"],C["blue_bg"]),("bus stop","time",C["green"],C["green_bg"]),("kitchen","measure",C["amber"],C["amber_bg"]),("playground","shape",C["purple"],C["purple_bg"])]
    for i,(place,maths,col,bg) in enumerate(items):
        x=34+i*104;_card(cv,x,62,90,60,col,bg,sw=1.4);cv.text(x+45,84,place,size=8.5,weight=700,color=col);cv.text(x+45,105,maths,size=8.5,color=col)
    _card(cv,88,160,276,28,C["red"],C["red_bg"],sw=1.5);cv.text(226,179,"real context -> meaningful mathematics",size=9.2,weight=700,color=C["red"])
    return cv.svg()


REGISTRY={
    "place-value-ctet":place_value,
    "number-line-ctet":number_line,
    "fraction-model":fraction_model,
    "shape-symmetry":shape_symmetry,
    "solid-net-ctet":solid_net,
    "measurement-scale":measurement_scale,
    "clock-ctet":clock_ctet,
    "math-data-ctet":math_data,
    "pattern-ctet":pattern_ctet,
    "money-ctet":money_ctet,
    "strategy-ctet":strategy_ctet,
    "assessment-cycle":assessment_cycle,
    "error-analysis-ctet":error_analysis_ctet,
    "remedial-cycle":remedial_cycle,
    "community-math":community_math,
}
