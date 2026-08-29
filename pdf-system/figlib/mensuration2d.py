"""
mensuration2d.py — visual figures for Chapter 38 (2-D Area & Perimeter).

rectangle-measure : rectangle length, breadth, perimeter and area
square-measure    : square side, diagonal, perimeter and area
triangle-measure  : triangle base, height and half-bh area
parallelogram-measure: base-height area model
rhombus-measure   : diagonal half-product area
trapezium-measure : parallel bases and height
circle-measure38  : radius, circumference and area
composite-lshape  : subtract a missing rectangle from an outer rectangle
path-around       : uniform path around a rectangle
sector-measure    : sector angle, arc and area fraction
unit-conversion-area: length and square-unit conversion
cost-fencing      : perimeter/area translated into quantity and cost
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=3800):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def _card(cv, x, y, w, h, col, bg, r=6, sw=1.4):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
           f'fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _fmt(value):
    value = float(value)
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def _dim(cv, x1, y1, x2, y2, label, color=C["purple"]):
    cv.line(x1, y1, x2, y2, color=color, w=1.2, dash="4 3")
    cv.text((x1+x2)/2, (y1+y2)/2 - 6, label, size=9.2, color=color, weight=700)


# ───────────────────────────── rectangle ───────────────────────────────────
def rectangle_measure(spec):
    l = float(spec.get("length", 12)); b = float(spec.get("breadth", 7))
    W, H = 452, 250
    cv = Canvas(W, H, seed=_seed(spec, 3801))
    cv.text(W/2, 20, "rectangle: area fills the region; perimeter walks its boundary",
            size=9.7, weight=700, color=C["soft"])
    scale = min(250/l, 120/b); w_, h_ = l*scale, b*scale
    x, y = 42, 55
    cv.rect(x, y, w_, h_, color=C["blue"], w=1.8, fill=C["blue_bg"])
    _dim(cv, x, y+h_+20, x+w_, y+h_+20, f"l = {_fmt(l)}")
    _dim(cv, x-18, y, x-18, y+h_, f"b = {_fmt(b)}")
    _card(cv, 300, 58, 126, 34, C["green"], C["green_bg"], sw=1.5)
    cv.text(363, 80, f"area = {_fmt(l*b)}", size=9.4, weight=700, color=C["green"])
    _card(cv, 300, 108, 126, 34, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(363, 130, f"perimeter = {_fmt(2*(l+b))}", size=8.8, weight=700, color=C["purple"])
    _card(cv, 300, 158, 126, 34, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(363, 180, f"diagonal = {_fmt(math.hypot(l,b))}", size=8.8, weight=700, color=C["amber"])
    cv.text(W/2, H-8, "area uses square units; perimeter uses length units", size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── square ──────────────────────────────────────
def square_measure(spec):
    a = float(spec.get("side", 8))
    W, H = 452, 242
    cv = Canvas(W, H, seed=_seed(spec, 3802))
    cv.text(W/2, 20, "square: all four sides and all four angles are equal",
            size=9.9, weight=700, color=C["soft"])
    x, y, s = 54, 48, 150
    cv.rect(x, y, s, s, color=C["blue"], w=1.8, fill=C["blue_bg"])
    for p1,p2 in (((x,y),(x+s,y)),((x+s,y),(x+s,y+s)),((x+s,y+s),(x,y+s)),((x,y+s),(x,y))):
        cv.ticks(p1, p2, count=1, color=C["green"])
    cv.line(x, y+s, x+s, y, color=C["red"], w=1.4, dash="4 3")
    cv.text(x+s/2, y+s+20, f"side = {_fmt(a)}", size=10, color=C["purple"], weight=700)
    rows=[("area",a*a,C["green"]),("perimeter",4*a,C["purple"]),("diagonal",a*math.sqrt(2),C["red"])]
    for i,(lab,val,col) in enumerate(rows):
        yy=54+i*40
        _card(cv,300,yy,120,28,col,"#ffffff",r=5,sw=1.2)
        cv.text(312,yy+18,lab,size=8.6,anchor="start",color=C["soft"])
        cv.text(408,yy+18,_fmt(val),size=9.2,anchor="end",weight=700,color=col)
    cv.text(W/2,H-8,"diagonal = side x sqrt(2)",size=8.8,color=C["ink"])
    return cv.svg()


# ───────────────────────────── triangle ────────────────────────────────────
def triangle_measure(spec):
    base=float(spec.get("base",12)); height=float(spec.get("height",8))
    W,H=452,248
    cv=Canvas(W,H,seed=_seed(spec,3803))
    cv.text(W/2,20,"triangle area is half the area of its base-height rectangle",size=9.7,weight=700,color=C["soft"])
    x,y,bw,bh=48,180,240,120
    p=[(x,y),(x+bw,y),(x+bw*.38,y-bh)]
    cv.polygon(p,color=C["blue"],w=1.8,fill=C["blue_bg"])
    cv.line(p[2][0],p[2][1],p[2][0],y,color=C["red"],w=1.2,dash="4 3")
    cv.right_angle(p[2][0],y,(p[2][0]+18,y),p[2],size=10,color=C["red"])
    cv.text(x+bw/2,y+20,f"base = {_fmt(base)}",size=9.7,color=C["purple"],weight=700)
    cv.text(p[2][0]-8,(p[2][1]+y)/2,f"h={_fmt(height)}",size=9.5,color=C["red"],anchor="end",weight=700)
    _card(cv,300,66,124,38,C["green"],C["green_bg"],sw=1.6)
    cv.text(362,90,f"area = 1/2 x b x h",size=8.7,weight=700,color=C["green"])
    _card(cv,300,120,124,38,C["purple"],C["purple_bg"],sw=1.6)
    cv.text(362,144,f"= {_fmt(base*height/2)}",size=11,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"height must be perpendicular to the chosen base",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── parallelogram ───────────────────────────────
def parallelogram_measure(spec):
    b=float(spec.get("base",10)); h=float(spec.get("height",6))
    W,H=452,242
    cv=Canvas(W,H,seed=_seed(spec,3804))
    cv.text(W/2,20,"parallelogram area uses base times perpendicular height",size=9.9,weight=700,color=C["soft"])
    p=[(48,176),(246,176),(284,68),(86,68)]
    cv.polygon(p,color=C["blue"],w=1.8,fill=C["blue_bg"])
    cv.line(86,68,86,176,color=C["red"],w=1.3,dash="4 3")
    cv.right_angle(86,176,(106,176),(86,68),size=10,color=C["red"])
    cv.text(146,194,f"base={_fmt(b)}",size=9.8,color=C["purple"],weight=700)
    cv.text(78,122,f"h={_fmt(h)}",size=9.5,color=C["red"],anchor="end",weight=700)
    _card(cv,300,76,124,34,C["green"],C["green_bg"],sw=1.5)
    cv.text(362,98,f"area={_fmt(b*h)}",size=10,weight=700,color=C["green"])
    cv.text(W/2,H-8,"slanted side is not the height",size=8.8,color=C["ink"])
    return cv.svg()


# ───────────────────────────── rhombus ─────────────────────────────────────
def rhombus_measure(spec):
    d1=float(spec.get("d1",16)); d2=float(spec.get("d2",12))
    W,H=452,246
    cv=Canvas(W,H,seed=_seed(spec,3805))
    cv.text(W/2,20,"rhombus area is half the product of perpendicular diagonals",size=9.6,weight=700,color=C["soft"])
    cx,cy,a,b=132,116,82,62
    p=[(cx,cy-b),(cx+a,cy),(cx,cy+b),(cx-a,cy)]
    cv.polygon(p,color=C["blue"],w=1.8,fill=C["blue_bg"])
    cv.line(cx-a,cy,cx+a,cy,color=C["red"],w=1.3,dash="4 3")
    cv.line(cx,cy-b,cx,cy+b,color=C["red"],w=1.3,dash="4 3")
    cv.right_angle(cx,cy,(cx+18,cy),(cx,cy-18),size=10,color=C["red"])
    cv.text(cx+a/2,cy-8,f"d1={_fmt(d1)}",size=9,color=C["red"],weight=700)
    cv.text(cx+8,cy-b/2,f"d2={_fmt(d2)}",size=9,color=C["red"],weight=700,anchor="start")
    _card(cv,278,76,142,38,C["purple"],C["purple_bg"],sw=1.6)
    cv.text(349,100,"A=1/2 d1 d2",size=9.2,weight=700,color=C["purple"])
    _card(cv,298,132,102,34,C["green"],C["green_bg"],sw=1.5)
    cv.text(349,154,f"={_fmt(d1*d2/2)}",size=10.5,weight=700,color=C["green"])
    cv.text(W/2,H-8,"diagonals are perpendicular in a rhombus",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── trapezium ───────────────────────────────────
def trapezium_measure(spec):
    a=float(spec.get("a",14)); b=float(spec.get("b",8)); h=float(spec.get("height",6))
    W,H=452,248
    cv=Canvas(W,H,seed=_seed(spec,3806))
    cv.text(W/2,20,"trapezium area: average of parallel bases times height",size=9.8,weight=700,color=C["soft"])
    x,y,scale=48,182,12
    lower=a*scale; upper=b*scale; hh=h*scale
    p=[(x,y),(x+lower,y),(x+(lower+upper)/2,y-hh),(x+(lower-upper)/2,y-hh)]
    cv.polygon(p,color=C["blue"],w=1.8,fill=C["blue_bg"])
    cv.line(p[3][0],p[3][1],p[3][0],y,color=C["red"],w=1.2,dash="4 3")
    cv.right_angle(p[3][0],y,(p[3][0]+18,y),p[3],size=10,color=C["red"])
    cv.text(x+lower/2,y+19,f"a={_fmt(a)}",size=9.5,color=C["purple"],weight=700)
    cv.text((p[2][0]+p[3][0])/2,p[2][1]-10,f"b={_fmt(b)}",size=9.5,color=C["purple"],weight=700)
    cv.text(p[3][0]-8,y-hh/2,f"h={_fmt(h)}",size=9.2,color=C["red"],anchor="end",weight=700)
    _card(cv,302,78,112,38,C["green"],C["green_bg"],sw=1.5)
    cv.text(358,101,f"A={_fmt((a+b)*h/2)}",size=10,weight=700,color=C["green"])
    cv.text(W/2,H-8,"A = 1/2 (a+b) h",size=9,color=C["ink"])
    return cv.svg()


# ───────────────────────────── circle ──────────────────────────────────────
def circle_measure38(spec):
    r=float(spec.get("radius",7)); W,H=452,250
    cx,cy,R=100,112,70
    cv=Canvas(W,H,seed=_seed(spec,3807))
    cv.text(W/2,20,"circle area and circumference depend only on radius",size=9.9,weight=700,color=C["soft"])
    cv.circle(cx,cy,R,color=C["blue"],w=1.8,fill=C["blue_bg"])
    cv.line(cx,cy,cx+R,cy,color=C["green"],w=1.4)
    cv.dot(cx,cy,r=2.5)
    cv.text(cx+R/2,cy-8,f"r={_fmt(r)}",size=10,color=C["green"],weight=700)
    rows=[("circumference","2 pi r",2*math.pi*r,C["blue"]),("area","pi r^2",math.pi*r*r,C["green"]),
          ("diameter","2r",2*r,C["purple"])]
    for i,(lab,form,val,col) in enumerate(rows):
        yy=56+i*38
        _card(cv,210,yy,202,30,col,"#ffffff",r=5,sw=1.2)
        cv.text(222,yy+20,lab,size=8.5,anchor="start",color=C["soft"])
        cv.text(330,yy+20,form,size=8.1,anchor="middle",color=col)
        cv.text(400,yy+20,_fmt(val),size=8.8,anchor="end",weight=700,color=col)
    cv.text(W/2,H-8,"use pi=22/7 when radius is a multiple of 7",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── composite L ──────────────────────────────────
def composite_lshape(spec):
    outer_l=float(spec.get("outer_l",12)); outer_b=float(spec.get("outer_b",10)); cut_l=float(spec.get("cut_l",5)); cut_b=float(spec.get("cut_b",4))
    W,H=452,260; x,y=48,50; scale=13
    cv=Canvas(W,H,seed=_seed(spec,3808))
    cv.text(W/2,20,"composite area: outer rectangle minus missing rectangle",size=9.8,weight=700,color=C["soft"])
    ow,oh=outer_l*scale,outer_b*scale
    cv.rect(x,y,ow,oh,color=C["blue"],w=1.7,fill=C["blue_bg"])
    cw,ch=cut_l*scale,cut_b*scale
    cv.raw(f'<rect x="{x+ow-cw:.1f}" y="{y:.1f}" width="{cw:.1f}" height="{ch:.1f}" fill="{C["paper"]}" stroke="{C["red"]}" stroke-width="1.5"/>')
    cv.text(x+ow-cw/2,y+ch/2+4,"cut",size=9,color=C["red"],weight=700)
    _card(cv,250,66,164,36,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(332,89,f"outer={_fmt(outer_l*outer_b)}",size=9.2,weight=700,color=C["purple"])
    _card(cv,250,120,164,36,C["red"],C["red_bg"],sw=1.5)
    cv.text(332,143,f"cut={_fmt(cut_l*cut_b)}",size=9.2,weight=700,color=C["red"])
    _card(cv,250,174,164,36,C["green"],C["green_bg"],sw=1.5)
    cv.text(332,197,f"area={_fmt(outer_l*outer_b-cut_l*cut_b)}",size=9.8,weight=700,color=C["green"])
    cv.text(W/2,H-8,"split complex figures into rectangles and subtract",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── path around rectangle ────────────────────────
def path_around(spec):
    l=float(spec.get("length",20)); b=float(spec.get("breadth",12)); w=float(spec.get("width",2))
    W,H=452,260; x,y=54,48; scale=10
    cv=Canvas(W,H,seed=_seed(spec,3809))
    cv.text(W/2,20,"uniform path around a rectangle: use expanded dimensions",size=9.6,weight=700,color=C["soft"])
    ow,oh=l*scale,b*scale
    cv.rect(x,y,ow,oh,color=C["blue"],w=1.5,fill=C["blue_bg"])
    cv.rect(x-w*scale,y-w*scale,ow+2*w*scale,oh+2*w*scale,color=C["red"],w=1.7,fill=None)
    cv.text(x+ow/2,y+oh/2+4,"original",size=9,color=C["blue"],weight=700)
    _card(cv,284,60,132,34,C["purple"],C["purple_bg"],sw=1.4)
    cv.text(350,82,f"outer L={_fmt(l+2*w)}",size=8.8,weight=700,color=C["purple"])
    _card(cv,284,110,132,34,C["green"],C["green_bg"],sw=1.4)
    cv.text(350,132,f"outer B={_fmt(b+2*w)}",size=8.8,weight=700,color=C["green"])
    added=(l+2*w)*(b+2*w)-l*b
    _card(cv,284,160,132,34,C["red"],C["red_bg"],sw=1.4)
    cv.text(350,182,f"path area={_fmt(added)}",size=8.8,weight=700,color=C["red"])
    cv.text(W/2,H-8,"path width is added on both sides",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── fencing/cost ──────────────────────────────────
def cost_fencing(spec):
    l=float(spec.get("length",20)); b=float(spec.get("breadth",12)); rate=float(spec.get("rate",15)); area_rate=float(spec.get("area_rate",8))
    W,H=452,252; x,y=48,52; scale=10
    cv=Canvas(W,H,seed=_seed(spec,3810))
    cv.text(W/2,20,"perimeter gives fencing cost; area gives flooring or painting cost",size=9.5,weight=700,color=C["soft"])
    cv.rect(x,y,l*scale,b*scale,color=C["blue"],w=1.8,fill=C["blue_bg"])
    cv.text(x+l*scale/2,y+b*scale+18,f"{_fmt(l)} x {_fmt(b)}",size=9.2,color=C["blue"],weight=700)
    per=2*(l+b); ar=l*b
    rows=[("perimeter",per,rate,per*rate,C["purple"]),("area",ar,area_rate,ar*area_rate,C["green"])]
    for i,(lab,qty,r,tot,col) in enumerate(rows):
        yy=58+i*58
        _card(cv,290,yy,128,44,col,"#ffffff",sw=1.3)
        cv.text(354,yy+16,lab,size=8.8,weight=700,color=col)
        cv.text(354,yy+31,f"{_fmt(qty)} x {_fmt(r)} = {_fmt(tot)}",size=8.4,color=col)
    cv.text(W/2,H-8,"read the question: boundary or surface?",size=8.8,color=C["red"],weight=700)
    return cv.svg()


REGISTRY={
    "rectangle-measure":rectangle_measure,
    "square-measure":square_measure,
    "triangle-measure":triangle_measure,
    "parallelogram-measure":parallelogram_measure,
    "rhombus-measure":rhombus_measure,
    "trapezium-measure":trapezium_measure,
    "circle-measure38":circle_measure38,
    "composite-lshape":composite_lshape,
    "path-around":path_around,
    "cost-fencing":cost_fencing,
}
