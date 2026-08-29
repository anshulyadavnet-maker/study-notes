"""
prisms_pyramids.py — visual figures for Chapter 40.

prism-general       : prism volume and surface structure
triangular-prism    : triangular base extruded along a length
square-pyramid      : square base, apex, height and slant height
triangular-pyramid  : triangular-base pyramid
cone-frustum        : conical frustum with two radii
frustum-slant       : slant-height right triangle of a frustum
prism-area          : base area x prism height
pyramid-net         : square pyramid net and faces
square-frustum      : truncated square pyramid
solid-comparison40  : prism versus pyramid with same base and height
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=4000):
    value=spec.get("seed",default)
    try:return int(value)
    except Exception:return sum(ord(ch) for ch in str(value))


def _card(cv,x,y,w,h,col,bg,r=6,sw=1.4):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _fmt(v):
    v=float(v)
    if abs(v-round(v))<1e-9:return str(int(round(v)))
    return f"{v:.2f}".rstrip("0").rstrip(".")


def prism_general(spec):
    base_area=float(spec.get("base_area",24)); base_perim=float(spec.get("base_perimeter",20)); h=float(spec.get("height",10))
    W,H=452,260
    cv=Canvas(W,H,seed=_seed(spec,4001))
    cv.text(W/2,20,"a prism repeats the same base along a height",size=10,weight=700,color=C["soft"])
    ox,oy,w_,hh,d=48,80,175,88,42
    front=[(ox,oy+d),(ox+w_,oy+d),(ox+w_,oy+d+hh),(ox,oy+d+hh)]
    top=[(ox,oy+d),(ox+d,oy),(ox+w_+d,oy),(ox+w_,oy+d)]
    side=[(ox+w_,oy+d),(ox+w_+d,oy),(ox+w_+d,oy+hh),(ox+w_,oy+d+hh)]
    cv.polygon(front,color=C["blue"],w=1.7,fill=C["blue_bg"])
    cv.polygon(top,color=C["green"],w=1.5,fill=C["green_bg"])
    cv.polygon(side,color=C["amber"],w=1.5,fill=C["amber_bg"])
    cv.line(ox+w_/2,oy+d,ox+w_/2,oy+d+hh,color=C["red"],w=1.2,dash="4 3")
    cv.text(ox+w_/2,oy+d+hh+20,f"prism height={_fmt(h)}",size=8.8,color=C["red"],weight=700)
    rows=[("volume",base_area*h,C["green"]),("LSA",base_perim*h,C["blue"]),("TSA",base_perim*h+2*base_area,C["purple"])]
    for i,(lab,val,col) in enumerate(rows):
        yy=58+i*42
        _card(cv,294,yy,126,30,col,"#ffffff",r=5,sw=1.2)
        cv.text(306,yy+20,lab,size=8.4,anchor="start",color=C["soft"])
        cv.text(408,yy+20,_fmt(val),size=9,anchor="end",weight=700,color=col)
    cv.text(W/2,H-8,"V=base area x height; LSA=base perimeter x height",size=8.7,color=C["ink"])
    return cv.svg()


def triangular_prism(spec):
    b=float(spec.get("base",6)); h=float(spec.get("base_height",4)); length=float(spec.get("length",10))
    base_area=b*h/2; base_perim=b+math.hypot(b/2,h)*2
    W,H=452,270
    cv=Canvas(W,H,seed=_seed(spec,4002))
    cv.text(W/2,20,"triangular prism: triangular base repeated along length",size=9.8,weight=700,color=C["soft"])
    x,y,tw,hh,d=52,72,120,98,150
    front=[(x,y+d),(x+tw,y+d),(x+tw*.48,y+d-hh)]
    back=[(p[0]+d,p[1]-18) for p in front]
    cv.polygon(front,color=C["blue"],w=1.7,fill=C["blue_bg"])
    cv.polygon(back,color=C["green"],w=1.5,fill=C["green_bg"])
    for p,q in zip(front,back):cv.line(*p,*q,color=C["amber"],w=1.5)
    cv.line(front[2][0],front[2][1],front[2][0],front[0][1],color=C["red"],w=1.1,dash="4 3")
    cv.text(100,205,f"base area=1/2 x {_fmt(b)} x {_fmt(h)}={_fmt(base_area)}",size=8.8,color=C["purple"],weight=700)
    _card(cv,282,64,136,34,C["green"],C["green_bg"],sw=1.5)
    cv.text(350,86,f"V={_fmt(base_area*length)}",size=10,weight=700,color=C["green"])
    _card(cv,282,114,136,34,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(350,136,f"LSA={_fmt(base_perim*length)}",size=9,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"two congruent triangular ends + three rectangular faces",size=8.6,color=C["ink"])
    return cv.svg()


def square_pyramid(spec):
    a=float(spec.get("side",8)); h=float(spec.get("height",12)); l=math.sqrt(h*h+(a/2)**2)
    W,H=452,280; cx,by=132,194; bw=140; bd=42
    cv=Canvas(W,H,seed=_seed(spec,4003))
    cv.text(W/2,20,"square pyramid: apex over the centre of a square base",size=9.8,weight=700,color=C["soft"])
    base=[(cx-bw/2,by),(cx+bw/2,by),(cx+bw/2+bd,by-bd),(cx-bw/2+bd,by-bd)]
    apex=(cx+bd/2,42)
    cv.polygon(base,color=C["blue"],w=1.7,fill=C["blue_bg"])
    for p in base:cv.line(*apex,*p,color=C["green"],w=1.5)
    cv.line(apex[0],apex[1],cx+bd/2,by-bd/2,color=C["red"],w=1.2,dash="4 3")
    cv.text(cx,by+20,f"square side={_fmt(a)}",size=9.3,color=C["purple"],weight=700)
    cv.text(cx+bd/2+9,(apex[1]+by-bd/2)/2,f"h={_fmt(h)}",size=9,color=C["red"],weight=700)
    cv.text(cx+bw/2+bd+12,(apex[1]+by)/2,f"l={_fmt(l)}",size=9,color=C["green"],weight=700)
    _card(cv,278,64,140,36,C["green"],C["green_bg"],sw=1.5)
    cv.text(348,87,f"V=1/3 a²h",size=9.5,weight=700,color=C["green"])
    _card(cv,278,116,140,36,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(348,139,f"LSA=2al",size=9.5,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"l²=h²+(a/2)² for a square pyramid face",size=8.6,color=C["ink"])
    return cv.svg()


def triangular_pyramid(spec):
    b=float(spec.get("base",6)); bh=float(spec.get("base_height",4)); h=float(spec.get("height",9))
    base_area=b*bh/2; volume=base_area*h/3
    W,H=452,270; cv=Canvas(W,H,seed=_seed(spec,4004))
    cv.text(W/2,20,"triangular pyramid: one apex joined to a triangular base",size=9.8,weight=700,color=C["soft"])
    base=[(58,190),(230,190),(130,92)]; apex=(190,42)
    cv.polygon(base,color=C["blue"],w=1.7,fill=C["blue_bg"])
    for p in base:cv.line(*apex,*p,color=C["green"],w=1.5)
    cv.line(apex[0],apex[1],130,190,color=C["red"],w=1.2,dash="4 3")
    cv.text(124,211,f"base area={_fmt(base_area)}",size=9,color=C["purple"],weight=700)
    _card(cv,282,68,136,36,C["green"],C["green_bg"],sw=1.5)
    cv.text(350,91,f"V=1/3 Bh={_fmt(volume)}",size=8.8,weight=700,color=C["green"])
    _card(cv,282,122,136,36,C["red"],C["red_bg"],sw=1.5)
    cv.text(350,145,f"height={_fmt(h)}",size=9,weight=700,color=C["red"])
    cv.text(W/2,H-8,"any pyramid volume = one-third base area x perpendicular height",size=8.5,color=C["ink"])
    return cv.svg()


def cone_frustum(spec):
    R=float(spec.get("R",7)); r=float(spec.get("r",3)); h=float(spec.get("height",8)); l=math.sqrt(h*h+(R-r)**2)
    W,H=452,274; cx,top,rx1,ry=130,54,42,14; rx2=82; bot=top+h*9
    cv=Canvas(W,H,seed=_seed(spec,4005))
    cv.text(W/2,20,"frustum: a cone cut parallel to its base",size=10,weight=700,color=C["soft"])
    cv.raw(f'<path d="M{cx-rx1},{top} L{cx-rx2},{bot} A{rx2},{ry} 0 0 0 {cx+rx2},{bot} L{cx+rx1},{top} Z" fill="{C["blue_bg"]}" stroke="none"/>')
    cv.ellipse(cx,top,rx1,ry,color=C["blue"],w=1.6,fill=C["paper"])
    cv.ellipse(cx,bot,rx2,ry,color=C["blue"],w=1.6,fill=None)
    cv.line(cx-rx1,top,cx-rx2,bot,color=C["blue"],w=1.7);cv.line(cx+rx1,top,cx+rx2,bot,color=C["blue"],w=1.7)
    cv.line(cx,top,cx,bot,color=C["red"],w=1.2,dash="4 3")
    cv.text(cx+rx1/2,top-8,f"r={_fmt(r)}",size=9,color=C["green"],weight=700)
    cv.text(cx+rx2/2,bot+22,f"R={_fmt(R)}",size=9,color=C["purple"],weight=700)
    cv.text(cx+8,(top+bot)/2,f"h={_fmt(h)}",size=9,color=C["red"],weight=700)
    cv.text(cx+55,(top+bot)/2-13,f"l={_fmt(l)}",size=9,color=C["amber"],weight=700)
    _card(cv,280,62,140,38,C["green"],C["green_bg"],sw=1.5)
    cv.text(350,86,"V=1/3πh(R²+r²+Rr)",size=8.5,weight=700,color=C["green"])
    _card(cv,280,118,140,38,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(350,142,"CSA=π(R+r)l",size=9,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"l²=h²+(R−r)²",size=8.8,color=C["ink"])
    return cv.svg()


def frustum_slant(spec):
    R=float(spec.get("R",7)); r=float(spec.get("r",3)); h=float(spec.get("height",8)); diff=R-r; l=math.sqrt(h*h+diff*diff)
    W,H=452,230; cv=Canvas(W,H,seed=_seed(spec,4006))
    cv.text(W/2,20,"frustum slant height comes from a right triangle",size=10,weight=700,color=C["soft"])
    p=[(62,178),(62,72),(190,178)]
    cv.polygon(p,color=C["blue"],w=1.7,fill=C["blue_bg"])
    cv.right_angle(62,178,(82,178),(62,72),size=11,color=C["red"])
    cv.text(48,126,f"h={_fmt(h)}",size=9.5,color=C["red"],anchor="end",weight=700)
    cv.text(126,194,f"R-r={_fmt(diff)}",size=9.5,color=C["green"],weight=700)
    cv.text(136,116,f"l={_fmt(l)}",size=10,color=C["purple"],weight=700)
    _card(cv,240,72,166,44,C["purple"],C["purple_bg"],sw=1.6)
    cv.text(323,98,"l²=h²+(R-r)²",size=10,weight=700,color=C["purple"])
    _card(cv,260,140,126,32,C["green"],C["green_bg"],sw=1.5)
    cv.text(323,161,f"l={_fmt(l)}",size=10,weight=700,color=C["green"])
    cv.text(W/2,H-8,"use the difference of radii, not their sum, for a frustum",size=8.6,color=C["ink"])
    return cv.svg()


def prism_area(spec):
    B=float(spec.get("base_area",24)); h=float(spec.get("height",10)); V=B*h
    W,H=452,240; cv=Canvas(W,H,seed=_seed(spec,4007))
    cv.text(W/2,20,"every prism uses the same base-area x height rule",size=10,weight=700,color=C["soft"])
    cv.rect(48,64,150,110,color=C["blue"],w=1.7,fill=C["blue_bg"])
    cv.text(123,120,"base",size=12,weight=700,color=C["blue"])
    cv.arrow(215,120,270,120,color=C["grey"],w=1.3)
    _card(cv,286,56,132,36,C["green"],C["green_bg"],sw=1.5)
    cv.text(352,79,f"B={_fmt(B)}",size=10,weight=700,color=C["green"])
    _card(cv,286,106,132,36,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(352,129,f"h={_fmt(h)}",size=10,weight=700,color=C["purple"])
    _card(cv,286,156,132,36,C["red"],C["red_bg"],sw=1.5)
    cv.text(352,179,f"V={_fmt(V)}",size=10,weight=700,color=C["red"])
    cv.text(W/2,H-8,"base can be triangular, rectangular or any fixed polygon",size=8.7,color=C["ink"])
    return cv.svg()


def pyramid_net(spec):
    W,H=320,240; cv=Canvas(W,H,seed=_seed(spec,4008))
    cv.text(W/2,20,"a square pyramid net has one square and four triangular faces",size=9.6,weight=700,color=C["soft"])
    cx,cy,s=150,112,72
    base=[(cx-s/2,cy-s/2),(cx+s/2,cy-s/2),(cx+s/2,cy+s/2),(cx-s/2,cy+s/2)]
    cv.polygon(base,color=C["blue"],w=1.7,fill=C["blue_bg"])
    tris=[([(base[0][0],base[0][1]),(base[1][0],base[1][1]),(cx,cy-s/2-58)],C["green"]),
          ([(base[1][0],base[1][1]),(base[2][0],base[2][1]),(cx+s/2+58,cy)],C["amber"]),
          ([(base[2][0],base[2][1]),(base[3][0],base[3][1]),(cx,cy+s/2+58)],C["purple"]),
          ([(base[3][0],base[3][1]),(base[0][0],base[0][1]),(cx-s/2-58,cy)],C["red"])]
    for p,col in tris:cv.polygon(p,color=col,w=1.5,fill=None)
    cv.text(cx,cy+5,"base",size=9.5,weight=700,color=C["blue"])
    cv.text(W/2,H-8,"net folds along the four base edges",size=8.7,color=C["ink"])
    return cv.svg()


def square_frustum(spec):
    a=float(spec.get("bottom",10)); b=float(spec.get("top",4)); h=float(spec.get("height",6));
    W,H=452,260; cv=Canvas(W,H,seed=_seed(spec,4009))
    cv.text(W/2,20,"square frustum: two parallel square bases and four trapezoid faces",size=9.5,weight=700,color=C["soft"])
    cx,by,s1,s2,hh=130,192,150,78,105
    bottom=[(cx-s1/2,by),(cx+s1/2,by),(cx+s1/2+38,by-32),(cx-s1/2+38,by-32)]
    top=[(cx-s2/2+38,by-hh),(cx+s2/2+38,by-hh),(cx+s2/2+38+26,by-hh-22),(cx-s2/2+38+26,by-hh-22)]
    # simplified perspective: show lower and upper loops connected
    cv.polygon(bottom,color=C["blue"],w=1.7,fill=C["blue_bg"])
    cv.polygon(top,color=C["green"],w=1.5,fill=C["green_bg"])
    for p,q in zip(bottom,top):cv.line(*p,*q,color=C["amber"],w=1.5)
    cv.text(cx,by+20,f"bottom side={_fmt(a)}",size=8.9,color=C["blue"],weight=700)
    cv.text(cx+55,by-hh-31,f"top side={_fmt(b)}",size=8.9,color=C["green"],weight=700)
    cv.text(290,120,f"h={_fmt(h)}",size=9.2,color=C["red"],weight=700)
    _card(cv,270,164,144,34,C["purple"],C["purple_bg"],sw=1.5)
    cv.text(342,186,"V = h/3(B1+B2+sqrt(B1B2))",size=7.9,weight=700,color=C["purple"])
    return cv.svg()


def solid_comparison40(spec):
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4010))
    cv.text(W/2,20,"same base and height: pyramid volume is one-third of prism",size=9.8,weight=700,color=C["soft"])
    _card(cv,38,52,174,82,C["blue"],C["blue_bg"],sw=1.6)
    cv.text(125,74,"prism",size=11,weight=700,color=C["blue"])
    cv.text(125,98,"V = B x h",size=10,color=C["blue"])
    cv.text(125,119,"3 equal parts",size=9,color=C["blue"])
    _card(cv,240,52,174,82,C["green"],C["green_bg"],sw=1.6)
    cv.text(327,74,"pyramid",size=11,weight=700,color=C["green"])
    cv.text(327,98,"V = 1/3 B x h",size=10,color=C["green"])
    cv.text(327,119,"1 of 3 parts",size=9,color=C["green"])
    _card(cv,70,166,312,32,C["purple"],C["purple_bg"],sw=1.6)
    cv.text(226,187,"same B and h -> V pyramid = V prism / 3",size=9.4,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"this relation is valid for any matching base and perpendicular height",size=8.4,color=C["ink"])
    return cv.svg()


REGISTRY={
    "prism-general":prism_general,
    "triangular-prism":triangular_prism,
    "square-pyramid":square_pyramid,
    "triangular-pyramid":triangular_pyramid,
    "cone-frustum":cone_frustum,
    "frustum-slant":frustum_slant,
    "prism-area":prism_area,
    "pyramid-net":pyramid_net,
    "square-frustum":square_frustum,
    "solid-comparison40":solid_comparison40,
}
