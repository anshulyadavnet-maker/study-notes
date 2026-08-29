# अध्याय 31 — द्विघात समीकरण (Quadratic Equations)

## 31.1 :icon-target: परिचय व वेटेज

Chapter 30 में हमने linear equations देखीं जिनमें variable की highest power $1$ होती है। अब ऐसी equations आएँगी जिनमें variable की highest power $2$ है। इन्हें quadratic equations कहते हैं।

> *"$x^2-5x+6=0$ में x के कितने values सम्भव हैं?"*

Factorisation से $(x-2)(x-3)=0$ मिलता है, इसलिए $x=2$ या $x=3$। Quadratic equation में दो roots, एक repeated root या कोई real root नहीं हो सकता।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | roots और factorisation |
| **SSC CGL Tier-2** | **2–3** | formula, discriminant |
| SSC CHSL / MTS / GD | 1–2 | basic quadratic |
| **SSC CPO** | **1–2** | roots and nature |
| **IBPS / SBI PO** | **3–5** | quadratic comparison की नींव |
| IBPS / SBI Clerk | 2–3 | roots और sign analysis |
| **RRB NTPC / ALP** | **1–2** | factor method |
| UP Police SI / Constable | 1–2 | equation solving |
| UPSSSC PET | 1 | elementary quadratic |
| Super TET / UPTET | 1 | concept based |

> :icon-key: **पूरे अध्याय का एक वाक्य:** Standard form में $a,b,c$ पहचानिए, फिर factorisation, formula या discriminant में से सही method चुनिए।

---

## 31.2 :icon-number: Quadratic equation की मूल अवधारणा

Standard form —

$$ax^2+bx+c=0$$

जहाँ $a$ zero नहीं है।

```figure
type: quadratic-form
a: 2
b: -7
c: 3
caption: standard form ax²+bx+c=0 में a, b और c पहचानिए
```

| Symbol | भूमिका |
|---|---|
| $a$ | $x^2$ का coefficient |
| $b$ | $x$ का coefficient |
| $c$ | constant term |
| degree | $2$ |

**उदाहरण 1.** $3x^2-5x+2=0$ में $a=3,b=-5,c=2$।

**उदाहरण 2.** $x^2-9=0$ में $a=1,b=0,c=-9$। $x$ term absent होने पर उसका coefficient $0$ होता है।

**उदाहरण 3.** $5x+2=0$ quadratic नहीं, linear equation है क्योंकि $x^2$ term नहीं है।

### Root या solution

ऐसा $x$ value जो equation को zero बनाए, root कहलाता है।

**उदाहरण:** $x^2-5x+6$ में $x=2$ रखने पर $4-10+6=0$। इसलिए $2$ root है।

---

## 31.3 :icon-calc: Factorisation method

Chapter 29 की factorisation quadratic equations का सबसे तेज़ method है।

**उदाहरण 4.** $x^2-5x+6=0$।

Product $6$ और sum $-5$ वाले numbers $-2,-3$ हैं:

$$x^2-5x+6=(x-2)(x-3)$$

अब zero-product property:

$$(x-2)(x-3)=0$$

इसलिए —

$$x-2=0\quad\text{or}\quad x-3=0$$

अतः roots $=\mathbf{2,3}$।

```figure
type: factor-roots
r1: 2
r2: 3
caption: factorised quadratic से दो root branches मिलती हैं
```

**उदाहरण 5.** $2x^2+7x+3=0$।

Chapter 29 के middle split से:

$$2x^2+7x+3=(2x+1)(x+3)$$

अतः —

$$x=-\frac{1}{2}\quad\text{or}\quad x=-3$$

**उदाहरण 6.** $3x^2-5x-2=0$।

$$3x^2-5x-2=(3x+1)(x-2)$$

Roots $=\mathbf{-1/3,2}$।

> :icon-key: Factorisation तब सबसे तेज़ है जब integer या simple rational factor pair साफ़ दिखे। नहीं दिखे तो quadratic formula लगाइए।

---

## 31.4 :icon-formula: Quadratic formula

किसी भी quadratic equation $ax^2+bx+c=0$ के roots —

$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

यहाँ $\pm$ के कारण सामान्यतः दो values मिलती हैं।

**उदाहरण 7.** $2x^2-7x+3=0$।

यहाँ $a=2,b=-7,c=3$।

$$b^2-4ac=(-7)^2-4(2)(3)=49-24=25$$

$$x=\frac{-(-7)\pm\sqrt{25}}{4}=\frac{7\pm5}{4}$$

इसलिए —

$$x=\frac{12}{4}=\mathbf{3}\quad\text{or}\quad x=\frac{2}{4}=\mathbf{\frac{1}{2}}$$

```figure
type: formula-steps
a: 2
b: -7
c: 3
caption: quadratic formula में पहले discriminant, फिर plus/minus roots निकालिए
```

**उदाहरण 8.** $x^2+4x+1=0$।

$$x=\frac{-4\pm\sqrt{16-4}}{2}=\frac{-4\pm\sqrt{12}}{2}$$

$$x=\mathbf{-2\pm\sqrt{3}}$$

यहाँ factorisation में simple integer roots नहीं आते, इसलिए formula उपयोगी है।

### Formula का proof: completing square

$$ax^2+bx+c=0$$

$a$ से multiply करके:

$$4a^2x^2+4abx+4ac=0$$

पहले दो terms में $b^2$ जोड़कर घटाएँ:

$$(2ax+b)^2=b^2-4ac$$

Square root लेने पर:

$$2ax+b=\pm\sqrt{b^2-4ac}$$

अतः:

$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

---

## 31.5 :icon-chart: Discriminant और roots की प्रकृति

Quadratic formula में square root के अंदर का भाग —

$$\Delta=b^2-4ac$$

Discriminant कहलाता है।

```figure
type: discriminant
caption: discriminant positive, zero या negative होने से roots की प्रकृति तय होती है
```

| Discriminant | Roots की प्रकृति | Graph का व्यवहार |
|---|---|---|
| $\Delta>0$ | दो अलग real roots | x-axis को दो जगह काटता है |
| $\Delta=0$ | दो बराबर real roots | x-axis को एक जगह touch करता है |
| $\Delta<0$ | कोई real root नहीं | real x-axis को नहीं काटता |

**उदाहरण 9.** $x^2-5x+6=0$।

$$\Delta=(-5)^2-4(1)(6)=25-24=1>0$$

दो अलग real roots हैं।

**उदाहरण 10.** $x^2-6x+9=0$।

$$\Delta=(-6)^2-4(1)(9)=36-36=0$$

Repeated root $x=3$ है।

**उदाहरण 11.** $2x^2+3x+5=0$।

$$\Delta=3^2-4(2)(5)=9-40=-31$$

कोई real root नहीं। Complex numbers इस chapter के scope से बाहर हैं।

### Parameter से nature of roots

**उदाहरण 12.** $x^2-4x+k=0$ में equal roots के लिए $k$?

Equal roots के लिए $\Delta=0$:

$$(-4)^2-4(1)(k)=0\quad\Rightarrow\quad16-4k=0$$

अतः $k=\mathbf{4}$।

---

## 31.6 :icon-divide: Roots और coefficients का सम्बन्ध

यदि $\alpha$ और $\beta$ equation $ax^2+bx+c=0$ के roots हैं, तो —

$$\alpha+\beta=-\frac{b}{a}$$

$$\alpha\beta=\frac{c}{a}$$

**उदाहरण 13.** $2x^2-7x+3=0$ के roots का sum और product।

$$\alpha+\beta=-\frac{-7}{2}=\mathbf{\frac{7}{2}}$$

$$\alpha\beta=\frac{3}{2}=\mathbf{\frac{3}{2}}$$

Actual roots $3$ और $1/2$ हैं; sum $7/2$, product $3/2$ check होता है।

### Roots से equation बनाना

यदि roots $\alpha$ और $\beta$ हों, तो monic quadratic —

$$x^2-(\alpha+\beta)x+\alpha\beta=0$$

**उदाहरण 14.** Roots $3$ और $-2$ वाली equation?

- sum $=1$
- product $=-6$

$$\mathbf{x^2-x-6=0}$$

**उदाहरण 15.** Roots $1/2$ और $3$ वाली integer-coefficient equation?

$$x^2-\frac{7}{2}x+\frac{3}{2}=0$$

Fractions हटाने के लिए $2$ से multiply करें:

$$\mathbf{2x^2-7x+3=0}$$

```figure
type: root-relations
a: 2
b: -7
c: 3
caption: coefficients से roots का sum और product बिना पूरा solution निकाले मिलते हैं
```

### Roots के expressions

यदि roots $\alpha,\beta$ हों:

- $\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta$
- $\frac{1}{\alpha}+\frac{1}{\beta}=\frac{\alpha+\beta}{\alpha\beta}$
- $(\alpha-\beta)^2=(\alpha+\beta)^2-4\alpha\beta$

**उदाहरण 16.** $2x^2-7x+3=0$ के roots $\alpha,\beta$ के लिए $\alpha^2+\beta^2$।

$$\alpha+\beta=\frac{7}{2},\quad\alpha\beta=\frac{3}{2}$$

$$\alpha^2+\beta^2=\left(\frac{7}{2}\right)^2-2\left(\frac{3}{2}\right)=\frac{49}{4}-3=\mathbf{\frac{37}{4}}$$

---

## 31.7 :icon-brain: Completing square और parabola

Completing square method में $x^2+bx$ के साथ $(b/2)^2$ जोड़कर perfect square बनाते हैं।

**उदाहरण 17.** $x^2+6x+5=0$।

$$x^2+6x+9-9+5=0$$

$$ (x+3)^2-4=0$$

$$ (x+3)^2=4\quad\Rightarrow\quad x+3=\pm2$$

Roots $=\mathbf{-1,-5}$।

### Quadratic graph

Equation $y=ax^2+bx+c$ का graph parabola होता है। उसके x-intercepts वे roots होते हैं जहाँ $y=0$।

**उदाहरण 18.**

$$y=x^2-4x+3=(x-1)(x-3)$$

Roots $1$ और $3$ हैं, इसलिए graph x-axis को $(1,0)$ और $(3,0)$ पर काटेगा।

Vertex का x-coordinate roots का average है:

$$x=\frac{1+3}{2}=2$$

और $y=2^2-4(2)+3=-1$। Vertex $(2,-1)$।

```figure
type: parabola-roots
caption: quadratic parabola के x-intercepts ही उसके real roots होते हैं
```

### Opening direction

- $a>0$: parabola ऊपर खुलती है
- $a<0$: parabola नीचे खुलती है

Discriminant graph से जुड़ता है:

- two x-intercepts ⟺ two real roots
- one touch point ⟺ equal roots
- no x-intercept ⟺ no real roots

---

## 31.8 :icon-steps: Word problems और applications

### Consecutive numbers

**उदाहरण 19.** दो consecutive positive integers का product $56$ है। numbers?

मान लें पहला $x$, दूसरा $x+1$।

$$x(x+1)=56\quad\Rightarrow\quad x^2+x-56=0$$

$$ (x+8)(x-7)=0$$

$x=7$ या $-8$। Positive pair $=\mathbf{7,8}$।

### Rectangle dimensions

**उदाहरण 20.** Rectangle की length width से $3$ m अधिक है और area $40$ m² है। dimensions?

Width $=x$, length $=x+3$।

$$x(x+3)=40\quad\Rightarrow\quad x^2+3x-40=0$$

$$ (x+8)(x-5)=0$$

Positive width $x=5$; length $=8$ m।

### Number and reciprocal style

**उदाहरण 21.** किसी positive number और उसके reciprocal का sum $5/2$ है। number?

मान लें number $x$।

$$x+\frac{1}{x}=\frac{5}{2}$$

$2x$ से multiply:

$$2x^2+2=5x\quad\Rightarrow\quad2x^2-5x+2=0$$

$$ (2x-1)(x-2)=0$$

अतः $x=\mathbf{1/2}$ या $\mathbf{2}$।

> :icon-key: Word problem में variable define कीजिए, condition से quadratic बनाइए, roots निकालिए और context के अनुसार negative/impossible root हटाइए।

---

## 31.9 :icon-bulb: शॉर्टकट व उनके प्रमाण

### :icon-timer: शॉर्टकट 1 — method selection

| स्थिति | fastest method |
|---|---|
| simple integer factor pair | factorisation |
| $a,b,c$ awkward हों | quadratic formula |
| roots की प्रकृति पूछी हो | discriminant |
| roots से sum/product पूछा हो | coefficient relations |
| repeated powers हों | substitution |
| word problem | variable बनाकर equation |

### :icon-timer: शॉर्टकट 2 — roots from coefficients

$$\alpha+\beta=-b/a,\qquad\alpha\beta=c/a$$

इससे roots का sum/product बिना formula लगाए मिल जाता है।

### :icon-timer: शॉर्टकट 3 — equal roots

Repeated roots के लिए:

$$b^2-4ac=0$$

और repeated root:

$$x=-\frac{b}{2a}$$

### :icon-timer: शॉर्टकट 4 — difference of roots

$$\alpha-\beta=\frac{\sqrt{b^2-4ac}}{a}$$

इसलिए —

$$ (\alpha-\beta)^2=\frac{b^2-4ac}{a^2}$$

### :icon-timer: शॉर्टकट 5 — equation construction

Roots $r_1,r_2$ हों:

$$x^2-(r_1+r_2)x+r_1r_2=0$$

यदि integer coefficients चाहिए, तो पूरी equation को denominators के LCM से multiply करें।

### :icon-timer: शॉर्टकट 6 — verify a root

$P(k)=0$ आए तो $(x-k)$ factor होने की सम्भावना है। Factor theorem से इसे confirm करिए।

### :icon-timer: शॉर्टकट 7 — completing square

For $x^2+bx+c=0$:

$$\left(x+\frac{b}{2}\right)^2=\frac{b^2}{4}-c$$

यह formula quadratic formula का एक रूप है और graph के vertex से भी जुड़ा है।

---

## 31.10 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** $a,b,c$ में sign गलत लेना।
> $2x^2-7x+3$ में $b=-7$ है, $+7$ नहीं।

> :icon-cross: **जाल 2.** Formula में denominator $2a$ भूलना।
> पूरा denominator $2a$ है, केवल $2$ नहीं।

> :icon-cross: **जाल 3.** Discriminant में $4ac$ का sign गलत करना।
> $\Delta=b^2-4ac$ carefully लिखिए।

> :icon-cross: **जाल 4.** $\pm$ से मिलने वाले दोनों roots में से एक छोड़ देना।
> दोनों values निकालकर context में जाँचिए।

> :icon-cross: **जाल 5.** Equal roots को two different roots मानना।
> $\Delta=0$ पर दोनों roots identical होते हैं।

> :icon-cross: **जाल 6.** Negative root को हर word problem में स्वीकार कर लेना।
> Length, age या positive number में impossible root हटाइए।

> :icon-cross: **जाल 7.** Root sum में $-b/a$ की जगह $b/a$ लिखना।
> Standard form में sum हमेशा $-b/a$ है।

> :icon-cross: **जाल 8.** Roots से equation बनाते समय product का sign भूलना।
> Equation $x^2-(sum)x+(product)=0$।

> :icon-cross: **जाल 9.** Graph के roots को y-values समझना।
> Roots x-intercepts हैं; वहाँ $y=0$ होता है।

---

## 31.11 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* $x^2-5x+6=0$ solve करें।

**हल:** $(x-2)(x-3)=0$ ⟹ $\mathbf{x=2,3}$।

**PYQ 2.** *(SSC CHSL)* $2x^2+7x+3=0$।

**हल:** $(2x+1)(x+3)=0$ ⟹ $\mathbf{x=-1/2,-3}$।

**PYQ 3.** *(RRB NTPC)* $x^2-6x+9=0$ में roots की प्रकृति?

**हल:** $\Delta=0$ ⟹ equal real roots, root $\mathbf{3}$।

**PYQ 4.** *(IBPS Clerk)* $2x^2-7x+3=0$ के roots का sum और product।

**हल:** sum $\mathbf{7/2}$, product $\mathbf{3/2}$।

**PYQ 5.** *(UP Police SI)* Consecutive positive numbers का product $56$।

**हल:** $x(x+1)=56$ ⟹ numbers $\mathbf{7,8}$।

**PYQ 6.** *(SSC MTS)* $2x^2+3x+5=0$ में real roots?

**हल:** $\Delta=-31<0$ ⟹ **कोई real root नहीं**।

---

## 31.12 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | $x^2-5x+6=0$ | $x=2,3$ | factorisation |
| 2 | $2x^2+7x+3=0$ | $x=-1/2,-3$ | factorisation |
| 3 | $3x^2-5x-2=0$ | $x=2,-1/3$ | factorisation |
| 4 | $x^2+4x+1=0$ | $-2\pm\sqrt{3}$ | formula |
| 5 | $x^2-6x+9=0$ | repeated root 3 | $D=0$ |
| 6 | $2x^2+3x+5=0$ | no real roots | $D=-31$ |
| 7 | $2x^2-7x+3=0$; root sum | $7/2$ | $-b/a$ |
| 8 | same equation; root product | $3/2$ | $c/a$ |
| 9 | roots $3,-2$; equation | $x^2-x-6=0$ | sum/product |
| 10 | roots $1/2,3$; integer equation | $2x^2-7x+3=0$ | clear denominator |
| 11 | $x^2+4x+4=0$ | repeated root $-2$ | perfect square |
| 12 | equal roots for $x^2-4x+k=0$ | $k=4$ | $D=0$ |
| 13 | $x^2+6x+5=0$ | $x=-1,-5$ | complete square |
| 14 | $x^2-4x+3$ roots | $1,3$ | factors |
| 15 | $x^2-4x+3$ vertex x-coordinate | $2$ | root average |
| 16 | roots of $x^2-4x+3$ graph | x-intercepts 1,3 | $y=0$ |
| 17 | consecutive product 56 | $7,8$ | $x(x+1)$ |
| 18 | rectangle area 40, length width+3 | $5$ m, $8$ m | quadratic |
| 19 | $x+1/x=5/2$ | $x=1/2,2$ | multiply by $2x$ |
| 20 | $x^2-9x+20=0$ | $4,5$ | factors |
| 21 | $4x^2-12x+9=0$ | repeated root $3/2$ | perfect square |
| 22 | $5x^2+x-6=0$ | $1,-6/5$ | factors |
| 23 | $x^2+2x-15=0$ | $3,-5$ | factors |
| 24 | $3x^2-12x+12=0$ | repeated root 2 | divide/factor |
| 25 | $x^2-8x+12=0$; root difference | $\sqrt{16}=4$ | discriminant/a |

---

## 31.13 :icon-trophy: अध्याय का सार

```
━━━ Standard form ━━━
ax² + bx + c = 0, a ≠ 0

a: x² coefficient
b: x coefficient
c: constant

━━━ Factorisation ━━━
x²−5x+6 = (x−2)(x−3)
roots: 2, 3

━━━ Quadratic formula ━━━
x = (−b ± √(b²−4ac))/(2a)

━━━ Discriminant ━━━
Δ = b²−4ac
Δ>0 → two different real roots
Δ=0 → equal real roots
Δ<0 → no real roots

━━━ Root relations ━━━
α+β = −b/a
αβ = c/a

roots r₁,r₂:
x²−(r₁+r₂)x+r₁r₂=0

━━━ Completing square ━━━
x²+6x+5=0
(x+3)²=4
x=−1,−5

━━━ Graph ━━━
roots = x-intercepts of y=ax²+bx+c
D>0: crosses twice
D=0: touches once
D<0: misses x-axis

━━━ Word problems ━━━
variable define करें
condition से equation बनाइए
roots निकालिए
context के अनुसार valid root चुनिए
```

> :icon-trophy: **Chapter 30 की linear equations के बाद degree-2 equations का पूरा आधार तैयार है।** Factorisation, formula, discriminant, roots और parabola अब एक ही structure में जुड़ते हैं।
>
> **आगे:** Chapter 32 — **द्विघात तुलना (Quadratic Comparison)**। वहाँ दो quadratic equations के roots को बिना पूरा solve किए compare करना सीखेंगे।
