# अध्याय 32 — द्विघात तुलना (Quadratic Comparison)

## 32.1 :icon-target: परिचय व वेटेज

Quadratic comparison Banking exams का विशेष प्रकार है। सामान्यतः दो equations दी जाती हैं:

- Equation I में variable $x$
- Equation II में variable $y$

फिर पूछा जाता है कि $x>y$, $x<y$, $x=y$ या relation निर्धारित नहीं किया जा सकता।

> *"Equation I के roots 3 और 4 हैं तथा Equation II के roots 5 और 6। x और y के बीच सम्बन्ध?"*

यदि $x$ और $y$ किसी भी valid roots को दर्शाते हैं, तो Equation I का हर root Equation II के हर root से छोटा है। इसलिए $x<y$ निश्चित है।

लेकिन यदि पहली equation के roots $2,5$ और दूसरी के $3,4$ हों, तो कभी $x<y$ और कभी $x>y$ हो सकता है। ऐसी स्थिति में सही answer **cannot be determined** होगा।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **IBPS / SBI PO** | **3–5** | मुख्यतः quadratic comparison |
| **IBPS / SBI Clerk** | **2–3** | factorise करके relation |
| RRB PO / Office Assistant | 2–3 | roots और ranges |
| **SSC CGL Tier-2** | 1–2 | algebraic comparison |
| SSC CPO / CHSL | 1 | quadratic foundation |
| State Banking Exams | 2–4 | direct comparison format |

> :icon-key: **पूरे अध्याय का एक वाक्य:** दोनों equations के **सभी सम्भव roots की range** देखिए; केवल एक arbitrary root देखकर relation मत निकालिए।

---

## 32.2 :icon-number: Quadratic comparison का format

Typical question:

**Equation I:** $x^2-7x+12=0$

**Equation II:** $y^2-11y+30=0$

Options:

1. $x>y$
2. $x<y$
3. $x\geq y$
4. $x\leq y$
5. Cannot be determined

पहला step दोनों equations को solve/factorise करना है।

**Equation I:**

$$x^2-7x+12=(x-3)(x-4)=0$$

$x=3$ या $4$।

**Equation II:**

$$y^2-11y+30=(y-5)(y-6)=0$$

$y=5$ या $6$।

I के roots $[3,4]$ और II के roots $[5,6]$ हैं। हर possible $x$, हर possible $y$ से छोटा है:

$$\mathbf{x<y}$$

```figure
type: compare-factor-roots
caption: दोनों equations के root ranges अलग हों तो comparison निश्चित होता है
```

### सबसे जरूरी सावधानी

Banking convention में $x$ और $y$ equation के किसी valid root को represent करते हैं। इसलिए relation तभी निश्चित होगा जब सभी valid choices पर वही relation रहे।

---

## 32.3 :icon-calc: Factorisation से तुलना

यदि equations आसानी से factorise हों, तो यही सबसे तेज method है।

**उदाहरण 1.**

**I:** $x^2-5x+6=0$

**II:** $y^2-9y+20=0$

I के roots $2,3$। II के roots $4,5$।

$$x\in\{2,3\},\qquad y\in\{4,5\}$$

हर possible $x$ हर possible $y$ से छोटा है।

अतः $\mathbf{x<y}$।

**उदाहरण 2.**

**I:** $x^2-9x+20=0$

**II:** $y^2-5y+6=0$

- I: $(x-4)(x-5)=0$ ⟹ $x=4,5$
- II: $(y-2)(y-3)=0$ ⟹ $y=2,3$

अतः $\mathbf{x>y}$।

```figure
type: root-numberline
caption: number line पर disjoint root intervals देखकर x और y की दिशा समझिए
```

**उदाहरण 3.**

**I:** $x^2-5x+6=0$ ⟹ $x=2,3$

**II:** $y^2-7y+12=0$ ⟹ $y=3,4$

Possible pairs में $x=3,y=3$ हो सकता है। इसलिए:

$$\mathbf{x\leq y}$$

यहाँ strict $x<y$ नहीं, क्योंकि equality सम्भव है।

> :icon-warn: यदि roots touch करते हैं, तो $<$ या $>$ की जगह $\leq$ या $\geq$ की सम्भावना जाँचिए।

---

## 32.4 :icon-chart: तीन comparison outcomes

```figure
type: comparison-cases
caption: सभी possible roots देखकर greater, less या cannot-determine चुनिए
```

### Case 1: $x>y$

Equation I के smallest root से भी Equation II का largest root छोटा हो।

उदाहरण: $x\in[6,8]$, $y\in[2,4]$। हर स्थिति में $x>y$।

### Case 2: $x<y$

Equation I का largest root भी Equation II के smallest root से छोटा हो।

उदाहरण: $x\in[1,3]$, $y\in[5,7]$। हर स्थिति में $x<y$।

### Case 3: Cannot be determined

Root ranges overlap या cross करें।

उदाहरण:

$$x\in\{2,5\},\qquad y\in\{3,4\}$$

- $x=2,y=3$ ⟹ $x<y$
- $x=5,y=4$ ⟹ $x>y$

इसलिए relation निश्चित नहीं।

> :icon-key: “Cannot be determined” कमजोरी नहीं है; overlapping roots में यही mathematical answer है।

---

## 32.5 :icon-divide: Formula और root bounds

हर quadratic factorise नहीं होती। तब formula से roots निकालिए या कम से कम उनकी bounds निकालकर compare कीजिए।

**उदाहरण 4.**

**I:** $2x^2-7x+3=0$

**II:** $3y^2-14y+8=0$

### Equation I

$$\Delta=(-7)^2-4(2)(3)=25$$

$$x=\frac{7\pm5}{4}=3,\frac{1}{2}$$

### Equation II

$$\Delta=(-14)^2-4(3)(8)=100$$

$$y=\frac{14\pm10}{6}=4,\frac{2}{3}$$

Compare:

$$x\in\{\frac{1}{2},3\},\qquad y\in\{\frac{2}{3},4\}$$

$1/2<2/3$ और $3<4$। इसलिए हर possible choice पर $\mathbf{x<y}$।

```figure
type: formula-bound
a: 1
b: -7
c: 12
caption: formula से roots की approximate range निकालकर comparison कीजिए
```

### Approximation कब पर्याप्त है?

यदि roots के intervals दूर हों, exact radical निकालना जरूरी नहीं।

उदाहरण: एक equation के roots $1.4,3.2$ के आसपास और दूसरी के $5.1,6.8$ के आसपास हों, तो $x<y$ तुरंत तय है।

लेकिन intervals overlap के करीब हों तो exact calculation या sign test कीजिए।

---

## 32.6 :icon-ruler: Discriminant और roots की nature

Comparison से पहले यह देखिए कि roots real हैं भी या नहीं।

$$\Delta=b^2-4ac$$

| $\Delta$ | स्थिति |
|---|---|
| positive | दो अलग real roots |
| zero | repeated real root |
| negative | कोई real root नहीं |

**उदाहरण 5.**

**I:** $x^2-6x+9=0$

$$\Delta_x=36-36=0$$

$x=3$ repeated root।

**II:** $y^2-10y+25=0$

$$\Delta_y=100-100=0$$

$y=5$ repeated root।

अतः $\mathbf{x<y}$।

**उदाहरण 6.** यदि Equation I के roots real हैं लेकिन Equation II का discriminant negative है, तो real-number comparison में Equation II का कोई valid root नहीं। Question के options और stated domain देखकर answer चुनिए; बिना domain assume किए relation न लिखें।

> :icon-warn: Banking questions सामान्यतः real roots design करते हैं, लेकिन discriminant check करने से hidden error और wrong option से बचेंगे।

---

## 32.7 :icon-brain: Vieta relations से comparison

For $ax^2+bx+c=0$ with roots $\alpha,\beta$:

$$\alpha+\beta=-\frac{b}{a},\qquad\alpha\beta=\frac{c}{a}$$

```figure
type: vieta-box
caption: roots का sum और product coefficients से मिलाकर range compare कीजिए
```

**उदाहरण 7.**

**I:** $x^2-9x+20=0$

**II:** $y^2-11y+30=0$

I के roots का sum $9$, product $20$; roots $4,5$।

II का sum $11$, product $30$; roots $5,6$।

इसलिए $x\leq y$; equality $x=5,y=5$ पर सम्भव है।

### Vieta की सीमा

केवल sum compare करने से individual roots का relation हमेशा तय नहीं होता।

उदाहरण:

- roots I: $2,5$, sum $7$
- roots II: $3,4$, sum $7$

Sums equal हैं, लेकिन possible choices में $2<4$ और $5>3$ दोनों हो सकते हैं। इसलिए “sum बड़ा है” से सीधे $x>y$ मत लिखिए।

### Root expressions

यदि $x$ के roots $\alpha,\beta$ हों, तो:

$$\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta$$

$$|\alpha-\beta|=\frac{\sqrt{\Delta}}{|a|}$$

यह root spread compare करने में उपयोगी है।

---

## 32.8 :icon-steps: Root intervals और sign method

यदि exact roots कठिन हों, तो polynomial के अलग-अलग values निकालकर root को interval में bracket कर सकते हैं।

मान लें $f(t)=t^2-7t+10$।

- $f(1)=1-7+10=4$ positive
- $f(2)=4-14+10=0$ ⟹ root exactly $2$
- $f(5)=25-35+10=0$ ⟹ root exactly $5$

यदि दो nearby values पर signs बदलें, continuous quadratic के कारण उनके बीच root होता है।

```figure
type: quadratic-interval
caption: sign change से root का interval bracket किया जा सकता है
```

**उदाहरण 8.** Equation I का root interval $(1,3)$ में है और Equation II के दोनों roots $5$ से बड़े हैं। Exact roots न निकालकर relation?

Equation I का relevant root $<3$ और Equation II का हर root $>5$ है। अतः $\mathbf{x<y}$।

### Root ranges लिखने की आदत

हर equation के लिए छोटा table बनाइए:

| Equation | smaller root | larger root | range |
|---|---:|---:|---|
| I | $r_1$ | $r_2$ | $[r_1,r_2]$ |
| II | $s_1$ | $s_2$ | $[s_1,s_2]$ |

फिर:

- $r_2<s_1$ ⟹ $x<y$
- $s_2<r_1$ ⟹ $x>y$
- intervals overlap ⟹ अधिक जाँच या cannot determine

---

## 32.9 :icon-bulb: Exam algorithm और shortcuts

### :icon-timer: Seven-step algorithm

1. दोनों equations को standard form में लिखिए।
2. $a,b,c$ और discriminant check करें।
3. पहले factorisation try करें।
4. न हो तो formula या bounds लगाएँ।
5. दोनों equations के **दोनों** roots लिखें।
6. Smallest/largest root का interval compare करें।
7. Equality और overlap check करके option चुनें।

### :icon-timer: Shortcut 1 — easy factor pairs

$x^2+bx+c$ में product $c$ और sum $b$ वाले pair सीधे खोजिए।

### :icon-timer: Shortcut 2 — sign of roots

For $ax^2+bx+c=0$:

- $c/a<0$ ⟹ roots opposite signs
- $c/a>0$ और sum positive ⟹ दोनों positive या complex check करें
- $c/a>0$ और sum negative ⟹ दोनों negative या complex check करें

Discriminant से real nature confirm करें।

### :icon-timer: Shortcut 3 — repeated root

$\Delta=0$ हो तो एक ही root है:

$$x=-\frac{b}{2a}$$

दो repeated roots compare करना बहुत तेज़ है।

### :icon-timer: Shortcut 4 — roots from constructed form

यदि equation $(x-p)(x-q)=0$ हो, roots सीधे $p,q$ हैं। Expanded form में वापस जाने की जरूरत नहीं।

### :icon-timer: Shortcut 5 — overlap test

यदि I का बड़ा root, II के छोटे root से बड़ा है और I का छोटा root, II के बड़े root से छोटा है, intervals overlap करते हैं। केवल sum/product देखकर relation force न करें।

### :icon-timer: Shortcut 6 — inequality options

यदि $x=3,4$ और $y=4,5$:

- $x<y$ हर case में सही नहीं, equality possible
- $x\leq y$ हर case में सही

Option में non-strict relation हो तो equality को ध्यान से देखिए।

---

## 32.10 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** हर equation से केवल एक root निकालना।
> Quadratic के दोनों roots comparison में valid हो सकते हैं।

> :icon-cross: **जाल 2.** Root sets overlap होने पर $x>y$ या $x<y$ force करना।
> कम से कम दो possible choices बनाकर check करें।

> :icon-cross: **जाल 3.** $x\leq y$ और $x<y$ को एक ही मानना।
> Equal roots possible हों तो strict sign गलत होगा।

> :icon-cross: **जाल 4.** Vieta में root sum compare करके individual root compare करना।
> Sum/product range की पूरी जानकारी न दें तो factor/formula से roots निकालिए।

> :icon-cross: **जाल 5.** Discriminant negative होने पर भी real root लिखना।
> पहले root domain और $\Delta$ check करें।

> :icon-cross: **जाल 6.** Formula में $a,b,c$ के signs बदल देना।
> Standard form में $b$ negative हो तो formula में $-b$ positive होगा।

> :icon-cross: **जाल 7.** Approximation को close roots पर भरोसे से लगाना।
> Roots पास हों तो exact factor/formula method अपनाएँ।

> :icon-cross: **जाल 8.** Question के variables और roots की convention न पढ़ना।
> यदि question larger root या positive root specify करे, उसी root को compare करें।

> :icon-cross: **जाल 9.** “Cannot be determined” को बिना counterexample चुना।
> दो valid root choices बनाकर एक $<$ और दूसरा $>$ दिखाइए।

---

## 32.11 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(IBPS PO)* I: $x^2-7x+12=0$; II: $y^2-11y+30=0$। relation?

**हल:** $x=3,4$ और $y=5,6$ ⟹ $\mathbf{x<y}$।

**PYQ 2.** *(SBI Clerk)* I: $x^2-9x+20=0$; II: $y^2-5y+6=0$।

**हल:** $x=4,5$, $y=2,3$ ⟹ $\mathbf{x>y}$।

**PYQ 3.** *(IBPS Clerk)* I roots $2,3$; II roots $3,4$। strongest relation?

**हल:** equality possible, इसलिए $\mathbf{x\leq y}$।

**PYQ 4.** *(RRB PO)* I roots $2,5$; II roots $3,4$।

**हल:** choices cross करते हैं ⟹ **cannot be determined**।

**PYQ 5.** *(SBI PO)* I: $2x^2-7x+3=0$; II: $3y^2-14y+8=0$।

**हल:** I roots $1/2,3$; II roots $2/3,4$ ⟹ $\mathbf{x<y}$।

**PYQ 6.** *(IBPS Clerk)* $x^2-6x+9=0$ और $y^2-10y+25=0$।

**हल:** repeated roots $x=3,y=5$ ⟹ $\mathbf{x<y}$।

---

## 32.12 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | I roots $3,4$; II roots $5,6$ | $x<y$ | disjoint ranges |
| 2 | I roots $2,3$; II roots $4,5$ | $x<y$ | factorise |
| 3 | I roots $4,5$; II roots $2,3$ | $x>y$ | factorise |
| 4 | I roots $2,3$; II roots $3,4$ | $x\leq y$ | equality possible |
| 5 | I roots $2,5$; II roots $3,4$ | cannot determine | overlap/cross |
| 6 | $2x^2-7x+3$ vs $3y^2-14y+8$ | $x<y$ | roots $1/2,3$ vs $2/3,4$ |
| 7 | repeated roots 3 and 5 | $x<y$ | $D=0$ |
| 8 | $2x^2+3x+5$ | no real roots | $D<0$ |
| 9 | $2x^2-7x+3$ root sum | $7/2$ | Vieta |
| 10 | same equation root product | $3/2$ | Vieta |
| 11 | I roots $4,7$; II roots $5,6$ | cannot determine | crossing choices |
| 12 | larger roots of $x^2-8x+15$ and $y^2-10y+24$ | $x<y$ | $5<6$ |
| 13 | smaller roots of $x^2-7x+12$ and $y^2-9y+20$ | $x<y$ | $3<4$ |
| 14 | $x^2-4x+3$ and $y^2-8y+15$ | $x\leq y$ | roots $1,3$ vs $3,5$; equality possible |
| 15 | I roots lie in $(1,3)$, II roots $>5$ | $x<y$ | interval method |
| 16 | $x^2-5x+6$ discriminant | $1$ | $D=b^2-4ac$ |
| 17 | equal roots for $x^2-4x+k$ | $k=4$ | $D=0$ |
| 18 | $x^2-9x+20$ root sum/product | $9,20$ | Vieta |
| 19 | roots $4,7$; equation | $x^2-11x+28=0$ | construction |
| 20 | roots $2,5$; equation | $x^2-7x+10=0$ | construction |
| 21 | roots $2,5$ vs $3,4$; compare squares? | cannot determine | root choices |
| 22 | $P(2)=0$ for $P(x)=x^2-5x+6$ | $(x-2)$ factor | factor theorem |
| 23 | roots of I in $[1,2]$, II in $[4,6]$ | $x<y$ | bounds |
| 24 | $x^2-2kx+k^2-1=0$ roots | $k-1,k+1$ | perfect square |
| 25 | I larger root 6, II larger root 8 | $x<y$ | specified roots |

---

## 32.13 :icon-trophy: अध्याय का सार

```
━━━ Comparison format ━━━
Equation I → roots of x
Equation II → roots of y
सभी valid roots compare करें

━━━ Factor method ━━━
x²−7x+12 → x=3,4
 y²−11y+30 → y=5,6
हर x < हर y → x<y

━━━ Three outcomes ━━━
all x roots right of all y roots → x>y
all x roots left of all y roots → x<y
root ranges overlap/cross → cannot determine

━━━ Discriminant ━━━
Δ=b²−4ac
Δ>0: two real roots
Δ=0: equal root
Δ<0: no real roots

━━━ Vieta ━━━
α+β = −b/a
αβ = c/a
sum/product तभी compare करें जब root ranges तय हों

━━━ Bounds ━━━
exact roots कठिन हों तो interval bracket करें
sign changes and number line उपयोगी हैं

━━━ Algorithm ━━━
standard form
factor/formula
both roots
smallest/largest range
strict/equal check
option choose
```

> :icon-trophy: **Quadratic Comparison complete।** अब quadratic roots को factorisation, formula, discriminant, Vieta और intervals से compare किया जा सकता है—विशेषकर Banking exam के “x और y” format में।
>
> **आगे:** Chapter 33 — **रेखाएँ व कोण (Lines & Angles)**। अब Part 5 में geometry, mensuration और trigonometry की शुरुआत होगी।
