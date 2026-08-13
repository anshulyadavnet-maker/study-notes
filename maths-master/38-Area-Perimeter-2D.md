# अध्याय 38 — क्षेत्रफल व परिमाप: 2-D Mensuration (Area & Perimeter)

## 38.1 :icon-target: परिचय व वेटेज

Chapter 33–37 में हमने geometry figures और उनके properties पढ़े। अब उन figures के अंदर का region कितना है और boundary कितनी लम्बी है—यह निकालेंगे।

> *"क्या question boundary cover करने की cost पूछ रहा है या पूरा surface cover करने की?"*

Boundary के लिए perimeter और surface के लिए area लगता है। Fencing, wire, border और running track में perimeter; flooring, painting, grass, tiles और land में area।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **2–3** | area, perimeter, composite shapes |
| **SSC CGL Tier-2** | **3–5** | mensuration, cost, circle |
| SSC CHSL / MTS / GD | 1–2 | rectangle, triangle, circle |
| **SSC CPO** | **2–3** | mixed 2-D figures |
| **IBPS / SBI PO** | 1–2 | arithmetic mensuration |
| IBPS / SBI Clerk | 1–2 | direct formula |
| **RRB NTPC / ALP** | **2–3** | area and perimeter |
| UP Police SI / Constable | 1–2 | fencing and field |
| UPSSSC PET | 1–2 | basic area |
| Super TET / UPTET | 1–2 | visual measurement |

> :icon-key: **पूरे अध्याय का एक वाक्य:** पहले shape और required quantity पहचानिए—boundary के लिए perimeter, region के लिए area—फिर units एक जैसी रखिए।

---

## 38.2 :icon-number: Units और basic distinction

### Length units

$$1\text{ m}=100\text{ cm}$$

$$1\text{ km}=1000\text{ m}$$

### Area units

Area में conversion square होता है:

$$1\text{ m}^2=10000\text{ cm}^2$$

क्योंकि $1$ m $=100$ cm और $1\text{ m}^2=100\times100\text{ cm}^2$।

| Quantity | Unit |
|---|---|
| Length/perimeter | cm, m, km |
| Area | cm², m², km² |
| Cost of fencing | currency per metre × metre |
| Cost of flooring | currency per m² × m² |

### Area और perimeter

- Perimeter: बाहर की boundary की total length
- Area: figure के अन्दर का region

Rectangle $l\times b$ के लिए:

$$\text{area}=lb$$

$$\text{perimeter}=2(l+b)$$

> :icon-warn: $m$ को $cm$ में बदलते समय $100$; $m^2$ को $cm^2$ में बदलते समय $10000$ लगेगा।

---

## 38.3 :icon-calc: Rectangle और square

### Rectangle

```figure
type: rectangle-measure
length: 12
breadth: 7
caption: rectangle में area अंदर का region और perimeter चारों sides की boundary है
```

**उदाहरण 1.** Rectangle की length $12$ m और breadth $7$ m।

$$A=12\times7=\mathbf{84\text{ m}^2}$$

$$P=2(12+7)=\mathbf{38\text{ m}}$$

**उदाहरण 2.** Rectangle का area $96$ m² और length $12$ m है। Breadth और perimeter?

$$b=96/12=8\text{ m}$$

$$P=2(12+8)=\mathbf{40\text{ m}}$$

**उदाहरण 3.** Rectangle का perimeter $50$ m और length $15$ m है। Breadth और area?

$$2(15+b)=50\quad\Rightarrow\quad15+b=25\quad\Rightarrow\quad b=10$$

Area $=15\times10=\mathbf{150\text{ m}^2}$।

### Square

```figure
type: square-measure
side: 8
caption: square के लिए area a², perimeter 4a और diagonal a√2
```

Side $a$:

$$A=a^2,\qquad P=4a,\qquad d=a\sqrt{2}$$

**उदाहरण 4.** Square की side $8$ cm।

- Area $=8^2=\mathbf{64\text{ cm}^2}$
- Perimeter $=4\times8=\mathbf{32\text{ cm}}$
- Diagonal $=\mathbf{8\sqrt{2}\text{ cm}}$

---

## 38.4 :icon-steps: Triangle और parallelogram

### Triangle

Base $b$ और perpendicular height $h$:

$$A=\frac{1}{2}bh$$

```figure
type: triangle-measure
base: 12
height: 8
caption: triangle area के लिए height base पर perpendicular होनी चाहिए
```

**उदाहरण 5.** Base $12$ cm और height $8$ cm।

$$A=\frac{1}{2}\times12\times8=\mathbf{48\text{ cm}^2}$$

यदि तीन sides दी हों, तो Heron formula:

$$s=\frac{a+b+c}{2}$$

$$A=\sqrt{s(s-a)(s-b)(s-c)}$$

### Parallelogram

Base $b$ और perpendicular height $h$:

$$A=bh$$

```figure
type: parallelogram-measure
base: 10
height: 6
caption: slanted side नहीं, perpendicular height area में लगती है
```

**उदाहरण 6.** Base $10$ cm और height $6$ cm।

$$A=10\times6=\mathbf{60\text{ cm}^2}$$

Parallelogram का perimeter $=2(a+b)$, जहाँ $a,b$ adjacent sides हैं।

> :icon-warn: Parallelogram की slant side को height समझना गलत है। Height base पर $90°$ होनी चाहिए।

---

## 38.5 :icon-ruler: Rhombus और trapezium

### Rhombus

यदि diagonals $d_1,d_2$ हों:

$$A=\frac{1}{2}d_1d_2$$

```figure
type: rhombus-measure
d1: 16
d2: 12
caption: rhombus area diagonals के perpendicular half-product से
```

**उदाहरण 7.** Diagonals $16$ cm और $12$ cm।

$$A=\frac{1}{2}\times16\times12=\mathbf{96\text{ cm}^2}$$

यदि side $a$ हो, perimeter $=4a$।

### Trapezium

Parallel bases $a,b$ और height $h$:

$$A=\frac{1}{2}(a+b)h$$

```figure
type: trapezium-measure
a: 14
b: 8
height: 6
caption: trapezium area parallel bases के average times height है
```

**उदाहरण 8.** Bases $14,8$ cm और height $6$ cm।

$$A=\frac{1}{2}(14+8)6=\mathbf{66\text{ cm}^2}$$

Trapezium mid-segment:

$$m=\frac{a+b}{2}=\frac{14+8}{2}=\mathbf{11\text{ cm}}$$

### Kite

यदि perpendicular diagonals $d_1,d_2$ हों:

$$A=\frac{1}{2}d_1d_2$$

**उदाहरण 9.** Kite diagonals $10$ cm और $16$ cm।

$$A=\frac{1}{2}\times10\times16=\mathbf{80\text{ cm}^2}$$

---

## 38.6 :icon-chart: Circle, semicircle और sector

### Circle

```figure
type: circle-measure38
radius: 7
caption: radius से circumference, area और diameter तीनों measures मिलते हैं
```

$$C=2\pi r=\pi d$$

$$A=\pi r^2$$

**उदाहरण 10.** Radius $7$ cm के circle के लिए $\pi=22/7$।

$$C=2\times\frac{22}{7}\times7=\mathbf{44\text{ cm}}$$

$$A=\frac{22}{7}\times49=\mathbf{154\text{ cm}^2}$$

### Semicircle

Semicircle का area:

$$A=\frac{1}{2}\pi r^2$$

Semicircle का perimeter curved arc और diameter दोनों से:

$$P=\pi r+2r$$

**उदाहरण 11.** Radius $7$ cm semicircle का area और perimeter।

- Area $=\frac{1}{2}\times\frac{22}{7}\times49=\mathbf{77\text{ cm}^2}$
- Perimeter $=22+14=\mathbf{36\text{ cm}}$

### Sector

Central angle $\theta$ हो:

$$\text{arc}=\frac{\theta}{360}\times2\pi r$$

$$\text{sector area}=\frac{\theta}{360}\times\pi r^2$$

**उदाहरण 12.** $r=14$ cm और $\theta=90°$।

- Arc $=\frac{90}{360}\times2\pi(14)=\mathbf{7\pi\text{ cm}}$
- Sector area $=\frac{90}{360}\times\pi(14)^2=\mathbf{49\pi\text{ cm}^2}$

---

## 38.7 :icon-chart: Composite figures और L-shape

Complex figure को छोटे rectangles, triangles और circles में बाँटिए। यदि कोई हिस्सा missing/cut है, outer area में से उसे subtract करें।

```figure
type: composite-lshape
outer_l: 12
outer_b: 10
cut_l: 5
cut_b: 4
caption: L-shaped region = outer rectangle area − missing rectangle area
```

**उदाहरण 13.** $12\times10$ rectangle के corner से $5\times4$ rectangle काट दिया गया। Remaining area?

$$A=12\times10-5\times4=120-20=\mathbf{100\text{ square units}}$$

### Composite perimeter

Perimeter में केवल visible outer boundary जोड़ें। Cut-out के अंदर की boundary तभी जोड़ेंगे जब वह region की actual boundary हो।

**उदाहरण 14.** ऊपर के L-shape में outer boundary lengths: $12,6,5,4,7,10$ हों, तो perimeter:

$$P=12+6+5+4+7+10=\mathbf{44\text{ units}}$$

> :icon-key: Composite area में split/subtract आसान है; composite perimeter में हर visible edge को एक बार trace करें।

---

## 38.8 :icon-steps: Path, border और uniform strip

### Path outside a rectangle

Rectangle $l\times b$ के चारों ओर uniform width $w$ path हो, तो outer dimensions:

$$L=l+2w,\qquad B=b+2w$$

Path area:

$$A_{path}=(l+2w)(b+2w)-lb$$

```figure
type: path-around
length: 20
breadth: 12
width: 2
caption: बाहर का uniform path दोनों dimensions में 2w बढ़ाता है
```

**उदाहरण 15.** $20$ m × $12$ m garden के चारों ओर $2$ m चौड़ा path है। Path area?

- Outer length $=20+4=24$ m
- Outer breadth $=12+4=16$ m

$$A_{path}=24\times16-20\times12=384-240=\mathbf{144\text{ m}^2}$$

### Path inside a rectangle

यदि path rectangle के अंदर हो, तो inner dimensions:

$$L=l-2w,\qquad B=b-2w$$

Path area $=lb-(l-2w)(b-2w)$।

**उदाहरण 16.** $20$ m × $12$ m floor के अंदर $2$ m border है। Border area?

Inner region $=16\times8=128$ m²।

$$A_{border}=240-128=\mathbf{112\text{ m}^2}$$

---

## 38.9 :icon-calc: Fencing, flooring, painting और cost

Question में quantity और rate अलग करें:

$$\text{total cost}=\text{quantity}\times\text{rate}$$

```figure
type: cost-fencing
length: 20
breadth: 12
rate: 15
area_rate: 8
caption: fencing perimeter से और flooring area से cost निकालती है
```

### Fencing

Fencing boundary पर होती है, इसलिए perimeter:

**उदाहरण 17.** $20$ m × $12$ m field को ₹15/m की दर से fence करना है।

$$P=2(20+12)=64\text{ m}$$

$$\text{cost}=64\times15=\mathbf{₹960}$$

### Flooring

Flooring surface पर होती है, इसलिए area:

**उदाहरण 18.** उसी field पर ₹8/m² की दर से grass लगानी है।

$$A=20\times12=240\text{ m}^2$$

$$\text{cost}=240\times8=\mathbf{₹1920}$$

### Four walls painting

Room की चार walls का area:

$$2h(l+b)$$

यदि doors/windows हों, तो उनका area subtract करें।

**उदाहरण 19.** Room $l=6$ m, $b=4$ m, $h=3$ m। Four walls area?

$$A=2\times3(6+4)=\mathbf{60\text{ m}^2}$$

### Tiles

Number of tiles:

$$\text{tiles}=\frac{\text{total area}}{\text{area of one tile}}$$

यदि fraction आए तो next whole tile तक round up करें।

---

## 38.10 :icon-bulb: Shortcuts और transformations

### :icon-timer: Shortcut 1 — dimensions बदलने पर area

Rectangle की length $p\%$ बढ़े और breadth $q\%$ बढ़े, तो new area factor:

$$\left(1+\frac{p}{100}\right)\left(1+\frac{q}{100}\right)$$

### :icon-timer: Shortcut 2 — same perimeter rectangle

Fixed perimeter में square का area maximum होता है।

यदि perimeter $P$ है, square side $=P/4$ और maximum area $=(P/4)^2$।

### :icon-timer: Shortcut 3 — circle changes

Radius $r$ को $kr$ करने पर:

- circumference $k$ times
- area $k^2$ times

Radius double ⟹ area four times।

### :icon-timer: Shortcut 4 — diagonal division

- Parallelogram का diagonal उसे two equal-area triangles में बाँटता है।
- Rectangle/square का diagonal भी equal-area triangles बनाता है।
- Rhombus area half diagonal product है।

### :icon-timer: Shortcut 5 — path area expansion

Outside path के लिए outer dimensions में $2w$ जोड़ें। Inside path में $2w$ घटाएँ।

### :icon-timer: Shortcut 6 — perimeter versus area

| शब्द | Quantity |
|---|---|
| fencing, wire, border, boundary | perimeter |
| flooring, painting surface, grass, tiles | area |
| circular track lap | circumference |
| sector region | sector area |

### :icon-timer: Shortcut 7 — formula selection

Figure की parallel/perpendicular markings पढ़ें; slant length को height न मानें।

---

## 38.11 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Area और perimeter की units मिलाना।
> Area m² में, perimeter m में लिखिए।

> :icon-cross: **जाल 2.** Square-unit conversion में केवल 100 लगाना।
> $1$ m² = $10000$ cm²।

> :icon-cross: **जाल 3.** Parallelogram की slant side को height मानना।
> Height perpendicular distance है।

> :icon-cross: **जाल 4.** Semicircle perimeter में diameter भूलना।
> Perimeter $=\pi r+2r$।

> :icon-cross: **जाल 5.** Sector में $\theta/180$ लगाना।
> Full circle $360°$ है।

> :icon-cross: **जाल 6.** Composite perimeter में inner cut-out की हर line जोड़ना।
> केवल actual exposed boundary trace करें।

> :icon-cross: **जाल 7.** Outside path में dimensions में केवल w जोड़ना।
> दोनों sides पर path है, इसलिए $2w$ जोड़ना है।

> :icon-cross: **जाल 8.** Fencing में area rate और flooring में perimeter rate लगाना।
> Boundary बनाम surface पहचानें।

> :icon-cross: **जाल 9.** Circle radius double होने पर area double लिखना।
> Area radius के square के proportional है।

> :icon-cross: **जाल 10.** Tile count fraction होने पर कम tiles लेना।
> Practical quantity को next whole tile तक round up करें।

---

## 38.12 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* Rectangle $12\times7$ का area और perimeter?

**हल:** $\mathbf{84\text{ m}^2}$ और $\mathbf{38\text{ m}}$।

**PYQ 2.** *(SSC CHSL)* Rhombus diagonals $16,12$ cm। Area?

**हल:** $\mathbf{96\text{ cm}^2}$।

**PYQ 3.** *(RRB NTPC)* $14,8$ bases और height $6$ trapezium। Area?

**हल:** $\mathbf{66\text{ cm}^2}$।

**PYQ 4.** *(IBPS Clerk)* $20\times12$ field fencing ₹15/m। Cost?

**हल:** perimeter $64$ m; cost $\mathbf{₹960}$।

**PYQ 5.** *(UP Police SI)* $20\times12$ garden के बाहर $2$ m path। Path area?

**हल:** $24\times16-240=\mathbf{144\text{ m}^2}$।

**PYQ 6.** *(SSC MTS)* Radius $7$ semicircle का perimeter?

**हल:** $22+14=\mathbf{36}$ cm।

---

## 38.13 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | Rectangle $12\times7$ area | $84$ | $lb$ |
| 2 | उसी rectangle perimeter | $38$ | $2(l+b)$ |
| 3 | Area $96$, length $12$ | breadth $8$ | $A/l$ |
| 4 | Perimeter $50$, length $15$ | breadth $10$ | equation |
| 5 | Square side $8$ area | $64$ | $a^2$ |
| 6 | Square side $8$ diagonal | $8\sqrt{2}$ | Pythagoras |
| 7 | Triangle $b=12,h=8$ | area $48$ | $1/2bh$ |
| 8 | Parallelogram $b=10,h=6$ | area $60$ | $bh$ |
| 9 | Rhombus diagonals $16,12$ | area $96$ | half-product |
| 10 | Kite diagonals $10,16$ | area $80$ | half-product |
| 11 | Trapezium $a=14,b=8,h=6$ | area $66$ | formula |
| 12 | Trapezium same bases | midline $11$ | average |
| 13 | Circle $r=7$ circumference | $44$ | $2\pi r$ |
| 14 | Circle $r=7$ area | $154$ | $\pi r^2$ |
| 15 | Semicircle $r=7$ area | $77$ | half circle |
| 16 | Semicircle $r=7$ perimeter | $36$ | arc + diameter |
| 17 | Sector $r=14,\theta=90$ area | $49\pi$ | fraction |
| 18 | Ring radii $7,3$ area | $40\pi$ | difference areas |
| 19 | L-shape outer $12\times10$, cut $5\times4$ | $100$ | subtract |
| 20 | $20\times12$ outside path width $2$ | $144$ | outer-inner |
| 21 | $20\times12$ inside border width $2$ | $112$ | inner subtract |
| 22 | Field $20\times12$ fence ₹15/m | ₹960 | perimeter cost |
| 23 | Same field grass ₹8/m² | ₹1920 | area cost |
| 24 | Room $6,4,3$ four walls area | $60$ | $2h(l+b)$ |
| 25 | Radius tripled | area 9 times | square factor |

---

## 38.14 :icon-trophy: अध्याय का सार

```
━━━ Rectangle ━━━
area = l×b
perimeter = 2(l+b)
diagonal = sqrt(l²+b²)

━━━ Square ━━━
area = a²
perimeter = 4a
diagonal = a√2

━━━ Triangle ━━━
area = 1/2 bh
Heron: sqrt[s(s-a)(s-b)(s-c)]

━━━ Parallelogram ━━━
area = base×perpendicular height
perimeter = 2(a+b)

━━━ Rhombus / Kite ━━━
area = 1/2 d₁d₂

━━━ Trapezium ━━━
area = 1/2(a+b)h
mid-segment = (a+b)/2

━━━ Circle ━━━
circumference = 2πr
area = πr²
semicircle perimeter = πr+2r
arc = (θ/360)×2πr
sector area = (θ/360)×πr²

━━━ Composite/path ━━━
outer area − cut area
outside path: dimensions +2w
inside path: dimensions −2w

━━━ Cost ━━━
fencing = perimeter×rate
flooring/painting = area×rate
```

> :icon-trophy: **2-D mensuration complete।** अब basic figures, composite regions, circles, paths और cost applications के area/perimeter formulas एक जगह व्यवस्थित हैं।
>
> **आगे:** Chapter 39 — **ठोस आकृतियाँ: Cube, Cuboid, Cylinder, Cone और Sphere**।
