# अध्याय 29 — गुणनखंडन (Factorisation)

## 29.1 :icon-target: परिचय व वेटेज

Chapter 27 में हमने algebraic expressions और Chapter 28 में identities सीखी। Factorisation उन्हीं identities को **उल्टी दिशा** में लगाने की कला है। Expansion में factors को multiply करके expression बनता है; factorisation में expression को ऐसे factors में तोड़ते हैं जिनका product वही original expression देता है।

> *"$x^2+5x+6$ को factors में कैसे तोड़ेंगे?"*

ऐसे दो numbers चाहिए जिनका product $6$ और sum $5$ हो: $2$ और $3$। इसलिए —

$$x^2+5x+6=(x+2)(x+3)$$

Factorisation algebraic fractions को simplify करने, quadratic equations को solve करने और polynomial structure पहचानने की नींव है।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | common factor, quadratic |
| **SSC CGL Tier-2** | **2–3** | splitting middle term |
| SSC CHSL / MTS / GD | 1–2 | identity-based factors |
| **SSC CPO** | **1–2** | polynomial factorisation |
| **IBPS / SBI PO** | **2–3** | quadratic comparison की तैयारी |
| IBPS / SBI Clerk | 1–2 | direct factor pairs |
| **RRB NTPC / ALP** | **1–2** | factorisation और equations |
| UP Police SI / Constable | 1–2 | common factor, identities |
| UPSSSC PET | 1 | basic factorisation |
| Super TET / UPTET | 1 | algebraic reasoning |

> :icon-key: **पूरे अध्याय का एक वाक्य:** पहले common factor देखिए, फिर identity pattern पहचानिए, और quadratic में middle term को suitable parts में split कीजिए।

---

## 29.2 :icon-number: Factor और factorisation की भाषा

यदि दो या अधिक expressions का product किसी expression को बनाता है, तो वे उसके factors हैं।

$$3(x+2)=3x+6$$

यहाँ $3$ और $(x+2)$, $3x+6$ के factors हैं।

| शब्द | अर्थ | उदाहरण |
|---|---|---|
| factor | product बनाने वाला भाग | $3$, $(x+2)$ |
| factorisation | expression को factors में लिखना | $3x+6=3(x+2)$ |
| common factor | सभी terms में पाया जाने वाला factor | $3$ in $3x+6$ |
| factor pair | दो factors जिनका product original हो | $2,3$ for $x^2+5x+6$ |
| irreducible factor | दिए हुए number system में आगे न टूटे | $x+2$ over integers |

Factorisation की जाँच के लिए factors को वापस multiply करें। यदि original expression मिले, factorisation सही है।

---

## 29.3 :icon-calc: Common factor method

हर term के numerical coefficients का HCF और variables की common lowest power बाहर निकालिए।

```figure
type: common-factor
factor: 3
a: 2
b: 3
caption: हर term में common factor निकालकर bracket में शेष expression रखिए
```

**उदाहरण 1.** $6x+9$ का factorisation।

दोनों coefficients का HCF $3$ है:

$$6x+9=\mathbf{3(2x+3)}$$

**उदाहरण 2.** $12a^2b-8ab^2$।

- numerical HCF $=4$
- दोनों terms में $a$ है
- दोनों में $b$ की lowest power $b^1$ है

$$12a^2b-8ab^2=\mathbf{4ab(3a-2b)}$$

**उदाहरण 3.** $15x^3y^2+10x^2y^3$।

Common factor $=5x^2y^2$।

$$=\mathbf{5x^2y^2(3x+2y)}$$

> :icon-bulb: Common factor बाहर निकालने के बाद bracket में कोई common factor बचा हो तो factorisation अधूरा है।

### Negative common factor

यदि bracket का पहला term negative हो, तो पूरी expression को $-1$ बाहर निकालना उपयोगी है।

**उदाहरण 4.** $-x^2+5x-6$।

$$-(x^2-5x+6)=\mathbf{-(x-2)(x-3)}$$

---

## 29.4 :icon-steps: Grouping method

चार terms में पहले दो और आखिरी दो को group करके common bracket बनाइए।

```figure
type: grouping-factor
caption: दो groups से एक ही binomial बाहर निकालकर final factors बनाइए
```

**उदाहरण 5.** $ax+ay+bx+by$।

पहले दो और आखिरी दो group करें:

$$ax+ay+bx+by=a(x+y)+b(x+y)$$

अब $(x+y)$ common है:

$$=\mathbf{(a+b)(x+y)}$$

**उदाहरण 6.** $3x^2+6x+2x+4$।

$$3x(x+2)+2(x+2)$$

$$=\mathbf{(3x+2)(x+2)}$$

**उदाहरण 7.** $xy-3x+2y-6$।

$$x(y-3)+2(y-3)=\mathbf{(x+2)(y-3)}$$

### Grouping में sign adjustment

कभी-कभी दूसरे group को $-1$ से multiply करके समान bracket बनाना पड़ता है।

**उदाहरण 8.** $ax-ay-bx+by$।

$$a(x-y)-b(x-y)=\mathbf{(a-b)(x-y)}$$

> :icon-warn: Grouping के बाद दोनों brackets exactly same होने चाहिए। $(x+y)$ और $(y+x)$ mathematically same हैं, लेकिन signs carefully check करें।

---

## 29.5 :icon-formula: Identities से factorisation

Chapter 28 की identities को reverse direction में लगाइए।

### Difference of squares

$$a^2-b^2=(a+b)(a-b)$$

```figure
type: identity-factor
a: 5
b: 2
caption: a²−b² को conjugate factors (a+b)(a−b) में बदलें
```

**उदाहरण 9.** $x^2-49$।

$$x^2-7^2=\mathbf{(x+7)(x-7)}$$

**उदाहरण 10.** $25a^2-16b^2$।

$$=(5a)^2-(4b)^2=\mathbf{(5a+4b)(5a-4b)}$$

### Perfect square trinomials

$$a^2+2ab+b^2=(a+b)^2$$

$$a^2-2ab+b^2=(a-b)^2$$

**उदाहरण 11.** $x^2+10x+25$।

Middle term $2\times x\times5=10x$ है:

$$=\mathbf{(x+5)^2}$$

**उदाहरण 12.** $4a^2-12ab+9b^2$।

$$=(2a)^2-2(2a)(3b)+(3b)^2=\mathbf{(2a-3b)^2}$$

### Sum और difference of cubes

$$a^3+b^3=(a+b)(a^2-ab+b^2)$$

$$a^3-b^3=(a-b)(a^2+ab+b^2)$$

**उदाहरण 13.** $x^3+8$।

$$=x^3+2^3=\mathbf{(x+2)(x^2-2x+4)}$$

**उदाहरण 14.** $27a^3-8b^3$।

$$=(3a)^3-(2b)^3=\mathbf{(3a-2b)(9a^2+6ab+4b^2)}$$

---

## 29.6 :icon-chart: Quadratic factorisation — middle term split

Standard quadratic:

$$ax^2+bx+c$$

यदि $a=1$ हो, तो ऐसे दो numbers $p,q$ खोजिए जिनका —

$$pq=c,\qquad p+q=b$$

फिर —

$$x^2+bx+c=(x+p)(x+q)$$

**उदाहरण 15.** $x^2+7x+12$।

Product $12$ और sum $7$ वाले numbers $3,4$ हैं:

$$\mathbf{x^2+7x+12=(x+3)(x+4)}$$

**उदाहरण 16.** $x^2-5x+6$।

Product $6$, sum $-5$: numbers $-2,-3$।

$$\mathbf{x^2-5x+6=(x-2)(x-3)}$$

### जब $a\ne1$: splitting the middle term

$ax^2+bx+c$ में पहले $ac$ निकालिए। ऐसे $p,q$ ढूँढिए:

$$pq=ac,\qquad p+q=b$$

फिर $bx$ को $px+qx$ में split करके grouping कीजिए।

```figure
type: quadratic-split
a: 2
b: 7
c: 3
p: 1
q: 6
caption: 2x²+7x+3 में ac=6 और middle coefficient 7 को 1+6 में split करें
```

**उदाहरण 17.** $2x^2+7x+3$।

- $ac=2\times3=6$
- Product $6$, sum $7$: $1,6$

$$2x^2+x+6x+3$$

$$=x(2x+1)+3(2x+1)=\mathbf{(2x+1)(x+3)}$$

**उदाहरण 18.** $6x^2-x-2$।

- $ac=6\times(-2)=-12$
- Product $-12$, sum $-1$: $3,-4$

$$6x^2+3x-4x-2$$

$$=3x(2x+1)-2(2x+1)=\mathbf{(3x-2)(2x+1)}$$

> :icon-key: Splitting में middle coefficient के sign को exactly match करना चाहिए। Product $ac$ और sum $b$ दोनों check करें।

---

## 29.7 :icon-brain: Substitution और polynomial factors

जब powers में gap हो, temporary variable रखकर factorisation आसान होती है।

```figure
type: substitution-factor
caption: x⁴−5x²+4 में y=x² रखकर पहले quadratic factor कीजिए
```

**उदाहरण 19.** $x^4-5x^2+4$।

मान लें $y=x^2$। तब —

$$y^2-5y+4=(y-1)(y-4)$$

अब वापस $y=x^2$ रखें:

$$=(x^2-1)(x^2-4)$$

Difference of squares से —

$$=\mathbf{(x-1)(x+1)(x-2)(x+2)}$$

**उदाहरण 20.** $a^4-16$।

$$a^4-4^2=(a^2-4)(a^2+4)$$

$$=\mathbf{(a-2)(a+2)(a^2+4)}$$

$a^2+4$ real/integer factors में आगे नहीं टूटता।

### Factor theorem की नींव

यदि polynomial $P(x)$ में $x=k$ रखने पर $P(k)=0$ आए, तो $(x-k)$ उसका factor होता है।

**उदाहरण 21.** $P(x)=x^2-5x+6$।

$$P(2)=4-10+6=0$$

इसलिए $(x-2)$ factor है। वास्तव में —

$$x^2-5x+6=(x-2)(x-3)$$

यह idea आगे polynomial equations और remainders में उपयोगी होगा।

---

## 29.8 :icon-divide: Algebraic fractions और zero product

### Algebraic fractions simplify करना

Numerator और denominator को पहले factorise कीजिए, फिर common factor cancel करें।

**उदाहरण 22.**

$$\frac{x^2-9}{x^2+5x+6}$$

ऊपर और नीचे factorise करें:

$$\frac{(x-3)(x+3)}{(x+2)(x+3)}=\mathbf{\frac{x-3}{x+2}}$$

लेकिन original denominator zero नहीं होना चाहिए, इसलिए $x\ne-3,-2$।

> :icon-warn: Common factor cancel करने के बाद original denominator की restrictions मत भूलिए।

### Zero product property

यदि दो factors का product zero है —

$$AB=0$$

तो $A=0$ या $B=0$।

```figure
type: zero-product
r1: 2
r2: 3
caption: (x−2)(x−3)=0 को दो simple equations में बाँटिए
```

**उदाहरण 23.** $x^2-5x+6=0$।

$$ (x-2)(x-3)=0$$

इसलिए —

$$x-2=0\quad\text{or}\quad x-3=0$$

अतः $x=\mathbf{2}$ या $x=\mathbf{3}$।

**उदाहरण 24.** $2x^2+7x+3=0$।

$$ (2x+1)(x+3)=0$$

अतः —

$$x=-\frac{1}{2}\quad\text{or}\quad x=-3$$

Quadratic equations का systematic treatment Chapter 31 में होगा।

---

## 29.9 :icon-bulb: शॉर्टकट व उनके प्रमाण

### :icon-timer: शॉर्टकट 1 — factorisation order

हर expression पर यह checklist चलाइए:

1. क्या सभी terms में common factor है?
2. क्या two terms difference of squares/cubes हैं?
3. क्या perfect square trinomial है?
4. क्या four terms grouping से टूटेंगे?
5. क्या quadratic में middle term split होगा?
6. क्या repeated powers के लिए substitution रख सकते हैं?

### :icon-timer: शॉर्टकट 2 — $x^2+bx+c$

ऐसे numbers खोजिए जिनका product $c$ और sum $b$ हो।

- $c>0$: दोनों signs same
- $c<0$: signs opposite
- $b>0$: positive number का absolute value बड़ा
- $b<0$: negative number का absolute value बड़ा

### :icon-timer: शॉर्टकट 3 — $ax^2+bx+c$

$ac$ product बनाइए; $b$ sum वाला pair खोजिए। फिर middle term split करें।

### :icon-timer: शॉर्टकट 4 — जल्दी जाँच

Factors multiply करके:

- first term का product $ax^2$ होना चाहिए,
- last term का product $c$ होना चाहिए,
- cross terms का sum $bx$ होना चाहिए।

### :icon-timer: शॉर्टकट 5 — factor theorem check

Candidate factor $(x-k)$ है तो केवल $P(k)$ निकालिए। यदि zero, factor सही; यदि non-zero, factor गलत।

### :icon-timer: शॉर्टकट 6 — algebraic fraction

Cancellation से पहले factorise, cancellation के बाद domain restriction लिखिए।

### :icon-timer: शॉर्टकट 7 — complete factorisation

Factor निकालने के बाद bracket को फिर देखिए। $x^2-9$ को केवल $(x^2-9)$ छोड़ना अधूरा है; इसे $(x-3)(x+3)$ तक तोड़िए।

---

## 29.10 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Common factor का पूरा HCF बाहर न निकालना।
> Numerical HCF और common variable powers दोनों check करें।

> :icon-cross: **जाल 2.** Difference of squares में plus लिखना।
> $a^2-b^2=(a+b)(a-b)$।

> :icon-cross: **जाल 3.** Perfect square में middle term का sign गलत करना।
> $a^2+2ab+b^2$ में plus, $a^2-2ab+b^2$ में minus।

> :icon-cross: **जाल 4.** Quadratic में केवल $b+c$ देखकर pair लेना।
> $x^2+bx+c$ में product $c$ और sum $b$ दोनों match होने चाहिए।

> :icon-cross: **जाल 5.** $ax^2+bx+c$ में $b$ को सीधे factor pair का product मानना।
> पहले $ac$ निकालिए, फिर middle split कीजिए।

> :icon-cross: **जाल 6.** Grouping के बाद common bracket अलग-अलग आना।
> Group signs adjust करके exactly same bracket बनाइए।

> :icon-cross: **जाल 7.** Substitution के बाद original variable में वापस न आना।
> $y=x^2$ रखा है तो final answer में $y$ नहीं छोड़ना।

> :icon-cross: **जाल 8.** Algebraic fraction में term cancel करना।
> केवल complete common factors cancel होते हैं; $x+3$ को $x$ से cancel नहीं कर सकते।

> :icon-cross: **जाल 9.** Zero product में केवल एक root लिखना।
> $(A)(B)=0$ में $A=0$ और $B=0$ दोनों cases लेने होते हैं।

---

## 29.11 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* $12a^2b-8ab^2$ factorise करें।

**हल:** $\mathbf{4ab(3a-2b)}$।

**PYQ 2.** *(SSC CHSL)* $x^2-49$।

**हल:** $\mathbf{(x-7)(x+7)}$।

**PYQ 3.** *(RRB NTPC)* $x^2+7x+12$।

**हल:** $\mathbf{(x+3)(x+4)}$।

**PYQ 4.** *(IBPS Clerk)* $2x^2+7x+3$।

**हल:** middle split $x+6x$ ⟹ $\mathbf{(2x+1)(x+3)}$।

**PYQ 5.** *(UP Police SI)* $x^4-5x^2+4$।

**हल:** $y=x^2$ ⟹ $\mathbf{(x-1)(x+1)(x-2)(x+2)}$।

**PYQ 6.** *(SSC MTS)* $x^2-5x+6=0$।

**हल:** $(x-2)(x-3)=0$ ⟹ $\mathbf{x=2,3}$।

---

## 29.12 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | $6x+9$ | $3(2x+3)$ | common factor |
| 2 | $12a^2b-8ab^2$ | $4ab(3a-2b)$ | HCF |
| 3 | $15x^3y^2+10x^2y^3$ | $5x^2y^2(3x+2y)$ | HCF |
| 4 | $ax+ay+bx+by$ | $(a+b)(x+y)$ | grouping |
| 5 | $3x^2+6x+2x+4$ | $(3x+2)(x+2)$ | grouping |
| 6 | $xy-3x+2y-6$ | $(x+2)(y-3)$ | grouping |
| 7 | $x^2-49$ | $(x-7)(x+7)$ | difference squares |
| 8 | $25a^2-16b^2$ | $(5a+4b)(5a-4b)$ | difference squares |
| 9 | $x^2+10x+25$ | $(x+5)^2$ | perfect square |
| 10 | $4a^2-12ab+9b^2$ | $(2a-3b)^2$ | perfect square |
| 11 | $x^3+8$ | $(x+2)(x^2-2x+4)$ | sum cubes |
| 12 | $27a^3-8b^3$ | $(3a-2b)(9a^2+6ab+4b^2)$ | difference cubes |
| 13 | $x^2+7x+12$ | $(x+3)(x+4)$ | product 12, sum 7 |
| 14 | $x^2-5x+6$ | $(x-2)(x-3)$ | product 6, sum -5 |
| 15 | $2x^2+7x+3$ | $(2x+1)(x+3)$ | split $x+6x$ |
| 16 | $6x^2-x-2$ | $(3x-2)(2x+1)$ | split $3x-4x$ |
| 17 | $x^4-5x^2+4$ | $(x-1)(x+1)(x-2)(x+2)$ | $y=x^2$ |
| 18 | $a^4-16$ | $(a-2)(a+2)(a^2+4)$ | two steps |
| 19 | $P(x)=x^2-5x+6$, check $x=2$ | factor $(x-2)$ | $P(2)=0$ |
| 20 | $(x^2-9)/(x^2+5x+6)$ | $(x-3)/(x+2)$ | factor/cancel |
| 21 | $(x-2)(x-3)=0$ | $x=2,3$ | zero product |
| 22 | $(2x+1)(x+3)=0$ | $x=-1/2,-3$ | zero product |
| 23 | $-x^2+5x-6$ | $-(x-2)(x-3)$ | negative factor |
| 24 | $x^2-16x+64$ | $(x-8)^2$ | perfect square |
| 25 | $x^2+2x-15$ | $(x+5)(x-3)$ | product -15, sum 2 |

---

## 29.13 :icon-trophy: अध्याय का सार

```
━━━ Factorisation order ━━━
1. common factor देखिए
2. identity pattern पहचानिए
3. grouping आजमाइए
4. quadratic में middle split कीजिए
5. repeated powers में substitution रखिए
6. final factors को multiply करके check कीजिए

━━━ Common factor ━━━
6x+9 = 3(2x+3)
12a²b−8ab² = 4ab(3a−2b)

━━━ Identities ━━━
a²−b² = (a+b)(a−b)
a²+2ab+b² = (a+b)²
a²−2ab+b² = (a−b)²
a³+b³ = (a+b)(a²−ab+b²)
a³−b³ = (a−b)(a²+ab+b²)

━━━ Grouping ━━━
ax+ay+bx+by
= a(x+y)+b(x+y)
= (a+b)(x+y)

━━━ Quadratic ━━━
x²+bx+c
product = c, sum = b

ax²+bx+c
product = ac, sum = b
middle term split → grouping

2x²+7x+3
= 2x²+x+6x+3
= (2x+1)(x+3)

━━━ Substitution ━━━
x⁴−5x²+4
let y=x²
= y²−5y+4
= (y−1)(y−4)
= (x−1)(x+1)(x−2)(x+2)

━━━ Zero product ━━━
AB=0 → A=0 or B=0

━━━ Algebraic fractions ━━━
पहले factorise
फिर complete factors cancel
original denominator restrictions लिखिए
```

> :icon-trophy: **Chapter 28 की identities अब factorisation में उल्टी दिशा में काम कर रही हैं।** Common factor, grouping, quadratic split और zero-product method की नींव तैयार है।
>
> **आगे:** Chapter 30 — **रैखिक समीकरण व आलेख (Linear Equations & Graphs)**। वहाँ algebraic equations को व्यवस्थित रूप से solve और graph किया जाएगा।
