# अध्याय 36 — चतुर्भुज व बहुभुज (Quadrilaterals & Polygons)

## 36.1 :icon-target: परिचय व वेटेज

Chapter 34–35 में triangles की properties, congruence और similarity पढ़ी। अब चार sides वाले figures और अनेक sides वाले polygons की geometry करेंगे। Quadrilateral के type को पहचानना जरूरी है क्योंकि हर type के diagonals, angles और area rules अलग हो सकते हैं।

> *"किस quadrilateral में diagonals एक-दूसरे को bisect करते हैं? किसमें वे equal भी होते हैं?"*

Parallelogram में diagonals bisect करते हैं; rectangle में वे equal भी होते हैं; rhombus में perpendicular भी होते हैं; square में दोनों properties साथ मिलती हैं।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | quadrilateral properties |
| **SSC CGL Tier-2** | **2–3** | diagonals, cyclic quadrilateral |
| SSC CHSL / MTS / GD | 1–2 | angle sum और area |
| **SSC CPO** | **2** | rectangle, rhombus, polygon |
| **IBPS / SBI PO** | 1–2 | geometry reasoning |
| IBPS / SBI Clerk | 1 | direct properties |
| **RRB NTPC / ALP** | **2–3** | quadrilaterals और polygons |
| UP Police SI / Constable | 1–2 | angle and area |
| UPSSSC PET | 1 | basic polygon rules |
| Super TET / UPTET | 1–2 | visual classification |

> :icon-key: **पूरे अध्याय का एक वाक्य:** पहले quadrilateral का type पहचानिए, फिर उसके sides, angles, diagonals और area की specific property लगाइए।

---

## 36.2 :icon-number: Quadrilateral की मूल properties

चार sides वाले closed figure को quadrilateral कहते हैं। इसके चार interior angles का sum —

$$\text{sum of angles}=(4-2)\times180=\mathbf{360°}$$

### General quadrilateral

- 4 sides
- 4 vertices
- 2 diagonals
- interior angle sum $360°$

**उदाहरण 1.** Quadrilateral के तीन angles $80°,95°,110°$ हैं। चौथा angle?

$$x=360-(80+95+110)=\mathbf{75°}$$

### मुख्य प्रकार

| Figure | मुख्य पहचान |
|---|---|
| Parallelogram | opposite sides parallel और equal |
| Rectangle | चार right angles; opposite sides equal |
| Square | चार equal sides और चार right angles |
| Rhombus | चार equal sides; opposite angles equal |
| Kite | दो pairs adjacent equal sides |
| Trapezium | एक pair opposite sides parallel |

```figure
type: quad-types
shape: parallelogram
caption: parallelogram में opposite sides parallel और equal होती हैं
```

```figure
type: quad-types
shape: rectangle
caption: rectangle में चारों angles 90° और diagonals equal होते हैं
```

```figure
type: quad-types
shape: square
caption: square rectangle और rhombus दोनों की properties रखता है
```

```figure
type: quad-types
shape: rhombus
caption: rhombus में चारों sides equal और diagonals perpendicular होते हैं
```

```figure
type: quad-types
shape: kite
caption: kite में adjacent sides के दो pairs equal होते हैं
```

```figure
type: quad-types
shape: trapezium
caption: trapezium में कम से कम एक pair opposite sides parallel होती हैं
```

---

## 36.3 :icon-calc: Parallelogram

Parallelogram में:

1. Opposite sides parallel और equal:

$$AB\parallel CD,\quad BC\parallel AD$$

$$AB=CD,\quad BC=AD$$

2. Opposite angles equal।
3. Adjacent angles supplementary।
4. Diagonals एक-दूसरे को bisect करते हैं।
5. एक diagonal इसे दो congruent triangles में बाँटता है।

**उदाहरण 2.** Parallelogram में एक angle $65°$ है। बाकी angles?

- opposite angle $=65°$
- दोनों adjacent $=180-65=115°$

अर्थात angles $\mathbf{65°,115°,65°,115°}$।

**उदाहरण 3.** Parallelogram के diagonals एक-दूसरे को $O$ पर काटते हैं। यदि $AO=8$ cm, तो $OC$?

Diagonals bisect होते हैं:

$$AO=OC=\mathbf{8\text{ cm}}$$

### Parallelogram की पहचान

यदि किसी quadrilateral में:

- दोनों pairs opposite sides equal, या
- एक pair opposite sides parallel और equal, या
- diagonals एक-दूसरे को bisect करें

तो वह parallelogram सिद्ध किया जा सकता है।

---

## 36.4 :icon-ruler: Rectangle और square

### Rectangle

Rectangle एक parallelogram है जिसमें सभी angles $90°$ होते हैं।

Properties:

- opposite sides equal और parallel
- सभी angles $90°$
- diagonals equal
- diagonals एक-दूसरे को bisect करते हैं

**उदाहरण 4.** Rectangle की length $12$ cm और breadth $5$ cm है। Diagonal?

Pythagoras से:

$$d=\sqrt{12^2+5^2}=\sqrt{169}=\mathbf{13\text{ cm}}$$

### Square

Square एक साथ rectangle और rhombus है।

Properties:

- चारों sides equal
- चारों angles $90°$
- diagonals equal
- diagonals perpendicular
- diagonals angles को bisect करते हैं
- diagonals एक-दूसरे को bisect करते हैं

**उदाहरण 5.** Square की side $a$ हो तो diagonal?

$$d=\sqrt{a^2+a^2}=\mathbf{a\sqrt{2}}$$

---

## 36.5 :icon-steps: Rhombus और kite

### Rhombus

Rhombus में चारों sides equal होती हैं, लेकिन angles जरूरी नहीं कि $90°$ हों।

Properties:

- opposite sides parallel
- opposite angles equal
- adjacent angles supplementary
- diagonals perpendicular
- diagonals एक-दूसरे को bisect करते हैं
- diagonals opposite angles को bisect करते हैं

```figure
type: quad-diagonals
shape: rhombus
caption: rhombus के diagonals perpendicular होकर एक-दूसरे को bisect करते हैं
```

**उदाहरण 6.** Rhombus के diagonals $16$ cm और $12$ cm हैं। Area?

$$\text{area}=\frac{1}{2}d_1d_2=\frac{1}{2}\times16\times12=\mathbf{96\text{ cm}^2}$$

### Kite

Kite में two pairs of adjacent equal sides होती हैं।

Properties:

- diagonals perpendicular हो सकते हैं
- एक diagonal दूसरे को bisect करती है
- एक diagonal opposite angles को bisect करती है
- सामान्य kite में दोनों diagonals equal होना जरूरी नहीं

**उदाहरण 7.** Kite के diagonals $10$ cm और $16$ cm हैं, और वे perpendicular हैं। Area?

$$\text{area}=\frac{1}{2}\times10\times16=\mathbf{80\text{ cm}^2}$$

> :icon-warn: Rhombus और kite दोनों में perpendicular diagonals हो सकते हैं, लेकिन rhombus में चारों sides equal; kite में adjacent pairs equal।

---

## 36.6 :icon-chart: Diagonals की तुलना

```figure
type: quad-diagonals
shape: parallelogram
caption: parallelogram के diagonals एक-दूसरे को bisect करते हैं
```

```figure
type: quad-diagonals
shape: rectangle
caption: rectangle के diagonals equal और bisecting होते हैं
```

| Quadrilateral | Diagonals की property |
|---|---|
| General quadrilateral | कोई सामान्य equality जरूरी नहीं |
| Parallelogram | bisect each other |
| Rectangle | equal और bisect each other |
| Rhombus | perpendicular और bisect each other |
| Square | equal, perpendicular और bisect each other |
| Kite | सामान्यतः एक diagonal दूसरी को bisect करती है |

**उदाहरण 8.** Quadrilateral के diagonals equal और एक-दूसरे को bisect करते हैं। यह कौन-सा special quadrilateral हो सकता है?

उत्तर: Rectangle; यदि perpendicular भी हों तो Square।

---

## 36.7 :icon-chart: Cyclic quadrilateral

जिस quadrilateral के चारों vertices एक ही circle पर हों, वह cyclic quadrilateral है।

```figure
type: cyclic-quad
caption: cyclic quadrilateral में opposite angles supplementary होते हैं
```

Properties:

1. Opposite angles supplementary:

$$\angle A+\angle C=180°$$

$$\angle B+\angle D=180°$$

2. Exterior angle opposite interior angle के बराबर होता है।
3. Converse: यदि opposite angles का sum $180°$ हो, तो quadrilateral cyclic हो सकता है।

**उदाहरण 9.** Cyclic quadrilateral में $\angle A=72°$। Opposite $\angle C$?

$$C=180-72=\mathbf{108°}$$

**उदाहरण 10.** Cyclic quadrilateral के opposite angles $(3x+10)°$ और $(5x-30)°$ हैं। $x$?

$$3x+10+5x-30=180$$

$$8x-20=180\quad\Rightarrow\quad x=\mathbf{25}$$

Angles $85°$ और $95°$।

---

## 36.8 :icon-chart: Polygons और diagonals

$n$ sides वाले polygon का interior angle sum:

$$S=(n-2)\times180°$$

एक vertex से diagonals:

$$n-3$$

Total diagonals:

$$D=\frac{n(n-3)}{2}$$

```figure
type: polygon-diagonals
sides: 7
caption: heptagon में एक vertex से 4 diagonals और कुल 14 diagonals होते हैं
```

**उदाहरण 11.** Heptagon ($n=7$) के interior sum और diagonals?

- interior sum $=(7-2)180=\mathbf{900°}$
- one vertex diagonals $=7-3=\mathbf{4}$
- total diagonals $=7(4)/2=\mathbf{14}$

### Regular polygon

```figure
type: regular-polygon36
sides: 8
caption: regular polygon में equal sides और equal exterior turns होते हैं
```

Regular $n$-gon:

$$\text{exterior angle}=\frac{360°}{n}$$

$$\text{interior angle}=180°-\frac{360°}{n}$$

**उदाहरण 12.** Regular decagon का प्रत्येक exterior और interior angle?

- exterior $=360/10=\mathbf{36°}$
- interior $=180-36=\mathbf{144°}$

---

## 36.9 :icon-ruler: Trapezium और mid-segment

Trapezium में एक pair parallel bases होती हैं। यदि parallel bases की lengths $a,b$ और height $h$ हो:

$$\text{area}=\frac{1}{2}(a+b)h$$

यदि दोनों non-parallel sides के midpoints join करें, तो mid-segment bases के parallel होता है और उसकी length:

$$m=\frac{a+b}{2}$$

```figure
type: trapezium-midline
a: 14
b: 8
height: 6
caption: trapezium का mid-segment दोनों bases के average के बराबर होता है
```

**उदाहरण 13.** Bases $14$ cm और $8$ cm हैं। Mid-segment?

$$m=\frac{14+8}{2}=\mathbf{11\text{ cm}}$$

**उदाहरण 14.** Bases $14,8$ cm और height $6$ cm। Area?

$$A=\frac{1}{2}(14+8)6=\mathbf{66\text{ cm}^2}$$

---

## 36.10 :icon-divide: Quadrilateral areas

```figure
type: quad-area
shape: parallelogram
caption: parallelogram का area base और perpendicular height से
```

```figure
type: quad-area
shape: rhombus
caption: rhombus का area diagonals के half-product से
```

```figure
type: quad-area
shape: trapezium
caption: trapezium का area parallel bases के average times height है
```

### Formulas

| Figure | Area |
|---|---|
| Rectangle | $l\times b$ |
| Square | $a^2$ |
| Parallelogram | $b\times h$ |
| Rhombus | $\frac{1}{2}d_1d_2$ |
| Kite | $\frac{1}{2}d_1d_2$ |
| Trapezium | $\frac{1}{2}(a+b)h$ |

**उदाहरण 15.** Parallelogram का base $15$ cm और height $8$ cm है। Area?

$$A=15\times8=\mathbf{120\text{ cm}^2}$$

**उदाहरण 16.** Rhombus diagonals $18$ और $10$ cm।

$$A=\frac{1}{2}\times18\times10=\mathbf{90\text{ cm}^2}$$

**उदाहरण 17.** Trapezium bases $20,12$ cm और height $5$ cm।

$$A=\frac{1}{2}(20+12)5=\mathbf{80\text{ cm}^2}$$

---

## 36.11 :icon-bulb: Shortcuts और identification tests

### :icon-timer: Shortcut 1 — quadrilateral angle sum

किसी भी quadrilateral में:

$$\sum\text{angles}=360°$$

दो triangles में divide करके proof किया जा सकता है।

### :icon-timer: Shortcut 2 — parallelogram tests

यदि opposite sides equal, या one opposite pair parallel और equal, या diagonals bisect करें—parallelogram सिद्ध हो सकता है।

### :icon-timer: Shortcut 3 — special hierarchy

$$\text{square}\subset\text{rectangle and rhombus}\subset\text{parallelogram}\subset\text{quadrilateral}$$

हर square rectangle है, लेकिन हर rectangle square नहीं।

### :icon-timer: Shortcut 4 — polygon

$$n=\frac{\text{interior sum}}{180}+2$$

यह तभी जब interior sum total दिया हो।

### :icon-timer: Shortcut 5 — regular polygon

$$n=\frac{360}{\text{exterior angle}}$$

Interior angle दिया हो तो पहले exterior $=180-interior$ निकालें।

### :icon-timer: Shortcut 6 — cyclic quadrilateral

Opposite angle मिलते ही $180°$ से subtract करें।

### :icon-timer: Shortcut 7 — area selection

- Parallel bases? Trapezium formula
- Perpendicular diagonals? Half-product
- Base and perpendicular height? Base × height
- Four right angles? Rectangle/square formula

---

## 36.12 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** हर quadrilateral को parallelogram मान लेना।
> Opposite sides parallel/equal का proof या marking चाहिए।

> :icon-cross: **जाल 2.** Rectangle के diagonals perpendicular मानना।
> Rectangle में diagonals equal और bisect होते हैं; perpendicular सामान्यतः नहीं।

> :icon-cross: **जाल 3.** Rhombus के diagonals हमेशा equal मानना।
> Rhombus में perpendicular/bisecting, equal केवल square में guaranteed।

> :icon-cross: **जाल 4.** Kite में opposite sides equal लिखना।
> Kite में adjacent sides के दो pairs equal होते हैं।

> :icon-cross: **जाल 5.** Cyclic quadrilateral के adjacent angles का sum 180 लेना।
> Opposite angles supplementary होते हैं।

> :icon-cross: **जाल 6.** Polygon diagonals का formula $n(n-1)/2$ लगाना।
> सही formula $n(n-3)/2$ है।

> :icon-cross: **जाल 7.** Regular polygon के interior angle को $360/n$ लेना।
> $360/n$ exterior angle है।

> :icon-cross: **जाल 8.** Trapezium mid-segment में bases का difference लेना।
> Mid-segment $=(a+b)/2$ average है।

> :icon-cross: **जाल 9.** Rhombus/kite area में diagonals का पूरा product लेना।
> Area $=\frac{1}{2}d_1d_2$।

> :icon-cross: **जाल 10.** Figure को देखकर property assume करना।
> Equal-side ticks, parallel arrows और right-angle marks को evidence मानें।

---

## 36.13 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* Quadrilateral के तीन angles $80°,95°,110°$ हैं। चौथा?

**हल:** $\mathbf{75°}$।

**PYQ 2.** *(SSC CHSL)* Parallelogram का एक angle $65°$। adjacent angle?

**हल:** $\mathbf{115°}$।

**PYQ 3.** *(RRB NTPC)* Rhombus diagonals $16,12$ cm। Area?

**हल:** $\mathbf{96\text{ cm}^2}$।

**PYQ 4.** *(IBPS Clerk)* Cyclic quadrilateral में one angle $72°$। opposite?

**हल:** $\mathbf{108°}$।

**PYQ 5.** *(UP Police SI)* Hexagon diagonals और interior sum?

**हल:** $\mathbf{9}$ diagonals, $\mathbf{720°}$ sum।

**PYQ 6.** *(SSC MTS)* Trapezium bases $14,8$ cm। Mid-segment?

**हल:** $\mathbf{11}$ cm।

---

## 36.14 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | Quadrilateral angle sum | $360°$ | $(4-2)180$ |
| 2 | angles $80,95,110$; fourth | $75°$ | subtract |
| 3 | parallelogram angle $65°$; adjacent | $115°$ | supplementary |
| 4 | parallelogram diagonal half $AO=8$ | $OC=8$ | bisect |
| 5 | rectangle $12\times5$ diagonal | $13$ | Pythagoras |
| 6 | square side $a$ diagonal | $a\sqrt{2}$ | Pythagoras |
| 7 | rhombus diagonals $16,12$ area | $96$ | half-product |
| 8 | kite diagonals $10,16$ area | $80$ | half-product |
| 9 | cyclic angle $72°$ opposite | $108°$ | supplementary |
| 10 | cyclic opposite $(3x+10),(5x-30)$ | $x=25$ | sum $180$ |
| 11 | heptagon interior sum | $900°$ | $(n-2)180$ |
| 12 | heptagon total diagonals | $14$ | $n(n-3)/2$ |
| 13 | regular octagon interior | $135°$ | $180-360/8$ |
| 14 | exterior $30°$ regular polygon | 12 sides | $360/e$ |
| 15 | trapezium bases $14,8$ midline | $11$ | average |
| 16 | trapezium bases $14,8$, h=6 area | $66$ | half sum × h |
| 17 | parallelogram b=15,h=8 area | $120$ | $bh$ |
| 18 | rhombus d=18,10 area | $90$ | half-product |
| 19 | square has which diagonal properties? | equal, perpendicular, bisect | square |
| 20 | rectangle diagonals | equal and bisect | property |
| 21 | rhombus diagonals | perpendicular and bisect | property |
| 22 | kite sides | two adjacent equal pairs | definition |
| 23 | polygon sum $1080°$ | 8 sides | solve n |
| 24 | regular decagon exterior | $36°$ | $360/10$ |
| 25 | $a=20,b=12,h=5$ trapezium area | $80$ | formula |

---

## 36.15 :icon-trophy: अध्याय का सार

```
━━━ Quadrilateral ━━━
4 sides, 2 diagonals
angle sum = 360°

━━━ Parallelogram ━━━
opposite sides parallel and equal
opposite angles equal
adjacent angles supplementary
diagonals bisect each other

━━━ Rectangle ━━━
all angles 90°
diagonals equal and bisect

━━━ Square ━━━
rectangle + rhombus
all sides equal
all angles 90°
diagonals equal, perpendicular and bisect

━━━ Rhombus ━━━
all sides equal
diagonals perpendicular and bisect

━━━ Kite ━━━
two pairs adjacent equal sides
diagonals perpendicular; one bisects other

━━━ Cyclic quadrilateral ━━━
opposite angles sum 180°

━━━ Polygon ━━━
interior sum = (n−2)×180°
diagonals = n(n−3)/2
regular exterior = 360°/n

━━━ Trapezium ━━━
area = 1/2(a+b)h
mid-segment = (a+b)/2

━━━ Areas ━━━
parallelogram = bh
rhombus/kite = 1/2 d₁d₂
rectangle = lb
square = a²
```

> :icon-trophy: **Quadrilaterals और polygons का visual property map तैयार है।** आगे circles में cyclic quadrilateral, chords और tangents की properties और अधिक महत्वपूर्ण होंगी।
>
> **आगे:** Chapter 37 — **वृत्त, जीवा, स्पर्श रेखा और उभयनिष्ठ स्पर्श रेखाएँ (Circles & Tangents)**।
