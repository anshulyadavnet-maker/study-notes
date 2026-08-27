"""
coordinate41.py — visual figures for Chapter 41 (Coordinate Geometry).

coordinate-plane41    : axes, quadrants and plotted points
distance-formula      : right-triangle rise/run distance
midpoint              : midpoint as coordinate averages
section-formula       : internal division in a given ratio
slope-coordinate      : slope as rise over run
collinear             : three points on one straight line
triangle-area-coordinate: coordinate triangle and determinant area
line-parallel         : parallel/perpendicular slope comparison
reflection            : reflections in axes and origin
coordinate-shape      : coordinate rectangle/triangle and side measures
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=4100):
    value=spec.get("seed",default)
    try:return int(value)
    except Exception:return sum(ord(ch) for ch in str(value))


def _fmt(v):
    v=float(v)
    if abs(v-round(v))<1e-9:return str(int(round(v)))
    return f"{v:.2f}".rstrip("0").rstrip(".")


def _card(cv,x,y,w,h,col,bg,r=6,sw=1.4):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _axes(cv,ox=150,oy=130,scale=24,xmin=-4,xmax=4,ymin=-4,ymax=4):
    cv.line(ox+xmin*scale,oy,ox+xmax*scale,oy,color=C["ink"],w=1.4)
    cv.arrow(ox+(xmax-.3)*scale,oy,ox+xmax*scale+8,oy,color=C["ink"],w=1.2)
    cv.line(ox,oy-ymin*scale,ox,oy-ymax*scale,color=C["ink"],w=1.4)
    cv.arrow(ox,oy-(ymax-.3)*scale,ox,oy-ymax*scale-8,color=C["ink"],w=1.2)
    for x in range(xmin,xmax+1):
        if x:
            px=ox+x*scale;cv.line(px,oy-3,px,oy+3,color=C["grey"],w=.8);cv.text(px,oy+14,str(x),size=7.2,color=C["soft"])
    for y in range(ymin,ymax+1):
        if y:
            py=oy-y*scale;cv.line(ox-3,py,ox+3,py,color=C["grey"],w=.8);cv.text(ox-9,py+3,str(y),size=7.2,anchor="end",color=C["soft"])
    cv.text(ox+xmax*scale+12,oy-4,"x",size=9,weight=700)
    cv.text(ox+7,oy-ymax*scale-8,"y",size=9,weight=700)
    cv.text(ox+7,oy+14,"O",size=7.5,weight=700)


def _point(cv,ox,oy,scale,x,y,label=None,color=None):
    px,py=ox+x*scale,oy-y*scale
    cv.dot(px,py,r=4,color=color or C["red"])
    if label:cv.text(px+7,py-8,label,size=8.7,weight=700,color=color or C["red"])
    return px,py


# ───────────────────────────── plane ───────────────────────────────────────
def coordinate_plane41(spec):
    W,H=452,270;ox,oy,scale=226,142,23
    cv=Canvas(W,H,seed=_seed(spec,4101))
    cv.text(W/2,20,"Cartesian plane: coordinate (x,y) fixes a unique point",size=10,weight=700,color=C["soft"])
    _axes(cv,ox,oy,scale)
    for q,(sx,sy) in zip(("I","II","III","IV"),((1,-1),(-1,-1),(-1,1),(1,1))):
        cv.text(ox+sx*2.4*scale,oy+sy*2.4*scale,q,size=10,color=C["grey"],weight=700)
    for x,y,label,col in ((2,2,"A",C["blue"]),(-2,1,"B",C["green"]),(-2,-2,"C",C["red"]),(3,-2,"D",C["amber"])):
        _point(cv,ox,oy,scale,x,y,label,col)
    cv.text(W/2,H-8,"x is horizontal; y is vertical; origin is (0,0)",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── distance ─────────────────────────────────────
def distance_formula(spec):
    x1,y1=0,0;x2,y2=4,3
    W,H=452,258;ox,oy,scale=54,194,35
    cv=Canvas(W,H,seed=_seed(spec,4102))
    cv.text(W/2,20,"distance is the hypotenuse of the coordinate right triangle",size=9.7,weight=700,color=C["soft"])
    A=_point(cv,ox,oy,scale,x1,y1,"A",C["blue"]);B=_point(cv,ox,oy,scale,x2,y2,"B",C["red"])
    Cc=(ox+x2*scale,oy-y1*scale)
    cv.line(*A,*Cc,color=C["green"],w=1.5,dash="4 3");cv.line(*Cc,*B,color=C["amber"],w=1.5,dash="4 3");cv.line(*A,*B,color=C["blue"],w=1.8)
    cv.text((A[0]+Cc[0])/2,A[1]+18,"4",size=9,color=C["green"],weight=700)
    cv.text(Cc[0]+10,(Cc[1]+B[1])/2,"3",size=9,color=C["amber"],weight=700)
    _card(cv,230,64,184,38,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(322,88,"d=sqrt((dx)^2+(dy)^2)",size=9,weight=700,color=C["purple"])
    _card(cv,250,120,144,34,C["green"],C["green_bg"],sw=1.5)
    cv.text(322,142,"d=sqrt(4²+3²)=5",size=9.5,weight=700,color=C["green"])
    cv.text(W/2,H-8,"horizontal and vertical changes make a right triangle",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── midpoint ────────────────────────────────────
def midpoint(spec):
    W,H=452,250;ox,oy,scale=226,136,25
    cv=Canvas(W,H,seed=_seed(spec,4103))
    cv.text(W/2,20,"midpoint averages x-coordinates and y-coordinates separately",size=9.6,weight=700,color=C["soft"])
    _axes(cv,ox,oy,scale,xmin=-4,xmax=4,ymin=-3,ymax=3)
    A=_point(cv,ox,oy,scale,-3,2,"A",C["blue"]);B=_point(cv,ox,oy,scale,3,-2,"B",C["green"])
    M=_point(cv,ox,oy,scale,0,0,"M",C["red"])
    cv.line(*A,*B,color=C["purple"],w=1.5,dash="4 3")
    _card(cv,56,204,340,26,C["purple"],C["purple_bg"],sw=1.4)
    cv.text(226,222,"M=((x1+x2)/2,(y1+y2)/2) = (0,0)",size=8.9,weight=700,color=C["purple"])
    return cv.svg()


# ───────────────────────────── section formula ──────────────────────────────
def section_formula(spec):
    m,n=2,3;A=(1,1);B=(6,6);P=((n*A[0]+m*B[0])/(m+n),(n*A[1]+m*B[1])/(m+n))
    W,H=452,238;ox,oy,scale=50,174,28
    cv=Canvas(W,H,seed=_seed(spec,4104))
    cv.text(W/2,20,"internal division: P divides AB in the ratio m:n",size=9.8,weight=700,color=C["soft"])
    ax,ay=ox+A[0]*scale,oy-A[1]*scale;bx,by=ox+B[0]*scale,oy-B[1]*scale;px,py=ox+P[0]*scale,oy-P[1]*scale
    cv.line(ax,ay,bx,by,color=C["blue"],w=1.8);cv.dot(ax,ay,r=4,color=C["blue"]);cv.dot(bx,by,r=4,color=C["green"]);cv.dot(px,py,r=4,color=C["red"])
    cv.text(ax-5,ay-10,"A",size=9,color=C["blue"],weight=700);cv.text(bx+7,by-8,"B",size=9,color=C["green"],weight=700);cv.text(px+7,py-8,"P",size=9,color=C["red"],weight=700)
    cv.text((ax+px)/2,(ay+py)/2-9,"m",size=9,color=C["red"],weight=700);cv.text((px+bx)/2,(py+by)/2-9,"n",size=9,color=C["red"],weight=700)
    _card(cv,222,58,196,42,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(320,80,"P=(nA+mB)/(m+n)",size=9.5,weight=700,color=C["purple"])
    cv.text(320,96,"ratio AP:PB = 2:3",size=8.4,color=C["soft"])
    cv.text(W/2,H-8,"the nearer endpoint receives the larger weight",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── slope ───────────────────────────────────────
def slope_coordinate(spec):
    W,H=452,260;ox,oy,scale=226,146,24
    cv=Canvas(W,H,seed=_seed(spec,4105))
    cv.text(W/2,20,"slope is rise divided by run",size=10.1,weight=700,color=C["soft"])
    _axes(cv,ox,oy,scale,xmin=-4,xmax=4,ymin=-4,ymax=4)
    A=_point(cv,ox,oy,scale,-2,-2,"A",C["blue"]);B=_point(cv,ox,oy,scale,2,2,"B",C["red"])
    Cc=(B[0],A[1]);cv.line(*A,*Cc,color=C["green"],w=1.4,dash="4 3");cv.line(*Cc,*B,color=C["amber"],w=1.4,dash="4 3");cv.line(*A,*B,color=C["blue"],w=1.8)
    cv.text((A[0]+Cc[0])/2,A[1]+18,"run 4",size=8.7,color=C["green"],weight=700)
    cv.text(Cc[0]+10,(Cc[1]+B[1])/2,"rise 4",size=8.7,color=C["amber"],weight=700)
    _card(cv,58,216,336,26,C["purple"],C["purple_bg"],sw=1.4)
    cv.text(226,234,"m=(y2-y1)/(x2-x1)=4/4=1",size=9.1,weight=700,color=C["purple"])
    return cv.svg()


# ───────────────────────────── collinearity ─────────────────────────────────
def collinear(spec):
    W,H=452,250;ox,oy,scale=50,184,32
    cv=Canvas(W,H,seed=_seed(spec,4106))
    cv.text(W/2,20,"three points are collinear when their slopes match",size=9.8,weight=700,color=C["soft"])
    pts=[(1,1),(3,3),(5,5)]; screen=[]
    for i,(x,y) in enumerate(pts):screen.append(_point(cv,ox,oy,scale,x,y,"ABC"[i],(C["blue"],C["green"],C["red"])[i]))
    cv.line(*screen[0],*screen[2],color=C["purple"],w=1.7)
    _card(cv,246,64,168,38,C["green"],C["green_bg"],sw=1.5)
    cv.text(330,87,"mAB = 1",size=9.5,weight=700,color=C["green"])
    _card(cv,246,118,168,38,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(330,141,"mBC = 1",size=9.5,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"equal slopes and a common point -> one straight line",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── triangle coordinate area ─────────────────────
def triangle_area_coordinate(spec):
    W,H=452,270;ox,oy,scale=70,206,28
    cv=Canvas(W,H,seed=_seed(spec,4107))
    cv.text(W/2,20,"coordinate determinant gives triangle area directly",size=9.8,weight=700,color=C["soft"])
    _axes(cv,ox,oy,scale,xmin=-1,xmax=8,ymin=-2,ymax=6)
    coords=[(1,1),(6,1),(2,5)];scr=[]
    for i,(x,y) in enumerate(coords):scr.append(_point(cv,ox,oy,scale,x,y,"ABC"[i],(C["blue"],C["green"],C["red"])[i]))
    cv.polygon(scr,color=C["purple"],w=1.6,fill=None)
    area=abs(coords[0][0]*(coords[1][1]-coords[2][1])+coords[1][0]*(coords[2][1]-coords[0][1])+coords[2][0]*(coords[0][1]-coords[1][1]))/2
    _card(cv,248,56,166,54,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(331,78,"A=1/2|x1(y2-y3)",size=8.2,weight=700,color=C["purple"])
    cv.text(331,96,f"+... = {_fmt(area)}",size=9.4,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"absolute value removes clockwise/anticlockwise sign",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── line relations ───────────────────────────────
def line_parallel(spec):
    W,H=452,258;ox,oy,scale=226,130,24
    cv=Canvas(W,H,seed=_seed(spec,4108))
    cv.text(W/2,20,"slopes identify parallel and perpendicular lines",size=9.9,weight=700,color=C["soft"])
    _axes(cv,ox,oy,scale,xmin=-4,xmax=4,ymin=-4,ymax=4)
    # y=x+1 and y=x-2 parallel
    cv.line(ox-4*scale,oy-3*scale,ox+3*scale,oy+4*scale,color=C["blue"],w=1.7)
    cv.line(ox-3*scale,oy-5*scale,ox+4*scale,oy+2*scale,color=C["green"],w=1.7)
    _card(cv,54,202,150,30,C["blue"],C["blue_bg"],sw=1.3)
    cv.text(129,222,"m1=1",size=9.5,weight=700,color=C["blue"])
    _card(cv,248,202,150,30,C["green"],C["green_bg"],sw=1.3)
    cv.text(323,222,"m2=1 -> parallel",size=8.8,weight=700,color=C["green"])
    return cv.svg()


# ───────────────────────────── reflection ───────────────────────────────────
def reflection(spec):
    W,H=452,254;ox,oy,scale=226,128,26
    cv=Canvas(W,H,seed=_seed(spec,4109))
    cv.text(W/2,20,"reflection changes the sign of the coordinate across an axis",size=9.8,weight=700,color=C["soft"])
    _axes(cv,ox,oy,scale,xmin=-4,xmax=4,ymin=-3,ymax=3)
    A=_point(cv,ox,oy,scale,2,1,"A",C["blue"]);B=_point(cv,ox,oy,scale,2,-1,"A'",C["red"])
    cv.line(*A,*B,color=C["purple"],w=1.2,dash="4 3")
    cv.text(330,60,"x-axis reflection",size=9,color=C["purple"],weight=700)
    cv.text(330,78,"(x,y) -> (x,-y)",size=9,color=C["red"],weight=700)
    _card(cv,62,210,328,26,C["green"],C["green_bg"],sw=1.4)
    cv.text(226,228,"y-axis: (x,y)->(-x,y); origin: (-x,-y)",size=8.7,weight=700,color=C["green"])
    return cv.svg()


# ───────────────────────────── coordinate shape ─────────────────────────────
def coordinate_shape(spec):
    W,H=452,258;ox,oy,scale=80,204,26
    cv=Canvas(W,H,seed=_seed(spec,4110))
    cv.text(W/2,20,"coordinates can reveal side lengths, slopes and area",size=9.8,weight=700,color=C["soft"])
    _axes(cv,ox,oy,scale,xmin=-1,xmax=8,ymin=-1,ymax=6)
    coords=[(1,1),(6,1),(6,4),(1,4)];pts=[]
    for i,(x,y) in enumerate(coords):pts.append(_point(cv,ox,oy,scale,x,y,"ABCD"[i],C["blue"]))
    cv.polygon(pts,color=C["purple"],w=1.7,fill=C["blue_bg"])
    cv.text(ox+3.5*scale,oy+18,"5 units",size=8.7,color=C["purple"],weight=700)
    cv.text(ox-12,oy-2.5*scale,"3 units",size=8.7,color=C["purple"],anchor="end",weight=700)
    _card(cv,284,58,132,34,C["green"],C["green_bg"],sw=1.4)
    cv.text(350,80,"area = 15",size=9.5,weight=700,color=C["green"])
    _card(cv,284,108,132,34,C["purple"],C["purple_bg"],sw=1.4)
    cv.text(350,130,"perimeter = 16",size=9.2,weight=700,color=C["purple"])
    return cv.svg()


REGISTRY={
    "coordinate-plane41":coordinate_plane41,
    "distance-formula":distance_formula,
    "midpoint":midpoint,
    "section-formula":section_formula,
    "slope-coordinate":slope_coordinate,
    "collinear":collinear,
    "triangle-area-coordinate":triangle_area_coordinate,
    "line-parallel":line_parallel,
    "reflection":reflection,
    "coordinate-shape":coordinate_shape,
}
