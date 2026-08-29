# अध्याय 43 — त्रिकोणमितीय सर्वसमिकाएँ व पूरक कोण (Trigonometric Identities & Complementary Angles)

## 43.1 :icon-target: परिचय व वेटेज

Chapter 42 में हमने trigonometric ratios और standard values सीखे। अब ऐसे relations पढ़ेंगे जो हर valid angle के लिए सत्य होते हैं। इन्हें trigonometric identities कहते हैं।

> *"$sec^2\theta-\tan^2\theta$ को simplify कीजिए।"*

Pythagorean identity से सीधे answer $1$ आता है। Identity questions में सबसे महत्वपूर्ण skill है—expression को sin और cos में बदलकर common denominator बनाना।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | identity simplification |
| **SSC CGL Tier-2** | **2–4** | proof और transformations |
| SSC CHSL / MTS / GD | 1 | basic identities |
| **SSC CPO** | **2–3** | complementary/allied angles |
| **IBPS / SBI PO** | **2–4** | identity-based algebra |
| IBPS / SBI Clerk | 1–2 | exact value and simplification |
| **RRB NTPC / ALP** | **1–2** | standard identities |
| UP Police SI / Constable | 1–2 | complementary angles |
| UPSSSC PET | 1 | direct identity |
| Super TET / UPTET | 1–2 | concept and proof |

> :icon-key: **पूरे अध्याय का एक वाक्य:** Pythagorean identity चुनिए, fractions को sin/cos में बदलिए और एक side को step-by-step दूसरे side तक पहुँचाइए।

---

## 43.2 :icon-number: Basic identities का source

Right triangle में Pythagoras:

$$O^2+A^2=H^2$$

दोनों sides को $H^2$ से divide करें:

$$\frac{O^2}{H^2}+\frac{A^2}{H^2}=1$$

इसलिए —

$$\mathbf{\sin^2\theta+\cos^2\theta=1}$$

```figure
type: identity-triangle
caption: Pythagoras से sin² theta + cos² theta = 1 बनती है
```

### Three Pythagorean identities

$$\sin^2\theta+\cos^2\theta=1$$

Cos² से divide:

$$\mathbf{1+\tan^2\theta=sec^2\theta}$$

Sin² से divide:

$$\mathbf{1+cot^2\theta=cosec^2\theta}$$

### Reciprocal और quotient identities

$$cosec\theta=\frac{1}{\sin\theta},\qquad sec\theta=\frac{1}{\cos\theta},\qquad cot\theta=\frac{1}{\tan\theta}$$

$$\tan\theta=\frac{\sin\theta}{\cos\theta},\qquad cot\theta=\frac{\cos\theta}{\sin\theta}$$

```figure
type: reciprocal-web
caption: reciprocal और quotient identities को एक connected web की तरह याद रखें
```

> :icon-bulb: Identity proof में Hindi words को formula के अन्दर न भरें; symbolic relation को साफ़ रखें और हर transformation का कारण लिखें।

---

## 43.3 :icon-formula: Complementary angles

दो angles का sum $90°$ हो तो वे complementary हैं। Right triangle के दो acute angles complementary होते हैं।

$$\sin(90°-\theta)=\cos\theta$$

$$\cos(90°-\theta)=\sin\theta$$

$$\tan(90°-\theta)=cot\theta$$

$$cot(90°-\theta)=\tan\theta$$

$$sec(90°-\theta)=cosec\theta$$

$$cosec(90°-\theta)=sec\theta$$

```figure
type: complementary-angle
caption: complementary angles में opposite और adjacent sides exchange हो जाती हैं
```

**उदाहरण 1.** $\sin60°$ को complementary form में लिखिए।

$$\sin60°=\cos(90°-60°)=\mathbf{\cos30°}$$

**उदाहरण 2.** $\tan35°$ का complementary relation:

$$\tan35°=cot(90°-35°)=\mathbf{cot55°}$$

**उदाहरण 3.** Simplify:

$$\sin(90°-\theta)+\cos(90°-\theta)$$

$$=\mathbf{\cos\theta+\sin\theta}$$

### Proof by right triangle

एक acute angle $\theta$ के लिए opposite और adjacent sides दूसरे acute angle $(90°-\theta)$ के respect में exchange होती हैं। Hypotenuse same रहती है, इसलिए sin/cos interchange होते हैं।

---

## 43.4 :icon-calc: Identity proof की सही method

Identity prove करते समय:

1. LHS या RHS में से आसान side चुनिए।
2. Complex ratio को sin/cos में बदलें।
3. Common denominator बनाइए।
4. $\sin^2+\cos^2=1$ लगाइए।
5. बिना unnecessary expansion के target expression तक पहुँचिए।

### Proof 1

Prove:

$$sec^2\theta-\tan^2\theta=1$$

```figure
type: identity-proof
caption: LHS को sec/tan से sin/cos में बदलकर Pythagorean identity लगाइए
```

$$sec^2\theta-\tan^2\theta=\frac{1}{\cos^2\theta}-\frac{\sin^2\theta}{\cos^2\theta}$$

$$=\frac{1-\sin^2\theta}{\cos^2\theta}=\frac{\cos^2\theta}{\cos^2\theta}=\mathbf{1}$$

### Proof 2

Prove:

$$\frac{1-\cos^2\theta}{\sin\theta}=\sin\theta$$

$$\frac{1-\cos^2\theta}{\sin\theta}=\frac{\sin^2\theta}{\sin\theta}=\mathbf{\sin\theta}$$

### Proof 3

Prove:

$$\frac{1-\sin^2\theta}{\cos\theta}=\cos\theta$$

$$\frac{\cos^2\theta}{\cos\theta}=\mathbf{\cos\theta}$$

> :icon-key: Proof के दोनों sides को एक साथ manipulate करके equality “मान लेना” proof नहीं है। एक side को transform करके दूसरी side बनाइए।

---

## 43.5 :icon-chart: Sec–tan identity

Cos² से divide करने पर:

$$\frac{\sin^2\theta}{\cos^2\theta}+\frac{\cos^2\theta}{\cos^2\theta}=\frac{1}{\cos^2\theta}$$

$$\mathbf{\tan^2\theta+1=sec^2\theta}$$

```figure
type: sec-tan
caption: Pythagorean identity को cos² से divide करके sec²−tan² relation बनाइए
```

**उदाहरण 4.** यदि $\tan\theta=3/4$, तो $sec\theta$ (acute angle)?

$$sec^2\theta=1+\tan^2\theta=1+\frac{9}{16}=\frac{25}{16}$$

$$sec\theta=\mathbf{\frac{5}{4}}$$

**उदाहरण 5.** Simplify:

$$\frac{sec^2\theta-1}{\tan\theta}$$

$$=\frac{\tan^2\theta}{\tan\theta}=\mathbf{\tan\theta}$$

---

## 43.6 :icon-divide: Cosec–cot identity

Sin² से divide करने पर:

$$\frac{\sin^2\theta}{\sin^2\theta}+\frac{\cos^2\theta}{\sin^2\theta}=\frac{1}{\sin^2\theta}$$

$$\mathbf{1+cot^2\theta=cosec^2\theta}$$

```figure
type: cosec-cot
caption: sin² से divide करने पर cosec² theta = 1 + cot² theta मिलता है
```

**उदाहरण 6.** यदि $cot\theta=7/24$, तो $cosec\theta$?

$$cosec^2\theta=1+\frac{49}{576}=\frac{625}{576}$$

$$cosec\theta=\mathbf{\frac{25}{24}}$$

**उदाहरण 7.** Simplify:

$$cosec^2\theta-cot^2\theta=\mathbf{1}$$

---

## 43.7 :icon-chart: Unit-circle proof और allied angles

Unit circle में point $P=(\cos\theta,\sin\theta)$ होता है। Radius $1$ के कारण:

$$x^2+y^2=1$$

अतः:

$$\cos^2\theta+\sin^2\theta=1$$

```figure
type: unit-circle-identities
caption: unit-circle coordinates का square sum हमेशा 1 होता है
```

### Allied-angle patterns

Reference angle वही magnitude देता है; quadrant sign तय करता है।

```figure
type: allied-angles
caption: 180 plus/minus और 360 minus shifts में sign pattern देखिए
```

Useful relations:

$$\sin(180°-\theta)=\sin\theta$$

$$\cos(180°-\theta)=-\cos\theta$$

$$\tan(180°-\theta)=-\tan\theta$$

$$\sin(180°+\theta)=-\sin\theta$$

$$\cos(180°+\theta)=-\cos\theta$$

$$\tan(180°+\theta)=\tan\theta$$

$$\sin(360°-\theta)=-\sin\theta$$

$$\cos(360°-\theta)=\cos\theta$$

$$\tan(360°-\theta)=-\tan\theta$$

**उदाहरण 8.** $\cos150°$।

$$\cos(180°-30°)=-\cos30°=\mathbf{-\frac{\sqrt{3}}{2}}$$

**उदाहरण 9.** $\tan225°$।

$$\tan(180°+45°)=\tan45°=\mathbf{1}$$

---

## 43.8 :icon-steps: Simplification और exact values

### Simplification 1

$$\frac{1-\cos^2\theta}{\sin\theta}$$

```figure
type: trig-simplify
caption: 1−cos² को sin² में बदलकर common factor cancel करें
```

$$=\frac{\sin^2\theta}{\sin\theta}=\mathbf{\sin\theta}$$

### Simplification 2

$$\frac{sec^2\theta-1}{cosec^2\theta-1}$$

$$=\frac{\tan^2\theta}{cot^2\theta}=\frac{\tan^2\theta}{1/\tan^2\theta}=\mathbf{\tan^4\theta}$$

### Simplification 3

$$\frac{\sin\theta}{\cos\theta}+\frac{\cos\theta}{\sin\theta}$$

$$=\frac{\sin^2\theta+\cos^2\theta}{\sin\theta\cos\theta}=\mathbf{\frac{1}{\sin\theta\cos\theta}}$$

### Given ratio से all values

यदि $\tan\theta=3/4$ और $\theta$ acute:

- $O=3k,A=4k,H=5k$
- $\sin\theta=3/5$
- $\cos\theta=4/5$
- $sec\theta=5/4$
- $cosec\theta=5/3$
- $cot\theta=4/3$

```figure
type: value-from-ratio
caption: एक ratio से right triangle बनाकर सभी six ratios निकालिए
```

---

## 43.9 :icon-bulb: Proof shortcuts और method map

### :icon-timer: Identity selection

| Expression दिखे | Identity लगाएँ |
|---|---|
| $1-\sin^2\theta$ | $\cos^2\theta$ |
| $1-\cos^2\theta$ | $\sin^2\theta$ |
| $sec^2\theta-1$ | $\tan^2\theta$ |
| $cosec^2\theta-1$ | $cot^2\theta$ |
| $1+\tan^2\theta$ | $sec^2\theta$ |
| $1+cot^2\theta$ | $cosec^2\theta$ |

### :icon-timer: Shortcut 1 — convert to sin/cos

Complex expression में sec, cosec, cot को reciprocal रूप में बदलें:

$$sec\theta=\frac{1}{\cos\theta},\quad cosec\theta=\frac{1}{\sin\theta},\quad cot\theta=\frac{\cos\theta}{\sin\theta}$$

### :icon-timer: Shortcut 2 — denominator rationalize नहीं, identity चुनें

$1-\sin^2$ दिखे तो तुरंत $\cos^2$; unnecessary expansion न करें।

### :icon-timer: Shortcut 3 — complementary swap

$90°-\theta$ के साथ:

**Cofunction pairs:** sin ↔ cos, tan ↔ cot, sec ↔ cosec

### :icon-timer: Shortcut 4 — allied sign

ASTC से function का sign चुनें; reference angle से exact magnitude।

### :icon-timer: Shortcut 5 — proof direction

- LHS complicated हो तो LHS से शुरू करें।
- दोनों sides fractions हों तो एक common denominator बनाइए।
- Cross multiplication के बाद भी हर step reversible होना चाहिए।

### :icon-timer: Shortcut 6 — value from ratio

$\sin\theta=p/q$ हो तो right triangle और Pythagoras से बाकी sides निकालें; angle find करना जरूरी नहीं।

---

## 43.10 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** $1-\sin^2\theta$ को $\sin^2\theta$ लिखना।
> सही result $\cos^2\theta$ है।

> :icon-cross: **जाल 2.** $1+\tan^2\theta=cosec^2\theta$ लिखना।
> सही identity $sec^2\theta$ है।

> :icon-cross: **जाल 3.** Complementary angle में sign बदलना।
> $0°$–$90°$ acute complementary pairs में functions exchange होते हैं, sign नहीं।

> :icon-cross: **जाल 4.** Allied angle में quadrant sign भूलना।
> $\cos(180°-\theta)$ negative, लेकिन $\sin(180°-\theta)$ positive है।

> :icon-cross: **जाल 5.** Identity proof में दोनों sides को एक साथ बदलना।
> एक side transform करके दूसरी side तक पहुँचिए।

> :icon-cross: **जाल 6.** $\tan\theta$ को $\cos/\sin$ लिखना।
> सही $\tan=\sin/\cos$ और $cot=\cos/\sin$।

> :icon-cross: **जाल 7.** Reciprocal का numerator/denominator उलटना भूलना।
> $sec=1/\cos$, $cosec=1/\sin$।

> :icon-cross: **जाल 8.** Negative angle/root sign को बिना quadrant context के चुनना।
> Domain और given quadrant check करें।

> :icon-cross: **जाल 9.** $sec^2$ को $(sec)^2$ के बजाय $sec(2\theta)$ समझना।
> Power और double-angle अलग concepts हैं।

---

## 43.11 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* $sec^2\theta-\tan^2\theta$।

**हल:** $\mathbf{1}$।

**PYQ 2.** *(SSC CHSL)* $cosec^2\theta-cot^2\theta$।

**हल:** $\mathbf{1}$।

**PYQ 3.** *(RRB NTPC)* $\sin(90°-\theta)$।

**हल:** $\mathbf{\cos\theta}$।

**PYQ 4.** *(IBPS Clerk)* $\cos150°$।

**हल:** $\mathbf{-\sqrt{3}/2}$।

**PYQ 5.** *(UP Police SI)* $\tan225°$।

**हल:** $\mathbf{1}$।

**PYQ 6.** *(SSC MTS)* $\tan\theta=3/4$ acute; sec?

**हल:** $\mathbf{5/4}$।

---

## 43.12 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | $\sin^2\theta+\cos^2\theta$ | 1 | Pythagorean |
| 2 | $sec^2\theta-\tan^2\theta$ | 1 | identity |
| 3 | $cosec^2\theta-cot^2\theta$ | 1 | identity |
| 4 | $\sin(90°-\theta)$ | $\cos\theta$ | complementary |
| 5 | $\cos(90°-\theta)$ | $\sin\theta$ | complementary |
| 6 | $\tan(90°-\theta)$ | $cot\theta$ | complementary |
| 7 | $\tan\theta=3/4$, sec | $5/4$ | $1+tan²$ |
| 8 | $cot\theta=7/24$, cosec | $25/24$ | identity |
| 9 | $(1-\cos²\theta)/\sin\theta$ | $\sin\theta$ | substitute |
| 10 | $(1-\sin²\theta)/\cos\theta$ | $\cos\theta$ | substitute |
| 11 | $sec^2\theta-1$ | $\tan^2\theta$ | identity |
| 12 | $cosec^2\theta-1$ | $cot^2\theta$ | identity |
| 13 | $\sin^2\theta+\cos^2\theta$ proof | 1 | Pythagoras |
| 14 | $\sin60°$ complementary form | $\cos30°$ | cofunction |
| 15 | $\tan35°$ complementary form | $cot55°$ | cofunction |
| 16 | $\cos150°$ | $-\sqrt{3}/2$ | QII |
| 17 | $\sin210°$ | $-1/2$ | QIII |
| 18 | $\tan315°$ | $-1$ | QIV |
| 19 | $(\sin/\cos)+(\cos/\sin)$ | $1/(\sin\cos)$ | common denominator |
| 20 | $(sec²-1)/(cosec²-1)$ | $\tan^4$ | convert |
| 21 | $\tan\theta=3/4$, sin | $3/5$ | triangle |
| 22 | same, cot | $4/3$ | reciprocal |
| 23 | same, cosec | $5/3$ | reciprocal |
| 24 | $\sin(180°-\theta)$ | $\sin\theta$ | allied angle |
| 25 | $\cos(180°-\theta)$ | $-\cos\theta$ | allied angle |

---

## 43.13 :icon-trophy: अध्याय का सार

```
━━━ Pythagorean identities ━━━
sin²θ + cos²θ = 1
1 + tan²θ = sec²θ
1 + cot²θ = cosec²θ

━━━ Reciprocal ━━━
cosecθ = 1/sinθ
secθ = 1/cosθ
cotθ = 1/tanθ

━━━ Quotient ━━━
tanθ = sinθ/cosθ
cotθ = cosθ/sinθ

━━━ Complementary ━━━
sin(90−θ)=cosθ
cos(90−θ)=sinθ
tan(90−θ)=cotθ
sec(90−θ)=cosecθ

━━━ Allied angles ━━━
sin(180−θ)=sinθ
cos(180−θ)=−cosθ
tan(180−θ)=−tanθ
sin(180+θ)=−sinθ
cos(360−θ)=cosθ

━━━ Proof method ━━━
LHS से शुरू करें
sec/cosec/cot को sin/cos में बदलें
common denominator
Pythagorean identity
RHS तक पहुँचें

━━━ Traps ━━━
1−sin²=cos²
1−cos²=sin²
quadrant sign check
```

> :icon-trophy: **Trigonometric identities और complementary/allied angles complete।** अब identity proof, exact-value simplification और quadrant sign questions को एक systematic method से हल किया जा सकता है।
>
> **आगे:** Chapter 44 — **ऊँचाई व दूरी (Heights & Distances)**।
