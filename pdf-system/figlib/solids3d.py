"""
solids3d.py — visual figures for Chapter 39 (3-D Solids).

cube3d             : cube edges, diagonal, surface and volume
cuboid3d           : cuboid length, breadth, height and diagonal
cylinder3d         : cylinder radius, height, CSA and volume
cone3d             : cone radius, height, slant height and volume
sphere3d           : sphere radius, diameter, surface and volume
hemisphere3d       : hemisphere curved/total surface and volume
solid-comparison   : same volume / dimension comparison
melt-recast        : volume conservation in melting and recasting
capacity-container : hollow cylinder/cone capacity in litres
composite-solid    : combined cuboid and cylinder volume
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=3900):
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


def _ellipse(cv, cx, cy, rx, ry, col, fill=None):
    cv.ellipse(cx, cy, rx, ry, color=col, w=1.6, fill=fill)


# ───────────────────────────── cube ────────────────────────────────────────
def cube3d(spec):
    a=float(spec.get("side",6)); W,H=452,266
    cv=Canvas(W,H,seed=_seed(spec,3901))
    cv.text(W/2,20,"cube: six equal square faces",size=10.2,weight=700,color=C["soft"])
    ox,oy,s,d=62,62,132,42
    front=[(ox,oy+d),(ox+s,oy+d),(ox+s,oy+d+s),(ox,oy+d+s)]
    top=[(ox,oy+d),(ox+d,oy),(ox+s+d,oy),(ox+s,oy+d)]
    side=[(ox+s,oy+d),(ox+s+d,oy),(ox+s+d,oy+s),(ox+s,oy+d+s)]
    cv.polygon(front,color=C["blue"],w=1.7,fill=C["blue_bg"])
    cv.polygon(top,color=C["green"],w=1.5,fill=C["green_bg"])
    cv.polygon(side,color=C["amber"],w=1.5,fill=C["amber_bg"])
    cv.line(ox,oy+d+s,ox+s+d,oy+s,color=C["red"],w=1.2,dash="4 3")
    cv.text(ox+s/2,oy+d+s+20,f"a={_fmt(a)}",size=9.5,color=C["purple"],weight=700)
    _card(cv,272,62,144,34,C["green"],C["green_bg"],sw=1.5)
    cv.text(344,84,f"V=a^3={_fmt(a**3)}",size=9.5,weight=700,color=C["green"])
    _card(cv,272,112,144,34,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(344,134,f"TSA=6a^2={_fmt(6*a*a)}",size=8.8,weight=700,color=C["purple"])
    _card(cv,272,162,144,34,C["red"],C["red_bg"],sw=1.5)
    cv.text(344,184,f"diag=a sqrt3",size=9,weight=700,color=C["red"])
    cv.text(W/2,H-8,"LSA=4a^2; TSA=6a^2",size=8.8,color=C["ink"])
    return cv.svg()


# ───────────────────────────── cuboid ──────────────────────────────────────
def cuboid3d(spec):
    l=float(spec.get("length",8)); b=float(spec.get("breadth",5)); h=float(spec.get("height",4))
    W,H=452,270; ox,oy=44,70; sx,sy=20,34
    cv=Canvas(W,H,seed=_seed(spec,3902))
    cv.text(W/2,20,"cuboid: three dimensions control volume and surface area",size=9.9,weight=700,color=C["soft"])
    w_,hh,dd=180,100,45
    front=[(ox,oy+dd),(ox+w_,oy+dd),(ox+w_,oy+dd+hh),(ox,oy+dd+hh)]
    top=[(ox,oy+dd),(ox+dd,oy),(ox+w_+dd,oy),(ox+w_,oy+dd)]
    side=[(ox+w_,oy+dd),(ox+w_+dd,oy),(ox+w_+dd,oy+hh),(ox+w_,oy+dd+hh)]
    cv.polygon(front,color=C["blue"],w=1.7,fill=C["blue_bg"])
    cv.polygon(top,color=C["green"],w=1.5,fill=C["green_bg"])
    cv.polygon(side,color=C["amber"],w=1.5,fill=C["amber_bg"])
    cv.text(ox+w_/2,oy+dd+hh+20,f"l={_fmt(l)}",size=9.2,color=C["purple"],weight=700)
    cv.text(ox-12,oy+dd+hh/2,f"h={_fmt(h)}",size=9.2,color=C["purple"],anchor="end",weight=700)
    cv.text(ox+dd+w_+12,oy+17,f"b={_fmt(b)}",size=9.2,color=C["purple"],anchor="start",weight=700)
    rows=[("volume",l*b*h,C["green"]),("TSA",2*(l*b+b*h+h*l),C["purple"]),("diagonal",math.sqrt(l*l+b*b+h*h),C["red"])]
    for i,(lab,val,col) in enumerate(rows):
        yy=58+i*42
        _card(cv,296,yy,126,30,col,"#ffffff",r=5,sw=1.2)
        cv.text(308,yy+20,lab,size=8.5,anchor="start",color=C["soft"])
        cv.text(410,yy+20,_fmt(val),size=9,anchor="end",weight=700,color=col)
    cv.text(W/2,H-8,"V=lbh; TSA=2(lb+bh+hl); LSA=2h(l+b)",size=8.5,color=C["ink"])
    return cv.svg()


# ───────────────────────────── cylinder ────────────────────────────────────
def cylinder3d(spec):
    r=float(spec.get("radius",4)); h=float(spec.get("height",10))
    W,H=452,270; cx,top,rx,ry=128,54,72,18
    cv=Canvas(W,H,seed=_seed(spec,3903))
    cv.text(W/2,20,"cylinder: two circular bases and one curved surface",size=10,weight=700,color=C["soft"])
    bot=top+h*9
    cv.raw(f'<rect x="{cx-rx}" y="{top}" width="{2*rx}" height="{bot-top}" fill="{C["blue_bg"]}" stroke="none"/>')
    _ellipse(cv,cx,top,rx,ry,C["blue"],C["paper"])
    cv.line(cx-rx,top,cx-rx,bot,color=C["blue"],w=1.7)
    cv.line(cx+rx,top,cx+rx,bot,color=C["blue"],w=1.7)
    cv.arc(cx, bot, rx, 0, math.pi, color=C["blue"], w=1.7)
    cv.line(cx,top,cx+rx,top,color=C["green"],w=1.3)
    cv.line(cx,top,cx,bot,color=C["red"],w=1.2,dash="4 3")
    cv.text(cx+rx/2,top-8,f"r={_fmt(r)}",size=9.5,color=C["green"],weight=700)
    cv.text(cx+8,(top+bot)/2,f"h={_fmt(h)}",size=9.5,color=C["red"],weight=700)
    rows=[("volume",math.pi*r*r*h,C["green"]),("CSA",2*math.pi*r*h,C["blue"]),("TSA",2*math.pi*r*(h+r),C["purple"])]
    for i,(lab,val,col) in enumerate(rows):
        yy=54+i*42
        _card(cv,286,yy,136,30,col,"#ffffff",r=5,sw=1.2)
        cv.text(298,yy+20,lab,size=8.6,anchor="start",color=C["soft"])
        cv.text(410,yy+20,_fmt(val),size=8.8,anchor="end",weight=700,color=col)
    cv.text(W/2,H-8,"CSA=2πrh; TSA=2πr(h+r)",size=8.8,color=C["ink"])
    return cv.svg()


# ───────────────────────────── cone ─────────────────────────────────────────
def cone3d(spec):
    r=float(spec.get("radius",5)); h=float(spec.get("height",12)); sl=math.sqrt(r*r+h*h)
    W,H=452,278; cx,apex,rx,ry=130,52,78,20; bot=apex+h*8
    cv=Canvas(W,H,seed=_seed(spec,3904))
    cv.text(W/2,20,"cone: radius, perpendicular height and slant height",size=9.8,weight=700,color=C["soft"])
    cv.raw(f'<path d="M{cx},{apex} L{cx-rx},{bot} A{rx},{ry} 0 0 0 {cx+rx},{bot} Z" fill="{C["blue_bg"]}" stroke="none"/>')
    cv.line(cx,apex,cx-rx,bot,color=C["blue"],w=1.8)
    cv.line(cx,apex,cx+rx,bot,color=C["blue"],w=1.8)
    cv.ellipse(cx,bot,rx,ry,color=C["blue"],w=1.7)
    cv.line(cx,apex,cx,bot,color=C["red"],w=1.2,dash="4 3")
    cv.line(cx,bot,cx+rx,bot,color=C["green"],w=1.3)
    cv.right_angle(cx,bot,(cx+18,bot),(cx,apex),size=10,color=C["red"])
    cv.text(cx-8,(apex+bot)/2,f"h={_fmt(h)}",size=9.5,color=C["red"],anchor="end",weight=700)
    cv.text(cx+rx/2,bot+25,f"r={_fmt(r)}",size=9.5,color=C["green"],weight=700)
    cv.text(cx+38,(apex+bot)/2-14,f"l={_fmt(sl)}",size=9.5,color=C["purple"],weight=700)
    rows=[("volume",math.pi*r*r*h/3,C["green"]),("CSA",math.pi*r*sl,C["blue"]),("TSA",math.pi*r*(sl+r),C["purple"])]
    for i,(lab,val,col) in enumerate(rows):
        yy=54+i*42
        _card(cv,286,yy,136,30,col,"#ffffff",r=5,sw=1.2)
        cv.text(298,yy+20,lab,size=8.6,anchor="start",color=C["soft"])
        cv.text(410,yy+20,_fmt(val),size=8.8,anchor="end",weight=700,color=col)
    cv.text(W/2,H-8,"l²=r²+h²; V=1/3πr²h",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── sphere ──────────────────────────────────────
def sphere3d(spec):
    r=float(spec.get("radius",6)); W,H=452,240; cx,cy,R=112,108,70
    cv=Canvas(W,H,seed=_seed(spec,3905))
    cv.text(W/2,20,"sphere: every point on the surface is r from the centre",size=9.8,weight=700,color=C["soft"])
    cv.circle(cx,cy,R,color=C["blue"],w=1.8,fill=C["blue_bg"])
    cv.ellipse(cx,cy,R,20,color=C["grey"],w=1.1)
    cv.line(cx,cy,cx+R,cy,color=C["green"],w=1.4)
    cv.dot(cx,cy,r=2.5)
    cv.text(cx+R/2,cy-8,f"r={_fmt(r)}",size=10,color=C["green"],weight=700)
    rows=[("surface area",4*math.pi*r*r,C["purple"]),("volume",4*math.pi*r**3/3,C["green"]),("diameter",2*r,C["red"])]
    for i,(lab,val,col) in enumerate(rows):
        yy=58+i*40
        _card(cv,276,yy,144,30,col,"#ffffff",r=5,sw=1.2)
        cv.text(288,yy+20,lab,size=8.5,anchor="start",color=C["soft"])
        cv.text(408,yy+20,_fmt(val),size=9,anchor="end",weight=700,color=col)
    cv.text(W/2,H-8,"surface area=4πr²; volume=4/3πr³",size=8.8,color=C["ink"])
    return cv.svg()


# ───────────────────────────── hemisphere ──────────────────────────────────
def hemisphere3d(spec):
    r=float(spec.get("radius",6)); W,H=452,250; cx,cy,R=112,130,70
    cv=Canvas(W,H,seed=_seed(spec,3906))
    cv.text(W/2,20,"hemisphere: curved surface plus a circular base",size=9.8,weight=700,color=C["soft"])
    cv.raw(f'<path d="M{cx-R},{cy} A{R},{R} 0 0 1 {cx+R},{cy} Z" fill="{C["blue_bg"]}" stroke="none"/>')
    cv.arc(cx,cy,R,0,180,color=C["blue"],w=1.8)
    cv.ellipse(cx,cy,R,17,color=C["blue"],w=1.6)
    cv.line(cx,cy,cx+R,cy,color=C["green"],w=1.3)
    cv.text(cx+R/2,cy-8,f"r={_fmt(r)}",size=10,color=C["green"],weight=700)
    rows=[("volume",2*math.pi*r**3/3,C["green"]),("CSA",2*math.pi*r*r,C["blue"]),("TSA",3*math.pi*r*r,C["purple"])]
    for i,(lab,val,col) in enumerate(rows):
        yy=54+i*40
        _card(cv,276,yy,144,30,col,"#ffffff",r=5,sw=1.2)
        cv.text(288,yy+20,lab,size=8.5,anchor="start",color=C["soft"])
        cv.text(408,yy+20,_fmt(val),size=9,anchor="end",weight=700,color=col)
    cv.text(W/2,H-8,"CSA excludes base; TSA includes one circular base",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── comparison ───────────────────────────────────
def solid_comparison(spec):
    W,H=452,260
    cv=Canvas(W,H,seed=_seed(spec,3907))
    cv.text(W/2,20,"same volume can have very different surface areas",size=10,weight=700,color=C["soft"])
    _card(cv,42,52,168,84,C["blue"],C["blue_bg"],sw=1.6)
    cv.text(126,74,"cube",size=11,weight=700,color=C["blue"])
    cv.text(126,98,"side = 6",size=9,color=C["blue"])
    cv.text(126,120,"V = 216",size=9.5,weight=700,color=C["blue"])
    _card(cv,242,52,168,84,C["green"],C["green_bg"],sw=1.6)
    cv.text(326,74,"cuboid",size=11,weight=700,color=C["green"])
    cv.text(326,98,"3 x 6 x 12",size=9,color=C["green"])
    cv.text(326,120,"V = 216",size=9.5,weight=700,color=C["green"])
    _card(cv,70,164,312,34,C["purple"],C["purple_bg"],sw=1.6)
    cv.text(226,186,"volume equal; TSA depends on shape",size=9.5,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"choose the formula from the solid, not only from volume",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── melt/recast ──────────────────────────────────
def melt_recast(spec):
    r=float(spec.get("radius",3)); h=float(spec.get("height",8)); side=float(spec.get("side",2))
    volume=math.pi*r*r*h; cubes=volume/(side**3)
    W,H=452,248
    cv=Canvas(W,H,seed=_seed(spec,3908))
    cv.text(W/2,20,"melting and recasting preserves volume",size=10.1,weight=700,color=C["soft"])
    _card(cv,36,52,172,76,C["blue"],C["blue_bg"],sw=1.6)
    cv.text(122,72,"cylinder",size=10,weight=700,color=C["blue"])
    cv.text(122,94,f"r={_fmt(r)}, h={_fmt(h)}",size=8.8,color=C["blue"])
    cv.text(122,115,f"V=pi r²h={_fmt(volume)}",size=8.7,weight=700,color=C["blue"])
    cv.arrow(210,90,242,90,color=C["grey"],w=1.3)
    _card(cv,244,52,172,76,C["green"],C["green_bg"],sw=1.6)
    cv.text(330,72,"cubes",size=10,weight=700,color=C["green"])
    cv.text(330,94,f"side={_fmt(side)}",size=8.8,color=C["green"])
    cv.text(330,115,f"number={_fmt(cubes)}",size=8.7,weight=700,color=C["green"])
    _card(cv,70,160,312,34,C["purple"],C["purple_bg"],sw=1.6)
    cv.text(226,182,"old volume = new total volume",size=9.8,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"ignore thickness or wastage unless the question gives it",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── capacity container ───────────────────────────
def capacity_container(spec):
    r=float(spec.get("radius",5)); h=float(spec.get("height",12)); vol=math.pi*r*r*h
    W,H=452,250; cx,top,rx,ry=112,54,72,18; bot=top+h*7
    cv=Canvas(W,H,seed=_seed(spec,3909))
    cv.text(W/2,20,"capacity is the inside volume of a container",size=10,weight=700,color=C["soft"])
    cv.raw(f'<rect x="{cx-rx}" y="{top}" width="{2*rx}" height="{bot-top}" fill="{C["blue_bg"]}" stroke="none"/>')
    cv.ellipse(cx,top,rx,ry,color=C["blue"],w=1.7,fill=C["paper"])
    cv.line(cx-rx,top,cx-rx,bot,color=C["blue"],w=1.7);cv.line(cx+rx,top,cx+rx,bot,color=C["blue"],w=1.7)
    cv.arc(cx, bot, rx, 0, math.pi, color=C["blue"], w=1.7)
    cv.line(cx,top,cx+rx,top,color=C["green"],w=1.3);cv.line(cx,top,cx,bot,color=C["red"],w=1.2,dash="4 3")
    cv.text(cx+rx/2,top-8,f"r={_fmt(r)}",size=9.5,color=C["green"],weight=700)
    cv.text(cx+8,(top+bot)/2,f"h={_fmt(h)}",size=9.5,color=C["red"],weight=700)
    _card(cv,276,64,142,38,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(347,88,f"V={_fmt(vol)} cm^3",size=9.2,weight=700,color=C["purple"])
    _card(cv,276,122,142,38,C["green"],C["green_bg"],sw=1.5)
    cv.text(347,146,f"= {_fmt(vol/1000)} litres",size=9.1,weight=700,color=C["green"])
    cv.text(W/2,H-8,"1000 cm³ = 1 litre",size=8.8,color=C["ink"])
    return cv.svg()


# ───────────────────────────── composite solid ──────────────────────────────
def composite_solid(spec):
    W,H=452,270
    cv=Canvas(W,H,seed=_seed(spec,3910))
    cv.text(W/2,20,"composite solid: add or subtract component volumes",size=9.8,weight=700,color=C["soft"])
    # cuboid base + cylinder on top
    x,y,w_,hh=52,116,184,80
    cv.rect(x,y,w_,hh,color=C["blue"],w=1.7,fill=C["blue_bg"])
    cx,top,rx,ry=144,56,54,14
    cv.raw(f'<rect x="{cx-rx}" y="{top}" width="{2*rx}" height="{y-top+2}" fill="{C["green_bg"]}" stroke="none"/>')
    cv.ellipse(cx,top,rx,ry,color=C["green"],w=1.6,fill=C["green_bg"])
    cv.line(cx-rx,top,cx-rx,y,color=C["green"],w=1.5);cv.line(cx+rx,top,cx+rx,y,color=C["green"],w=1.5)
    cv.text(144,216,"cuboid + cylinder",size=9.5,color=C["purple"],weight=700)
    _card(cv,278,62,140,36,C["blue"],C["blue_bg"],sw=1.5)
    cv.text(348,85,"V1 = lbh",size=10,weight=700,color=C["blue"])
    _card(cv,278,116,140,36,C["green"],C["green_bg"],sw=1.5)
    cv.text(348,139,"V2 = pi r²h",size=9.4,weight=700,color=C["green"])
    _card(cv,278,170,140,36,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(348,193,"total = V1+V2",size=9.4,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"split the solid at the natural boundary",size=8.7,color=C["ink"])
    return cv.svg()


REGISTRY={
    "cube3d":cube3d,
    "cuboid3d":cuboid3d,
    "cylinder3d":cylinder3d,
    "cone3d":cone3d,
    "sphere3d":sphere3d,
    "hemisphere3d":hemisphere3d,
    "solid-comparison":solid_comparison,
    "melt-recast":melt_recast,
    "capacity-container":capacity_container,
    "composite-solid":composite_solid,
}
