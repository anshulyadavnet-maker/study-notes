# अध्याय 42 — त्रिकोणमितीय अनुपात, डिग्री व रेडियन (Trigonometric Ratios, Degrees & Radians)

## 42.1 :icon-target: परिचय व वेटेज

Part 6 की शुरुआत trigonometry से होती है। Chapter 34 के right triangles और Chapter 41 के coordinate system अब angles और ratios से जुड़ेंगे। Trigonometry का पहला कदम किसी angle के सामने sides को सही नाम देना है।

> *"एक right triangle में किसी angle के लिए opposite, adjacent और hypotenuse कौन-सी sides हैं?"*

एक ही triangle में angle बदलने पर opposite और adjacent बदल सकते हैं। इसलिए ratio लिखने से पहले selected angle को mark कीजिए।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **2–3** | ratios और standard values |
| **SSC CGL Tier-2** | **3–5** | trigonometry applications |
| SSC CHSL / MTS / GD | 1–2 | basic ratios |
| **SSC CPO** | **2–3** | degree/radian, exact values |
| **IBPS / SBI PO** | 1 | basic trig arithmetic |
| IBPS / SBI Clerk | 1 | standard values |
| **RRB NTPC / ALP** | **2–3** | right triangle ratios |
| UP Police SI / Constable | 1–2 | ratios and angles |
| UPSSSC PET | 1 | elementary trigonometry |
| Super TET / UPTET | 1–2 | visual ratio understanding |

> :icon-key: **पूरे अध्याय का एक वाक्य:** Selected angle के लिए $\sin=O/H$, $\cos=A/H$, $\tan=O/A$ पहचानिए और angle unit सही रखिए।

---

## 42.2 :icon-number: Right triangle और तीन basic ratios

Right triangle में selected acute angle $\theta$ के अनुसार:

- Opposite $O$: angle के सामने वाली side
- Adjacent $A$: angle से लगी हुई, लेकिन hypotenuse नहीं
- Hypotenuse $H$: $90°$ के opposite सबसे बड़ी side

```figure
type: right-trig
caption: theta के लिए opposite, adjacent और hypotenuse पहचानकर ratios बनाइए
```

### Primary ratios

$$\sin\theta=\frac{O}{H}$$

$$\cos\theta=\frac{A}{H}$$

$$\tan\theta=\frac{O}{A}$$

**उदाहरण 1.** Right triangle में $O=3,A=4,H=5$ हो।

$$\sin\theta=\frac{3}{5},\qquad\cos\theta=\frac{4}{5},\qquad\tan\theta=\frac{3}{4}$$

### Reciprocal ratios

$$cosec\theta=\frac{H}{O}=\frac{1}{\sin\theta}$$

$$sec\theta=\frac{H}{A}=\frac{1}{\cos\theta}$$

$$cot\theta=\frac{A}{O}=\frac{1}{\tan\theta}$$

```figure
type: trig-ratios
caption: sin/cosec, cos/sec और tan/cot reciprocal pairs हैं
```

**उदाहरण 2.** यदि $\tan\theta=3/4$, तो $cot\theta$?

$$cot\theta=\frac{4}{3}$$

> :icon-bulb: SOH–CAH–TOA याद रखें: **S**in = **O**pposite/**H**ypotenuse, **C**os = **A**djacent/**H**ypotenuse, **T**an = **O**pposite/**A**djacent।

---

## 42.3 :icon-calc: Pythagoras और ratios का connection

Right triangle में:

$$H^2=O^2+A^2$$

यदि $\sin\theta=O/H$ और $\cos\theta=A/H$, तो:

$$\sin^2\theta+\cos^2\theta=1$$

इस identity का proof और बाकी standard identities Chapter 43 में विस्तार से होगा।

**उदाहरण 3.** यदि $\sin\theta=3/5$ और $\theta$ acute है, तो $\cos\theta$ और $\tan\theta$?

$O:H=3:5$। Pythagorean triple से $A=4$:

$$\cos\theta=\frac{4}{5},\qquad\tan\theta=\frac{3}{4}$$

**उदाहरण 4.** यदि $\tan\theta=5/12$ हो, तो $\sin\theta$?

$O:A=5:12$ और $H=13$:

$$\sin\theta=\frac{5}{13}$$

### Ratio से triangle बनाना

किसी ratio को sides के रूप में रखिए:

- $\sin\theta=5/13$ ⟹ $O=5k,H=13k,A=12k$
- $\cos\theta=8/17$ ⟹ $A=8k,H=17k,O=15k$
- $\tan\theta=7/24$ ⟹ $O=7k,A=24k,H=25k$

---

## 42.4 :icon-chart: Special triangle $30°-60°-90°$

Equilateral triangle को altitude से दो right triangles में बाँटने पर side ratio मिलता है:

$$\text{opposite }30°:\text{opposite }60°:\text{hypotenuse}=1:\sqrt{3}:2$$

```figure
type: special-30-60
caption: 30-60-90 triangle का exact side ratio 1:sqrt3:2 है
```

### Exact values

$$\sin30°=\frac{1}{2},\qquad\cos30°=\frac{\sqrt{3}}{2},\qquad\tan30°=\frac{1}{\sqrt{3}}$$

$$\sin60°=\frac{\sqrt{3}}{2},\qquad\cos60°=\frac{1}{2},\qquad\tan60°=\sqrt{3}$$

**उदाहरण 5.** $20$ cm hypotenuse वाले $30°-60°-90°$ triangle की छोटी side और बड़ी leg?

- छोटी side $=20/2=\mathbf{10}$ cm
- बड़ी leg $=10\sqrt{3}=\mathbf{10\sqrt{3}}$ cm

---

## 42.5 :icon-ruler: Special triangle $45°-45°-90°$

Isosceles right triangle में दोनों legs equal और ratio:

$$1:1:\sqrt{2}$$

```figure
type: special-45
caption: 45-45-90 triangle में दोनों legs equal और hypotenuse sqrt2 times होती है
```

$$\sin45°=\cos45°=\frac{1}{\sqrt{2}}=\frac{\sqrt{2}}{2}$$

$$\tan45°=1$$

**उदाहरण 6.** Right isosceles triangle की leg $6$ cm। Hypotenuse?

$$H=6\sqrt{2}=\mathbf{6\sqrt{2}\text{ cm}}$$

### Standard values table

```figure
type: special-table
caption: 0, 30, 45, 60 और 90 degrees के standard exact values
```

| $\theta$ | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ |
|---|---:|---:|---:|---:|---:|
| $\sin\theta$ | $0$ | $1/2$ | $1/\sqrt{2}$ | $\sqrt{3}/2$ | $1$ |
| $\cos\theta$ | $1$ | $\sqrt{3}/2$ | $1/\sqrt{2}$ | $1/2$ | $0$ |
| $\tan\theta$ | $0$ | $1/\sqrt{3}$ | $1$ | $\sqrt{3}$ | defined नहीं |
| $cosec\theta$ | defined नहीं | $2$ | $\sqrt{2}$ | $2/\sqrt{3}$ | $1$ |
| $sec\theta$ | $1$ | $2/\sqrt{3}$ | $\sqrt{2}$ | $2$ | defined नहीं |
| $cot\theta$ | defined नहीं | $\sqrt{3}$ | $1$ | $1/\sqrt{3}$ | $0$ |

> :icon-key: Standard table में sin का sequence $0,1/2,1/\sqrt{2},\sqrt{3}/2,1$ है; cos उसी sequence का reverse है।

---

## 42.6 :icon-chart: Degrees और radians

Angle को दो common units में measure करते हैं:

- degree: complete turn $360°$
- radian: arc length और radius के ratio पर आधारित unit

एक semicircle:

$$180°=\pi\text{ radians}$$

इसलिए:

$$1°=\frac{\pi}{180}\text{ radian}$$

$$1\text{ radian}=\frac{180}{\pi}°$$

```figure
type: degree-radian
caption: 180 degrees और pi radians एक ही semicircle को measure करते हैं
```

### Conversion

Degree से radian:

$$\theta°=\theta\times\frac{\pi}{180}\text{ rad}$$

Radian से degree:

$$\theta\text{ rad}=\theta\times\frac{180}{\pi}°$$

**उदाहरण 7.** $60°$ को radians में बदलें।

$$60\times\frac{\pi}{180}=\mathbf{\frac{\pi}{3}}\text{ rad}$$

**उदाहरण 8.** $90°$:

$$90\times\frac{\pi}{180}=\mathbf{\frac{\pi}{2}}\text{ rad}$$

**उदाहरण 9.** $\pi/4$ radian को degree में:

$$\frac{\pi}{4}\times\frac{180}{\pi}=\mathbf{45°}$$

### Common conversion table

| Degrees | Radians |
|---:|---:|
| $0°$ | $0$ |
| $30°$ | $\pi/6$ |
| $45°$ | $\pi/4$ |
| $60°$ | $\pi/3$ |
| $90°$ | $\pi/2$ |
| $180°$ | $\pi$ |
| $270°$ | $3\pi/2$ |
| $360°$ | $2\pi$ |

---

## 42.7 :icon-chart: Unit circle और quadrants

Unit circle का radius $1$ होता है। Angle $\theta$ पर point के coordinates:

$$P=(\cos\theta,\sin\theta)$$

```figure
type: unit-circle
angle: 60
caption: unit circle में x-coordinate cos theta और y-coordinate sin theta है
```

### Quadrant signs — ASTC

```figure
type: quadrant-signs
caption: All-Sin-Tan-Cos से quadrants में signs याद रखें
```

| Quadrant | Positive ratios |
|---|---|
| I | all: sin, cos, tan |
| II | sin |
| III | tan |
| IV | cos |

ASTC mnemonic:

- QI: All positive
- QII: Sin positive
- QIII: Tan positive
- QIV: Cos positive

**उदाहरण 10.** $\theta$ QII में है और $\sin\theta=3/5$। $\cos\theta$ का sign?

QII में cos negative:

$$\cos\theta=-\frac{4}{5}$$

### Reference angle

Reference angle acute angle होता है जो x-axis से बनता है। Exact values reference angle से मिलती हैं, sign quadrant से।

---

## 42.8 :icon-steps: Right triangle में unknown sides

**उदाहरण 11.** Right triangle में $\theta=30°$ और hypotenuse $20$ cm है। Opposite और adjacent sides?

$$\sin30=\frac{O}{20}=\frac{1}{2}\quad\Rightarrow\quad O=\mathbf{10\text{ cm}}$$

$$\cos30=\frac{A}{20}=\frac{\sqrt{3}}{2}\quad\Rightarrow\quad A=\mathbf{10\sqrt{3}\text{ cm}}$$

```figure
type: angle-triangle
angle: 30
hyp: 10
caption: selected angle के आधार पर sin और cos से unknown legs निकालिए
```

**उदाहरण 12.** $\tan\theta=3/4$ और adjacent side $20$ cm है। Opposite और hypotenuse?

$$\tan\theta=\frac{O}{20}=\frac{3}{4}\quad\Rightarrow\quad O=15$$

$$H=\sqrt{15^2+20^2}=\mathbf{25\text{ cm}}$$

### Ratio selection

| Given/required sides | Ratio |
|---|---|
| opposite और hypotenuse | sin |
| adjacent और hypotenuse | cos |
| opposite और adjacent | tan |

> :icon-bulb: Ratio में side names selected angle के respect में होंगे। Angle बदलते ही opposite/adjacent बदल सकते हैं।

---

## 42.9 :icon-bulb: Shortcuts और exam method

### :icon-timer: Shortcut 1 — SOH-CAH-TOA

$$\sin=O/H,\qquad\cos=A/H,\qquad\tan=O/A$$

### :icon-timer: Shortcut 2 — reciprocals

$$cosec=1/\sin,\qquad sec=1/\cos,\qquad cot=1/\tan$$

### :icon-timer: Shortcut 3 — special triangles

- $30-60-90$: $1:\sqrt{3}:2$
- $45-45-90$: $1:1:\sqrt{2}$

### :icon-timer: Shortcut 4 — standard values

Sin table याद करें; cos को reverse पढ़ें और tan $=\sin/\cos$ से check करें।

### :icon-timer: Shortcut 5 — degree/radian

$$180°=\pi\text{ rad}$$

Degree $to$ radian: $\times\pi/180$। Radian $to$ degree: $\times180/\pi$।

### :icon-timer: Shortcut 6 — unit circle

$$(x,y)=(\cos\theta,\sin\theta)$$

x-coordinate cos और y-coordinate sin; quadrant sign अलग से लगाएँ।

### :icon-timer: Shortcut 7 — triangle solve

1. Angle mark करें।
2. O/A/H नाम दें।
3. सही ratio चुनें।
4. Unit और sign check करें।

---

## 42.10 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Opposite और adjacent side उलट देना।
> Selected angle के respect में names दें।

> :icon-cross: **जाल 2.** Hypotenuse को किसी भी बड़ी दिखने वाली side मानना।
> Hypotenuse हमेशा $90°$ के opposite होती है।

> :icon-cross: **जाल 3.** $\sin$ और $\cos$ की standard table same पढ़ना।
> Cos table, sin table का reverse है।

> :icon-cross: **जाल 4.** Degree को radian formula में सीधे रखना।
> $60$ degrees और $60$ radians एक चीज नहीं हैं।

> :icon-cross: **जाल 5.** Degree to radian में $180/\pi$ लगाना।
> Degree to radian: $\pi/180$; reverse में $180/\pi$।

> :icon-cross: **जाल 6.** QII/QIII/QIV में all ratios positive रखना।
> ASTC signs लगाएँ।

> :icon-cross: **जाल 7.** $\tan90°$ या $sec90°$ को finite value देना।
> Cos $90°=0$, इसलिए tan/sec defined नहीं।

> :icon-cross: **जाल 8.** Ratio से side निकालते समय scale factor भूलना।
> $O:A=3:4$ हो तो sides $3k,4k$ और hypotenuse $5k$ रखें।

---

## 42.11 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* $O=3,A=4,H=5$ के लिए sin, cos, tan?

**हल:** $\mathbf{3/5,4/5,3/4}$।

**PYQ 2.** *(SSC CHSL)* $\tan\theta=3/4$। Cot?

**हल:** $\mathbf{4/3}$।

**PYQ 3.** *(RRB NTPC)* $60°$ radians में?

**हल:** $\mathbf{\pi/3}$।

**PYQ 4.** *(IBPS Clerk)* $\pi/4$ radians degrees में?

**हल:** $\mathbf{45°}$।

**PYQ 5.** *(UP Police SI)* $30°-60°-90°$ triangle hypotenuse $20$। Short side?

**हल:** $\mathbf{10}$ cm।

**PYQ 6.** *(SSC MTS)* QII में $\sin\theta=3/5$। Cos?

**हल:** $\mathbf{-4/5}$।

---

## 42.12 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | $O=3,A=4,H=5$: sin | $3/5$ | $O/H$ |
| 2 | उसी triangle cos | $4/5$ | $A/H$ |
| 3 | उसी triangle tan | $3/4$ | $O/A$ |
| 4 | tan $=3/4$, cot | $4/3$ | reciprocal |
| 5 | sin $=5/13$, cos acute | $12/13$ | 5-12-13 |
| 6 | tan $=5/12$, sin | $5/13$ | triangle |
| 7 | sin $30°$ | $1/2$ | table |
| 8 | cos $60°$ | $1/2$ | table |
| 9 | tan $45°$ | $1$ | table |
| 10 | sin $60°$ | $\sqrt{3}/2$ | table |
| 11 | cos $30°$ | $\sqrt{3}/2$ | table |
| 12 | hypotenuse 20, angle 30, opposite | $10$ | sin |
| 13 | hypotenuse 20, angle 30, adjacent | $10\sqrt{3}$ | cos |
| 14 | $60°$ in radians | $\pi/3$ | conversion |
| 15 | $90°$ in radians | $\pi/2$ | conversion |
| 16 | $180°$ in radians | $\pi$ | conversion |
| 17 | $\pi/6$ in degrees | $30°$ | reverse |
| 18 | $3\pi/2$ in degrees | $270°$ | reverse |
| 19 | QII sin positive, cos sign | negative | ASTC |
| 20 | QIII tan sign | positive | ASTC |
| 21 | QIV sin sign | negative | ASTC |
| 22 | 45-45-90 leg 6, hypotenuse | $6\sqrt{2}$ | special triangle |
| 23 | 30-60-90 hypotenuse 20, long leg | $10\sqrt{3}$ | special triangle |
| 24 | tan angle, adjacent 20, tan $3/4$ | opposite 15 | ratio |
| 25 | right triangle angle 30, hyp 10 | opposite 5 | sin |

---

## 42.13 :icon-trophy: अध्याय का सार

```
━━━ Basic ratios ━━━
sin θ = O/H
cos θ = A/H
tan θ = O/A

cosec θ = H/O
sec θ = H/A
cot θ = A/O

━━━ Special triangles ━━━
30-60-90 → 1 : √3 : 2
45-45-90 → 1 : 1 : √2

━━━ Standard values ━━━
sin: 0, 1/2, 1/√2, √3/2, 1
cos: reverse of sin table
tan: sin/cos

━━━ Degree/radian ━━━
180° = π radians
1° = π/180 rad
1 rad = 180/π°

━━━ Unit circle ━━━
point = (cos θ, sin θ)

━━━ Quadrant signs ━━━
QI: All positive
QII: Sin positive
QIII: Tan positive
QIV: Cos positive

━━━ Method ━━━
angle mark करें
O/A/H पहचानें
ratio चुनें
unit और quadrant sign check करें
```

> :icon-trophy: **Part 6 की trigonometry शुरू।** Basic ratios, special angles, degree–radian conversion और unit-circle sign system तैयार है।
>
> **आगे:** Chapter 43 — **त्रिकोणमितीय सर्वसमिकाएँ व पूरक कोण (Trigonometric Identities & Complementary Angles)**।
