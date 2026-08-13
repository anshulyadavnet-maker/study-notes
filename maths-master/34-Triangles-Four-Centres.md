# अध्याय 34 — त्रिभुज: प्रकार, गुण व चारों केन्द्र (Triangles & Four Centres)

## 34.1 :icon-target: परिचय व वेटेज

Chapter 33 में हमने lines और angles की language सीखी। अब उन्हीं angles और segments को triangle में लागू करेंगे। Triangle geometry का सबसे अधिक उपयोग होने वाला figure है—इसके centres, medians, altitudes, angle bisectors और side-angle relations आगे circles, mensuration और trigonometry में बार-बार आएँगे।

> *"किसी triangle की sides 5, 6 और 8 हैं। क्या triangle बन सकता है? और सबसे बड़ी side के सामने कौन-सा angle सबसे बड़ा होगा?"*

पहले triangle inequality जाँचेंगे, फिर side-angle relation। Diagram को केवल drawing न मानकर properties का map समझिए।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **2–3** | triangle properties, centres |
| **SSC CGL Tier-2** | **3–5** | medians, altitudes, angle chase |
| SSC CHSL / MTS / GD | 1–2 | angle sum और classification |
| **SSC CPO** | **2–3** | triangle centres और similarity base |
| **IBPS / SBI PO** | 1–2 | geometry reasoning |
| IBPS / SBI Clerk | 1 | basic triangle rules |
| **RRB NTPC / ALP** | **2–3** | triangle and angles |
| UP Police SI / Constable | 1–2 | triangle properties |
| UPSSSC PET | 1 | elementary geometry |
| Super TET / UPTET | 2–3 | triangle teaching diagrams |

> :icon-key: **पूरे अध्याय का एक वाक्य:** Triangle में side, angle और special lines की relation पहचानिए; चार centres को उनके defining lines से याद कीजिए।

---

## 34.2 :icon-number: Triangle की classification

### Sides के आधार पर

| प्रकार | पहचान |
|---|---|
| Equilateral | तीनों sides equal; प्रत्येक angle $60°$ |
| Isosceles | दो sides equal; उनके opposite base angles equal |
| Scalene | तीनों sides अलग |

```figure
type: triangle-classify
kind: equilateral
caption: equilateral triangle में तीन equal sides और तीन 60° angles होते हैं
```

```figure
type: triangle-classify
kind: isosceles
caption: isosceles triangle में equal sides के opposite angles equal होते हैं
```

### Angles के आधार पर

| प्रकार | पहचान |
|---|---|
| Acute | तीनों angles $90°$ से छोटे |
| Right | एक angle exactly $90°$ |
| Obtuse | एक angle $90°$ से बड़ा |

```figure
type: triangle-classify
kind: right
caption: right triangle में एक perpendicular pair और 90° angle होता है
```

> :icon-warn: एक triangle में दो right या दो obtuse angles नहीं हो सकते, क्योंकि तीन angles का sum $180°$ है।

### Fundamental angle sum

$$\angle A+\angle B+\angle C=180°$$

**उदाहरण 1.** Triangle के angles $2x,3x,4x$ हैं।

$$2x+3x+4x=180\quad\Rightarrow\quad x=20$$

Angles $=\mathbf{40°,60°,80°}$।

---

## 34.3 :icon-ruler: Triangle inequality और side-angle relation

### Triangle inequality

किसी भी triangle में दो sides का sum तीसरी side से बड़ा होना चाहिए:

$$a+b>c,\qquad b+c>a,\qquad c+a>b$$

```figure
type: triangle-inequality
a: 5
b: 6
c: 8
caption: तीनों pair sums तीसरी side से बड़े हों तभी triangle संभव है
```

**उदाहरण 2.** Sides $5,6,8$ triangle बना सकती हैं?

- $5+6>8$ ✔
- $6+8>5$ ✔
- $8+5>6$ ✔

अतः triangle संभव है।

**उदाहरण 3.** Sides $3,4,8$।

$3+4=7<8$। इसलिए triangle बनना असम्भव है।

### Larger side और larger opposite angle

Triangle में:

- सबसे बड़ी side के सामने सबसे बड़ा angle
- बराबर sides के सामने बराबर angles
- सबसे छोटी side के सामने सबसे छोटा angle

```figure
type: side-angle
caption: side और उसके opposite angle की size साथ-साथ compare कीजिए
```

**उदाहरण 4.** Sides $7,9,12$ में सबसे बड़ा angle किसके opposite होगा?

सबसे बड़ी side $12$ है, इसलिए सबसे बड़ा angle $12$ के opposite होगा।

### Triangle area की basic relation

Base $b$ और corresponding perpendicular height $h$ हो:

$$\text{area}=\frac{1}{2}bh$$

**उदाहरण 5.** Base $12$ cm और height $7$ cm।

$$\text{area}=\frac{1}{2}\times12\times7=\mathbf{42\text{ cm}^2}$$

---

## 34.4 :icon-steps: Triangle की special lines

### Median (माध्यिका)

Vertex से opposite side के midpoint तक खींचा गया segment median है। तीनों medians centroid पर मिलते हैं।

```figure
type: median
caption: median opposite side को दो equal parts में बाँटती है
```

यदि $M$ side $BC$ का midpoint है:

$$BM=MC$$

Centroid $G$ median को vertex से midpoint की दिशा में $2:1$ में बाँटता है:

$$AG:GM=2:1$$

**उदाहरण 6.** Median $AM=15$ cm है। Centroid के लिए $AG$ और $GM$?

कुल ratio $3$ parts:

$$AG=\frac{2}{3}\times15=\mathbf{10\text{ cm}},\qquad GM=\frac{1}{3}\times15=\mathbf{5\text{ cm}}$$

### Altitude (लम्ब)

Vertex से opposite side या उसके extension पर खींचा गया perpendicular segment altitude है।

```figure
type: altitude
caption: altitude opposite side पर 90° बनाती है और height देती है
```

यदि $AH$ altitude है:

$$AH\perp BC$$

और area:

$$\text{area}=\frac{1}{2}\times BC\times AH$$

### Angle bisector

Vertex angle को दो equal angles में बाँटने वाली line angle bisector है।

```figure
type: triangle-bisector
caption: तीन angle bisectors incentre पर मिलती हैं
```

Angle Bisector Theorem:

यदि $AD$ angle $A$ को bisect करे, तो —

$$\frac{BD}{DC}=\frac{AB}{AC}$$

**उदाहरण 7.** $AB=6$, $AC=9$ और $BC=10$ cm। Angle bisector $AD$ side $BC$ को किस ratio में बाँटेगी?

$$BD:DC=AB:AC=6:9=\mathbf{2:3}$$

### Perpendicular bisector

किसी side के midpoint पर perpendicular line, उस side का perpendicular bisector है। इस line पर स्थित हर point, side के दोनों endpoints से equal distance पर होता है। तीन perpendicular bisectors circumcentre पर मिलती हैं।

---

## 34.5 :icon-star: चारों Centres — एक नजर में

Triangle के चार प्रसिद्ध centres हैं। इन्हें defining lines से याद करें:

| Centre | किन lines का intersection? | मुख्य property |
|---|---|---|
| Centroid $G$ | तीन medians | median को $2:1$ में बाँटता है |
| Incentre $I$ | तीन angle bisectors | sides से equal perpendicular distance |
| Circumcentre $O$ | perpendicular bisectors | तीन vertices से equal distance |
| Orthocentre $H$ | तीन altitudes | altitudes का common point |

> :icon-key: Mnemonic: **M-A-P-E** — Median → Centroid, Angle bisector → Incentre, Perpendicular bisector → Circumcentre, Altitude → Orthocentre।

---

## 34.6 :icon-calc: Centroid — गुरुत्व केन्द्र

Centroid $G$ तीनों medians का intersection है।

Properties:

1. हर triangle में centroid triangle के **अन्दर** होता है।
2. हर median को vertex से $2:1$ ratio में बाँटता है।
3. इसे centre of gravity भी कहते हैं।
4. तीनों medians triangle को equal-area छोटे triangles में बाँटती हैं।

```figure
type: triangle-centre34
centre: centroid
caption: तीन medians centroid G पर मिलती हैं और प्रत्येक median 2:1 में विभाजित होती है
```

**उदाहरण 8.** $AG=12$ cm और $GM$?

$AG:GM=2:1$। इसलिए $GM=\mathbf{6}$ cm।

**उदाहरण 9.** Median की total length $27$ cm हो तो vertex से centroid तक distance?

$$AG=\frac{2}{3}\times27=\mathbf{18\text{ cm}}$$

और $GM=9$ cm।

---

## 34.7 :icon-divide: Incentre — अन्तःकेन्द्र

Incentre $I$ तीनों internal angle bisectors का intersection है।

Properties:

1. यह हमेशा triangle के अन्दर होता है।
2. तीनों sides से इसकी perpendicular distance equal होती है।
3. यह incircle का centre है।
4. Incircle triangle की तीनों sides को touch करती है।
5. यदि inradius $r$ और semiperimeter $s$ हो, तो area:

$$\text{area}=r\times s$$

```figure
type: triangle-centre34
centre: incentre
caption: तीन angle bisectors incentre I पर मिलती हैं; I sides से समान दूरी पर है
```

**उदाहरण 10.** Triangle का semiperimeter $15$ cm और inradius $4$ cm है। Area?

$$\text{area}=r\times s=4\times15=\mathbf{60\text{ cm}^2}$$

**उदाहरण 11.** यदि तीन angle bisectors एक point पर मिलती हैं, तो वह कौन-सा centre है?

उत्तर: **Incentre**।

---

## 34.8 :icon-ruler: Circumcentre — परिकेन्द्र

Circumcentre $O$ तीनों sides के perpendicular bisectors का intersection है।

Properties:

1. $O$ तीनों vertices से equal distance पर होता है:

$$OA=OB=OC=R$$

2. यह circumcircle का centre है, जो तीनों vertices से गुजरती है।
3. Acute triangle में $O$ triangle के अन्दर।
4. Right triangle में $O$ hypotenuse का midpoint।
5. Obtuse triangle में $O$ triangle के बाहर।

```figure
type: triangle-centre34
centre: circumcentre
caption: perpendicular bisectors circumcentre O पर मिलती हैं और OA=OB=OC
```

**उदाहरण 12.** Right triangle की hypotenuse $10$ cm है। Circumradius?

Right triangle में circumcentre hypotenuse का midpoint होता है:

$$R=\frac{10}{2}=\mathbf{5\text{ cm}}$$

**उदाहरण 13.** यदि $OA=OB=OC=7$ cm है, तो circumradius?

$R=\mathbf{7}$ cm।

---

## 34.9 :icon-chart: Orthocentre — लम्बकेन्द्र

Orthocentre $H$ तीनों altitudes का intersection है।

Properties:

1. Acute triangle में $H$ अन्दर।
2. Right triangle में $H$ right-angle vertex पर।
3. Obtuse triangle में $H$ triangle के बाहर।
4. Altitude वह line है जो vertex से opposite side या उसके extension पर perpendicular होती है।

```figure
type: triangle-centre34
centre: orthocentre
caption: तीन altitudes orthocentre H पर मिलती हैं
```

**उदाहरण 14.** Right triangle का right-angle vertex $A$ है। Orthocentre कहाँ होगा?

उत्तर: $\mathbf{A}$ पर।

**उदाहरण 15.** यदि किसी acute triangle की दो altitudes draw की गई हैं, तो तीसरी altitude भी उसी common point से गुजरेगी। इस common point को कहते हैं?

उत्तर: **Orthocentre**।

---

## 34.10 :icon-brain: Euler line और special triangles

Non-equilateral triangle में Centroid $G$, Circumcentre $O$ और Orthocentre $H$ एक ही straight line पर होते हैं। इसे Euler line कहते हैं।

$$O,G,H\text{ are collinear}$$

और सामान्य triangle में:

$$OH=3OG$$

```figure
type: euler-line
caption: O, G और H Euler line पर collinear होते हैं और OH=3OG
```

### Right triangle

```figure
type: right-triangle-centres
caption: right triangle में H right vertex और O hypotenuse midpoint होता है
```

Right triangle में:

- $H$ right-angle vertex पर
- $O$ hypotenuse midpoint पर
- $G$ medians के intersection पर

### Equilateral triangle

```figure
type: equilateral-centres
caption: equilateral triangle में चारों centres एक ही point पर coincide करते हैं
```

Equilateral triangle में:

$$G=I=O=H$$

Median, altitude, angle bisector और perpendicular bisector एक ही line बन जाते हैं।

> :icon-star: Special triangle देखते ही centre location याद करें: right में $H$ vertex और $O$ hypotenuse midpoint; equilateral में सभी centres एक।

---

## 34.11 :icon-bulb: Shortcuts, theorems और proofs

### :icon-timer: Shortcut 1 — triangle validity

Sides $a,b,c$ के लिए केवल सबसे बड़ी side check करना काफी है:

$$\text{largest side}<\text{sum of other two sides}$$

यदि यह condition satisfy है, बाकी दो automatically satisfy होंगे क्योंकि largest side ही सबसे कठिन condition है।

### :icon-timer: Shortcut 2 — side-angle order

$$a>b\quad\Rightarrow\quad A>B$$

जहाँ $a$ के opposite angle $A$ है।

### :icon-timer: Shortcut 3 — median ratio

$$AG:GM=2:1$$

यदि total median $m$ है:

$$AG=\frac{2}{3}m,\qquad GM=\frac{1}{3}m$$

### :icon-timer: Shortcut 4 — angle bisector theorem

$$\frac{BD}{DC}=\frac{AB}{AC}$$

Side ratio को angle bisector के opposite side segments में copy करें।

### :icon-timer: Shortcut 5 — triangle area

$$K=\frac{1}{2}bh$$

यदि sides $a,b,c$ और semiperimeter $s$ दिए हों, तो Heron formula:

$$K=\sqrt{s(s-a)(s-b)(s-c)}$$

### :icon-timer: Shortcut 6 — centre पहचान

| Diagram में दिखे | Centre |
|---|---|
| medians | centroid |
| angle bisectors | incentre |
| perpendicular bisectors | circumcentre |
| altitudes | orthocentre |

### :icon-timer: Shortcut 7 — Euler line

यदि question $O,G,H$ के बीच distance दे:

$$OH=3OG$$

और यदि $OG=4$ cm, तो $OH=12$ cm।

---

## 34.12 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Median और altitude को एक ही समझना।
> Median midpoint पर जाती है; altitude 90° बनाती है। सामान्य triangle में दोनों अलग हो सकती हैं।

> :icon-cross: **जाल 2.** Incentre और circumcentre की defining lines बदलना।
> Incentre: angle bisectors; circumcentre: perpendicular bisectors।

> :icon-cross: **जाल 3.** Centroid ratio $1:2$ उलटा लिखना।
> Vertex से centroid : centroid से midpoint $=2:1$।

> :icon-cross: **जाल 4.** Circumcentre को हमेशा triangle के अन्दर रखना।
> Obtuse triangle में circumcentre बाहर होता है।

> :icon-cross: **जाल 5.** Orthocentre को हमेशा अन्दर मानना।
> Right triangle में vertex पर और obtuse triangle में बाहर हो सकता है।

> :icon-cross: **जाल 6.** Triangle inequality में केवल दो sides का sum देखना।
> सबसे बड़ी side बाकी दो के sum से छोटी होनी चाहिए।

> :icon-cross: **जाल 7.** Larger side के सामने smaller angle लिखना।
> Larger side के opposite angle larger होता है।

> :icon-cross: **जाल 8.** Exterior angle को adjacent interior angle का बराबर मानना।
> Exterior angle remote interior angles के sum के बराबर है।

> :icon-cross: **जाल 9.** Right triangle में circumcentre को right vertex मानना।
> Right vertex orthocentre है; circumcentre hypotenuse का midpoint है।

> :icon-cross: **जाल 10.** Figure को scale के अनुसार देखकर theorem लगाना।
> हमेशा markings, perpendicular signs और given values follow करें।

---

## 34.13 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* Sides $3,4,8$ से triangle बन सकता है?

**हल:** $3+4<8$ ⟹ **नहीं**।

**PYQ 2.** *(SSC CHSL)* Median की length $27$ cm है। Centroid से midpoint distance?

**हल:** $GM=27/3=\mathbf{9}$ cm।

**PYQ 3.** *(RRB NTPC)* Triangle के दो angles $45°,65°$ हैं। तीसरा?

**हल:** $\mathbf{70°}$।

**PYQ 4.** *(IBPS Clerk)* $AB=6,AC=9$; angle bisector $BC$ को किस ratio में बाँटेगा?

**हल:** $BD:DC=\mathbf{2:3}$।

**PYQ 5.** *(UP Police SI)* Right triangle की hypotenuse $10$ cm। Circumradius?

**हल:** midpoint property से $\mathbf{5}$ cm।

**PYQ 6.** *(SSC MTS)* Regular octagon का interior angle?

**हल:** $180-360/8=\mathbf{135°}$।

---

## 34.14 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | Sides $5,6,8$ valid? | हाँ | inequality |
| 2 | Sides $3,4,8$ valid? | नहीं | $3+4<8$ |
| 3 | Largest side $12,7,9$ | opposite angle largest | side-angle |
| 4 | Triangle angles $2x,3x,4x$ | $40°,60°,80°$ | sum $180$ |
| 5 | Base $12$, height $7$ | area $42$ | $1/2bh$ |
| 6 | Median total $27$ | $AG=18,GM=9$ | $2:1$ |
| 7 | $AG=12$ | $GM=6$ | ratio |
| 8 | $AB:AC=2:3$; angle bisector | $BD:DC=2:3$ | theorem |
| 9 | Semiperimeter $15$, inradius $4$ | area $60$ | $rs$ |
| 10 | Three angle bisectors meet at | incentre | definition |
| 11 | Perpendicular bisectors meet at | circumcentre | definition |
| 12 | Three altitudes meet at | orthocentre | definition |
| 13 | Median intersection | centroid | definition |
| 14 | Right triangle hypotenuse $16$ | circumradius $8$ | midpoint |
| 15 | Right triangle right vertex | orthocentre | special case |
| 16 | Equilateral triangle centres | all coincide | $G=I=O=H$ |
| 17 | Euler line relation | $OH=3OG$ | theorem |
| 18 | $OG=5$ cm | $OH=15$ cm | Euler line |
| 19 | Exterior remote angles $50°,70°$ | $120°$ | exterior theorem |
| 20 | Exterior $130°$, remote $55°$ | other $75°$ | difference |
| 21 | Hexagon interior sum | $720°$ | $(n-2)180$ |
| 22 | Hexagon diagonals | 9 | $n(n-3)/2$ |
| 23 | Regular octagon exterior | $45°$ | $360/n$ |
| 24 | Regular polygon exterior $30°$ | 12 sides | $360/e$ |
| 25 | Isosceles vertex angle $40°$ | base $70°$ each | equal angles |

---

## 34.15 :icon-trophy: अध्याय का सार

```
━━━ Classification ━━━
Equilateral: 3 equal sides, 60° each
Isosceles: 2 equal sides, equal base angles
Scalene: all sides different
Right: one 90° angle
Acute: all <90°
Obtuse: one >90°

━━━ Triangle rules ━━━
angle sum = 180°
side inequality: largest < other two sum
larger side ↔ larger opposite angle
area = 1/2 × base × height

━━━ Special lines ━━━
median → midpoint
altitude → perpendicular
angle bisector → equal angles
perpendicular bisector → equal endpoint distance

━━━ Four centres ━━━
Centroid G: medians, 2:1
Incentre I: angle bisectors, equal side distance
Circumcentre O: perpendicular bisectors, equal vertex distance
Orthocentre H: altitudes

━━━ Centre locations ━━━
acute: all usually inside
right: H at right vertex, O at hypotenuse midpoint
obtuse: O and H can be outside
Equilateral: G=I=O=H

━━━ Euler line ━━━
O, G, H collinear
OH = 3OG

━━━ Polygon link ━━━
interior sum = (n−2)×180°
regular exterior = 360°/n
```

> :icon-trophy: **Chapter 34 ने triangle को केवल three-sided figure नहीं, बल्कि एक complete property system के रूप में जोड़ा है।** चारों centres और special lines आगे के geometry chapters की रीढ़ हैं।
>
> **आगे:** Chapter 35 — **सर्वांगसमता व समरूपता (Congruence & Similarity of Triangles)**।
