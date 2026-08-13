# अध्याय 33 — रेखाएँ व कोण (Lines & Angles)

## 33.1 :icon-target: परिचय व वेटेज

Part 5 की शुरुआत geometry से होती है। रेखाएँ और कोण पूरे geometry section की भाषा हैं—triangles, quadrilaterals, circles, mensuration और trigonometry में इनके नियम बार-बार आते हैं।

> *"दो parallel lines को एक transversal काटती है। एक angle 65° है। बाकी angles कैसे मिलेंगे?"*

ऐसे प्रश्नों में calculation कम और diagram reading अधिक महत्वपूर्ण है। कौन-सा angle corresponding है, कौन alternate interior और कौन co-interior—यही पहचान answer तय करती है।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | parallel lines, angle pairs |
| **SSC CGL Tier-2** | **2–3** | geometry proofs और angle chase |
| SSC CHSL / MTS / GD | 1–2 | basic angle rules |
| **SSC CPO** | **2** | transversal और triangle angles |
| **IBPS / SBI PO** | 1–2 | geometry foundation |
| IBPS / SBI Clerk | 1 | direct angle calculation |
| **RRB NTPC / ALP** | **2–3** | lines, triangles, polygons |
| UP Police SI / Constable | 1–2 | angle chase |
| UPSSSC PET | 1 | elementary geometry |
| Super TET / UPTET | 1–2 | visual geometry and pedagogy |

> :icon-key: **पूरे अध्याय का एक वाक्य:** diagram में relation पहचानिए, फिर $90°$, $180°$, $360°$ और parallel-line rules लगाइए।

---

## 33.2 :icon-number: Point, line, ray और segment

### Point (बिन्दु)

Point exact position बताता है। इसका कोई length या breadth नहीं माना जाता। इसे capital letter $A,B,C$ से label करते हैं।

### Line (रेखा)

Line दोनों दिशाओं में अनन्त तक जाती है। $\overleftrightarrow{AB}$ से दिखा सकते हैं। इसके कोई endpoints नहीं होते।

### Ray (किरण)

Ray का एक initial point होता है और दूसरी दिशा में अनन्त तक जाती है। $\overrightarrow{AB}$ में A initial point है।

### Line segment (रेखाखण्ड)

Segment के दो fixed endpoints होते हैं। $\overline{AB}$ की finite length होती है।

```figure
type: point-line-ray
caption: line, ray और segment को endpoints और arrows से पहचानिए
```

### Lines के सम्बन्ध

- Intersecting lines: एक point पर मिलती हैं
- Parallel lines: कभी नहीं मिलतीं
- Perpendicular lines: $90°$ पर intersect करती हैं
- Transversal: दो या अधिक lines को काटने वाली line
- Collinear points: एक ही line पर स्थित points

> :icon-bulb: Diagram में arrow marks line की infinite extension और dot endpoints को दर्शाते हैं। इन्हें अनदेखा करके angle relation न निकालें।

---

## 33.3 :icon-calc: Angles के प्रकार

दो rays का common endpoint vertex कहलाता है। Angle को degrees में measure करते हैं।

| Angle | Measure |
|---|---|
| Zero angle | $0°$ |
| Acute angle | $0°$ से बड़ा और $90°$ से छोटा |
| Right angle | $90°$ |
| Obtuse angle | $90°$ से बड़ा और $180°$ से छोटा |
| Straight angle | $180°$ |
| Reflex angle | $180°$ से बड़ा और $360°$ से छोटा |
| Complete angle | $360°$ |

```figure
type: angle-types
kind: acute
degrees: 45
caption: acute angle 90° से छोटा होता है
```

```figure
type: angle-types
kind: right
degrees: 90
caption: right angle को छोटा square mark करके दिखाते हैं
```

**उदाहरण 1.** $35°$, $90°$, $125°$, $180°$ और $225°$ को classify करें।

- $35°$: acute
- $90°$: right
- $125°$: obtuse
- $180°$: straight
- $225°$: reflex

### Degree और angle measure

- एक complete turn $=360°$
- straight line पर angle $=180°$
- एक right angle $=90°$
- दो right angles $=180°$

---

## 33.4 :icon-steps: Angle pairs और basic rules

### Adjacent angles

दो angles adjacent हैं यदि उनका common vertex और एक common arm हो, तथा interiors overlap न करें।

### Complementary angles

दो angles का sum $90°$ हो:

$$x+y=90°$$

```figure
type: angle-pairs
kind: complementary
caption: complementary angles मिलकर right angle बनाते हैं
```

**उदाहरण 2.** Complementary angles में एक angle $35°$ है। दूसरा?

$$y=90-35=\mathbf{55°}$$

### Supplementary angles

दो angles का sum $180°$ हो:

$$x+y=180°$$

### Linear pair

एक common arm और बाकी arms एक straight line बनाएं, तो linear pair होता है। Linear pair supplementary होता है।

```figure
type: angle-pairs
kind: linear
caption: linear pair के adjacent angles का sum 180° होता है
```

**उदाहरण 3.** Linear pair का एक angle $65°$ है। दूसरा?

$$y=180-65=\mathbf{115°}$$

### Vertically opposite angles

दो lines intersect करें तो opposite angles equal होते हैं। Adjacent angles supplementary होते हैं।

```figure
type: vertical-angles
caption: vertically opposite angles बराबर और adjacent angles supplementary होते हैं
```

**उदाहरण 4.** Intersecting lines में एक angle $72°$ है। Opposite angle और दोनों adjacent angles?

- opposite $=\mathbf{72°}$
- each adjacent $=180-72=\mathbf{108°}$

### Angles around a point

एक point के चारों ओर angles का sum —

$$\text{sum around a point}=360°$$

**उदाहरण 5.** एक point के चार angles $80°$, $90°$, $70°$ और $x$ हैं।

$$x=360-(80+90+70)=\mathbf{120°}$$

---

## 33.5 :icon-ruler: Perpendicular lines और angle bisector

### Perpendicular lines

दो lines $90°$ पर मिलें तो perpendicular होती हैं। उनके चारों angles right angles होते हैं।

```figure
type: perpendicular
caption: perpendicular lines चार 90° angles बनाती हैं
```

### Angle bisector

जो ray किसी angle को दो equal parts में बाँटे, angle bisector कहलाती है।

```figure
type: angle-bisector
angle: 80
caption: angle bisector 80° को दो 40° parts में बाँटती है
```

**उदाहरण 6.** $80°$ angle का bisector दोनों parts को कितना बनाएगा?

$$\text{each part}=80/2=\mathbf{40°}$$

**उदाहरण 7.** An angle bisector से बने दोनों angles $(3x+5)°$ और $(5x-15)°$ हैं। $x$?

दोनों equal:

$$3x+5=5x-15\quad\Rightarrow\quad2x=20\quad\Rightarrow\quad x=\mathbf{10}$$

प्रत्येक angle $=35°$।

---

## 33.6 :icon-chart: Parallel lines और transversal

जब एक transversal दो parallel lines को काटती है, तो आठ angles बनते हैं। इनके बीच standard relations होते हैं।

```figure
type: parallel-transversal
caption: parallel lines को transversal काटे तो eight-angle pattern बनता है
```

मान लें $l\parallel m$।

### 1. Corresponding angles

एक ही relative position में बने angles equal होते हैं।

$$\angle1=\angle5,\quad\angle2=\angle6,\quad\angle3=\angle7,\quad\angle4=\angle8$$

### 2. Alternate interior angles

Parallel lines के बीच और transversal के opposite sides पर बने angles equal होते हैं।

$$\angle3=\angle5,\qquad\angle4=\angle6$$

### 3. Co-interior या same-side interior angles

Parallel lines के बीच एक ही side पर बने angles supplementary होते हैं।

$$\angle3+\angle6=180°$$

### 4. Alternate exterior angles

Parallel lines के बाहर और transversal के opposite sides पर बने angles equal होते हैं।

### Converse

यदि corresponding या alternate interior angles equal हों, तो lines parallel सिद्ध की जा सकती हैं।

> :icon-key: Figure में पहले दोनों lines और transversal पहचानिए। उसके बाद angle pair का नाम लगाइए; केवल position देखकर random equality न लिखें।

---

## 33.7 :icon-divide: Parallel-line angle chase

**उदाहरण 8.** दो parallel lines को transversal काटती है। एक alternate interior angle $65°$ है और दूसरा $x$ उसी alternate position में है। $x$?

```figure
type: parallel-angle-chase
given: 65
caption: alternate interior angle को दूसरी parallel line पर copy कीजिए
```

Alternate interior angles equal:

$$x=\mathbf{65°}$$

**उदाहरण 9.** एक corresponding angle $72°$ है। उसी intersection का adjacent angle?

Corresponding angle $=72°$। Adjacent linear pair:

$$x=180-72=\mathbf{108°}$$

**उदाहरण 10.** Co-interior angles $(3x+10)°$ और $(5x-30)°$ हैं। $x$?

$$3x+10+5x-30=180$$

$$8x-20=180\quad\Rightarrow\quad8x=200\quad\Rightarrow\quad x=\mathbf{25}$$

Angles $=85°$ और $95°$, जिनका sum $180°$ है।

**उदाहरण 11.** Corresponding angles $(4x-15)°$ और $(2x+45)°$ हैं।

$$4x-15=2x+45\quad\Rightarrow\quad2x=60\quad\Rightarrow\quad x=\mathbf{30}$$

Angle $=105°$।

---

## 33.8 :icon-steps: Triangle angles

Triangle के तीन interior angles का sum $180°$ होता है।

$$\angle A+\angle B+\angle C=180°$$

```figure
type: triangle-angle-sum
caption: triangle के तीन interior angles मिलकर 180° बनाते हैं
```

**उदाहरण 12.** Triangle के angles $2x$, $3x$ और $4x$ हैं। angles?

$$2x+3x+4x=180\quad\Rightarrow\quad9x=180\quad\Rightarrow\quad x=20$$

Angles $=\mathbf{40°,60°,80°}$।

**उदाहरण 13.** Triangle में दो angles $45°$ और $65°$ हैं। तीसरा?

$$180-45-65=\mathbf{70°}$$

### Isosceles triangle

दो equal sides के opposite angles equal होते हैं।

**उदाहरण 14.** Isosceles triangle का vertex angle $40°$ है। प्रत्येक base angle?

$$\text{base angle}=\frac{180-40}{2}=\mathbf{70°}$$

---

## 33.9 :icon-star: Exterior angle theorem

Triangle के किसी vertex पर एक side को extend करने से exterior angle बनता है। Exterior angle = दो opposite interior angles का sum।

```figure
type: triangle-exterior
caption: triangle का exterior angle remote interior angles के योग के बराबर होता है
```

$$\text{exterior angle}=\text{opposite interior angle 1}+\text{opposite interior angle 2}$$

**उदाहरण 15.** Triangle के दो remote interior angles $50°$ और $70°$ हैं। Exterior angle?

$$\text{exterior}=50+70=\mathbf{120°}$$

**उदाहरण 16.** Exterior angle $130°$ है और एक remote interior angle $55°$ है। दूसरा?

$$x+55=130\quad\Rightarrow\quad x=\mathbf{75°}$$

**उदाहरण 17.** Triangle का exterior angle $(4x+10)°$ और two remote angles $(2x+5)°$, $(x+20)°$ हैं। $x$?

$$4x+10=(2x+5)+(x+20)$$

$$4x+10=3x+25\quad\Rightarrow\quad x=\mathbf{15}$$

Exterior angle $70°$।

---

## 33.10 :icon-chart: Polygons और interior angles

$n$ sides वाले polygon को एक vertex से diagonals खींचकर $(n-2)$ triangles में बाँटा जा सकता है।

```figure
type: polygon-sum
sides: 6
caption: hexagon को एक vertex से चार triangles में बाँटकर interior sum निकालिए
```

### Interior angle sum

$$\text{sum}=(n-2)\times180°$$

**उदाहरण 18.** Hexagon के interior angles का sum?

$$ (6-2)\times180=\mathbf{720°}$$

**उदाहरण 19.** Polygon के interior angles का sum $900°$ है। sides?

$$(n-2)180=900\quad\Rightarrow\quad n-2=5\quad\Rightarrow\quad n=\mathbf{7}$$

### Diagonals

$n$-gon के diagonals —

$$\text{number of diagonals}=\frac{n(n-3)}{2}$$

Hexagon में $=6(3)/2=\mathbf{9}$ diagonals।

---

## 33.11 :icon-ruler: Regular polygons

Regular polygon में सभी sides और सभी interior angles equal होते हैं।

```figure
type: regular-polygon
sides: 8
caption: regular polygon में equal sides और equal angles होते हैं
```

### Exterior angle

किसी भी polygon के एक-एक exterior angle का total $360°$ होता है। Regular $n$-gon में —

$$\text{each exterior angle}=\frac{360°}{n}$$

### Interior angle

$$\text{each interior angle}=180°-\frac{360°}{n}$$

या —

$$\text{each interior angle}=\frac{(n-2)180°}{n}$$

**उदाहरण 20.** Regular octagon के प्रत्येक exterior और interior angle?

- exterior $=360/8=\mathbf{45°}$
- interior $=180-45=\mathbf{135°}$

**उदाहरण 21.** Regular polygon का प्रत्येक exterior angle $30°$ है। sides?

$$n=\frac{360}{30}=\mathbf{12}$$

---

## 33.12 :icon-bulb: Shortcuts और proof checklist

### :icon-timer: Shortcut 1 — angle pair order

| Diagram clue | Rule |
|---|---|
| right corner | $90°$ |
| straight line | $180°$ |
| around a point | $360°$ |
| vertically opposite | equal |
| linear pair | sum $180°$ |
| complementary | sum $90°$ |
| supplementary | sum $180°$ |

### :icon-timer: Shortcut 2 — parallel lines

- Corresponding: equal
- Alternate interior: equal
- Alternate exterior: equal
- Co-interior: sum $180°$

### :icon-timer: Shortcut 3 — triangle

$$\text{third angle}=180°-(\text{first} + \text{second})$$

Exterior angle direct:

$$\text{exterior}=\text{remote angle 1}+\text{remote angle 2}$$

### :icon-timer: Shortcut 4 — regular polygon

$$n=\frac{360°}{\text{exterior angle}}$$

$$\text{interior}=180°-\text{exterior}$$

### :icon-timer: Shortcut 5 — find unknown in a diagram

1. Given angle को mark करें।
2. Equal relation वाले angles copy करें।
3. Linear pair में $180°$ लगाएँ।
4. Triangle में $180°$ लगाएँ।
5. End में answer को angle range से check करें।

### :icon-timer: Shortcut 6 — proof language

| To prove | Sufficient observation |
|---|---|
| lines parallel | corresponding/alternate angles equal |
| lines perpendicular | one angle $90°$ |
| triangle is isosceles | two equal angles or two equal sides |
| regular polygon angle | $360/n$ exterior |

---

## 33.13 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Linear pair को equal मानना।
> Linear pair का sum $180°$ होता है; equal तभी होगा जब दोनों $90°$ हों।

> :icon-cross: **जाल 2.** Vertically opposite और adjacent angles को confuse करना।
> Opposite equal, adjacent supplementary।

> :icon-cross: **जाल 3.** Corresponding angles को alternate interior समझना।
> Position देखकर pair का नाम और rule दोनों जाँचिए।

> :icon-cross: **जाल 4.** Co-interior angles को equal लिखना।
> उनका sum $180°$ होता है।

> :icon-cross: **जाल 5.** Triangle angle sum $360°$ लिखना।
> Triangle के interior angles का sum $180°$ है; $360°$ point के आसपास लगता है।

> :icon-cross: **जाल 6.** Exterior angle में adjacent interior angle जोड़ना।
> Exterior angle remote opposite interior angles के sum के बराबर होता है।

> :icon-cross: **जाल 7.** Polygon interior sum में $n-1$ लेना।
> एक vertex से triangles की संख्या $n-2$ होती है।

> :icon-cross: **जाल 8.** Regular polygon के interior angle को $360/n$ लेना।
> $360/n$ exterior angle है; interior $180-360/n$।

> :icon-cross: **जाल 9.** Diagram में figure not-to-scale होने पर visual size से answer चुनना।
> केवल दिए हुए angle relations और theorems पर भरोसा करें।

---

## 33.14 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* Linear pair में एक angle $65°$ है। दूसरा?

**हल:** $180-65=\mathbf{115°}$।

**PYQ 2.** *(SSC CHSL)* Vertically opposite angle $72°$ है। adjacent angle?

**हल:** $180-72=\mathbf{108°}$।

**PYQ 3.** *(RRB NTPC)* Triangle angles $2x,3x,4x$ हैं। angles?

**हल:** $9x=180$ ⟹ $\mathbf{40°,60°,80°}$।

**PYQ 4.** *(IBPS Clerk)* Parallel lines में co-interior angles $(3x+10)°$, $(5x-30)°$ हैं। $x$?

**हल:** sum $180$ ⟹ $\mathbf{x=25}$।

**PYQ 5.** *(UP Police SI)* Hexagon interior angle sum?

**हल:** $(6-2)180=\mathbf{720°}$।

**PYQ 6.** *(SSC MTS)* Regular polygon का exterior angle $30°$ है। sides?

**हल:** $360/30=\mathbf{12}$।

---

## 33.15 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | $35°$ का complementary angle | $55°$ | sum $90$ |
| 2 | $65°$ का supplementary angle | $115°$ | sum $180$ |
| 3 | linear pair: one $72°$ | $108°$ | $180-72$ |
| 4 | vertically opposite one $84°$ | $84°$ | opposite equal |
| 5 | around point: $80,90,70,x$ | $120°$ | sum $360$ |
| 6 | bisector of $80°$ | $40°$ each | halve |
| 7 | bisector parts $3x+5$, $5x-15$ | $x=10$ | equal parts |
| 8 | corresponding angle to $65°$ | $65°$ | parallel lines |
| 9 | co-interior: one $72°$ | $108°$ | sum $180$ |
| 10 | vertical lines: angles $2x+10$, $4x-30$ | $x=20$ | equal |
| 11 | triangle angles $2x,3x,4x$ | $40,60,80°$ | sum $180$ |
| 12 | triangle angles $45°,65°$ | third $70°$ | sum $180$ |
| 13 | isosceles vertex angle $40°$ | base $70°$ each | equal base angles |
| 14 | exterior remote angles $50°,70°$ | $120°$ | exterior theorem |
| 15 | exterior $130°$, remote $55°$ | other $75°$ | difference |
| 16 | exterior $4x+10$, remote $2x+5,x+20$ | $x=15$ | theorem |
| 17 | hexagon interior sum | $720°$ | $(n-2)180$ |
| 18 | polygon sum $900°$ | 7 sides | solve n |
| 19 | hexagon diagonals | 9 | $n(n-3)/2$ |
| 20 | regular octagon interior | $135°$ | $180-360/8$ |
| 21 | regular polygon exterior $30°$ | 12 sides | $360/e$ |
| 22 | $l\parallel m$, alternate angle $78°$ | $78°$ | equal |
| 23 | $l\parallel m$, same-side angle $112°$ | other $68°$ | sum $180$ |
| 24 | perpendicular lines | four $90°$ angles | definition |
| 25 | regular decagon exterior angle | $36°$ | $360/10$ |

---

## 33.16 :icon-trophy: अध्याय का सार

```
━━━ Basic objects ━━━
line: both directions infinite
ray: one endpoint
segment: two endpoints
transversal: line crossing two or more lines

━━━ Angle sums ━━━
right angle = 90°
straight line = 180°
around a point = 360°
complementary = 90°
supplementary = 180°

━━━ Intersecting lines ━━━
vertically opposite angles equal
linear pair sum 180°

━━━ Parallel lines ━━━
corresponding equal
alternate interior equal
alternate exterior equal
co-interior sum 180°

━━━ Triangle ━━━
interior sum = 180°
exterior = two remote interior angles

━━━ Polygon ━━━
interior sum = (n−2)×180°
diagonals = n(n−3)/2
regular exterior = 360°/n
regular interior = 180°−360°/n

━━━ Angle chase ━━━
relation पहचानिए
known angle copy कीजिए
90/180/360 लगाइए
range और diagram check कीजिए
```

> :icon-trophy: **Part 5 की geometry अब lines और angles से शुरू हुई।** Parallel lines, triangles और polygons के सभी आगे के diagrams इसी angle language पर आधारित होंगे।
>
> **आगे:** Chapter 34 — **त्रिभुज — प्रकार, गुण और चारों केन्द्र (Triangles & Four Centres)**।
