# अध्याय 28 — सर्वसमिकाएँ (Algebraic Identities)

## 28.1 :icon-target: परिचय व वेटेज

Chapter 27 में हमने expressions, polynomials और brackets की नींव बनाई। अब कुछ ऐसी equalities सीखेंगे जो variables की हर value के लिए सत्य रहती हैं। इन्हें **algebraic identities** कहते हैं।

> *"103² बिना लंबा multiplication किए कैसे निकालेंगे?"*

$(100+3)^2$ को identity से खोलिए:

$$100^2+2(100)(3)+3^2=10609$$

Identities केवल formula याद करने के लिए नहीं हैं। वे expansion, factorisation, mental calculation, simplification और कई exam shortcuts की common language हैं।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | square और difference of squares |
| **SSC CGL Tier-2** | **2–3** | identity application और simplification |
| SSC CHSL / MTS / GD | 1–2 | basic identities |
| **SSC CPO** | **1–2** | cubes और numerical shortcuts |
| **IBPS / SBI PO** | **2–3** | algebraic simplification |
| IBPS / SBI Clerk | 1–2 | direct formula application |
| **RRB NTPC / ALP** | **1–2** | square, product, factorisation base |
| UP Police SI / Constable | 1–2 | identity-based arithmetic |
| UPSSSC PET | 1 | simple expansion |
| Super TET / UPTET | 1 | concept and pattern recognition |

> :icon-key: **पूरे अध्याय का एक वाक्य:** पहचानिए कि expression किस identity का pattern है, फिर values रखकर या terms compare करके तुरंत simplify कीजिए।

---

## 28.2 :icon-number: Identity क्या है?

Equation कुछ particular values पर सत्य हो सकती है। Identity variables के हर मान पर सत्य होती है।

उदाहरण:

- $x+2=5$ एक equation है; केवल $x=3$ पर सत्य।
- $(a+b)^2=a^2+2ab+b^2$ identity है; $a,b$ की हर value पर सत्य।

Identity का प्रमाण सामान्यतः expansion या area से किया जाता है।

### सबसे उपयोगी identities

| # | Identity |
|---:|---|
| 1 | $(a+b)^2=a^2+2ab+b^2$ |
| 2 | $(a-b)^2=a^2-2ab+b^2$ |
| 3 | $(a+b)(a-b)=a^2-b^2$ |
| 4 | $(x+a)(x+b)=x^2+(a+b)x+ab$ |
| 5 | $(x-a)(x-b)=x^2-(a+b)x+ab$ |
| 6 | $(a+b)^3=a^3+3a^2b+3ab^2+b^3$ |
| 7 | $(a-b)^3=a^3-3a^2b+3ab^2-b^3$ |
| 8 | $a^3+b^3=(a+b)(a^2-ab+b^2)$ |
| 9 | $a^3-b^3=(a-b)(a^2+ab+b^2)$ |
| 10 | $a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$ |

> :icon-bulb: Formula को blindly याद करने के बजाय left side को expand करके right side तक पहुँचना सीखिए। तब sign भूलने की सम्भावना कम होगी।

---

## 28.3 :icon-steps: Square identities — proof और उपयोग

### Identity 1: $(a+b)^2$

$$\text{LHS}=(a+b)^2=(a+b)(a+b)$$

Distributive law से —

$$a^2+ab+ab+b^2=a^2+2ab+b^2$$

```figure
type: square-sum
a: 3
b: 2
caption: side (a+b) वाले square का area a² + ab + ab + b² होता है
```

**उदाहरण 1.** $103^2$ निकालिए।

$$103^2=(100+3)^2$$

$$=100^2+2(100)(3)+3^2=10000+600+9=\mathbf{10609}$$

**उदाहरण 2.** $48^2$।

$$48^2=(50-2)^2=2500-200+4=\mathbf{2304}$$

### Identity 2: $(a-b)^2$

$$\text{LHS}=(a-b)(a-b)=a^2-ab-ab+b^2$$

अतः —

$$\mathbf{(a-b)^2=a^2-2ab+b^2}$$

```figure
type: square-difference
a: 5
b: 2
caption: (a−b)² में middle term −2ab होता है
```

**उदाहरण 3.** $97^2$।

$$97^2=(100-3)^2=10000-600+9=\mathbf{9409}$$

**उदाहरण 4.** $49^2$।

$$49^2=(50-1)^2=2500-100+1=\mathbf{2401}$$

> :icon-warn: $(a-b)^2$ को $a^2-b^2$ मत लिखिए। सही middle term $-2ab$ और अन्त में $+b^2$ रहेगा।

### Identity 3: Difference of squares

$$\text{LHS}=(a+b)(a-b)$$

$$=a^2-ab+ab-b^2=a^2-b^2$$

```figure
type: difference-squares
a: 7
b: 3
caption: conjugate factors में −ab और +ab cancel हो जाते हैं
```

**उदाहरण 5.** $103\times97$।

$$103\times97=(100+3)(100-3)=100^2-3^2=\mathbf{9991}$$

**उदाहरण 6.** $52\times48$।

$$52\times48=(50+2)(50-2)=2500-4=\mathbf{2496}$$

---

## 28.4 :icon-calc: Product identities

### Identity 4: $(x+a)(x+b)$

$$(x+a)(x+b)=x^2+bx+ax+ab=x^2+(a+b)x+ab$$

**उदाहरण 7.** $(x+3)(x+5)$।

$$=x^2+(3+5)x+3\times5=\mathbf{x^2+8x+15}$$

### Identity 5: $(x-a)(x-b)$

$$(x-a)(x-b)=x^2-bx-ax+ab=x^2-(a+b)x+ab$$

**उदाहरण 8.** $(x-4)(x-7)$।

$$=x^2-(4+7)x+28=\mathbf{x^2-11x+28}$$

### Mixed signs

**उदाहरण 9.** $(x+a)(x-b)$।

$$=x^2+(a-b)x-ab$$

**उदाहरण 10.** $(2x+3)(2x-5)$।

यहाँ common part $2x$ है और conjugate constants $3,-5$ नहीं हैं, इसलिए direct distribution करें:

$$4x^2-10x+6x-15=\mathbf{4x^2-4x-15}$$

> :icon-key: $(x+a)(x+b)$ identity में दोनों brackets का पहला term exactly $x$ होना चाहिए। अलग leading coefficients हों तो पहले सामान्य multiplication करें।

---

## 28.5 :icon-chart: Cube identities

### Identity 6: $(a+b)^3$

$$\mathbf{(a+b)^3=a^3+3a^2b+3ab^2+b^3}$$

Terms के coefficients $1,3,3,1$ होते हैं।

```figure
type: cube-identity
a: 2
b: 1
caption: (a+b)³ में a³, 3a²b, 3ab² और b³ चार contributions आते हैं
```

**उदाहरण 11.** $21^3$।

$$21^3=(20+1)^3$$

$$=20^3+3(20^2)(1)+3(20)(1^2)+1^3$$

$$=8000+1200+60+1=\mathbf{9261}$$

### Identity 7: $(a-b)^3$

$$\mathbf{(a-b)^3=a^3-3a^2b+3ab^2-b^3}$$

Signs का pattern: $+,-,+,-$।

**उदाहरण 12.** $19^3$।

$$19^3=(20-1)^3=8000-1200+60-1=\mathbf{6859}$$

> :icon-bulb: Cube expansion में middle terms के coefficients $3$ और $3$ भूलना सबसे सामान्य गलती है।

### Sum और difference of cubes

$$\mathbf{a^3+b^3=(a+b)(a^2-ab+b^2)}$$

$$\mathbf{a^3-b^3=(a-b)(a^2+ab+b^2)}$$

**उदाहरण 13.** $8^3+2^3$ को factor form में लिखिए।

$$8^3+2^3=(8+2)(8^2-8\times2+2^2)$$

$$=10(64-16+4)=\mathbf{520}$$

**उदाहरण 14.** $5^3-3^3$।

$$5^3-3^3=(5-3)(25+15+9)=2\times49=\mathbf{98}$$

```figure
type: mental-square
n: 103
base: 100
caption: nearby base के साथ square identity से तेज calculation
```

---

## 28.6 :icon-brain: Three-variable identity और special condition

तीन variables के लिए —

$$a^3+b^3+c^3-3abc$$

का factor form —

$$=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$$

```figure
type: three-variable
a: 1
b: 2
c: -3
caption: तीन-variable identity में पहले a+b+c की condition जाँचिए
```

### Special case: $a+b+c=0$

यदि $a+b+c=0$, तो पूरा right side zero हो जाता है। इसलिए —

$$\mathbf{a^3+b^3+c^3=3abc}$$

**उदाहरण 15.** यदि $a+b+c=0$, तो सिद्ध कीजिए:

$$a^3+b^3+c^3=3abc$$

**हल:**

$$a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$$

पहला factor $a+b+c=0$ है, इसलिए left side $=0$।

**उदाहरण 16.** $a=1,b=2,c=-3$ के लिए $a^3+b^3+c^3$।

क्योंकि $1+2-3=0$ —

$$a^3+b^3+c^3=3(1)(2)(-3)=\mathbf{-18}$$

सीधी जाँच: $1+8-27=-18$।

### Useful rearrangement

यदि $a+b+c$ दिया हो और तीन cubes का expression हो, तो पूरा expansion करने से पहले इस identity को पहचानिए।

> :icon-star: Three-variable question में पहला check हमेशा $a+b+c$ का करें। Zero condition मिलने पर calculation बहुत छोटी हो जाती है।

---

## 28.7 :icon-bulb: शॉर्टकट व उनके प्रमाण

### :icon-timer: शॉर्टकट 1 — nearest base square

$n^2$ के लिए पास की round number चुनें:

- $100+d$: $10000+200d+d^2$
- $100-d$: $10000-200d+d^2$
- $50+d$: $2500+100d+d^2$
- $50-d$: $2500-100d+d^2$

**उदाहरण:** $104^2=10000+800+16=10816$।

### :icon-timer: शॉर्टकट 2 — numbers equidistant from a base

$$(m+d)(m-d)=m^2-d^2$$

इससे $98\times102=100^2-2^2=9996$ तुरंत मिलता है।

### :icon-timer: शॉर्टकट 3 — product of consecutive numbers

$$n(n+1)=n^2+n$$

और —

$$n(n-1)=n^2-n$$

यह identities का direct expansion है और mental calculation में उपयोगी है।

### :icon-timer: शॉर्टकट 4 — square से middle product

यदि $(a+b)^2$ और $a^2+b^2$ दिए हों, तो —

$$2ab=(a+b)^2-a^2-b^2$$

**उदाहरण:** $a+b=10$, $a^2+b^2=58$।

$$2ab=100-58=42\quad\Rightarrow\quad ab=21$$

### :icon-timer: शॉर्टकट 5 — sum और difference से squares

$$a^2+b^2=\frac{(a+b)^2+(a-b)^2}{2}$$

$$ab=\frac{(a+b)^2-(a-b)^2}{4}$$

### :icon-timer: शॉर्टकट 6 — cube sign pattern

| Expression | Middle signs |
|---|---|
| $(a+b)^3$ | $+3a^2b+3ab^2$ |
| $(a-b)^3$ | $-3a^2b+3ab^2$ |
| $a^3+b^3$ factor | अंदर $-ab$ |
| $a^3-b^3$ factor | अंदर $+ab$ |

### :icon-timer: शॉर्टकट 7 — reverse recognition

यदि expression में:

- $a^2+2ab+b^2$ हो ⟹ $(a+b)^2$
- $a^2-2ab+b^2$ हो ⟹ $(a-b)^2$
- $a^2-b^2$ हो ⟹ $(a+b)(a-b)$
- $a^3+3a^2b+3ab^2+b^3$ हो ⟹ $(a+b)^3$

तो expansion करने के बजाय तुरंत reverse identity लगाइए।

---

## 28.8 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** $(a+b)^2=a^2+b^2$ लिखना।
> $2ab$ middle term कभी न भूलिए।

> :icon-cross: **जाल 2.** $(a-b)^2$ में अंतिम $b^2$ को negative करना।
> सही formula $a^2-2ab+b^2$ है।

> :icon-cross: **जाल 3.** $(a+b)(a-b)$ को $a^2+b^2$ लिखना।
> सही result $a^2-b^2$ है।

> :icon-cross: **जाल 4.** Cube identities में $3$ coefficients छोड़ देना।
> Pattern $1,3,3,1$ याद रखें।

> :icon-cross: **जाल 5.** $a^3+b^3$ के factor में अंदर plus लिखना।
> Sum of cubes: $(a+b)(a^2-ab+b^2)$।

> :icon-cross: **जाल 6.** $a^3-b^3$ के factor में अंदर minus लिखना।
> Difference of cubes: $(a-b)(a^2+ab+b^2)$।

> :icon-cross: **जाल 7.** $a+b+c=0$ condition check न करना।
> यह condition cubes वाले प्रश्न को एक line में बदल सकती है।

> :icon-cross: **जाल 8.** Identity को equation समझना।
> Identity हर variable value पर सत्य होती है; equation का solution सीमित हो सकता है।

> :icon-cross: **जाल 9.** Nearest base चुनकर correction का sign गलत करना।
> $100-d$ में middle term negative और $100+d$ में positive होगा।

---

## 28.9 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* $103^2$ identity से निकालिए।

**हल:** $(100+3)^2=10000+600+9=\mathbf{10609}$।

**PYQ 2.** *(SSC CHSL)* $97^2$।

**हल:** $(100-3)^2=10000-600+9=\mathbf{9409}$।

**PYQ 3.** *(RRB NTPC)* $52\times48$।

**हल:** $(50+2)(50-2)=2500-4=\mathbf{2496}$।

**PYQ 4.** *(IBPS Clerk)* $(x+3)(x+5)$ का विस्तार।

**हल:** $\mathbf{x^2+8x+15}$।

**PYQ 5.** *(UP Police SI)* $a+b+c=0$ हो तो $a^3+b^3+c^3$।

**हल:** $\mathbf{3abc}$।

**PYQ 6.** *(SSC MTS)* $21^3$ को identity से निकालिए।

**हल:** $(20+1)^3=\mathbf{9261}$।

---

## 28.10 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | $(a+b)^2$ | $a^2+2ab+b^2$ | square identity |
| 2 | $(a-b)^2$ | $a^2-2ab+b^2$ | square identity |
| 3 | $(a+b)(a-b)$ | $a^2-b^2$ | conjugates |
| 4 | $103^2$ | $10609$ | $(100+3)^2$ |
| 5 | $48^2$ | $2304$ | $(50-2)^2$ |
| 6 | $97^2$ | $9409$ | $(100-3)^2$ |
| 7 | $103\times97$ | $9991$ | $100^2-3^2$ |
| 8 | $52\times48$ | $2496$ | $50^2-2^2$ |
| 9 | $(x+3)(x+5)$ | $x^2+8x+15$ | product identity |
| 10 | $(x-4)(x-7)$ | $x^2-11x+28$ | product identity |
| 11 | $(2x+3)(2x-5)$ | $4x^2-4x-15$ | distribute |
| 12 | $(a+b)^3$ | $a^3+3a^2b+3ab^2+b^3$ | cube identity |
| 13 | $(a-b)^3$ | $a^3-3a^2b+3ab^2-b^3$ | cube identity |
| 14 | $21^3$ | $9261$ | $(20+1)^3$ |
| 15 | $19^3$ | $6859$ | $(20-1)^3$ |
| 16 | $8^3+2^3$ | $520$ | sum of cubes |
| 17 | $5^3-3^3$ | $98$ | difference of cubes |
| 18 | $a=1,b=2,c=-3$, $a^3+b^3+c^3$ | $-18$ | sum zero |
| 19 | $a+b=10$, $a^2+b^2=58$; find $ab$ | $21$ | $2ab$ formula |
| 20 | $a+b=12$, $a-b=4$; find $a^2+b^2$ | $80$ | square formula |
| 21 | $98\times102$ | $9996$ | $100^2-2^2$ |
| 22 | $(x+2)^2-(x-2)^2$ | $8x$ | difference of squares |
| 23 | $(x+1)^3$ | $x^3+3x^2+3x+1$ | cube expansion |
| 24 | $a^3+b^3$ factor form | $(a+b)(a^2-ab+b^2)$ | sum cubes |
| 25 | $P(x)=x^2+2x+1$, $P(9)$ | $100$ | $(x+1)^2$ |

---

## 28.11 :icon-trophy: अध्याय का सार

```
━━━ Square identities ━━━
(a+b)^2 = a^2 + 2ab + b^2
(a−b)^2 = a^2 − 2ab + b^2
(a+b)(a−b) = a^2 − b^2

103² = (100+3)² = 10609
97² = (100−3)² = 9409
103×97 = 100²−3² = 9991

━━━ Product identities ━━━
(x+a)(x+b) = x²+(a+b)x+ab
(x−a)(x−b) = x²−(a+b)x+ab

━━━ Cube identities ━━━
(a+b)³ = a³+3a²b+3ab²+b³
(a−b)³ = a³−3a²b+3ab²−b³

a³+b³ = (a+b)(a²−ab+b²)
a³−b³ = (a−b)(a²+ab+b²)

━━━ Three variables ━━━
a³+b³+c³−3abc
= (a+b+c)(a²+b²+c²−ab−bc−ca)

if a+b+c=0 → a³+b³+c³=3abc

━━━ Useful shortcuts ━━━
(a+d)(a−d)=a²−d²
P(0) = constant term
P(1) = coefficient sum
nearby base से square निकालिए

━━━ जाल ━━━
2ab मत भूलिए
(a−b)² में अंतिम +b²
sum/difference cube के अंदर signs उलटे
condition a+b+c=0 पहले जाँचिए
```

> :icon-trophy: **अध्याय 27 की algebra foundation अब identities से मजबूत हुई।** अब expressions को expand करने के साथ-साथ reverse करके factor form में भी पहचान सकेंगे।
>
> **आगे:** अध्याय 29 — **गुणनखंडन (Factorisation)**। वहाँ इन्हीं identities को उल्टी दिशा में लगाकर polynomial को factors में तोड़ेंगे।
