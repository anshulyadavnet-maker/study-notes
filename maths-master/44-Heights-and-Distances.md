# अध्याय 44 — ऊँचाई व दूरी (Heights & Distances)

## 44.1 :icon-target: परिचय व वेटेज

Heights & Distances trigonometry का सबसे practical application है। Tower, building, tree, pole, river और cliff की height सीधे measure करना कठिन हो सकता है; horizontal distance और angle of elevation/depression से height निकाली जाती है।

> *"किसी tower से 20 m दूर खड़े observer को top का angle of elevation 45° दिखता है। Tower की height?"*

Right triangle बनेगा और:

$$\tan45°=\frac{H}{20}=1$$

इसलिए height $20$ m होगी।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | tower, pole, angle |
| **SSC CGL Tier-2** | **2–4** | two-position observation |
| SSC CHSL / MTS / GD | 1 | basic height |
| **SSC CPO** | **2–3** | elevation/depression |
| **IBPS / SBI PO** | 1–2 | trig application |
| IBPS / SBI Clerk | 1 | direct tan |
| **RRB NTPC / ALP** | **2–3** | tower and shadow |
| UP Police SI / Constable | 1–2 | heights and distances |
| UPSSSC PET | 1 | basic right triangle |
| Super TET / UPTET | 1–2 | visual application |

> :icon-key: **पूरे अध्याय का एक वाक्य:** Horizontal distance और vertical height को right triangle में रखिए; सामान्यतः $\tan\theta=H/d$ सबसे तेज़ ratio है।

---

## 44.2 :icon-number: Line of sight और angle of elevation

### Line of sight

Observer की आँख से object के top तक खींची imaginary line line of sight है। Ground से eye-level horizontal line और line of sight के बीच angle **angle of elevation** कहलाता है।

```figure
type: elevation-basic
height: 20
distance: 20
angle: 45
caption: tower top को देखने पर horizontal और line of sight के बीच elevation angle बनता है
```

यदि observer ground level पर है और object height $H$, horizontal distance $d$:

$$\tan\theta=\frac{H}{d}$$

इसलिए:

$$H=d\tan\theta$$

$$d=\frac{H}{\tan\theta}$$

**उदाहरण 1.** Tower से $20$ m दूर angle of elevation $45°$ है। Height?

$$H=20\tan45°=20\times1=\mathbf{20\text{ m}}$$

**उदाहरण 2.** Pole की height $10\sqrt{3}$ m और distance $10$ m है। Angle?

$$\tan\theta=\frac{10\sqrt{3}}{10}=\sqrt{3}$$

अतः $\theta=\mathbf{60°}$।

**उदाहरण 3.** Tower की height $15$ m और angle $30°$ है। Distance?

$$d=\frac{15}{\tan30°}=\frac{15}{1/\sqrt{3}}=\mathbf{15\sqrt{3}\text{ m}}$$

---

## 44.3 :icon-ruler: Angle of depression

जब observer किसी ऊँचे point से नीचे object को देखता है, horizontal eye-line से नीचे line of sight का angle **angle of depression** है।

```figure
type: depression
height: 18
distance: 24
angle: 37
caption: ऊँचे observer से नीचे object तक line of sight depression angle बनाती है
```

यदि horizontal ground और eye-level horizontal parallel हैं, तो:

$$\text{angle of depression}=\text{angle of elevation from object}$$

**उदाहरण 4.** Cliff से boat का angle of depression $30°$ और cliff height $20$ m है। Boat से cliff का horizontal distance?

$$\tan30°=\frac{20}{d}$$

$$d=\frac{20}{1/\sqrt{3}}=\mathbf{20\sqrt{3}\text{ m}}$$

**उदाहरण 5.** Tower top से ground point का depression angle $45°$ है और distance $30$ m है। Tower height?

Depression = elevation $45°$।

$$H=30\tan45°=\mathbf{30\text{ m}}$$

> :icon-key: Depression diagram को उलटकर देखें: नीचे object से tower top तक वही alternate/elevation angle बनता है।

---

## 44.4 :icon-calc: Observer की eye height

यदि observer की आँख ground से $h$ height पर है और object की total height $H$ है, तो line-of-sight triangle में vertical rise $H-h$ होगा।

$$\tan\theta=\frac{H-h}{d}$$

इसलिए:

$$H=h+d\tan\theta$$

```figure
type: observer-height
eye: 1.6
object: 12
distance: 20
angle: 30
caption: eye level से object top तक rise H−h होता है; फिर eye height जोड़िए
```

**उदाहरण 6.** Observer की eye height $1.6$ m, pole से distance $20$ m और elevation angle $30°$ है। Pole की total height?

$$H=1.6+20\tan30°$$

$$H=1.6+\frac{20}{\sqrt{3}}\approx\mathbf{13.15\text{ m}}$$

**उदाहरण 7.** Eye height $2$ m, distance $10\sqrt{3}$ m और angle $45°$। Object height?

$$H=2+10\sqrt{3}\tan45°=\mathbf{2+10\sqrt{3}\text{ m}}$$

---

## 44.5 :icon-steps: Two positions से height

कभी observer एक ही straight line पर दो positions से top को देखता है। Near point पर angle बड़ा और far point पर angle छोटा होता है।

```figure
type: two-positions
caption: near और far observations दो right-triangle equations बनाते हैं
```

मान लें:

- tower height $H$
- far distance $d$
- near distance $d-x$
- far angle $\alpha$
- near angle $\beta$, जहाँ $\beta>\alpha$

तब:

$$H=d\tan\alpha$$

$$H=(d-x)\tan\beta$$

दो equations solve करके $H,d$ या $x$ निकाल सकते हैं।

**उदाहरण 8.** एक tower के top का angle दूर point से $30°$ और 20 m पास आने पर $60°$ हो जाता है। Tower height?

Far distance $=d$ मानें।

$$H=d\tan30°=\frac{d}{\sqrt{3}}$$

Near distance $=d-20$:

$$H=(d-20)\tan60°=\sqrt{3}(d-20)$$

Equate:

$$\frac{d}{\sqrt{3}}=\sqrt{3}(d-20)$$

$$d=3d-60\quad\Rightarrow\quad d=30$$

$$H=30\tan30°=\mathbf{10\sqrt{3}\text{ m}}$$

### Two-position shortcut

यदि angles $30°$ और $60°$ हों और positions का gap $x$ हो:

$$H=\frac{x\tan30°\tan60°}{\tan60°-\tan30°}$$

इसे values रखकर भी solve किया जा सकता है; formula रटने के बजाय two equations safer हैं।

---

## 44.6 :icon-chart: Shadows और similar triangles

एक ही समय पर vertical objects की shadows same sun angle बनाती हैं। इसलिए height/shadow ratio equal होता है।

```figure
type: shadow-height
height: 12
shadow: 8
knownH: 3
knownS: 2
caption: समान sun angle पर height और shadow के ratios equal रहते हैं
```

$$\frac{H_1}{S_1}=\frac{H_2}{S_2}$$

**उदाहरण 9.** $1.5$ m stick की shadow $1$ m है। Tower की shadow $20$ m। Height?

$$\frac{H}{20}=\frac{1.5}{1}\quad\Rightarrow\quad H=\mathbf{30\text{ m}}$$

**उदाहरण 10.** Pole height $12$ m और shadow $8$ m है। उसी समय $3$ m tree की shadow?

$$\frac{12}{8}=\frac{3}{S}\quad\Rightarrow\quad S=\mathbf{2\text{ m}}$$

> :icon-bulb: Shadow questions में trigonometric angle लिखना जरूरी नहीं; similar triangles का height/shadow ratio direct लगाइए।

---

## 44.7 :icon-ruler: Slant distance और two towers

### Slant distance

Height $H$, horizontal distance $d$ और line of sight $s$ right triangle बनाते हैं:

$$s=\sqrt{H^2+d^2}$$

```figure
type: slant-line
height: 12
distance: 5
caption: line of sight right triangle की hypotenuse है
```

**उदाहरण 11.** Tower height $12$ m, base distance $5$ m। Line of sight?

$$s=\sqrt{12^2+5^2}=\mathbf{13\text{ m}}$$

### Two towers

यदि दो towers की heights $H_1,H_2$ और bases के बीच distance $d$ हो, तो tops का vertical difference $H_1-H_2$ होगा।

$$\tan\theta=\frac{H_1-H_2}{d}$$

```figure
type: tower-distance
h1: 20
h2: 12
distance: 16
caption: दो towers के tops को join करने पर height difference वाला right triangle बनता है
```

**उदाहरण 12.** Heights $20$ m और $12$ m, bases distance $16$ m। Top-joining line का angle?

$$\tan\theta=\frac{20-12}{16}=\frac{1}{2}$$

अतः $\theta=\mathbf{\tan^{-1}(1/2)}$।

---

## 44.8 :icon-steps: Angle change और practical applications

Observer object के पास आए तो angle of elevation बढ़ता है।

```figure
type: angle-change
caption: same height के लिए near position पर angle बड़ा होता है
```

**उदाहरण 13.** Tower height fixed है। Far point distance $d$ और near point distance $d-10$ है।

$$\tan\alpha=\frac{H}{d},\qquad\tan\beta=\frac{H}{d-10}$$

क्योंकि $d-10<d$:

$$\tan\beta>\tan\alpha\quad\Rightarrow\quad\beta>\alpha$$

### Building और road

Road horizontal हो और building vertical, तो right triangle direct बनता है। Sloping road हो तो horizontal distance और actual slope distance अलग-अलग identify करें।

### Pole with observer

Eye height include करना न भूलें:

$$\text{total object height}=\text{eye height}+d\tan\theta$$

---

## 44.9 :icon-bulb: Shortcuts और method map

### :icon-timer: Basic ratio

$$\tan\theta=\frac{\text{vertical height}}{\text{horizontal distance}}$$

### :icon-timer: Eye height

$$H=h+d\tan\theta$$

### :icon-timer: Depression

$$\text{depression}=\text{elevation}$$

### :icon-timer: Shadow

$$H/S=\text{constant}$$

### :icon-timer: Slant distance

$$s^2=H^2+d^2$$

### :icon-timer: Two positions

Far observation और near observation की दो equations बनाइए:

$$H=d\tan\alpha=(d-x)\tan\beta$$

### :icon-timer: Standard values

| Angle | $\tan$ |
|---:|---:|
| $30°$ | $1/\sqrt{3}$ |
| $45°$ | $1$ |
| $60°$ | $\sqrt{3}$ |

### :icon-timer: Diagram checklist

1. Object vertical draw करें।
2. Ground horizontal draw करें।
3. Eye-level horizontal mark करें।
4. Line of sight join करें।
5. Angle observer पर mark करें।
6. Opposite/adjacent identify करें।

---

## 44.10 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Angle object के top पर लगाना।
> Angle of elevation/depression observer की eye position पर होता है।

> :icon-cross: **जाल 2.** Eye height भूल जाना।
> Rise $H-h$ है; final height में $h$ जोड़िए।

> :icon-cross: **जाल 3.** Depression और elevation को unrelated मानना।
> Parallel horizontal lines के कारण दोनों equal होते हैं।

> :icon-cross: **जाल 4.** Shadow में height और shadow ratio उलटना।
> $H/S$ दोनों objects के लिए same रखिए।

> :icon-cross: **जाल 5.** Slant line को horizontal distance मानना।
> Slant line hypotenuse है; ground distance adjacent है।

> :icon-cross: **जाल 6.** Two-position question में near/far distance गलत लेना।
> Near distance = far distance − movement।

> :icon-cross: **जाल 7.** Two towers में heights जोड़ना।
> Joining line के लिए vertical difference $H_1-H_2$ लगेगा।

> :icon-cross: **जाल 8.** Diagram की visual steepness से angle चुनना।
> Figure not-to-scale हो सकती है; given values use करें।

> :icon-cross: **जाल 9.** $30°,45°,60°$ values को गलत ratio देना।
> Standard table और special triangles से check करें।

---

## 44.11 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* Tower से $20$ m दूर angle $45°$। Height?

**हल:** $20\tan45=\mathbf{20}$ m।

**PYQ 2.** *(SSC CHSL)* $15$ m tower का angle $30°$। Distance?

**हल:** $d=15/(1/\sqrt{3})=\mathbf{15\sqrt{3}}$ m।

**PYQ 3.** *(RRB NTPC)* Depression angle $45°$, horizontal distance $30$ m। Height?

**हल:** $\mathbf{30}$ m।

**PYQ 4.** *(IBPS Clerk)* Stick $1.5$ m/shadow $1$ m, tower shadow $20$ m। Height?

**हल:** $\mathbf{30}$ m।

**PYQ 5.** *(UP Police SI)* Tower height $12$, distance $5$। Slant line?

**हल:** $\mathbf{13}$ m।

**PYQ 6.** *(SSC MTS)* $30°$ और $60°$ observations में movement $20$ m। Tower height?

**हल:** $\mathbf{10\sqrt{3}}$ m।

---

## 44.12 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | $d=20,\theta=45°$ tower height | $20$ m | $d\tan\theta$ |
| 2 | height $10\sqrt{3}$, distance 10 | $60°$ | tan |
| 3 | height 15, angle $30°$ distance | $15\sqrt{3}$ | $H/\tan$ |
| 4 | depression $45°$, distance 30 | height 30 | equal angle |
| 5 | eye height 1.6, d=20, angle 30 | $1.6+20/\sqrt{3}$ | add eye |
| 6 | eye height 2, d=$10\sqrt{3}$, angle45 | $2+10\sqrt{3}$ | add eye |
| 7 | tower height 12, shadow 8 | ratio $3/2$ | height/shadow |
| 8 | stick 3, shadow2; tower shadow20 | height30 | similar triangles |
| 9 | slant H=12,d=5 | 13 | Pythagoras |
| 10 | two towers 20,12; distance16 | tan theta $1/2$ | difference |
| 11 | near angle larger? | yes | distance smaller |
| 12 | far angle 30, near angle60, movement20 | height $10\sqrt{3}$ | two equations |
| 13 | tan theta=1, d=25 | H=25 | 45° |
| 14 | tan theta=$1/\sqrt{3}$, d=18 | H=$6\sqrt{3}$ | 30° |
| 15 | tan theta=$\sqrt{3}$, d=10 | H=$10\sqrt{3}$ | 60° |
| 16 | angle depression equals | elevation | parallel horizontals |
| 17 | object 20, eye 2, d=18, angle45 | check H=20 | $2+18$ |
| 18 | H=30,d=30 | angle45° | tan |
| 19 | H=10,d=$10\sqrt{3}$ | angle30° | tan |
| 20 | H=$10\sqrt{3}$,d=10 | angle60° | tan |
| 21 | two observations equations | $H=d\tan\alpha$ | setup |
| 22 | pole H=6, eye=1.5, d=4.5 | tan theta=1 | $H-h$ |
| 23 | shadow ratio H/S=2, shadow 15 | H=30 | proportion |
| 24 | tower H=24, slant 25 | horizontal 7 | Pythagoras |
| 25 | two towers difference8,d=16 | tan theta=1/2 | difference/d |

---

## 44.13 :icon-trophy: अध्याय का सार

```
━━━ Basic elevation ━━━
tan θ = H/d
H = d tan θ
d = H/tan θ

━━━ Eye height ━━━
tan θ = (H−h)/d
H = h + d tan θ

━━━ Depression ━━━
depression angle = elevation angle

━━━ Shadow ━━━
H₁/S₁ = H₂/S₂
similar right triangles

━━━ Slant distance ━━━
s² = H²+d²

━━━ Two positions ━━━
H = d tan α
H = (d−x) tan β
near angle β > far angle α

━━━ Two towers ━━━
tan θ = (H₁−H₂)/d

━━━ Standard tan ━━━
tan30 = 1/√3
tan45 = 1
tan60 = √3

━━━ Diagram method ━━━
vertical object
horizontal ground/eye line
line of sight
angle at observer
O/A/H identify
```

> :icon-trophy: **Heights & Distances complete।** Trigonometric ratios अब towers, poles, shadows, cliffs और two-position observations के practical diagrams में लागू हो गए हैं।
>
> **आगे:** Chapter 45 — **सांख्यिकी (Statistics)**।
