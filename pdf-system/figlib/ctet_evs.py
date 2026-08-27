"""
ctet_evs.py — figures for CTET Paper I Environmental Studies MCQs.

family-tree-evs   : family and relationships map
food-source-evs  : plant/animal food sources
food-chain-evs   : simple food-chain arrows
house-climate-evs: shelters adapted to climate
water-cycle-evs  : evaporation, condensation, precipitation and collection
water-filter-evs : simple filtration sequence
travel-map-evs   : route, direction and transport
materials-cycle-evs: daily material use and reuse
observation-evs  : observe, question, record and explain
integrated-evs   : family/food/water themes connect subjects
activity-evs     : EVS activity inquiry sequence
assessment-evs   : observation to feedback cycle
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=5300):
    value=spec.get("seed",default)
    try:return int(value)
    except Exception:return sum(ord(ch) for ch in str(value))


def _card(cv,x,y,w,h,col,bg,r=5,sw=1.3):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _fmt(v):
    v=float(v)
    if abs(v-round(v))<1e-9:return str(int(round(v)))
    return f"{v:.2f}".rstrip("0").rstrip(".")


def _arrow_row(cv,labels,colors=None,y=90):
    if colors is None:
        labels, colors = zip(*labels)
    xs=[48+i*(356/(len(labels)-1)) for i in range(len(labels))]
    for i,(lab,col) in enumerate(zip(labels,colors)):
        _card(cv,xs[i]-42,y-18,84,36,col,"#ffffff",sw=1.3);cv.text(xs[i],y+5,lab,size=8.5,weight=700,color=col)
        if i<len(labels)-1:cv.arrow(xs[i]+46,y,xs[i+1]-46,y,color=C["grey"],w=1.0)


# ───────────────────────────── family ──────────────────────────────────────
def family_tree(spec):
    W,H=452,230;cv=Canvas(W,H,seed=_seed(spec,5301));cv.text(W/2,20,"family and friends: relationships are explored through lived experience",size=9.5,weight=700,color=C["soft"])
    nodes=[("grandparents",226,58,C["purple"],C["purple_bg"]),("parents",150,116,C["blue"],C["blue_bg"]),("child",226,174,C["green"],C["green_bg"]),("siblings",302,174,C["amber"],C["amber_bg"])]
    for lab,x,y,col,bg in nodes:_card(cv,x-52,y-17,104,34,col,bg,sw=1.4);cv.text(x,y+5,lab,size=8.4,weight=700,color=col)
    cv.line(226,75,150,99,color=C["grey"],w=1.1);cv.line(226,75,226,99,color=C["grey"],w=1.1);cv.line(150,133,226,157,color=C["grey"],w=1.1);cv.line(150,133,302,157,color=C["grey"],w=1.1)
    cv.text(W/2,H-8,"relationships, roles and care can be discussed from children's contexts",size=8.5,color=C["ink"])
    return cv.svg()


# ───────────────────────────── food sources ─────────────────────────────────
def food_source(spec):
    W,H=452,230;cv=Canvas(W,H,seed=_seed(spec,5302));cv.text(W/2,20,"food comes from plants, animals and human processes",size=9.8,weight=700,color=C["soft"])
    _card(cv,42,58,128,54,C["green"],C["green_bg"],sw=1.5);cv.text(106,79,"plants",size=10,weight=700,color=C["green"]);cv.text(106,99,"rice, fruits, pulses",size=8,color=C["green"])
    _card(cv,188,58,128,54,C["blue"],C["blue_bg"],sw=1.5);cv.text(252,79,"animals",size=10,weight=700,color=C["blue"]);cv.text(252,99,"milk, eggs, honey",size=8,color=C["blue"])
    _card(cv,334,58,84,54,C["amber"],C["amber_bg"],sw=1.5);cv.text(376,79,"process",size=9,weight=700,color=C["amber"]);cv.text(376,99,"cook/store",size=8,color=C["amber"])
    cv.arrow(170,85,184,85,color=C["grey"],w=1.0);cv.arrow(316,85,330,85,color=C["grey"],w=1.0)
    _card(cv,84,154,284,32,C["purple"],C["purple_bg"],sw=1.5);cv.text(226,175,"food -> health, culture and daily life",size=9.2,weight=700,color=C["purple"])
    return cv.svg()


# ───────────────────────────── food chain ───────────────────────────────────
def food_chain(spec):
    W,H=452,210;cv=Canvas(W,H,seed=_seed(spec,5303));cv.text(W/2,20,"food chain shows transfer of food energy",size=10,weight=700,color=C["soft"])
    _arrow_row(cv,[("plant",C["green"]),("insect",C["amber"]),("frog",C["blue"]),("snake",C["purple"]),("eagle",C["red"])],y=94)
    _card(cv,82,146,284,28,C["green"],C["green_bg"],sw=1.4);cv.text(226,165,"producer -> consumers",size=9.5,weight=700,color=C["green"])
    cv.text(W/2,H-8,"removing one link can affect the whole chain",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── houses/climate ──────────────────────────────
def house_climate(spec):
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,5304));cv.text(W/2,20,"shelter reflects climate, materials and local needs",size=9.6,weight=700,color=C["soft"])
    for i,(lab,col,bg,roof) in enumerate((("snow",C["blue"],C["blue_bg"],"steep"),("rain",C["green"],C["green_bg"],"sloping"),("hot",C["amber"],C["amber_bg"],"ventilated"))):
        x=42+i*136;cv.raw(f'<path d="M{x+18},116 L{x+62},72 L{x+106},116 Z" fill="{bg}" stroke="{col}" stroke-width="1.5"/>');cv.raw(f'<rect x="{x+30}" y="116" width="64" height="44" fill="{bg}" stroke="{col}" stroke-width="1.5"/>');cv.text(x+62,180,lab,size=9,weight=700,color=col);cv.text(x+62,196,roof,size=7.7,color=col)
    cv.text(W/2,H-8,"compare design with environment, not as a memorised list only",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── water cycle ──────────────────────────────────
def water_cycle(spec):
    W,H=452,260;cv=Canvas(W,H,seed=_seed(spec,5305));cv.text(W/2,20,"water cycle: water changes form and moves through the environment",size=9.3,weight=700,color=C["soft"])
    nodes=[("evaporation",72,150,C["blue"],C["blue_bg"]),("condensation",226,64,C["purple"],C["purple_bg"]),("precipitation",380,150,C["green"],C["green_bg"]),("collection",226,214,C["amber"],C["amber_bg"])]
    for lab,x,y,col,bg in nodes:_card(cv,x-58,y-17,116,34,col,bg,sw=1.4);cv.text(x,y+5,lab,size=8.2,weight=700,color=col)
    for (x1,y1),(x2,y2),col in (((130,136),(168,82),C["blue"]),((284,82),(322,136),C["purple"]),((380,167),(280,207),C["green"]),((168,207),(110,167),C["amber"])):cv.arrow(x1,y1,x2,y2,color=col,w=1.1)
    cv.text(W/2,184,"sun + heat",size=8.5,color=C["red"],weight=700)
    return cv.svg()


# ───────────────────────────── water filter ─────────────────────────────────
def water_filter(spec):
    W,H=452,230;cv=Canvas(W,H,seed=_seed(spec,5306));cv.text(W/2,20,"separation and filtration can make visibly dirty water clearer",size=9.4,weight=700,color=C["soft"])
    _arrow_row(cv,[("dirty water",C["red"]),("cloth",C["amber"]),("sand/gravel",C["blue"]),("filtered",C["green"])],y=94)
    _card(cv,88,150,276,30,C["purple"],C["purple_bg"],sw=1.5);cv.text(226,170,"observe change; filtration is not disinfection",size=8.9,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"activity must include safe handling and discussion",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── travel map ──────────────────────────────────
def travel_map(spec):
    W,H=452,240;cv=Canvas(W,H,seed=_seed(spec,5307));cv.text(W/2,20,"travel: route, direction, distance and transport are connected",size=9.7,weight=700,color=C["soft"])
    cv.line(54,174,380,64,color=C["blue"],w=2);cv.line(54,174,208,174,color=C["green"],w=1.4,dash="4 3");cv.line(208,174,380,64,color=C["green"],w=1.4,dash="4 3")
    for x,y,lab,col in ((54,174,"home",C["red"]),(208,174,"market",C["amber"]),(380,64,"school",C["purple"])):cv.dot(x,y,r=4,color=col);cv.text(x,y+18 if y>100 else y-10,lab,size=8.8,weight=700,color=col)
    _card(cv,72,48,154,34,C["green"],C["green_bg"],sw=1.4);cv.text(149,70,"map: route + direction",size=9,weight=700,color=C["green"])
    cv.text(W/2,H-8,"children can map familiar journeys and compare routes",size=8.6,color=C["ink"])
    return cv.svg()


# ───────────────────────────── materials cycle ──────────────────────────────
def materials_cycle(spec):
    W,H=452,230;cv=Canvas(W,H,seed=_seed(spec,5308));cv.text(W/2,20,"things we make and do: material use can be traced through its life",size=9.5,weight=700,color=C["soft"])
    _arrow_row(cv,[("material",C["blue"]),("object",C["green"]),("use",C["amber"]),("reuse/recycle",C["purple"])],y=92)
    _card(cv,82,148,284,30,C["red"],C["red_bg"],sw=1.5);cv.text(226,168,"reduce waste; ask who made it and how",size=9,weight=700,color=C["red"])
    return cv.svg()


# ───────────────────────────── observation ──────────────────────────────────
def observation_evs(spec):
    W,H=452,230;cv=Canvas(W,H,seed=_seed(spec,5309));cv.text(W/2,20,"EVS learning begins with looking closely and asking questions",size=9.8,weight=700,color=C["soft"])
    _arrow_row(cv,[("observe",C["blue"]),("question",C["green"]),("record",C["amber"]),("explain",C["purple"])],y=94)
    _card(cv,88,150,276,30,C["red"],C["red_bg"],sw=1.5);cv.text(226,170,"experience -> evidence -> discussion",size=9.1,weight=700,color=C["red"])
    return cv.svg()


# ───────────────────────────── integrated EVS ───────────────────────────────
def integrated_evs(spec):
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,5310));cv.text(W/2,20,"one EVS theme can connect science, society, language and mathematics",size=9.1,weight=700,color=C["soft"])
    _card(cv,164,48,124,36,C["green"],C["green_bg"],sw=1.5);cv.text(226,71,"water",size=11,weight=700,color=C["green"])
    items=[("science",72,132,C["blue"]),("society",178,174,C["purple"]),("language",274,174,C["amber"]),("maths",380,132,C["red"])]
    for lab,x,y,col in items:_card(cv,x-42,y-16,84,32,col,"#ffffff",sw=1.2);cv.text(x,y+5,lab,size=8.5,weight=700,color=col);cv.line(226,84,x,y-18,color=C["grey"],w=1.0)
    cv.text(W/2,H-8,"integrated EVS starts from a meaningful theme, not isolated facts",size=8.5,color=C["ink"])
    return cv.svg()


# ───────────────────────────── activity sequence ────────────────────────────
def activity_evs(spec):
    W,H=452,230;cv=Canvas(W,H,seed=_seed(spec,5311));cv.text(W/2,20,"EVS activity: children investigate, share evidence and reflect",size=9.7,weight=700,color=C["soft"])
    _arrow_row(cv,[("question",C["red"]),("explore",C["blue"]),("discuss",C["green"]),("reflect",C["purple"])],y=92)
    _card(cv,84,150,284,30,C["amber"],C["amber_bg"],sw=1.5);cv.text(226,170,"teacher guides; children actively participate",size=9.1,weight=700,color=C["amber"])
    return cv.svg()


# ───────────────────────────── assessment cycle ─────────────────────────────
def assessment_evs(spec):
    W,H=452,230;cv=Canvas(W,H,seed=_seed(spec,5312));cv.text(W/2,20,"EVS assessment uses observation, conversation and work samples",size=9.5,weight=700,color=C["soft"])
    _arrow_row(cv,[("observe",C["blue"]),("record",C["green"]),("feedback",C["amber"]),("support",C["purple"])],y=92)
    _card(cv,82,150,288,30,C["red"],C["red_bg"],sw=1.5);cv.text(226,170,"assessment improves the next learning experience",size=8.9,weight=700,color=C["red"])
    return cv.svg()


REGISTRY={
    "family-tree-evs":family_tree,
    "food-source-evs":food_source,
    "food-chain-evs":food_chain,
    "house-climate-evs":house_climate,
    "water-cycle-evs":water_cycle,
    "water-filter-evs":water_filter,
    "travel-map-evs":travel_map,
    "materials-cycle-evs":materials_cycle,
    "observation-evs":observation_evs,
    "integrated-evs":integrated_evs,
    "activity-evs":activity_evs,
    "assessment-evs":assessment_evs,
}
