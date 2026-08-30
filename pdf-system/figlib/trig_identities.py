"""
trig_identities.py — visual figures for Chapter 43.

identity-triangle    : Pythagorean identity from a right triangle
reciprocal-web       : reciprocal and quotient identities
complementary-angle  : theta and (90-theta) cofunction pair
identity-proof       : convert one side step by step
sec-tan              : sec^2 = 1 + tan^2 triangle relation
cosec-cot            : cosec^2 = 1 + cot^2 relation
unit-circle-identities: sin^2+cos^2 from unit-circle coordinates
allied-angles        : signs and values after angle shifts
trig-simplify        : simplify a mixed identity expression
value-from-ratio     : derive all ratios from one given ratio
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=4300):
    value=spec.get("seed",default)
    try:return int(value)
    except Exception:return sum(ord(ch) for ch in str(value))


def _card(cv,x,y,w,h,col,bg,r=6,sw=1.4):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _fmt(v):
    v=float(v)
    if abs(v-round(v))<1e-9:return str(int(round(v)))
    return f"{v:.2f}".rstrip("0").rstrip(".")


def _tri(cv,A,B,Cc,col=C["blue"],fill=C["blue_bg"]):
    cv.polygon([A,B,Cc],color=col,w=1.8,fill=fill)


# ───────────────────────────── identity triangle ───────────────────────────
def identity_triangle(spec):
    W,H=452,260;cv=Canvas(W,H,seed=_seed(spec,4301))
    cv.text(W/2,20,"Pythagoras becomes sin² theta + cos² theta = 1",size=9.8,weight=700,color=C["soft"])
    A,B,Cc=(48,188),(220,188),(48,70);_tri(cv,A,B,Cc)
    cv.right_angle(A[0],A[1],B,Cc,size=13,color=C["red"])
    cv.text(126,205,"hypotenuse = 1",size=9,color=C["purple"],weight=700)
    cv.text(38,130,"sin",size=9,color=C["red"],anchor="end",weight=700)
    cv.text(128,180,"cos",size=9,color=C["green"],weight=700)
    _card(cv,274,60,146,38,C["purple"],C["purple_bg"],sw=1.5);cv.text(347,84,"sin² + cos² = 1",size=9.8,weight=700,color=C["purple"])
    _card(cv,274,116,146,38,C["green"],C["green_bg"],sw=1.5);cv.text(347,140,"sec² = 1 + tan²",size=9.2,weight=700,color=C["green"])
    _card(cv,274,172,146,38,C["amber"],C["amber_bg"],sw=1.5);cv.text(347,196,"cosec² = 1 + cot²",size=8.8,weight=700,color=C["amber"])
    return cv.svg()


# ───────────────────────────── reciprocal web ──────────────────────────────
def reciprocal_web(spec):
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4302))
    cv.text(W/2,20,"three ratios, their reciprocals and quotient forms",size=9.8,weight=700,color=C["soft"])
    rows=[("sin","O/H","cosec","H/O",C["red"]),("cos","A/H","sec","H/A",C["green"]),("tan","O/A","cot","A/O",C["purple"])]
    for i,(a,af,b,bf,col) in enumerate(rows):
        y=48+i*50
        _card(cv,32,y,150,34,col,"#ffffff",sw=1.4);cv.text(107,y+15,a,size=9,weight=700,color=col);cv.text(107,y+29,af,size=9,color=col)
        cv.arrow(190,y+17,250,y+17,color=C["grey"],w=1.1)
        _card(cv,268,y,150,34,col,"#ffffff",sw=1.4);cv.text(343,y+15,b,size=9,weight=700,color=col);cv.text(343,y+29,bf,size=9,color=col)
    _card(cv,70,204,312,26,C["purple"],C["purple_bg"],sw=1.4);cv.text(226,222,"tan = sin/cos    |    cot = cos/sin",size=8.9,weight=700,color=C["purple"])
    return cv.svg()


# ───────────────────────────── complementary ───────────────────────────────
def complementary_angle(spec):
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4303));vx,vy=70,178
    cv.text(W/2,20,"complementary angles exchange sine and cosine",size=9.8,weight=700,color=C["soft"])
    p1=(vx+125,vy);p2=(vx+125*math.cos(math.radians(90)),vy-125*math.sin(math.radians(90)));pm=(vx+125*math.cos(math.radians(35)),vy-125*math.sin(math.radians(35)))
    cv.line(vx,vy,*p1,color=C["blue"],w=1.7);cv.line(vx,vy,*p2,color=C["blue"],w=1.7);cv.line(vx,vy,*pm,color=C["green"],w=1.6)
    cv.arc(vx,vy,30,0,35,color=C["red"],w=1.3);cv.arc(vx,vy,43,35,90,color=C["purple"],w=1.3)
    cv.text(vx+47,vy-15,"theta",size=9,color=C["red"],weight=700);cv.text(vx+23,vy-52,"90-theta",size=8.5,color=C["purple"],weight=700)
    rows=[("sin(90-theta)","= cos theta",C["red"]),("cos(90-theta)","= sin theta",C["green"]),("tan(90-theta)","= cot theta",C["purple"])]
    for i,(a,b,col) in enumerate(rows):
        yy=58+i*42;_card(cv,250,yy,166,30,col,"#ffffff",r=5,sw=1.2);cv.text(333,yy+20,f"{a} {b}",size=8.2,weight=700,color=col)
    cv.text(W/2,H-8,"the two acute angles of a right triangle are complementary",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── identity proof ──────────────────────────────
def identity_proof(spec):
    W,H=452,272;cv=Canvas(W,H,seed=_seed(spec,4304))
    cv.text(W/2,20,"prove an identity by changing one side step by step",size=9.8,weight=700,color=C["soft"])
    lines=[("LHS = sec² theta - tan² theta","start",C["blue"],C["blue_bg"]),("= (1/cos²) - (sin²/cos²)","write in sin/cos",C["green"],C["green_bg"]),("= (1-sin²)/cos²","common denominator",C["amber"],C["amber_bg"]),("= cos²/cos² = 1","Pythagorean identity",C["purple"],C["purple_bg"])]
    for i,(t,n,col,bg) in enumerate(lines):
        y=46+i*44;_card(cv,34,y,338,32,col,bg,r=5,sw=1.3);cv.text(48,y+21,t,size=9,anchor="start",weight=700,color=col);cv.text(404,y+21,n,size=7.7,anchor="end",color=C["soft"])
    cv.text(W/2,H-8,"never assume the result; transform LHS or RHS until they match",size=8.5,color=C["ink"])
    return cv.svg()


# ───────────────────────────── sec/tan ─────────────────────────────────────
def sec_tan(spec):
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4305))
    cv.text(W/2,20,"divide sin² theta + cos² theta = 1 by cos² theta",size=9.6,weight=700,color=C["soft"])
    cv.line(52,184,216,184,color=C["blue"],w=1.8);cv.line(52,184,52,70,color=C["green"],w=1.8);cv.line(52,70,216,184,color=C["purple"],w=1.8)
    cv.right_angle(52,184,(72,184),(52,164),size=12,color=C["red"])
    cv.text(130,202,"cos",size=9,color=C["blue"],weight=700);cv.text(38,128,"sin",size=9,color=C["green"],anchor="end",weight=700);cv.text(130,120,"1",size=10,color=C["purple"],weight=700)
    _card(cv,270,58,144,36,C["purple"],C["purple_bg"],sw=1.5);cv.text(342,81,"sec² = 1 + tan²",size=9.2,weight=700,color=C["purple"])
    _card(cv,270,112,144,36,C["green"],C["green_bg"],sw=1.5);cv.text(342,135,"tan² = sec² - 1",size=9.1,weight=700,color=C["green"])
    _card(cv,270,166,144,36,C["amber"],C["amber_bg"],sw=1.5);cv.text(342,189,"divide by cos²",size=9,weight=700,color=C["amber"])
    return cv.svg()


# ───────────────────────────── cosec/cot ───────────────────────────────────
def cosec_cot(spec):
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4306))
    cv.text(W/2,20,"divide sin² theta + cos² theta = 1 by sin² theta",size=9.5,weight=700,color=C["soft"])
    _card(cv,48,54,164,46,C["red"],C["red_bg"],sw=1.5);cv.text(130,75,"sin² + cos² = 1",size=10,weight=700,color=C["red"]);cv.text(130,92,"divide by sin²",size=8.5,color=C["red"])
    cv.arrow(216,77,246,77,color=C["grey"],w=1.2)
    _card(cv,254,54,164,46,C["purple"],C["purple_bg"],sw=1.5);cv.text(336,75,"cosec² = 1 + cot²",size=9.5,weight=700,color=C["purple"]);cv.text(336,92,"main identity",size=8.5,color=C["purple"])
    _card(cv,74,136,304,34,C["green"],C["green_bg"],sw=1.5);cv.text(226,158,"cot² = cosec² - 1",size=10,weight=700,color=C["green"])
    cv.text(W/2,H-8,"same Pythagorean identity, a different denominator",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── unit circle ──────────────────────────────────
def unit_circle_id(spec):
    W,H=452,260;cx,cy,R=130,132,82;cv=Canvas(W,H,seed=_seed(spec,4307))
    cv.text(W/2,20,"unit-circle coordinates prove sin² theta + cos² theta = 1",size=9.5,weight=700,color=C["soft"])
    cv.circle(cx,cy,R,color=C["blue"],w=1.7,fill=C["blue_bg"]);cv.line(cx-R-10,cy,cx+R+10,cy,color=C["ink"],w=1.1);cv.line(cx,cy-R-10,cx,cy+R+10,color=C["ink"],w=1.1)
    p=(cx+R*math.cos(math.radians(50)),cy-R*math.sin(math.radians(50)))
    cv.line(cx,cy,*p,color=C["red"],w=1.5);cv.line(p[0],p[1],p[0],cy,color=C["green"],w=1.2,dash="4 3");cv.dot(*p,r=4,color=C["red"])
    _card(cv,264,60,150,40,C["purple"],C["purple_bg"],sw=1.5);cv.text(339,84,"x=cos theta",size=9.4,weight=700,color=C["purple"])
    _card(cv,264,116,150,40,C["green"],C["green_bg"],sw=1.5);cv.text(339,140,"y=sin theta",size=9.4,weight=700,color=C["green"])
    _card(cv,264,172,150,40,C["amber"],C["amber_bg"],sw=1.5);cv.text(339,196,"x²+y²=1",size=10,weight=700,color=C["amber"])
    return cv.svg()


# ───────────────────────────── allied angles ────────────────────────────────
def allied_angles(spec):
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4308))
    cv.text(W/2,20,"angle shifts change signs according to the quadrant",size=9.7,weight=700,color=C["soft"])
    rows=[("theta","sin +","cos +","QI",C["green"]),("180-theta","sin +","cos -","QII",C["blue"]),("180+theta","sin -","cos -","QIII",C["red"]),("360-theta","sin -","cos +","QIV",C["purple"])]
    for i,(ang,sn,cs,q,col) in enumerate(rows):
        y=46+i*42;_card(cv,30,y,392,30,col,"#ffffff",r=5,sw=1.2);cv.text(48,y+20,ang,size=8.9,anchor="start",weight=700,color=col);cv.text(180,y+20,sn,size=8.5,color=col);cv.text(274,y+20,cs,size=8.5,color=col);cv.text(398,y+20,q,size=8.5,anchor="end",weight=700,color=col)
    cv.text(W/2,H-8,"reference angle gives magnitude; quadrant gives sign",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── simplification ───────────────────────────────
def trig_simplify(spec):
    W,H=452,252;cv=Canvas(W,H,seed=_seed(spec,4309))
    cv.text(W/2,20,"simplify by converting everything to sin and cos",size=9.9,weight=700,color=C["soft"])
    lines=[("(1-cos² theta)/sin theta","given",C["blue"],C["blue_bg"]),("= sin² theta / sin theta","1-cos²=sin²",C["green"],C["green_bg"]),("= sin theta","cancel one sin",C["purple"],C["purple_bg"])]
    for i,(t,n,col,bg) in enumerate(lines):
        y=48+i*45;_card(cv,42,y,368,32,col,bg,r=5,sw=1.3);cv.text(54,y+21,t,size=9.3,anchor="start",weight=700,color=col);cv.text(398,y+21,n,size=8,anchor="end",color=C["soft"])
    cv.text(W/2,H-8,"cancel only complete common factors, not terms",size=8.7,color=C["red"])
    return cv.svg()


# ───────────────────────────── derive ratios ────────────────────────────────
def value_from_ratio(spec):
    O,A,H=3,4,5
    W,Hh=452,250;cv=Canvas(W,Hh,seed=_seed(spec,4310))
    cv.text(W/2,20,"one ratio plus a right triangle gives every ratio",size=9.8,weight=700,color=C["soft"])
    cv.polygon([(48,184),(218,184),(48,84)],color=C["blue"],w=1.8,fill=C["blue_bg"]);cv.right_angle(48,184,(218,184),(48,84),size=12,color=C["red"])
    cv.text(130,200,"A=4",size=9.5,color=C["green"],weight=700);cv.text(38,136,"O=3",size=9.5,color=C["red"],anchor="end",weight=700);cv.text(128,117,"H=5",size=9.5,color=C["purple"],weight=700)
    rows=[("sin","3/5",C["red"]),("cos","4/5",C["green"]),("tan","3/4",C["purple"]),("sec","5/4",C["amber"])]
    for i,(lab,val,col) in enumerate(rows):
        y=56+i*36;_card(cv,286,y,128,26,col,"#ffffff",r=5,sw=1.1);cv.text(350,y+18,f"{lab}={val}",size=9,weight=700,color=col)
    return cv.svg()


REGISTRY={
    "identity-triangle":identity_triangle,
    "reciprocal-web":reciprocal_web,
    "complementary-angle":complementary_angle,
    "identity-proof":identity_proof,
    "sec-tan":sec_tan,
    "cosec-cot":cosec_cot,
    "unit-circle-identities":unit_circle_id,
    "allied-angles":allied_angles,
    "trig-simplify":trig_simplify,
    "value-from-ratio":value_from_ratio,
}
