# अध्याय 30 — रैखिक समीकरण व आलेख (Linear Equations & Graphs)

## 30.1 :icon-target: परिचय व वेटेज

Chapter 27 में हमने equation की भाषा और Chapter 29 में factorisation सीखी। अब equations को केवल symbols में solve नहीं करेंगे; उन्हें coordinate plane पर **line** के रूप में देखेंगे।

> *"$2x+y=6$ के कितने solutions हैं?"*

एक variable वाली equation का सामान्यतः एक solution होता है। लेकिन दो variables वाली linear equation के बहुत से ordered pairs हो सकते हैं। उन सभी points को graph पर plot करने पर एक सीधी रेखा बनती है।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | linear equation, slope, intercept |
| **SSC CGL Tier-2** | **2–3** | graphs और simultaneous equations |
| SSC CHSL / MTS / GD | 1 | basic equation |
| **SSC CPO** | **1–2** | graph और coordinate reading |
| **IBPS / SBI PO** | **2–3** | equation comparison और algebra base |
| IBPS / SBI Clerk | 1–2 | linear equations |
| **RRB NTPC / ALP** | **1–2** | graph of linear equation |
| UP Police SI / Constable | 1–2 | simultaneous equations |
| UPSSSC PET | 1 | elementary graph |
| Super TET / UPTET | 1–2 | coordinate plane और teaching method |

> :icon-key: **पूरे अध्याय का एक वाक्य:** दो-variable linear equation के ordered pairs बनाइए, उन्हें coordinate plane पर plot कीजिए और line का slope/intercept पढ़िए।

---

## 30.2 :icon-number: Linear equation की नींव

जिस equation में variable की highest power $1$ हो, वह linear equation है।

Examples:

- $3x+5=20$
- $2x-y=7$
- $4a+3b=12$

$x^2+2x+1=0$ linear नहीं, quadratic है क्योंकि highest power $2$ है।

### One-variable linear equation

**उदाहरण 1.** $3x+5=20$।

$$3x=20-5=15\quad\Rightarrow\quad x=\mathbf{5}$$

**उदाहरण 2.** $2(x-3)+4=16$।

$$2x-6+4=16\quad\Rightarrow\quad2x=18\quad\Rightarrow\quad x=\mathbf{9}$$

**उदाहरण 3.** $\dfrac{x+5}{3}=7$।

$$x+5=21\quad\Rightarrow\quad x=\mathbf{16}$$

### General form

One-variable equation:

$$ax+b=0\quad\Rightarrow\quad x=-\frac{b}{a}$$

जहाँ $a$ zero नहीं है।

> :icon-bulb: Equation solve करते समय दोनों sides पर समान operation करना balance बनाए रखता है। “Term दूसरी side गया तो sign बदला” इसी balance का shortcut है।

---

## 30.3 :icon-list: Two-variable equation और ordered pairs

दो-variable linear equation का सामान्य रूप —

$$ax+by=c$$

इसमें $x$ और $y$ के बहुत से values equation को satisfy कर सकते हैं। किसी एक pair को ordered pair $(x,y)$ लिखते हैं।

**उदाहरण 4.** $2x+y=6$।

कुछ values:

| $x$ | $y=6-2x$ | Ordered pair |
|---:|---:|---|
| $0$ | $6$ | $(0,6)$ |
| $1$ | $4$ | $(1,4)$ |
| $2$ | $2$ | $(2,2)$ |
| $3$ | $0$ | $(3,0)$ |

```figure
type: coordinate-plane
caption: ordered pair (x,y) पहले x-direction और फिर y-direction बताता है
```

हर pair को equation में रखकर जाँचिए:

- $(2,2)$: $2(2)+2=6$ ✔
- $(3,0)$: $2(3)+0=6$ ✔

### Ordered pair का क्रम

$(2,5)$ और $(5,2)$ अलग points हैं। पहला coordinate $x$ और दूसरा coordinate $y$ है।

### Intercept से pair

$2x+y=6$ में:

- $x=0$ रखने पर $y=6$: y-intercept $(0,6)$
- $y=0$ रखने पर $x=3$: x-intercept $(3,0)$

> :icon-key: Graph बनाने के लिए कम से कम दो सही ordered pairs चाहिए। Intercepts सबसे आसान दो points देते हैं।

---

## 30.4 :icon-chart: Coordinate plane

Coordinate plane में दो perpendicular axes होते हैं:

- horizontal axis: $x$-axis
- vertical axis: $y$-axis
- दोनों का intersection: origin $O=(0,0)$

चार quadrants में signs:

| Quadrant | $x$ का sign | $y$ का sign |
|---|---|---|
| I | positive | positive |
| II | negative | positive |
| III | negative | negative |
| IV | positive | negative |

**उदाहरण 5.** Points $(3,2)$, $(-3,1)$, $(-2,-2)$ और $(3,-2)$ क्रमशः किन quadrants में हैं?

- $(3,2)$ ⟹ I
- $(-3,1)$ ⟹ II
- $(-2,-2)$ ⟹ III
- $(3,-2)$ ⟹ IV

Distance from axes:

- point $(x,y)$ की y-axis से दूरी $=|x|$
- x-axis से दूरी $=|y|$

---

## 30.5 :icon-steps: Table से straight-line graph

Equation को $y$ के रूप में लिखिए, कुछ $x$ values चुनिए, $y$ निकालिए और points plot कीजिए।

**उदाहरण 6.** $y=2x+1$ का graph बनाइए।

| $x$ | $y=2x+1$ | Point |
|---:|---:|---|
| $-2$ | $-3$ | $(-2,-3)$ |
| $-1$ | $-1$ | $(-1,-1)$ |
| $0$ | $1$ | $(0,1)$ |
| $1$ | $3$ | $(1,3)$ |
| $2$ | $5$ | $(2,5)$ |

```figure
type: linear-table
a: 2
c: 1
caption: y=2x+1 के x values से ordered pairs बनाइए
```

```figure
type: line-graph
a: 2
c: 1
caption: points को join करने पर y=2x+1 की straight line मिलती है
```

### क्यों straight line?

Equation $y=mx+c$ में $x$ के साथ $y$ समान दर से बदलता है। हर $1$ unit x बढ़ने पर y में $m$ units का change होता है। इसलिए points एक ही दिशा में रहते हैं और उन्हें join करने पर straight line बनती है।

### Slope-intercept form

$$y=mx+c$$

जहाँ:

- $m$ = slope/ढाल
- $c$ = y-intercept

**उदाहरण 7.** $y=-3x+4$ में slope $=-3$ और y-intercept $=4$ है।

---

## 30.6 :icon-ruler: Slope और intercepts

### Slope

दो points $(x_1,y_1)$ और $(x_2,y_2)$ के लिए —

$$m=\frac{y_2-y_1}{x_2-x_1}$$

इसे rise/run भी कहते हैं:

$$m=\frac{\text{change in }y}{\text{change in }x}$$

```figure
type: slope-lines
caption: positive, zero और negative slope की दिशा पहचानिए
```

**उदाहरण 8.** Points $(1,2)$ और $(3,6)$ से गुजरने वाली line का slope?

$$m=\frac{6-2}{3-1}=\frac{4}{2}=\mathbf{2}$$

### Slope का अर्थ

- $m>0$: line ऊपर की ओर बढ़ती है
- $m<0$: line नीचे की ओर घटती है
- $m=0$: horizontal line
- vertical line का slope defined नहीं माना जाता

### Intercepts

Equation $ax+by=c$ में:

- x-intercept के लिए $y=0$ रखें: $x=c/a$
- y-intercept के लिए $x=0$ रखें: $y=c/b$

**उदाहरण 9.** $2x+3y=6$ के intercepts।

- $y=0$: $2x=6$ ⟹ x-intercept $(3,0)$
- $x=0$: $3y=6$ ⟹ y-intercept $(0,2)$

```figure
type: intercept-graph
a: 2
b: 3
c: 6
caption: x=0 और y=0 रखकर line के दोनों intercepts निकालिए
```

### Special lines

- $x=4$: vertical line, हर point का x-coordinate $4$
- $y=-2$: horizontal line, हर point का y-coordinate $-2$

इन lines को slope-intercept form $y=mx+c$ में लिखना आवश्यक नहीं।

---

## 30.7 :icon-divide: Simultaneous linear equations का graphical meaning

दो linear equations के common solution को दोनों lines का intersection point दिखाता है।

**उदाहरण 10.**

$$x+y=5$$

$$x-y=1$$

दोनों equations जोड़िए:

$$2x=6\quad\Rightarrow\quad x=3$$

फिर $x+y=5$ में:

$$3+y=5\quad\Rightarrow\quad y=2$$

Solution $(3,2)$ है।

```figure
type: system-intersection
caption: दो lines का intersection point दोनों equations को satisfy करता है
```

### Graphical cases

| Lines | Algebraic result | Solutions |
|---|---|---|
| एक point पर काटें | consistent independent | एक solution |
| parallel और अलग | inconsistent | कोई solution नहीं |
| एक ही line | dependent | अनन्त solutions |

**उदाहरण 11 — parallel lines।**

$$y=2x+1,\qquad y=2x-3$$

दोनों का slope $2$ है लेकिन intercept अलग हैं। इसलिए lines parallel हैं और कोई common point नहीं।

**उदाहरण 12 — coincident lines।**

$$2x+4y=6,\qquad x+2y=3$$

पहली equation दूसरी की $2$ गुनी है। दोनों same line हैं, इसलिए हर common point solution है।

### Algebra और graph का सम्बन्ध

- algebra से solution $(x,y)$ निकालिए
- graph पर दोनों lines draw कीजिए
- intersection पर वही $(x,y)$ मिलेगा

---

## 30.8 :icon-brain: Word problems और applications

### Sum और difference

**उदाहरण 13.** दो numbers का sum $40$ और difference $8$ है। numbers?

मान लें numbers $x,y$।

$$x+y=40,\qquad x-y=8$$

दोनों जोड़ें:

$$2x=48\quad\Rightarrow\quad x=24$$

$$y=40-24=\mathbf{16}$$

### Fixed charge और variable charge

**उदाहरण 14.** Taxi का fixed charge ₹50 और प्रति km ₹10 है। $x$ km के लिए fare $y$ हो, तो equation?

$$\mathbf{y=10x+50}$$

- slope $10$: प्रति km fare में ₹10 बढ़ता है
- y-intercept $50$: zero km पर fixed charge

$3$ km के लिए $y=10(3)+50=\mathbf{₹80}$।

### Two quantities and conditions

**उदाहरण 15.** एक class में boys और girls कुल $40$ हैं। boys, girls से $8$ अधिक हैं। संख्या?

मान लें boys $b$, girls $g$।

$$b+g=40,\qquad b-g=8$$

अतः $b=24,g=16$।

> :icon-key: Word problem में पहले quantities को variables दीजिए, फिर प्रत्येक sentence को अलग equation में बदलिए।

---

## 30.9 :icon-bulb: शॉर्टकट व उनके प्रमाण

### :icon-timer: शॉर्टकट 1 — intercept method

$ax+by=c$ के graph के लिए:

1. $y=0$ रखकर x-intercept निकालिए
2. $x=0$ रखकर y-intercept निकालिए
3. दोनों points join करिए

दो non-identical points एक straight line निर्धारित करते हैं।

### :icon-timer: शॉर्टकट 2 — slope-intercept reading

$$y=mx+c$$

बिना table बनाए:

- y-axis पर $c$ से शुरू करें
- slope $m$ के अनुसार rise/run करें

उदाहरण: $y=2x+1$ में point $(0,1)$ और slope $2=2/1$। अगला point $(1,3)$।

### :icon-timer: शॉर्टकट 3 — point-slope form

Slope $m$ और point $(x_1,y_1)$ दिया हो —

$$y-y_1=m(x-x_1)$$

**उदाहरण:** slope $2$, point $(1,3)$:

$$y-3=2(x-1)\quad\Rightarrow\quad y=2x+1$$

### :icon-timer: शॉर्टकट 4 — parallel lines

दो non-vertical lines parallel हों तो उनके slopes बराबर और intercept अलग होंगे।

$$m_1=m_2,\qquad c_1\ne c_2$$

### :icon-timer: शॉर्टकट 5 — simultaneous equations elimination

यदि:

$$a_1x+b_1y=c_1$$

$$a_2x+b_2y=c_2$$

तो किसी variable के coefficients बराबर करके equations जोड़/घटा दीजिए। Graphically यही intersection point ढूँढना है।

### :icon-timer: शॉर्टकट 6 — check a point

Point $(p,q)$ line $ax+by=c$ पर है या नहीं, जाँचने के लिए $x=p,y=q$ रखिए। Equality मिले तो point line पर है।

### :icon-timer: शॉर्टकट 7 — vertical/horizontal पहचान

- $x=k$: vertical line
- $y=k$: horizontal line
- $y=mx+c$ में $m=0$: horizontal line

---

## 30.10 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Ordered pair में coordinates उलट देना।
> $(x,y)$ में पहला x और दूसरा y होता है।

> :icon-cross: **जाल 2.** $2x+y=6$ में $x=2$ रखने पर y को भी 2 रख देना।
> पहले $y=6-2x$ निकालिए; $x=2$ पर y=2 होगा, हर value पर नहीं।

> :icon-cross: **जाल 3.** Graph में केवल एक point plot करना।
> Straight line के लिए कम से कम दो सही points चाहिए।

> :icon-cross: **जाल 4.** x-intercept और y-intercept के लिए गलत variable zero करना।
> x-intercept: $y=0$; y-intercept: $x=0$।

> :icon-cross: **जाल 5.** Slope में denominator उलट देना।
> $m=(y_2-y_1)/(x_2-x_1)$।

> :icon-cross: **जाल 6.** Same slope वाली हर दो lines को same line मान लेना।
> Intercept भी compare करें; अलग intercept पर lines parallel हैं।

> :icon-cross: **जाल 7.** Vertical line $x=4$ को $y=4$ लिखना।
> $x=4$ vertical और $y=4$ horizontal line है।

> :icon-cross: **जाल 8.** Graphical intersection को दोनों equations में check न करना।
> Point को दोनों equations में substitute करके जाँचिए।

> :icon-cross: **जाल 9.** Word problem में variables की units भूलना।
> Taxi equation में x km और y rupees का अर्थ स्पष्ट रखें।

---

## 30.11 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* $3x+5=20$ में x?

**हल:** $\mathbf{x=5}$।

**PYQ 2.** *(SSC CHSL)* $y=2x+1$ में $x=3$ पर y?

**हल:** $y=6+1=\mathbf{7}$।

**PYQ 3.** *(RRB NTPC)* $2x+3y=6$ का x-intercept क्या होगा?

**हल:** $y=0$ ⟹ $x=\mathbf{3}$, point $(3,0)$।

**PYQ 4.** *(IBPS Clerk)* $x+y=5$, $x-y=1$ का solution?

**हल:** $\mathbf{x=3,y=2}$।

**PYQ 5.** *(UP Police SI)* Points $(1,2)$ और $(3,6)$ से गुजरती line का slope?

**हल:** $\mathbf{2}$।

**PYQ 6.** *(SSC MTS)* $y=2x+1$ और $y=2x-3$ कैसी lines हैं?

**हल:** Same slope, अलग intercept ⟹ **parallel**।

---

## 30.12 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | $3x+5=20$ | $x=5$ | subtract/divide |
| 2 | $2(x-3)+4=16$ | $x=9$ | expand |
| 3 | $(x+5)/3=7$ | $x=16$ | multiply/add |
| 4 | $5x-7=3x+9$ | $x=8$ | collect terms |
| 5 | $2x+3y=6$, $x=0$ | $y=2$ | y-intercept |
| 6 | $x+y=5$, $x=0$ | $(0,5)$ | ordered pair |
| 7 | $y=2x+1$, $x=3$ | $y=7$ | substitution |
| 8 | $y=-3x+4$ | slope $-3$, intercept $4$ | $y=mx+c$ |
| 9 | points $(1,2),(3,6)$ | slope $2$ | rise/run |
| 10 | $2x+3y=6$, x-intercept | $(3,0)$ | $y=0$ |
| 11 | $2x+3y=6$, y-intercept | $(0,2)$ | $x=0$ |
| 12 | $x+y=5$, $x-y=1$ | $(3,2)$ | add equations |
| 13 | $2x+y=7$, $x-y=2$ | $(3,1)$ | elimination |
| 14 | $y=2x+1$, $y=2x-3$ | parallel | same slope |
| 15 | $x=4$ का graph | vertical line | fixed x |
| 16 | $y=-2$ का graph | horizontal line | fixed y |
| 17 | $y=3x-1$, $x=-1$ | $y=-4$ | substitution |
| 18 | sum $40$, difference $8$ | $24,16$ | two equations |
| 19 | taxi $y=10x+50$, $x=3$ | ₹80 | substitution |
| 20 | $y=3x$, $x=4$ | $y=12$ | origin line |
| 21 | slope $2$, point $(1,3)$ | $y=2x+1$ | point-slope |
| 22 | $y=x+2$, $y=-x+6$ | $(2,4)$ | intersection |
| 23 | $3x+2y=12$ intercepts | $(4,0),(0,6)$ | put zero |
| 24 | $y=5$ का graph | horizontal line | fixed y |
| 25 | $4x-2y=8$ | $y=2x-4$ | rearrange |

---

## 30.13 :icon-trophy: अध्याय का सार

```
━━━ Linear equation ━━━
variable की highest power 1
one variable: ax+b=0 → x=−b/a
two variables: ax+by=c

━━━ Ordered pair ━━━
(x,y) में पहले x, फिर y
2x+y=6:
(0,6), (1,4), (2,2), (3,0)

━━━ Coordinate plane ━━━
origin = (0,0)
QI: +,+
QII: −,+
QIII: −,−
QIV: +,−

━━━ Graph ━━━
y=mx+c
m = slope
c = y-intercept
दो points plot करके line join करें

━━━ Intercepts ━━━
ax+by=c
x-intercept: y=0
 y-intercept: x=0
2x+3y=6 → (3,0), (0,2)

━━━ Slope ━━━
m=(y₂−y₁)/(x₂−x₁)
m>0: rising
m<0: falling
m=0: horizontal
x=k: vertical

━━━ Simultaneous equations ━━━
intersection point = common solution
same slope, different intercept → parallel
same line → infinitely many solutions
```

> :icon-trophy: **Part 4 में equations और graphs की नींव तैयार है।** अब linear expressions को visual line, slope और intersection के रूप में पढ़ सकते हैं।
>
> **आगे:** Chapter 31 — **द्विघात समीकरण (Quadratic Equations)**। वहाँ degree 2 वाली equations, roots, discriminant और factor/quadratic formula का विस्तार होगा।
