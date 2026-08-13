"""
heights.py — visual figures for Chapter 44 (Heights & Distances).

elevation-basic : tower, horizontal distance and angle of elevation
depression      : angle of depression from a horizontal eye line
observer-height : eye height added to the line-of-sight rise
two-positions    : two observation points and two elevation angles
shadow-height    : height/shadow similar triangles
tower-distance   : two towers and a line-of-sight angle
a ngle-change    : distance from two angles of elevation
slant-line       : right triangle with height, base and line of sight
two-towers       : angle between two lines of sight to two objects
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=4400):
    value=spec.get("seed",default)
    try:return int(value)
    except Exception:return sum(ord(ch) for ch in str(value))


def _card(cv,x,y,w,h,col,bg,r=6,sw=1.4):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _fmt(v):
    v=float(v)
    if abs(v-round(v))<1e-9:return str(int(round(v)))
    return f"{v:.2f}".rstrip("0").rstrip(".")


def _angle(cv,vx,vy,r,start,end,col=C["red"]):
    cv.arc(vx,vy,r,math.radians(-end),math.radians(-start),color=col,w=1.3)


# ───────────────────────────── basic elevation ─────────────────────────────
def elevation_basic(spec):
    height=float(spec.get("height",20)); distance=float(spec.get("distance",20)); angle=float(spec.get("angle",45))
    W,H=452,270;ground=190;x0=68;top=x0+height*4.2;tx=x0+distance*4.2
    cv=Canvas(W,H,seed=_seed(spec,4401))
    cv.text(W/2,20,"angle of elevation: line of sight rises above the horizontal",size=9.7,weight=700,color=C["soft"])
    cv.line(32,ground,410,ground,color=C["ink"],w=1.5)
    cv.line(x0,ground,x0,ground-height*4.2,color=C["blue"],w=3)
    cv.line(x0,ground-height*4.2,tx,ground,color=C["red"],w=1.7)
    cv.line(x0,ground,tx,ground,color=C["green"],w=1.3,dash="4 3")
    cv.right_angle(x0,ground,(x0+20,ground),(x0,ground-height*4.2),size=11,color=C["purple"])
    _angle(cv,x0,ground,30,0,angle,C["red"])
    cv.text(x0+42,ground-20,f"{_fmt(angle)} deg",size=9,color=C["red"],weight=700)
    cv.text(x0-9,ground-height*2.2,f"H={_fmt(height)}",size=9,color=C["blue"],anchor="end",weight=700)
    cv.text((x0+tx)/2,ground+18,f"d={_fmt(distance)}",size=9,color=C["green"],weight=700)
    _card(cv,282,58,132,38,C["purple"],C["purple_bg"],sw=1.5);cv.text(348,81,"tan theta=H/d",size=9.5,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"measure the angle at the observer on the ground",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── depression ───────────────────────────────────
def depression(spec):
    height=float(spec.get("height",18)); distance=float(spec.get("distance",24)); angle=float(spec.get("angle",37))
    W,H=452,270;ground=194;obsx=70;top=48;targetx=obsx+distance*5
    cv=Canvas(W,H,seed=_seed(spec,4402))
    cv.text(W/2,20,"angle of depression is measured down from the horizontal eye line",size=9.5,weight=700,color=C["soft"])
    cv.line(32,ground,420,ground,color=C["ink"],w=1.5)
    cv.line(obsx,top,obsx,ground,color=C["blue"],w=3)
    cv.line(obsx,top,targetx,ground,color=C["red"],w=1.7)
    cv.line(obsx,top,410,top,color=C["green"],w=1.3,dash="4 3")
    _angle(cv,obsx,top,30,0,angle,C["red"])
    cv.text(obsx+35,top+28,f"{_fmt(angle)} deg",size=9,color=C["red"],weight=700)
    cv.text(obsx-9,(top+ground)/2,f"eye height={_fmt(height)}",size=8.8,color=C["blue"],anchor="end",weight=700)
    cv.text((obsx+targetx)/2,ground+18,f"distance={_fmt(distance)}",size=8.8,color=C["green"],weight=700)
    _card(cv,280,82,138,40,C["purple"],C["purple_bg"],sw=1.5);cv.text(349,106,"depression = elevation",size=9.2,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"horizontal eye line and ground are parallel",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── observer height ──────────────────────────────
def observer_height(spec):
    eye=float(spec.get("eye",1.6)); object_height=float(spec.get("object",12)); distance=float(spec.get("distance",20)); angle=float(spec.get("angle",30))
    rise=object_height-eye
    W,H=452,270;ground=194;x=70;tx=x+distance*4
    cv=Canvas(W,H,seed=_seed(spec,4403))
    cv.text(W/2,20,"use the vertical rise from the observer's eye, then add eye height",size=9.6,weight=700,color=C["soft"])
    cv.line(30,ground,420,ground,color=C["ink"],w=1.5)
    cv.line(x,ground,x,ground-eye*6,color=C["green"],w=2.5)
    cv.line(tx,ground,tx,ground-object_height*6,color=C["blue"],w=3)
    cv.line(x,ground-eye*6,tx,ground-object_height*6,color=C["red"],w=1.6)
    cv.line(x,ground-eye*6,tx,ground-eye*6,color=C["purple"],w=1.1,dash="4 3")
    _angle(cv,x,ground-eye*6,27,0,angle,C["red"])
    cv.text(x+32,ground-eye*6+26,f"{_fmt(angle)} deg",size=8.8,color=C["red"],weight=700)
    cv.text(x-8,ground-eye*3.1,f"eye={_fmt(eye)}",size=8.5,color=C["green"],anchor="end",weight=700)
    cv.text(tx+8,ground-object_height*3,f"H={_fmt(object_height)}",size=8.8,color=C["blue"],weight=700)
    _card(cv,270,70,148,42,C["purple"],C["purple_bg"],sw=1.5);cv.text(344,93,f"tan theta=({object_height}-{eye})/d",size=8.3,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"object height = eye height + d tan theta",size=8.8,color=C["ink"])
    return cv.svg()


# ───────────────────────────── two positions ────────────────────────────────
def two_positions(spec):
    W,H=452,270;ground=194;tx=310;top=58;P1=70;P2=175
    cv=Canvas(W,H,seed=_seed(spec,4404))
    cv.text(W/2,20,"two observation points create two right triangles",size=9.7,weight=700,color=C["soft"])
    cv.line(30,ground,420,ground,color=C["ink"],w=1.5);cv.line(tx,ground,tx,top,color=C["blue"],w=3)
    cv.line(P1,ground,tx,top,color=C["red"],w=1.5);cv.line(P2,ground,tx,top,color=C["green"],w=1.5)
    cv.line(P1,ground,P2,ground,color=C["purple"],w=1.2,dash="4 3")
    _angle(cv,P1,ground,28,0,27,C["red"]);_angle(cv,P2,ground,28,0,50,C["green"])
    cv.text(P1+30,ground-22,"alpha",size=8.5,color=C["red"],weight=700);cv.text(P2+30,ground-24,"beta",size=8.5,color=C["green"],weight=700)
    cv.text(P1,ground+17,"near",size=8,color=C["red"],weight=700);cv.text(P2,ground+17,"far",size=8,color=C["green"],weight=700)
    _card(cv,46,54,168,42,C["purple"],C["purple_bg"],sw=1.5);cv.text(130,77,"tan beta = H/d",size=9.3,weight=700,color=C["purple"])
    _card(cv,238,54,168,42,C["green"],C["green_bg"],sw=1.5);cv.text(322,77,"tan alpha = H/(d+x)",size=8.8,weight=700,color=C["green"])
    cv.text(W/2,H-8,"subtract the two equations to find unknown height or distance",size=8.5,color=C["ink"])
    return cv.svg()


# ───────────────────────────── shadow ───────────────────────────────────────
def shadow_height(spec):
    H=float(spec.get("height",12)); shadow=float(spec.get("shadow",8)); knownH=float(spec.get("knownH",3)); knownS=float(spec.get("knownS",2)); known_shadow=H*knownS/knownH
    W,Hh=452,250;ground=182;cv=Canvas(W,Hh,seed=_seed(spec,4405))
    cv.text(W/2,20,"same sun angle makes height/shadow ratios equal",size=9.8,weight=700,color=C["soft"])
    x1,x2=90,300
    cv.line(35,ground,415,ground,color=C["ink"],w=1.5)
    cv.line(x1,ground,x1,ground-H*7,color=C["blue"],w=3);cv.line(x1,ground,x1+shadow*8,ground,color=C["blue"],w=2)
    cv.line(x2,ground,x2,ground-knownH*7,color=C["green"],w=3);cv.line(x2,ground,x2+knownS*8,ground,color=C["green"],w=2)
    cv.line(x1,ground-H*7,x2+knownS*8,ground,color=C["amber"],w=1.3,dash="4 3")
    cv.text(x1-9,ground-H*3.5,f"H={_fmt(H)}",size=8.8,color=C["blue"],anchor="end",weight=700);cv.text(x1+shadow*4,ground+17,f"S={_fmt(shadow)}",size=8.8,color=C["blue"],weight=700)
    cv.text(x2-8,ground-knownH*3.5,f"{_fmt(knownH)}",size=8.6,color=C["green"],anchor="end",weight=700);cv.text(x2+knownS*4,ground+17,f"{_fmt(knownS)}",size=8.6,color=C["green"],weight=700)
    _card(cv,60,212,330,26,C["purple"],C["purple_bg"],sw=1.4);cv.text(225,230,f"H/S = {knownH}/{knownS}; required shadow={_fmt(known_shadow)}",size=8.7,weight=700,color=C["purple"])
    return cv.svg()


# ───────────────────────────── tower distance ───────────────────────────────
def tower_distance(spec):
    h1=float(spec.get("h1",20));h2=float(spec.get("h2",12));distance=float(spec.get("distance",16));
    W,H=452,270;ground=192;x1=70;x2=x1+distance*8
    cv=Canvas(W,H,seed=_seed(spec,4406))
    cv.text(W/2,20,"two vertical towers and a joining line create a height-difference triangle",size=9.4,weight=700,color=C["soft"])
    cv.line(32,ground,420,ground,color=C["ink"],w=1.5)
    cv.line(x1,ground,x1,ground-h1*5,color=C["blue"],w=3);cv.line(x2,ground,x2,ground-h2*5,color=C["green"],w=3)
    cv.line(x1,ground-h1*5,x2,ground-h2*5,color=C["red"],w=1.6)
    cv.line(x1,ground-h2*5,x2,ground-h2*5,color=C["purple"],w=1.1,dash="4 3")
    cv.text(x1-8,ground-h1*2.5,f"H1={_fmt(h1)}",size=8.7,color=C["blue"],anchor="end",weight=700);cv.text(x2+8,ground-h2*2.5,f"H2={_fmt(h2)}",size=8.7,color=C["green"],weight=700)
    cv.text((x1+x2)/2,ground+17,f"d={_fmt(distance)}",size=8.8,color=C["purple"],weight=700)
    _card(cv,274,58,144,42,C["red"],C["red_bg"],sw=1.5);cv.text(346,82,"tan theta=(H1-H2)/d",size=8.7,weight=700,color=C["red"])
    cv.text(W/2,H-8,"compare height difference when sight line joins two tops",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── angle change ─────────────────────────────────
def angle_change(spec):
    W,H=452,270;ground=194;tx=320;top=58;near=86;far=190
    cv=Canvas(W,H,seed=_seed(spec,4407))
    cv.text(W/2,20,"moving closer increases the angle of elevation",size=9.9,weight=700,color=C["soft"])
    cv.line(30,ground,420,ground,color=C["ink"],w=1.5);cv.line(tx,ground,tx,top,color=C["blue"],w=3)
    cv.line(near,ground,tx,top,color=C["red"],w=1.6);cv.line(far,ground,tx,top,color=C["green"],w=1.6)
    _angle(cv,near,ground,26,0,54,C["red"]);_angle(cv,far,ground,26,0,32,C["green"])
    cv.text(near+32,ground-22,"beta",size=8.7,color=C["red"],weight=700);cv.text(far+32,ground-20,"alpha",size=8.7,color=C["green"],weight=700)
    cv.text(near,ground+17,"near",size=8,color=C["red"],weight=700);cv.text(far,ground+17,"far",size=8,color=C["green"],weight=700)
    _card(cv,50,58,164,40,C["purple"],C["purple_bg"],sw=1.5);cv.text(132,82,"tan alpha=H/d_far",size=8.9,weight=700,color=C["purple"])
    _card(cv,238,58,164,40,C["red"],C["red_bg"],sw=1.5);cv.text(320,82,"tan beta=H/d_near",size=8.9,weight=700,color=C["red"])
    cv.text(W/2,H-8,"for the same H, shorter horizontal distance means larger angle",size=8.4,color=C["ink"])
    return cv.svg()


# ───────────────────────────── slant line ──────────────────────────────────
def slant_line(spec):
    h=float(spec.get("height",12));d=float(spec.get("distance",5));s=math.sqrt(h*h+d*d)
    W,H=452,238;cv=Canvas(W,H,seed=_seed(spec,4408))
    cv.text(W/2,20,"line of sight is the hypotenuse of the observation triangle",size=9.7,weight=700,color=C["soft"])
    A,B,Cc=(62,184),(250,184),(62,184-h*7)
    cv.polygon([A,B,Cc],color=C["blue"],w=1.8,fill=C["blue_bg"]);cv.right_angle(A[0],A[1],B,Cc,size=13,color=C["red"]);cv.line(*B,*Cc,color=C["red"],w=1.7)
    cv.text(150,202,f"d={_fmt(d)}",size=9,color=C["green"],weight=700);cv.text(51,116,f"H={_fmt(h)}",size=9,color=C["blue"],anchor="end",weight=700);cv.text(150,105,f"s={_fmt(s)}",size=9,color=C["red"],weight=700)
    _card(cv,286,68,130,36,C["purple"],C["purple_bg"],sw=1.5);cv.text(351,91,"s²=H²+d²",size=9.5,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"use sin/cos for slant distance when angle is known",size=8.7,color=C["ink"])
    return cv.svg()


REGISTRY={
    "elevation-basic":elevation_basic,
    "depression":depression,
    "observer-height":observer_height,
    "two-positions":two_positions,
    "shadow-height":shadow_height,
    "tower-distance":tower_distance,
    "angle-change":angle_change,
    "slant-line":slant_line,
}
