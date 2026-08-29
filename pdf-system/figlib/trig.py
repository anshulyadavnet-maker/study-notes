"""
trig.py — visual figures for Chapter 42 (Trigonometric Ratios, Degrees & Radians).

right-trig       : opposite, adjacent, hypotenuse around an angle
trig-ratios      : six ratios and reciprocal pairs
special-30-60    : 30-60-90 triangle side ratios
special-45       : 45-45-90 triangle
unit-circle      : angle and coordinates on the unit circle
degree-radian    : semicircle and pi-radian conversion
special-table    : exact values at standard angles
quadrant-signs   : ASTC sign pattern
trig-graph       : basic sine-wave cycle markers
angle-triangle   : solve a right triangle from an angle and side
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=4200):
    value=spec.get("seed",default)
    try:return int(value)
    except Exception:return sum(ord(ch) for ch in str(value))


def _card(cv,x,y,w,h,col,bg,r=6,sw=1.4):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _fmt(v):
    v=float(v)
    if abs(v-round(v))<1e-9:return str(int(round(v)))
    return f"{v:.2f}".rstrip("0").rstrip(".")


def _tri(cv,A,B,Cc,color=None,fill=C["blue_bg"]):
    cv.polygon([A,B,Cc],color=color or C["blue"],w=1.8,fill=fill)


# ───────────────────────────── right triangle ratios ─────────────────────────
def right_trig(spec):
    W,H=452,270
    cv=Canvas(W,H,seed=_seed(spec,4201))
    cv.text(W/2,20,"choose an acute angle, then name opposite, adjacent and hypotenuse",size=9.5,weight=700,color=C["soft"])
    A,B,Cc=(55,190),(250,190),(55,65)
    _tri(cv,A,B,Cc)
    cv.right_angle(A[0],A[1],B,Cc,size=14,color=C["red"])
    cv.arc(Cc[0],Cc[1],24,0,33,color=C["purple"],w=1.3)
    cv.text(Cc[0]+31,Cc[1]+10,"theta",size=10,color=C["purple"],weight=700)
    cv.text(150,204,"adjacent",size=9,color=C["green"],weight=700)
    cv.text(36,127,"opposite",size=8.8,color=C["red"],anchor="end",weight=700)
    cv.text(142,117,"hypotenuse",size=9,color=C["blue"],weight=700)
    rows=[("sin theta","opposite / hypotenuse",C["red"]),("cos theta","adjacent / hypotenuse",C["green"]),("tan theta","opposite / adjacent",C["purple"])]
    for i,(lab,val,col) in enumerate(rows):
        yy=52+i*42
        _card(cv,286,yy,136,30,col,"#ffffff",r=5,sw=1.2)
        cv.text(354,yy+20,lab,size=8.5,weight=700,color=col)
        cv.text(354,yy+34,val,size=6.8,color=C["soft"])
    return cv.svg()


# ───────────────────────────── six ratios ──────────────────────────────────
def trig_ratios(spec):
    W,H=452,264
    cv=Canvas(W,H,seed=_seed(spec,4202))
    cv.text(W/2,20,"three basic ratios and their reciprocal partners",size=10,weight=700,color=C["soft"])
    rows=[("sin theta","O/H","cosec theta","H/O",C["red"],C["red_bg"]),
          ("cos theta","A/H","sec theta","H/A",C["green"],C["green_bg"]),
          ("tan theta","O/A","cot theta","A/O",C["purple"],C["purple_bg"])]
    for i,(left,lval,right,rval,col,bg) in enumerate(rows):
        y=48+i*52
        _card(cv,34,y,166,38,col,bg,sw=1.5);cv.text(117,y+17,left,size=9,weight=700,color=col);cv.text(117,y+32,lval,size=9,color=col)
        cv.text(226,y+20,"<->",size=11,weight=700,color=C["grey"])
        _card(cv,252,y,166,38,col,"#ffffff",sw=1.3);cv.text(335,y+17,right,size=9,weight=700,color=col);cv.text(335,y+32,rval,size=9,color=col)
    cv.text(W/2,H-8,"reciprocal pairs multiply to 1",size=8.8,color=C["ink"])
    return cv.svg()


# ───────────────────────────── 30-60-90 ────────────────────────────────────
def special_30_60(spec):
    W,H=452,260;cv=Canvas(W,H,seed=_seed(spec,4203))
    cv.text(W/2,20,"30-60-90 triangle: sides 1 : sqrt(3) : 2",size=10.2,weight=700,color=C["soft"])
    A,B,Cc=(52,190),(52,70),(260,190)
    _tri(cv,A,B,Cc,color=C["blue"],fill=C["blue_bg"]);cv.right_angle(A[0],A[1],B,Cc,size=13,color=C["red"])
    cv.text(42,130,"1",size=11,color=C["green"],weight=700,anchor="end")
    cv.text(154,198,"sqrt(3)",size=10,color=C["purple"],weight=700)
    cv.text(158,119,"2",size=11,color=C["red"],weight=700)
    cv.text(61,177,"60 deg",size=8.5,color=C["green"],weight=700)
    cv.text(58,84,"30 deg",size=8.5,color=C["purple"],weight=700)
    _card(cv,300,62,122,46,C["purple"],C["purple_bg"],sw=1.5);cv.text(361,84,"sin 30=1/2",size=9.2,weight=700,color=C["purple"]);cv.text(361,101,"cos 30=sqrt3/2",size=8.2,color=C["purple"])
    _card(cv,300,128,122,46,C["green"],C["green_bg"],sw=1.5);cv.text(361,150,"sin 60=sqrt3/2",size=8.4,weight=700,color=C["green"]);cv.text(361,167,"tan 60=sqrt3",size=8.4,color=C["green"])
    cv.text(W/2,H-8,"short side opposite 30 deg; hypotenuse double it",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── 45-45-90 ─────────────────────────────────────
def special_45(spec):
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4204))
    cv.text(W/2,20,"45-45-90 triangle: equal legs and hypotenuse sqrt(2) times a leg",size=9.7,weight=700,color=C["soft"])
    A,B,Cc=(55,184),(55,72),(167,184)
    _tri(cv,A,B,Cc,color=C["blue"],fill=C["blue_bg"]);cv.right_angle(A[0],A[1],B,Cc,size=13,color=C["red"])
    cv.ticks(A,B,count=1,color=C["green"]);cv.ticks(A,Cc,count=1,color=C["green"])
    cv.text(40,130,"1",size=10,color=C["green"],anchor="end",weight=700);cv.text(110,199,"1",size=10,color=C["green"],weight=700);cv.text(118,119,"sqrt(2)",size=10,color=C["purple"],weight=700)
    cv.text(69,92,"45 deg",size=8.5,color=C["red"],weight=700);cv.text(133,172,"45 deg",size=8.5,color=C["red"],weight=700)
    _card(cv,250,70,160,40,C["purple"],C["purple_bg"],sw=1.5);cv.text(330,94,"sin45=cos45=1/sqrt2",size=8.5,weight=700,color=C["purple"])
    _card(cv,250,132,160,40,C["green"],C["green_bg"],sw=1.5);cv.text(330,156,"tan45=1",size=10,weight=700,color=C["green"])
    return cv.svg()


# ───────────────────────────── unit circle ──────────────────────────────────
def unit_circle(spec):
    theta=float(spec.get("angle",60)); W,H=452,270;cx,cy,R=150,140,88
    cv=Canvas(W,H,seed=_seed(spec,4205))
    cv.text(W/2,20,"unit circle: point coordinates are (cos theta, sin theta)",size=9.7,weight=700,color=C["soft"])
    cv.circle(cx,cy,R,color=C["blue"],w=1.7,fill=C["blue_bg"])
    cv.line(cx-R-15,cy,cx+R+15,cy,color=C["ink"],w=1.1);cv.line(cx,cy-R-15,cx,cy+R+15,color=C["ink"],w=1.1)
    p=(cx+R*math.cos(math.radians(theta)),cy-R*math.sin(math.radians(theta)))
    cv.line(cx,cy,*p,color=C["red"],w=1.5);cv.line(p[0],p[1],p[0],cy,color=C["green"],w=1.2,dash="4 3")
    cv.dot(*p,r=4,color=C["red"]);cv.arc(cx,cy,30,0,theta,color=C["purple"],w=1.3)
    cv.text(p[0]+8,p[1]-8,f"({math.cos(math.radians(theta)):.2f},{math.sin(math.radians(theta)):.2f})",size=8.5,color=C["red"],anchor="start",weight=700)
    _card(cv,286,72,140,54,C["purple"],C["purple_bg"],sw=1.5);cv.text(356,94,f"theta={_fmt(theta)} deg",size=9.4,weight=700,color=C["purple"]);cv.text(356,113,"x=cos, y=sin",size=8.7,color=C["purple"])
    cv.text(W/2,H-8,"radius = 1; sin and cos are coordinate projections",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── degree radian ───────────────────────────────
def degree_radian(spec):
    W,H=452,250;cx,cy,R=142,128,86
    cv=Canvas(W,H,seed=_seed(spec,4206))
    cv.text(W/2,20,"one complete semicircle measures 180 degrees or pi radians",size=9.8,weight=700,color=C["soft"])
    cv.arc(cx,cy,R,0,180,color=C["blue"],w=1.8);cv.line(cx-R,cy,cx+R,cy,color=C["ink"],w=1.2)
    cv.line(cx,cy,cx+R,cy,color=C["green"],w=1.3);cv.arc(cx,cy,28,0,60,color=C["red"],w=1.3)
    cv.text(cx+R/2,cy-8,"180 deg = pi rad",size=10,color=C["purple"],weight=700)
    cv.text(cx+42,cy-34,"theta",size=9,color=C["red"],weight=700)
    _card(cv,286,70,136,38,C["green"],C["green_bg"],sw=1.5);cv.text(354,93,"deg -> rad: x pi/180",size=8.6,weight=700,color=C["green"])
    _card(cv,286,124,136,38,C["purple"],C["purple_bg"],sw=1.5);cv.text(354,147,"rad -> deg: x 180/pi",size=8.6,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"90 deg=pi/2; 180 deg=pi; 360 deg=2pi",size=8.8,color=C["ink"])
    return cv.svg()


# ───────────────────────────── exact table ──────────────────────────────────
def special_table(spec):
    W,H=452,270;cv=Canvas(W,H,seed=_seed(spec,4207))
    cv.text(W/2,20,"standard-angle values follow 0,1,2,3,4 under square roots",size=9.4,weight=700,color=C["soft"])
    headers=["theta","0","30","45","60","90"]
    rows=[("sin","0","1/2","1/sqrt2","sqrt3/2","1",C["red"]),("cos","1","sqrt3/2","1/sqrt2","1/2","0",C["green"]),("tan","0","1/sqrt3","1","sqrt3","undef",C["purple"])]
    x0,y0,cw,ch=26,48,70,36
    for j,v in enumerate(headers):
        _card(cv,x0+j*cw,y0,cw-4,ch-4,C["blue"],C["blue_bg"],r=4,sw=1.1);cv.text(x0+j*cw+(cw-4)/2,y0+21,v,size=8.7,weight=700,color=C["blue"])
    for i,(lab,*vals,col) in enumerate(rows):
        y=y0+(i+1)*ch
        for j,v in enumerate([lab]+vals):
            _card(cv,x0+j*cw,y,cw-4,ch-4,col,"#ffffff",r=4,sw=1.1);cv.text(x0+j*cw+(cw-4)/2,y+21,v,size=8.2,weight=700 if j==0 else 400,color=col)
    cv.text(W/2,H-8,"memorise sin; cos reverses sin table; tan=sin/cos",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── quadrant signs ──────────────────────────────
def quadrant_signs(spec):
    W,H=452,248;cx,cy=140,126;R=78
    cv=Canvas(W,H,seed=_seed(spec,4208))
    cv.text(W/2,20,"ASTC: signs of trigonometric ratios by quadrant",size=10,weight=700,color=C["soft"])
    cv.circle(cx,cy,R,color=C["blue"],w=1.5,fill=C["blue_bg"]);cv.line(cx-R-12,cy,cx+R+12,cy,color=C["ink"],w=1.2);cv.line(cx,cy-R-12,cx,cy+R+12,color=C["ink"],w=1.2)
    for text,x,y,col in (("A: all +",cx-54,cy-48,C["green"]),("S: sin +",cx+32,cy-48,C["blue"]),("T: tan +",cx-54,cy+58,C["red"]),("C: cos +",cx+32,cy+58,C["purple"])):
        cv.text(x,y,text,size=8.4,weight=700,color=col)
    _card(cv,274,58,142,82,C["green"],C["green_bg"],sw=1.5);cv.text(345,82,"QI: all +",size=9.5,weight=700,color=C["green"]);cv.text(345,103,"QII: sin",size=8.5,color=C["green"]);cv.text(345,120,"QIII: tan",size=8.5,color=C["green"]);cv.text(345,137,"QIV: cos",size=8.5,color=C["green"])
    cv.text(W/2,H-8,"ASTC = All, Sin, Tan, Cos",size=9,color=C["ink"])
    return cv.svg()


# ───────────────────────────── basic solve triangle ─────────────────────────
def angle_triangle(spec):
    angle=float(spec.get("angle",30)); hyp=float(spec.get("hyp",10)); opp=hyp*math.sin(math.radians(angle));adj=hyp*math.cos(math.radians(angle))
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4209))
    cv.text(W/2,20,"right-triangle values come from the selected angle",size=9.7,weight=700,color=C["soft"])
    A,B,Cc=(52,184),(250,184),(52,184-hyp*8)
    # fixed-scale visual triangle
    _tri=None
    cv.polygon([A,B,Cc],color=C["blue"],w=1.8,fill=C["blue_bg"]);cv.right_angle(A[0],A[1],B,Cc,size=13,color=C["red"])
    cv.text(74,171,f"angle={_fmt(angle)}",size=8.5,color=C["purple"],weight=700);cv.text(130,198,f"adj={_fmt(adj)}",size=9,color=C["green"],weight=700);cv.text(42,105,f"opp={_fmt(opp)}",size=8.8,color=C["red"],anchor="end",weight=700);cv.text(150,94,f"hyp={_fmt(hyp)}",size=9,color=C["blue"],weight=700)
    _card(cv,286,68,128,38,C["purple"],C["purple_bg"],sw=1.5);cv.text(350,91,f"sin={_fmt(opp/hyp)}",size=9.4,weight=700,color=C["purple"])
    _card(cv,286,122,128,38,C["green"],C["green_bg"],sw=1.5);cv.text(350,145,f"cos={_fmt(adj/hyp)}",size=9.4,weight=700,color=C["green"])
    cv.text(W/2,H-8,"choose ratio from the sides named relative to theta",size=8.7,color=C["ink"])
    return cv.svg()


REGISTRY={
    "right-trig":right_trig,
    "trig-ratios":trig_ratios,
    "special-30-60":special_30_60,
    "special-45":special_45,
    "unit-circle":unit_circle,
    "degree-radian":degree_radian,
    "special-table":special_table,
    "quadrant-signs":quadrant_signs,
    "trig-graph":special_table,
    "angle-triangle":angle_triangle,
}
