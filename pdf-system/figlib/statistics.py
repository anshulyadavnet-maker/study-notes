"""
statistics.py — visual figures for Chapter 45 (Statistics).

data-table       : observations and frequencies
mean-bars        : weighted mean as total value / total frequency
median-position  : ordered data and median position
mode-bar         : highest-frequency mode
histogram        : continuous class intervals with touching bars
frequency-polygon: midpoints joined by straight segments
bar-chart        : discrete categories with separated bars
pie-chart        : sector angles from category frequencies
ogive            : cumulative-frequency curve
missing-frequency: solve a missing frequency from a known mean
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=4500):
    value=spec.get("seed",default)
    try:return int(value)
    except Exception:return sum(ord(ch) for ch in str(value))


def _card(cv,x,y,w,h,col,bg,r=5,sw=1.3):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _fmt(v):
    v=float(v)
    if abs(v-round(v))<1e-9:return str(int(round(v)))
    return f"{v:.2f}".rstrip("0").rstrip(".")


# ───────────────────────────── data table ───────────────────────────────────
def data_table(spec):
    values=[10,20,30,40,50];freq=[2,5,8,4,1];total=sum(freq);s=sum(v*f for v,f in zip(values,freq))
    W,H=452,248;cv=Canvas(W,H,seed=_seed(spec,4501))
    cv.text(W/2,20,"frequency table compresses repeated observations",size=10,weight=700,color=C["soft"])
    x0,y0,cw=48,52,118
    for j,(lab,col,bg) in enumerate((("value x",C["blue"],C["blue_bg"]),("frequency f",C["green"],C["green_bg"]),("product xf",C["purple"],C["purple_bg"]))):
        _card(cv,x0+j*cw,y0,cw-5,28,col,bg,r=4,sw=1.2);cv.text(x0+j*cw+(cw-5)/2,y0+19,lab,size=8.8,weight=700,color=col)
    for i,(v,f) in enumerate(zip(values,freq)):
        y=y0+34+i*26
        for j,val in enumerate((v,f,v*f)):
            col=(C["blue"],C["green"],C["purple"])[j]
            _card(cv,x0+j*cw,y,cw-5,22,col,"#ffffff",r=3,sw=1.0);cv.text(x0+j*cw+(cw-5)/2,y+15,str(val),size=8.8,color=col,weight=700 if j==2 else 400)
    _card(cv,56,218,340,24,C["amber"],C["amber_bg"],sw=1.4)
    cv.text(226,235,f"sum f = {total}; sum xf = {s}; mean = {s}/{total}",size=8.7,weight=700,color=C["amber"])
    return cv.svg()


# ───────────────────────────── mean bars ────────────────────────────────────
def mean_bars(spec):
    values=[10,20,30,40];freq=[1,2,4,1];total=sum(freq);mean=sum(v*f for v,f in zip(values,freq))/total
    W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4502))
    cv.text(W/2,20,"mean is the balance point: total value divided by total count",size=9.8,weight=700,color=C["soft"])
    x0,y0,bw,scale=44,180,34,3.2
    for i,(v,f) in enumerate(zip(values,freq)):
        x=x0+i*90
        for j in range(f):
            yy=y0-j*18
            cv.raw(f'<rect x="{x}" y="{yy-14}" width="{bw}" height="14" fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1"/>')
        cv.text(x+bw/2,y0+18,str(v),size=8.8,weight=700,color=C["blue"])
        cv.text(x+bw/2,y0-f*18-20,f"f={f}",size=8.2,color=C["soft"])
    mx=x0+mean*scale
    cv.line(mx,52,mx,y0+5,color=C["red"],w=1.6,dash="4 3")
    cv.text(mx,42,f"mean={_fmt(mean)}",size=9.2,weight=700,color=C["red"])
    _card(cv,56,54,340,30,C["purple"],C["purple_bg"],sw=1.5);cv.text(226,75,"mean = sum(value x frequency) / sum frequency",size=9.1,weight=700,color=C["purple"])
    return cv.svg()


# ───────────────────────────── median position ─────────────────────────────
def median_position(spec):
    data=[3,5,6,8,10,12,15,18,20];n=len(data);median=data[n//2]
    W,H=452,210;cv=Canvas(W,H,seed=_seed(spec,4503))
    cv.text(W/2,20,"sort first; the middle observation is the median",size=10.2,weight=700,color=C["soft"])
    x0,y=38,100;gap=42
    for i,v in enumerate(data):
        x=x0+i*gap;col=C["red"] if i==n//2 else C["blue"]
        _card(cv,x,y,34,34,col,C["red_bg"] if i==n//2 else C["blue_bg"],r=5,sw=1.3);cv.text(x+17,y+22,str(v),size=9,weight=700,color=col);cv.text(x+17,y+52,str(i+1),size=7.8,color=C["soft"])
    _card(cv,78,164,296,26,C["purple"],C["purple_bg"],sw=1.4);cv.text(226,182,"n=9 -> position (n+1)/2 = 5 -> median=10",size=8.8,weight=700,color=C["purple"])
    return cv.svg()


# ───────────────────────────── mode bar ─────────────────────────────────────
def mode_bar(spec):
    values=[10,20,30,40,50];freq=[3,6,12,5,2];W,H=452,250;cv=Canvas(W,H,seed=_seed(spec,4504))
    cv.text(W/2,20,"mode is the observation with the highest frequency",size=10.1,weight=700,color=C["soft"])
    x0,y0,bw,gap=42,190,48,24;scale=8
    for v,f in zip(values,freq):
        x=x0+values.index(v)*(bw+gap);hh=f*scale
        cv.raw(f'<rect x="{x}" y="{y0-hh}" width="{bw}" height="{hh}" fill="{C["red_bg"] if f==max(freq) else C["blue_bg"]}" stroke="{C["red"] if f==max(freq) else C["blue"]}" stroke-width="1.4"/>')
        cv.text(x+bw/2,y0+17,str(v),size=8.8,weight=700,color=C["soft"])
        cv.text(x+bw/2,y0-hh-8,str(f),size=8.5,weight=700,color=C["red"] if f==max(freq) else C["blue"])
    _card(cv,80,48,292,30,C["purple"],C["purple_bg"],sw=1.5);cv.text(226,69,"highest bar -> mode = 30",size=10,weight=700,color=C["purple"])
    return cv.svg()


# ───────────────────────────── histogram ───────────────────────────────────
def histogram(spec):
    classes=["0-10","10-20","20-30","30-40","40-50"];freq=[3,7,12,8,4];W,H=452,270;cv=Canvas(W,H,seed=_seed(spec,4505))
    cv.text(W/2,20,"histogram: continuous class intervals have touching bars",size=9.8,weight=700,color=C["soft"])
    x0,y0,bw,gap=46,202,62,0;scale=9
    for i,(cl,f) in enumerate(zip(classes,freq)):
        x=x0+i*bw;hh=f*scale
        cv.raw(f'<rect x="{x}" y="{y0-hh}" width="{bw}" height="{hh}" fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.2"/>')
        cv.text(x+bw/2,y0+18,cl,size=7.8,weight=700,color=C["soft"]);cv.text(x+bw/2,y0-hh-8,str(f),size=8.5,weight=700,color=C["blue"])
    cv.line(x0,y0,x0+len(classes)*bw,y0,color=C["ink"],w=1.2);cv.line(x0,y0-150,x0,y0,color=C["ink"],w=1.2)
    cv.text(24,70,"f",size=9,weight=700,color=C["ink"]);cv.text(W/2,H-8,"no gaps between bars; bar area represents frequency",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── frequency polygon ────────────────────────────
def frequency_polygon(spec):
    mids=[5,15,25,35,45];freq=[3,7,12,8,4];W,H=452,270;cv=Canvas(W,H,seed=_seed(spec,4506))
    cv.text(W/2,20,"frequency polygon joins class midpoints with straight lines",size=9.8,weight=700,color=C["soft"])
    x0,y0,sx,sy=42,204,7.1,9
    pts=[]
    for m,f in zip(mids,freq):
        p=(x0+m*sx,y0-f*sy);pts.append(p);cv.dot(*p,r=4,color=C["red"]);cv.text(p[0],p[1]-9,str(f),size=8.2,color=C["red"],weight=700)
    for p,q in zip(pts,pts[1:]):cv.line(*p,*q,color=C["blue"],w=1.8)
    cv.line(x0,y0,x0+50* sx,y0,color=C["ink"],w=1.2);cv.line(x0,y0-145,x0,y0,color=C["ink"],w=1.2)
    for m in mids:cv.text(x0+m*sx,y0+17,str(m),size=8,color=C["soft"])
    cv.text(W/2,H-8,"plot frequency at each class midpoint",size=8.8,color=C["ink"])
    return cv.svg()


# ───────────────────────────── bar chart ───────────────────────────────────
def bar_chart(spec):
    cats=["A","B","C","D"];vals=[12,8,15,10];W,H=452,252;cv=Canvas(W,H,seed=_seed(spec,4507))
    cv.text(W/2,20,"bar diagram: discrete categories have separated bars",size=10.1,weight=700,color=C["soft"])
    x0,y0,bw,gap=56,194,48,32;scale=8
    for i,(cat,val) in enumerate(zip(cats,vals)):
        x=x0+i*(bw+gap);hh=val*scale
        cv.raw(f'<rect x="{x}" y="{y0-hh}" width="{bw}" height="{hh}" fill="{C["green_bg"]}" stroke="{C["green"]}" stroke-width="1.3"/>')
        cv.text(x+bw/2,y0+17,cat,size=9,weight=700,color=C["soft"]);cv.text(x+bw/2,y0-hh-8,str(val),size=8.5,weight=700,color=C["green"])
    cv.line(x0,y0,x0+4*(bw+gap)-gap,y0,color=C["ink"],w=1.2);cv.line(x0,y0-145,x0,y0,color=C["ink"],w=1.2)
    cv.text(W/2,H-8,"gaps separate categories; bar width is not a class interval",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── pie chart ───────────────────────────────────
def pie_chart(spec):
    vals=[30,20,25,25];labels=["A","B","C","D"];colors=[C["blue"],C["green"],C["amber"],C["red"]];cx,cy,r=125,112,76;W,H=452,236;cv=Canvas(W,H,seed=_seed(spec,4508));cv.text(W/2,20,"pie chart: sector angle = frequency/total x 360 degrees",size=9.4,weight=700,color=C["soft"])
    start=-math.pi/2;total=sum(vals)
    for val,lab,col in zip(vals,labels,colors):
        end=start+2*math.pi*val/total;steps=10;arc=[(cx+r*math.cos(start+(end-start)*i/steps),cy+r*math.sin(start+(end-start)*i/steps)) for i in range(steps+1)]
        d=f"M{cx},{cy} L"+" L".join(f"{x:.1f},{y:.1f}" for x,y in arc)+" Z";cv.raw(f'<path d="{d}" fill="{col}" opacity="0.75" stroke="#ffffff" stroke-width="1.2"/>')
        mid=(start+end)/2;cv.text(cx+48*math.cos(mid),cy+48*math.sin(mid),lab,size=9,weight=700,color=C["ink"]);start=end
    for i,(lab,val,col) in enumerate(zip(labels,vals,colors)):
        y=54+i*34;_card(cv,274,y,126,26,col,"#ffffff",r=5,sw=1.1);cv.text(287,y+17,f"{lab}: {val}% = {val*3.6:.0f} deg",size=8.3,anchor="start",weight=700,color=col)
    cv.text(W/2,H-8,"total sector angles = 360 degrees",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── ogive ───────────────────────────────────────
def ogive(spec):
    x=[0,10,20,30,40,50];cf=[0,3,10,22,30,34];W,H=452,262;cv=Canvas(W,H,seed=_seed(spec,4509));cv.text(W/2,20,"less-than ogive: cumulative frequency never decreases",size=9.7,weight=700,color=C["soft"])
    x0,y0,sx,sy=48,204,6.7,5
    pts=[]
    for xv,yv in zip(x,cf):
        p=(x0+xv*sx,y0-yv*sy);pts.append(p);cv.dot(*p,r=3.5,color=C["red"]);cv.text(p[0],p[1]-8,str(yv),size=7.8,color=C["red"])
    for p,q in zip(pts,pts[1:]):cv.line(*p,*q,color=C["blue"],w=1.8)
    cv.line(x0,y0,x0+50*sx,y0,color=C["ink"],w=1.1);cv.line(x0,y0-180,x0,y0,color=C["ink"],w=1.1)
    for xv in x:cv.text(x0+xv*sx,y0+16,str(xv),size=7.8,color=C["soft"])
    cv.text(W/2,H-8,"median can be read near half of total cumulative frequency",size=8.7,color=C["ink"])
    return cv.svg()


# ───────────────────────────── missing frequency ───────────────────────────
def missing_frequency(spec):
    # values 10,20,30,40 with frequencies 2, x, 5, 3; target mean 25 -> solve x=5
    W,H=452,244;cv=Canvas(W,H,seed=_seed(spec,4510));cv.text(W/2,20,"missing frequency: use total xf = mean x total f",size=9.7,weight=700,color=C["soft"])
    _card(cv,40,52,372,36,C["blue"],C["blue_bg"],sw=1.5);cv.text(226,75,"values: 10, 20, 30, 40   |   frequencies: 2, x, 5, 3",size=8.6,weight=700,color=C["blue"])
    _card(cv,54,108,344,34,C["green"],C["green_bg"],sw=1.5);cv.text(226,130,"mean 25 -> sum xf = 25(x+10)",size=9.5,weight=700,color=C["green"])
    _card(cv,70,164,312,34,C["purple"],C["purple_bg"],sw=1.5);cv.text(226,186,"10(2)+20x+30(5)+40(3)=25(x+10)",size=8.4,weight=700,color=C["purple"])
    cv.text(W/2,H-8,"solve the resulting linear equation for x",size=8.8,color=C["red"])
    return cv.svg()


REGISTRY={
    "data-table":data_table,
    "mean-bars":mean_bars,
    "median-position":median_position,
    "mode-bar":mode_bar,
    "histogram":histogram,
    "frequency-polygon":frequency_polygon,
    "bar-chart":bar_chart,
    "pie-chart":pie_chart,
    "ogive":ogive,
    "missing-frequency":missing_frequency,
}
