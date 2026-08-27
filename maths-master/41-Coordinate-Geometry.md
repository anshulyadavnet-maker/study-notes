# अध्याय 41 — निर्देशांक ज्यामिति (Coordinate Geometry)

## 41.1 :icon-target: परिचय व वेटेज

Coordinate geometry algebra और geometry को एक ही system में जोड़ती है। किसी point को $(x,y)$ से लिखकर distance, midpoint, slope, area, line relation और shapes को बिना scale drawing के solve किया जा सकता है।

> *"दो points $(1,2)$ और $(4,6)$ के बीच की दूरी और line की slope क्या है?"*

Difference in coordinates से right triangle बनता है: horizontal change $3$, vertical change $4$, distance $5$ और slope $4/3$।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | distance, midpoint, slope |
| **SSC CGL Tier-2** | **2–3** | area, section, line relation |
| SSC CHSL / MTS / GD | 1 | coordinate basics |
| **SSC CPO** | **2** | line and triangle coordinates |
| **IBPS / SBI PO** | 1–2 | geometry/algebra combination |
| IBPS / SBI Clerk | 1 | direct formula |
| **RRB NTPC / ALP** | **2–3** | distance, slope, area |
| UP Police SI / Constable | 1–2 | coordinate plane |
| UPSSSC PET | 1 | basic coordinate geometry |
| Super TET / UPTET | 1–2 | visual coordinate reasoning |

> :icon-key: **पूरे अध्याय का एक वाक्य:** Coordinates लिखिए, differences निकालिए और सही formula से distance, midpoint, slope या area find कीजिए।

---

## 41.2 :icon-number: Cartesian plane और quadrants

Cartesian plane में:

- horizontal axis: $x$-axis
- vertical axis: $y$-axis
- intersection: origin $O=(0,0)$
- point: ordered pair $(x,y)$

```figure
type: coordinate-plane41
caption: coordinates में पहले x-direction और फिर y-direction move करते हैं
```

### Quadrants और signs

| Quadrant | x | y |
|---|---|---|
| I | $+$ | $+$ |
| II | $-$ | $+$ |
| III | $-$ | $-$ |
| IV | $+$ | $-$ |

**उदाहरण 1.** Points $(3,2)$, $(-3,2)$, $(-3,-2)$ और $(3,-2)$ के quadrants?

- $(3,2)$ ⟹ I
- $(-3,2)$ ⟹ II
- $(-3,-2)$ ⟹ III
- $(3,-2)$ ⟹ IV

### Axis पर points

- $(x,0)$ x-axis पर
- $(0,y)$ y-axis पर
- $(0,0)$ origin

### Reflections

- x-axis: $(x,y)\to(x,-y)$
- y-axis: $(x,y)\to(-x,y)$
- origin: $(x,y)\to(-x,-y)$

---

## 41.3 :icon-ruler: Distance formula

Points $A(x_1,y_1)$ और $B(x_2,y_2)$ के लिए:

$$AB=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$$

```figure
type: distance-formula
caption: coordinate differences एक right triangle बनाते हैं और distance hypotenuse होती है
```

**उदाहरण 2.** $(1,2)$ और $(4,6)$ की distance।

$$d=\sqrt{(4-1)^2+(6-2)^2}=\sqrt{9+16}=\mathbf{5}$$

**उदाहरण 3.** $(2,-3)$ और $(-4,5)$।

$$d=\sqrt{(-4-2)^2+(5+3)^2}=\sqrt{36+64}=\mathbf{10}$$

### Distance from axes

Point $(x,y)$ की:

- y-axis से distance $=|x|$
- x-axis से distance $=|y|$

**उदाहरण 4.** $(-5,3)$ की x-axis और y-axis से distances $\mathbf{3}$ और $\mathbf{5}$।

### Section check

Distance formula में coordinate differences का sign square होने के बाद positive हो जाता है। इसलिए subtraction order कोई भी लें, result same रहेगा।

---

## 41.4 :icon-calc: Midpoint और section formula

### Midpoint

Points $A(x_1,y_1)$ और $B(x_2,y_2)$ का midpoint:

$$M=\left(\frac{x_1+x_2}{2},\frac{y_1+y_2}{2}\right)$$

```figure
type: midpoint
caption: midpoint दोनों endpoints के x और y coordinates का average है
```

**उदाहरण 5.** $A(-3,2)$ और $B(3,-2)$ का midpoint?

$$M=\left(\frac{-3+3}{2},\frac{2-2}{2}\right)=\mathbf{(0,0)}$$

**उदाहरण 6.** $A(2,5)$ और $B(8,1)$।

$$M=\left(\frac{10}{2},\frac{6}{2}\right)=\mathbf{(5,3)}$$

### Internal section formula

यदि point $P$ line segment $AB$ को $m:n$ ratio में internally divide करे:

$$P=\left(\frac{mx_2+nx_1}{m+n},\frac{my_2+ny_1}{m+n}\right)$$

ध्यान दें: $AP:PB=m:n$ में A को $n$ और B को $m$ का weight मिलता है।

```figure
type: section-formula
caption: internal division में endpoint weights ratio के opposite लगते हैं
```

**उदाहरण 7.** $A(1,1)$ और $B(6,6)$ को $AP:PB=2:3$ में divide करने वाला P?

$$P=\left(\frac{2(6)+3(1)}{5},\frac{2(6)+3(1)}{5}\right)=\mathbf{(3,3)}$$

### External division

यदि point externally $m:n$ ratio में divide करे:

$$P=\left(\frac{mx_2-nx_1}{m-n},\frac{my_2-ny_1}{m-n}\right)$$

जहाँ $m\ne n$।

---

## 41.5 :icon-steps: Slope और straight lines

दो points के बीच slope:

$$m=\frac{y_2-y_1}{x_2-x_1}$$

```figure
type: slope-coordinate
caption: slope = rise/run और line की steepness/direction बताती है
```

**उदाहरण 8.** $(1,2)$ और $(3,6)$ का slope:

$$m=\frac{6-2}{3-1}=\mathbf{2}$$

### Slope की nature

- $m>0$: line rising
- $m<0$: line falling
- $m=0$: horizontal line
- vertical line: slope undefined

### Parallel lines

दो non-vertical lines parallel हों तो:

$$m_1=m_2$$

**उदाहरण 9.** $y=3x+5$ और $y=3x-7$ parallel हैं क्योंकि दोनों का slope $3$ है।

### Perpendicular lines

दो non-vertical perpendicular lines के slopes $m_1,m_2$:

$$m_1m_2=-1$$

**उदाहरण 10.** यदि एक line का slope $2$ है, तो perpendicular line का slope $-1/2$।

### Line equation

Slope $m$ और y-intercept $c$:

$$y=mx+c$$

Point-slope form:

$$y-y_1=m(x-x_1)$$

**उदाहरण 11.** Point $(2,5)$ से गुजरती और slope $3$ वाली line:

$$y-5=3(x-2)\quad\Rightarrow\quad y=\mathbf{3x-1}$$

---

## 41.6 :icon-chart: Collinearity और coordinate area

### Collinearity

तीन points collinear हों तो उनके slopes equal होंगे:

$$m_{AB}=m_{BC}$$

```figure
type: collinear
caption: equal consecutive slopes तीन points को एक straight line पर रखते हैं
```

**उदाहरण 12.** $(1,1),(3,3),(5,5)$ collinear हैं?

$$m_{AB}=\frac{3-1}{3-1}=1$$

$$m_{BC}=\frac{5-3}{5-3}=1$$

हाँ, points collinear हैं।

### Triangle area by coordinates

Points $(x_1,y_1),(x_2,y_2),(x_3,y_3)$ के लिए:

$$A=\frac{1}{2}\left|x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)\right|$$

```figure
type: triangle-area-coordinate
caption: determinant formula coordinate triangle का area सीधे देता है
```

**उदाहरण 13.** Points $(1,1),(6,1),(2,5)$ का area:

$$A=\frac{1}{2}|1(1-5)+6(5-1)+2(1-1)|$$

$$=\frac{1}{2}|-4+24+0|=\mathbf{10\text{ square units}}$$

यदि area $0$ आए, तो तीन points collinear हैं।

---

## 41.7 :icon-divide: Coordinate shapes और applications

### Rectangle from coordinates

Points $(1,1),(6,1),(6,4),(1,4)$ rectangle बनाते हैं।

- length $=6-1=5$
- breadth $=4-1=3$
- area $=5\times3=15$
- perimeter $=2(5+3)=16$

```figure
type: coordinate-shape
caption: coordinates से rectangle की side lengths, area और perimeter निकलिए
```

### Area और midpoint check

Shape के diagonals का same midpoint rectangle/parallelogram पहचानने में मदद करता है।

**उदाहरण 14.** Quadrilateral के vertices $(0,0),(4,0),(6,3),(2,3)$ हैं। क्या यह parallelogram है?

Diagonals:

- midpoint of $(0,0)$ and $(6,3)$ = $(3,1.5)$
- midpoint of $(4,0)$ and $(2,3)$ = $(3,1.5)$

Diagonals bisect करते हैं, इसलिए यह parallelogram है।

### Reflection

```figure
type: reflection
caption: axes और origin के across reflection में signs बदलते हैं
```

**उदाहरण 15.** Point $(3,-4)$ की x-axis reflection?

$$\mathbf{(3,4)}$$

y-axis reflection $=(-3,-4)$ और origin reflection $=(-3,4)$।

---

## 41.8 :icon-ruler: Distance, midpoint और slope का combined application

**उदाहरण 16.** $A(1,2)$ और $B(7,10)$ के लिए distance, midpoint और slope।

- Distance:

$$d=\sqrt{6^2+8^2}=\mathbf{10}$$

- Midpoint:

$$M=\left(\frac{1+7}{2},\frac{2+10}{2}\right)=\mathbf{(4,6)}$$

- Slope:

$$m=\frac{10-2}{7-1}=\mathbf{\frac{4}{3}}$$

### Equidistant point

यदि point x-axis पर हो और दो given points से equal distance हो, तो distances बराबर करके equation बनाइए।

**उदाहरण 17.** x-axis पर point $P(x,0)$, $A(2,3)$ से equal distance और $B(6,1)$ से भी equal distance है। $x$?

$$PA^2=(x-2)^2+9$$

$$PB^2=(x-6)^2+1$$

Equal:

$$(x-2)^2+9=(x-6)^2+1$$

$$x^2-4x+13=x^2-12x+37$$

$$8x=24\quad\Rightarrow\quad x=\mathbf{3}$$

Point $P=(3,0)$।

---

## 41.9 :icon-bulb: Shortcuts और proof checklist

### :icon-timer: Distance

$$d^2=(\Delta x)^2+(\Delta y)^2$$

पहले differences निकालने से signs की गलती कम होती है।

### :icon-timer: Midpoint

Coordinates को अलग-अलग average करें:

$$M_x=\frac{x_1+x_2}{2},\qquad M_y=\frac{y_1+y_2}{2}$$

### :icon-timer: Section formula

Internal ratio $m:n$ में:

$$P=\frac{nA+mB}{m+n}$$

Endpoint weights opposite ratio में आते हैं।

### :icon-timer: Slope

$$m=\frac{\text{rise}}{\text{run}}$$

- parallel: equal slopes
- perpendicular: product $-1$

### :icon-timer: Collinearity

Slope method या coordinate-area method:

- equal slopes ⟹ collinear
- triangle area $0$ ⟹ collinear

### :icon-timer: Coordinate area

Determinant formula में absolute value जरूरी है; orientation से area negative नहीं हो सकता।

### :icon-timer: Shape identification

| Coordinate clue | Shape/property |
|---|---|
| equal diagonals and same midpoint | rectangle/parallelogram clue |
| all sides equal | rhombus/square clue |
| slopes product $-1$ | perpendicular sides |
| three points area $0$ | collinear |

---

## 41.10 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Ordered pair में x और y उलट देना।
> $(x,y)$ में first coordinate horizontal और second vertical है।

> :icon-cross: **जाल 2.** Distance formula में coordinate differences जोड़ना।
> Differences के squares का sum लेकर square root करें।

> :icon-cross: **जाल 3.** Midpoint में केवल x या केवल y average करना।
> दोनों coordinates अलग-अलग average होते हैं।

> :icon-cross: **जाल 4.** Section formula में ratio weights same endpoint पर लगा देना।
> $AP:PB=m:n$ में A को n और B को m weight मिलता है।

> :icon-cross: **जाल 5.** Slope denominator zero होने पर slope 0 लिखना।
> Vertical line का slope undefined होता है।

> :icon-cross: **जाल 6.** Perpendicular slopes का product $1$ लिखना।
> सही relation $m_1m_2=-1$ है।

> :icon-cross: **जाल 7.** Triangle coordinate area में absolute value भूलना।
> Area positive quantity है।

> :icon-cross: **जाल 8.** Reflection में दोनों signs बदलना जबकि केवल axis reflection हो।
> x-axis: y sign; y-axis: x sign; origin: दोनों signs।

> :icon-cross: **जाल 9.** Collinear points के लिए केवल visual straightness देखना।
> Slopes या area से prove करें।

---

## 41.11 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* $(1,2)$ और $(4,6)$ की distance?

**हल:** $\mathbf{5}$।

**PYQ 2.** *(SSC CHSL)* $(-3,2)$ और $(3,-2)$ का midpoint?

**हल:** $\mathbf{(0,0)}$।

**PYQ 3.** *(RRB NTPC)* $(1,2)$ और $(3,6)$ का slope?

**हल:** $\mathbf{2}$।

**PYQ 4.** *(IBPS Clerk)* Three points $(1,1),(3,3),(5,5)$?

**हल:** Equal slopes, इसलिए **collinear**।

**PYQ 5.** *(UP Police SI)* Points $(1,1),(6,1),(2,5)$ triangle area?

**हल:** $\mathbf{10}$ square units।

**PYQ 6.** *(SSC MTS)* $(3,-4)$ का x-axis reflection?

**हल:** $\mathbf{(3,4)}$।

---

## 41.12 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | Point $(3,2)$ quadrant | I | signs |
| 2 | $(-3,2)$ quadrant | II | signs |
| 3 | $(-3,-2)$ quadrant | III | signs |
| 4 | $(3,-2)$ quadrant | IV | signs |
| 5 | $(1,2),(4,6)$ distance | 5 | distance formula |
| 6 | $(2,-3),(-4,5)$ distance | 10 | distance formula |
| 7 | $(-3,2),(3,-2)$ midpoint | $(0,0)$ | averages |
| 8 | $(2,5),(8,1)$ midpoint | $(5,3)$ | averages |
| 9 | $(1,1),(6,6)$ ratio $2:3$ | $(3,3)$ | section formula |
| 10 | $(1,2),(3,6)$ slope | 2 | rise/run |
| 11 | $y=3x+5$ and $y=3x-7$ | parallel | equal slopes |
| 12 | slope 2 perpendicular slope | $-1/2$ | product -1 |
| 13 | $(1,1),(3,3),(5,5)$ | collinear | slopes |
| 14 | $(1,1),(6,1),(2,5)$ area | 10 | determinant |
| 15 | $x$-axis reflection of $(3,-4)$ | $(3,4)$ | y sign |
| 16 | y-axis reflection of $(3,-4)$ | $(-3,-4)$ | x sign |
| 17 | origin reflection of $(3,-4)$ | $(-3,4)$ | both signs |
| 18 | $y=2x+1$ slope/intercept | 2,1 | form |
| 19 | line slope 3 through $(2,5)$ | $y=3x-1$ | point-slope |
| 20 | distance from $(−5,3)$ to axes | 5,3 | absolute coordinates |
| 21 | $3x+4y=12$ x-intercept | $(4,0)$ | y=0 |
| 22 | same line y-intercept | $(0,3)$ | x=0 |
| 23 | rectangle $(1,1),(6,1),(6,4),(1,4)$ area | 15 | side differences |
| 24 | same rectangle perimeter | 16 | $2(l+b)$ |
| 25 | $P(x,0)$ equidistant from $(2,3),(6,1)$ | $(3,0)$ | equal squares |

---

## 41.13 :icon-trophy: अध्याय का सार

```
━━━ Cartesian plane ━━━
point = (x,y)
origin = (0,0)
QI +,+; QII −,+; QIII −,−; QIV +,−

━━━ Distance ━━━
d = sqrt[(x₂−x₁)²+(y₂−y₁)²]

━━━ Midpoint ━━━
M=((x₁+x₂)/2,(y₁+y₂)/2)

━━━ Section ━━━
AP:PB=m:n
P=(nA+mB)/(m+n)

━━━ Slope ━━━
m=(y₂−y₁)/(x₂−x₁)
parallel: m₁=m₂
perpendicular: m₁m₂=−1

━━━ Collinearity ━━━
equal slopes or coordinate triangle area = 0

━━━ Triangle area ━━━
A=1/2 |x₁(y₂−y₃)+x₂(y₃−y₁)+x₃(y₁−y₂)|

━━━ Reflection ━━━
x-axis: (x,y)→(x,−y)
y-axis: (x,y)→(−x,y)
origin: (x,y)→(−x,−y)

━━━ Shape use ━━━
side differences, distance, slopes and midpoint
```

> :icon-trophy: **Coordinate Geometry complete।** Algebraic coordinates अब distance, midpoint, slope, area, collinearity, reflections और shape identification से जुड़ गए हैं।
>
> **आगे:** Part 6 की शुरुआत Chapter 42 — **त्रिकोणमितीय अनुपात, डिग्री व रेडियन** से होगी।
