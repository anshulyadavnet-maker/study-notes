# अध्याय 27 — बीजगणित की नींव व बहुपद (Algebra Foundations & Polynomials)

## 27.1 :icon-target: परिचय व वेटेज

अध्याय 1–26 में हमने संख्याओं, अनुपात, समय, चाल और कार्य को शब्दों और सूत्रों में बदला। अब गणित की भाषा को और सामान्य बनाएँगे। जब कोई संख्या अज्ञात हो या बदल सकती हो, तो उसे $x$, $y$, $a$ जैसे variable से लिखना बीजगणित है।

> *"किसी संख्या का तीन गुना, उस संख्या से 5 अधिक है। संख्या क्या है?"*

इसे $3x=x+5$ लिखते ही verbal problem algebraic equation बन जाती है। Algebra का उद्देश्य symbols को कठिन बनाना नहीं, बल्कि बहुत से समान प्रश्नों को एक ही नियम से हल करना है।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | expression, equation, polynomial |
| **SSC CGL Tier-2** | **2–3** | simplification और algebraic operations |
| SSC CHSL / MTS / GD | 1 | basic algebra |
| SSC CPO | 1–2 | polynomial और equations |
| **IBPS / SBI PO** | **2–3** | quadratic foundation और comparison की तैयारी |
| IBPS / SBI Clerk | 1–2 | substitution और simplification |
| **RRB NTPC / ALP** | **1–2** | elementary algebra |
| UP Police SI / Constable | 1–2 | equations और identities की नींव |
| UPSSSC PET | 1 | basic symbols |
| Super TET / UPTET | 1–2 | algebraic thinking और teaching foundation |

> :icon-key: **पूरे अध्याय का एक वाक्य:** symbols को terms में बाँटिए, like terms को जोड़िए, brackets खोलिए और substitution से value जाँचिए।

---

## 27.2 :icon-number: Algebra की भाषा

### 1. Variable (चर)

ऐसी quantity जिसका मान बदल सकता है, variable कहलाती है। $x$, $y$, $a$, $b$ इसके सामान्य symbols हैं।

### 2. Constant (अचर)

जिसका मान स्थिर हो, वह constant है। $7$, $-3$, $1/2$ constants हैं।

### 3. Coefficient (गुणांक)

किसी variable के साथ गुणा होने वाली संख्या coefficient है। $5x$ में $5$ coefficient और $x$ variable है। $x$ का coefficient $1$ और $-x$ का coefficient $-1$ माना जाता है।

### 4. Term (पद)

$+$ या $-$ से अलग होने वाला प्रत्येक भाग एक term है।

$$3x^2-5x+7$$

में तीन terms हैं: $3x^2$, $-5x$ और $7$।

```figure
type: algebra-parts
a: 3
b: -5
c: 7
caption: 3x² − 5x + 7 में terms, coefficients, powers और constant पहचानिए
```

### 5. Power या exponent (घात)

$x^3$ में $3$ बताता है कि $x$ को तीन बार गुणा किया गया है।

$$x^3=x\times x\times x$$

### 6. Expression (व्यंजक)

जिसमें numbers, variables और operations हों, लेकिन बराबर का चिन्ह जरूरी न हो, वह expression है।

उदाहरण: $3x+5$, $a^2-4a+4$, $2p-q+7$।

### 7. Equation (समीकरण)

जिस statement में $=$ हो और दो expressions बराबर बताए गए हों, वह equation है।

उदाहरण: $3x+5=20$। Equation को सत्य बनाने वाला $x$ उसका solution है।

### 8. Identity (सर्वसमिका)

जो equality variables के हर मान के लिए सत्य हो, वह identity है।

उदाहरण: $(a+b)^2=a^2+2ab+b^2$। इसकी विस्तृत पढ़ाई Chapter 28 में होगी।

| वस्तु | उदाहरण | मुख्य पहचान |
|---|---|---|
| term | $-5x^2$ | $+$/$-$ से अलग भाग |
| expression | $2x+7$ | बराबर का चिन्ह नहीं भी हो सकता |
| equation | $2x+7=15$ | कुछ values पर सत्य |
| identity | $(a+b)^2=a^2+2ab+b^2$ | हर value पर सत्य |

> :icon-bulb: Expression का कोई एक निश्चित answer नहीं होता जब तक variable का मान न दिया जाए। Equation में variable का ऐसा मान ढूँढते हैं जो equality को सत्य बनाए।

---

## 27.3 :icon-steps: Like terms और algebraic operations

### Like terms

जिन terms में variables और उनके powers बिल्कुल समान हों, वे like terms हैं।

- $3x$ और $-5x$ like terms हैं
- $2x^2$ और $7x^2$ like terms हैं
- $4a^2$ और $4a$ unlike terms हैं
- $3x$ और $3y$ unlike terms हैं

Like terms में केवल coefficients जोड़े या घटाए जाते हैं; variable part वैसा ही रहता है।

```figure
type: like-terms
a: 3
b: 5
c: -2
caption: 3x + 5x − 2x में केवल coefficients को जोड़िए
```

**उदाहरण 1.** Simplify: $3x+5x-2x$।

$$3x+5x-2x=(3+5-2)x=\mathbf{6x}$$

**उदाहरण 2.** Simplify: $4a^2+3a-2a^2+5a$।

- $a^2$ terms: $4a^2-2a^2=2a^2$
- $a$ terms: $3a+5a=8a$

उत्तर $=\mathbf{2a^2+8a}$।

> :icon-warn: $3x+2y$ को $5xy$ या $5x$ मत बनाइए। Different variables वाले terms like नहीं हैं।

### Addition और subtraction

Polynomial जोड़ने के लिए like terms को एक column में रखिए।

**उदाहरण 3.**

$$(2x^2+3x+1)+(x^2-5x+4)$$

$$=(2+1)x^2+(3-5)x+(1+4)=\mathbf{3x^2-2x+5}$$

**उदाहरण 4.**

$$(5x^2-2x+1)-(2x^2+3x-4)$$

दूसरे bracket के हर sign को बदलें:

$$5x^2-2x+1-2x^2-3x+4=\mathbf{3x^2-5x+5}$$

### Multiplication of a monomial

Distributive law लगाइए:

$$a(b+c)=ab+ac$$

**उदाहरण 5.** $3x(2x^2-5x+4)$।

$$=6x^3-15x^2+12x$$

---

## 27.4 :icon-formula: Brackets और distributive law

Bracket के बाहर की संख्या या term bracket के प्रत्येक term से multiply होती है।

```figure
type: expression-tree
caption: 2x + 3(x − 1) को भीतर से बाहर की ओर evaluate कीजिए
```

**उदाहरण 6.** Simplify: $3(2x-5)+2(x+1)$।

$$3(2x-5)+2(x+1)=6x-15+2x+2=\mathbf{8x-13}$$

**उदाहरण 7.** Simplify: $-2(3a-4b+5)$।

$$-2(3a-4b+5)=-6a+8b-10$$

Minus sign bracket के हर term पर लगा।

### Two brackets का multiplication

पहले bracket के हर term को दूसरे bracket के हर term से multiply करें।

**उदाहरण 8.**

$$(x+3)(x+2)$$

$$=x\times x+x\times2+3\times x+3\times2$$

$$=\mathbf{x^2+5x+6}$$

**उदाहरण 9.** $(2a-3)(a+4)$।

$$=2a^2+8a-3a-12=\mathbf{2a^2+5a-12}$$

> :icon-key: FOIL केवल दो binomials के लिए याद रखने की trick है: First, Outside, Inside, Last। लेकिन हर product में distributive law हमेशा सुरक्षित विधि है।

### Sign rules

| Operation | Result |
|---|---|
| $(+)(+)$ | $+$ |
| $(+)(-)$ | $-$ |
| $(-)(+)$ | $-$ |
| $(-)(-)$ | $+$ |

**उदाहरण 10.** $-(a-3b+2)=-a+3b-2$।

---

## 27.5 :icon-chart: Polynomials और degree

Polynomial ऐसा algebraic expression है जिसमें variable की powers non-negative whole numbers होती हैं और terms की संख्या सीमित होती है।

### Terms की संख्या के आधार पर

| नाम | Terms | उदाहरण |
|---|---:|---|
| Monomial | 1 | $5x^3$ |
| Binomial | 2 | $x^2-4$ |
| Trinomial | 3 | $x^2+3x+2$ |
| Polynomial | कई | $2x^4-x^3+5x^2-7x+1$ |

### Degree

Polynomial में variable की सबसे बड़ी power उसका degree है।

```figure
type: polynomial-degree
degree: 4
caption: polynomial की highest power उसका degree बताती है
```

**उदाहरण 11.** $5x^4-2x^3+x-9$ का degree $4$ है।

**उदाहरण 12.** $7x^2+3x+1$ quadratic polynomial है और degree $2$ है।

**उदाहरण 13.** $9x^5-4x^2+6$ का degree $5$ है, भले बीच की powers मौजूद न हों।

### Standard form

Polynomial को सामान्यतः descending powers में लिखते हैं।

**उदाहरण 14.** $5-2x^3+x-4x^2$ को standard form में लिखिए।

सबसे बड़ी power से शुरू करें:

$$\mathbf{-2x^3-4x^2+x+5}$$

### Constant और zero polynomial

- Non-zero constant polynomial जैसे $7$ का degree $0$ होता है।
- Zero polynomial $0$ की degree सामान्यतः निर्धारित नहीं मानी जाती।
- किसी term का coefficient $0$ हो तो वह term लिखी नहीं जाती: $3x^2+0x+5=3x^2+5$।

### Polynomial operations

Polynomials को जोड़ते और घटाते समय like powers मिलाइए। गुणा करते समय हर term distribute कीजिए।

**उदाहरण 15.**

$$(2x^3-x+1)+(x^3+4x^2+2)$$

$$=\mathbf{3x^3+4x^2-x+3}$$

**उदाहरण 16.** $x(x^2-3x+2)=\mathbf{x^3-3x^2+2x}$।

> :icon-star: Degree के लिए केवल highest exponent देखना है; coefficients का size या terms की संख्या degree तय नहीं करती।

---

## 27.6 :icon-divide: Substitution और simple equations

### Substitution

Variable की जगह उसका दिया हुआ value रखने को substitution कहते हैं। हर occurrence में वही value replace करनी है।

```figure
type: substitution
a: 2
b: -3
c: 1
x: 2
caption: P(x) = 2x² − 3x + 1 में x = 2 रखने की क्रमिक प्रक्रिया
```

**उदाहरण 17.** $P(x)=2x^2-3x+1$ में $x=2$ रखें।

$$P(2)=2(2)^2-3(2)+1=8-6+1=\mathbf{3}$$

**उदाहरण 18.** $Q(a)=3a^2-2a+5$ में $a=-1$ रखें।

$$Q(-1)=3(-1)^2-2(-1)+5=3+2+5=\mathbf{10}$$

**उदाहरण 19.** $P(x)=4x^3-2x+7$ का $P(0)$।

$$P(0)=4(0)^3-2(0)+7=\mathbf{7}$$

**उदाहरण 20.** $P(x)=2x^2-5x+3$ का $P(1)$।

$$P(1)=2-5+3=\mathbf{0}$$

इसका अर्थ है कि $x=1$ रखने पर polynomial का value zero आता है। Factor और zero का विस्तृत सम्बन्ध Chapter 29 में आएगा।

### Simple equation

Equation में दोनों sides का balance बनाए रखना होता है। जो operation एक side पर करें, वही दूसरी side पर करें।

```figure
type: equation-balance
a: 2
b: 5
answer: 6
caption: 2x + 5 = 17 में हर step पर equality का balance बनाए रखिए
```

**उदाहरण 21.** $3x+5=20$।

$$3x=20-5=15\quad\Rightarrow\quad x=\mathbf{5}$$

**उदाहरण 22.** $2x-7=13$।

$$2x=13+7=20\quad\Rightarrow\quad x=\mathbf{10}$$

**उदाहरण 23.** $4(x-2)=24$।

$$x-2=6\quad\Rightarrow\quad x=\mathbf{8}$$

**उदाहरण 24.** $3(x+4)-2=19$।

$$3x+12-2=19\quad\Rightarrow\quad3x=9\quad\Rightarrow\quad x=\mathbf{3}$$

> :icon-warn: “Term को दूसरी side ले जाने पर sign बदलता है” shortcut है। असली कारण दोनों sides पर opposite operation करना है।

---

## 27.7 :icon-bulb: शॉर्टकट व उनके प्रमाण

### :icon-timer: शॉर्टकट 1 — coefficient और power अलग पहचानिए

$-7x^3$ में:

- coefficient $=-7$
- variable $=x$
- power $=3$
- term का degree $=3$

### :icon-timer: शॉर्टकट 2 — like terms test

दो terms like हैं यदि:

1. variables वही हों,
2. प्रत्येक variable की power वही हो,
3. coefficient कोई भी हो सकता है।

$3a^2b$ और $-5a^2b$ like हैं; $3a^2b$ और $3ab^2$ unlike हैं।

### :icon-timer: शॉर्टकट 3 — bracket खोलने का नियम

$$k(A+B+C)=kA+kB+kC$$

और —

$$-k(A-B+C)=-kA+kB-kC$$

हर term पर sign और multiplier लगाइए।

### :icon-timer: शॉर्टकट 4 — polynomial degree

- Sum का degree अधिकतम degrees में से हो सकता है; highest terms cancel हों तो actual degree घटेगा।
- Product का degree, non-zero polynomials के degrees का योग होता है।

उदाहरण: degree $2$ और degree $3$ के product का degree $5$।

### :icon-timer: शॉर्टकट 5 — special values

Polynomial $P(x)$ के लिए:

- $P(0)$ = constant term
- $P(1)$ = सभी coefficients का योग
- $P(-1)$ = alternating coefficient sum

**उदाहरण:** $P(x)=2x^2-5x+3$।

$$P(0)=3,\qquad P(1)=0,\qquad P(-1)=2+5+3=10$$

### :icon-timer: शॉर्टकट 6 — equation check

Solution मिलने के बाद उसे मूल equation में रखकर जाँचिए।

$x=5$ in $3x+5=20$:

$$3(5)+5=15+5=20\quad\checkmark$$

### :icon-timer: शॉर्टकट 7 — word statement translation

| शब्द | Algebra |
|---|---|
| किसी संख्या | $x$ |
| संख्या से 5 अधिक | $x+5$ |
| संख्या से 5 कम | $x-5$ |
| संख्या का 3 गुना | $3x$ |
| संख्या का आधा | $x/2$ |
| दो संख्याओं का योग | $x+y$ |
| दो संख्याओं का अन्तर | $x-y$ |

---

## 27.8 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Unlike terms को जोड़ देना।
> $3x+2y$ को $5xy$ या $5x$ नहीं बना सकते।

> :icon-cross: **जाल 2.** Minus bracket के हर term पर न लगाना।
> $-(a-b+c)=-a+b-c$।

> :icon-cross: **जाल 3.** Polynomial की degree को terms की संख्या समझना।
> $5x^4+x+1$ में तीन terms हैं, लेकिन degree $4$ है।

> :icon-cross: **जाल 4.** $-x$ का coefficient $1$ लिखना।
> $-x$ का coefficient $-1$ है।

> :icon-cross: **जाल 5.** Substitution में negative value का bracket न लगाना।
> $x=-2$ हो तो $x^2=(-2)^2=4$ लिखिए, केवल $-2^2$ नहीं।

> :icon-cross: **जाल 6.** Polynomial को standard form में न लिखना।
> Highest power से descending order में arrange करें।

> :icon-cross: **जाल 7.** Equation में केवल एक side पर operation करना।
> Equality balance रखने के लिए दोनों sides पर समान operation करें।

> :icon-cross: **जाल 8.** $P(1)$ और $P(-1)$ में signs भूलना।
> $P(-1)$ में odd powers के signs बदलते हैं।

> :icon-cross: **जाल 9.** Expression, equation और identity को एक ही मानना।
> Expression general form है; equation कुछ values पर सत्य; identity हर value पर सत्य।

---

## 27.9 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* $3x+5=20$ में $x$?

**हल:** $3x=15$ ⟹ $\mathbf{x=5}$।

**PYQ 2.** *(SSC CHSL)* $4a^2+3a-2a^2+5a$ simplify करें।

**हल:** $\mathbf{2a^2+8a}$।

**PYQ 3.** *(RRB NTPC)* $5-2x^3+x-4x^2$ का standard form और degree?

**हल:** $\mathbf{-2x^3-4x^2+x+5}$; degree $\mathbf{3}$।

**PYQ 4.** *(IBPS Clerk)* $P(x)=2x^2-3x+1$ में $x=2$।

**हल:** $8-6+1=\mathbf{3}$।

**PYQ 5.** *(UP Police SI)* $(x+3)(x+2)$ का विस्तार।

**हल:** $\mathbf{x^2+5x+6}$।

**PYQ 6.** *(SSC MTS)* $P(x)=2x^2-5x+3$ के लिए $P(1)$।

**हल:** $2-5+3=\mathbf{0}$।

---

## 27.10 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | $7x^2-3x+4$ के terms और degree | 3 terms, degree 2 | highest power |
| 2 | $-5x^2+7x-1$ में $x^2$ का coefficient | $-5$ | coefficient |
| 3 | $3x$ और $-5x$ like/unlike? | like | same variable/power |
| 4 | $3x+5x-2x$ | $6x$ | coefficients |
| 5 | $4a^2+3a-2a^2+5a$ | $2a^2+8a$ | like terms |
| 6 | $(2x^2+3x+1)+(x^2-5x+4)$ | $3x^2-2x+5$ | add powers |
| 7 | $(5x^2-2x+1)-(2x^2+3x-4)$ | $3x^2-5x+5$ | change signs |
| 8 | $3(2x-5)$ | $6x-15$ | distribute |
| 9 | $3(2x-5)+2(x+1)$ | $8x-13$ | expand/combine |
| 10 | $(x+3)(x+2)$ | $x^2+5x+6$ | distributive product |
| 11 | $5-2x^3+x-4x^2$ degree | 3 | highest power |
| 12 | उसी polynomial का standard form | $-2x^3-4x^2+x+5$ | descending powers |
| 13 | $P(x)=2x^2-3x+1$, $P(2)$ | 3 | substitution |
| 14 | $Q(a)=3a^2-2a+5$, $Q(-1)$ | 10 | bracket negative value |
| 15 | $P(x)=4x^3-2x+7$, $P(0)$ | 7 | constant term |
| 16 | $P(x)=2x^2-5x+3$, $P(1)$ | 0 | coefficient sum |
| 17 | $3x+5=20$ | $x=5$ | subtract/divide |
| 18 | $2x-7=13$ | $x=10$ | add/divide |
| 19 | $4(x-2)=24$ | $x=8$ | divide/add |
| 20 | $3(x+4)-2=19$ | $x=3$ | expand |
| 21 | $5x/2=15$ | $x=6$ | multiply $2/5$ |
| 22 | किसी संख्या से 7 अधिक = 19 | $x=12$ | $x+7=19$ |
| 23 | $x+y=20$, $x-y=4$ | $x=12,y=8$ | add equations |
| 24 | $(2x^3-x+1)+(x^3+4x^2+2)$ | $3x^3+4x^2-x+3$ | combine powers |
| 25 | $P(x)=x^2-4x+4$, $P(2)$ | 0 | substitution |

---

## 27.11 :icon-trophy: अध्याय का सार

```
━━━ Algebra language ━━━
variable: बदलने वाली quantity
constant: स्थिर number
coefficient: variable के साथ लगी संख्या
term: + या − से अलग भाग
expression: algebraic form, जरूरी नहीं कि = हो
equation: दो expressions की equality
identity: हर value पर true equality

━━━ Expression parts ━━━
3x² − 5x + 7
terms: 3x², −5x, 7
coefficients: 3, −5, 7
powers: 2, 1, 0
constant term: 7

━━━ Like terms ━━━
3x + 5x − 2x = 6x
same variable और same power वाले terms के coefficients जोड़िए

━━━ Brackets ━━━
k(A+B+C) = kA+kB+kC
−k(A−B+C) = −kA+kB−kC

━━━ Polynomial ━━━
monomial: 1 term
binomial: 2 terms
trinomial: 3 terms
degree = highest power

5 − 2x³ + x − 4x²
standard form = −2x³ − 4x² + x + 5
degree = 3

━━━ Substitution ━━━
P(0) = constant term
P(1) = coefficients का sum
P(−1) = alternating sum

━━━ Simple equation ━━━
3x+5=20
3x=15
x=5
दोनों sides पर समान operation

━━━ जाल ━━━
unlike terms मत जोड़िए
minus bracket में हर sign बदलिए
negative substitution में brackets लगाइए
degree को terms की संख्या मत समझिए
share operation दोनों sides पर कीजिए
```

> :icon-trophy: **Part 4 आरंभ।** अब algebraic terms, expressions और polynomials की भाषा तैयार है।
>
> **आगे:** अध्याय 28 — **सर्वसमिकाएँ (Identities)**। वहाँ $(a+b)^2$, $(a-b)^2$, $a^2-b^2$ और अन्य identities को proof, shortcut और exam applications के साथ पढ़ेंगे।
