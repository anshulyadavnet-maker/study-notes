# अध्याय 35 — सर्वांगसमता व समरूपता (Congruence & Similarity of Triangles)

## 35.1 :icon-target: परिचय व वेटेज

Chapter 34 में हमने triangles की properties और centres पढ़े। अब दो triangles के बीच exact equality और same shape का सम्बन्ध स्थापित करेंगे। Geometry में diagram देखकर “दोनों समान लग रहे हैं” पर्याप्त नहीं; सही criterion से proof करना होता है।

> *"दो triangles में तीन corresponding sides बराबर हैं। क्या वे congruent होंगे?"*

हाँ—SSS criterion से। लेकिन केवल तीन angles बराबर हों तो triangles similar होंगे, congruent जरूरी नहीं।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | congruence rules |
| **SSC CGL Tier-2** | **2–3** | similarity और proportional sides |
| SSC CHSL / MTS / GD | 1 | basic criteria |
| **SSC CPO** | **2** | theorem-based geometry |
| **IBPS / SBI PO** | 1–2 | similar triangles, ratios |
| IBPS / SBI Clerk | 1 | direct application |
| **RRB NTPC / ALP** | **2–3** | congruence and BPT |
| UP Police SI / Constable | 1–2 | height, shadow, similarity |
| UPSSSC PET | 1 | triangle matching |
| Super TET / UPTET | 2–3 | proof and visual reasoning |

> :icon-key: **पूरे अध्याय का एक वाक्य:** Congruent triangles में shape और size दोनों समान; similar triangles में shape समान और corresponding sides proportional।

---

## 35.2 :icon-number: Congruence की मूल अवधारणा

दो figures congruent हैं यदि एक को बिना आकार बदले दूसरे पर exactly superimpose किया जा सके। Triangles के लिए:

- corresponding sides equal
- corresponding angles equal
- same shape और same size

Notation:

$$\triangle ABC\cong\triangle PQR$$

इसका क्रम correspondence बताता है:

$$A\leftrightarrow P,\qquad B\leftrightarrow Q,\qquad C\leftrightarrow R$$

इसलिए:

$$AB=PQ,\quad BC=QR,\quad CA=RP$$

और:

$$\angle A=\angle P,\quad\angle B=\angle Q,\quad\angle C=\angle R$$

### Correspondence का महत्व

यदि सही statement $\triangle ABC\cong\triangle PQR$ है, तो $AB$ का corresponding side $PQ$ है। $AB$ को $QR$ से compare करना गलत correspondence होगा।

---

## 35.3 :icon-calc: Congruence criteria

### SSS — Side Side Side

तीनों corresponding sides equal हों तो triangles congruent।

```figure
type: congruence-rule
rule: SSS
caption: SSS में तीन corresponding sides के matching marks हैं
```

$$AB=PQ,\quad BC=QR,\quad CA=RP$$

अतः $\triangle ABC\cong\triangle PQR$ by SSS।

### SAS — Side Angle Side

दो corresponding sides और उनके बीच का included angle equal हो।

```figure
type: congruence-rule
rule: SAS
caption: SAS में equal sides के बीच का included angle महत्वपूर्ण है
```

> :icon-warn: SAS में angle उन दोनों दिए हुए sides के **बीच** का होना चाहिए। Non-included angle से SAS नहीं बनेगा।

### ASA — Angle Side Angle

दो corresponding angles और उनके बीच की side equal हो।

```figure
type: congruence-rule
rule: ASA
caption: ASA में दो angles और included side match करते हैं
```

### AAS — Angle Angle Side

दो angles और एक corresponding non-included side भी congruence के लिए पर्याप्त है, क्योंकि तीसरा angle triangle sum से निर्धारित हो जाता है।

### RHS — Right angle Hypotenuse Side

दो right triangles में:

1. एक angle $90°$,
2. hypotenuse equal,
3. एक corresponding side equal

हो तो triangles congruent।

```figure
type: congruence-rule
rule: RHS
caption: RHS में right angle, hypotenuse और एक side बराबर हैं
```

### कौन-से data पर्याप्त नहीं?

#### AAA

तीन angles equal होने से shape same और size बदल सकता है। इसलिए AAA similarity देता है, congruence नहीं।

```figure
type: not-congruent
caption: AAA same angles देता है, लेकिन छोटे और बड़े triangles का size अलग हो सकता है
```

#### SSA

दो sides और एक non-included angle सामान्यतः congruence guarantee नहीं करते। यह ambiguous case हो सकता है।

> :icon-key: SSS, SAS, ASA, AAS और RHS valid criteria हैं। AAA similarity criterion है; SSA general congruence criterion नहीं।

---

## 35.4 :icon-steps: CPCTC — corresponding parts

CPCTC का अर्थ है:

**Corresponding Parts of Congruent Triangles are Congruent**

पहले triangles को congruent prove करें; उसके बाद corresponding sides और angles equal लिख सकते हैं।

```figure
type: cpctc
caption: congruence prove होने के बाद corresponding sides और angles बराबर होते हैं
```

**उदाहरण 1.** यदि $\triangle ABC\cong\triangle PQR$, तो:

- $AB=PQ$
- $BC=QR$
- $CA=RP$
- $\angle A=\angle P$
- $\angle B=\angle Q$
- $\angle C=\angle R$

**उदाहरण 2.** यदि two triangles SSS से congruent हैं और $AB=8$ cm, तो corresponding $PQ=\mathbf{8}$ cm।

**उदाहरण 3.** यदि congruent triangles में $\angle B=55°$, तो corresponding $\angle Q=\mathbf{55°}$।

> :icon-bulb: CPCTC को proof की शुरुआत में नहीं लिखना चाहिए। पहले congruence criterion, फिर CPCTC conclusion।

---

## 35.5 :icon-chart: Similarity की मूल अवधारणा

दो triangles similar हैं यदि उनका shape same हो, corresponding angles equal हों और corresponding sides एक ही ratio में हों। Size अलग हो सकता है।

Notation:

$$\triangle ABC\sim\triangle PQR$$

यदि scale factor $k$ है:

$$\frac{PQ}{AB}=\frac{QR}{BC}=\frac{RP}{CA}=k$$

और angles:

$$\angle A=\angle P,\quad\angle B=\angle Q,\quad\angle C=\angle R$$

### Similarity criteria

#### AA — Angle Angle

दो corresponding angles equal हों, तो तीसरा angle भी triangle sum से equal होगा और triangles similar होंगे।

```figure
type: similar-aa
caption: AA में दो equal angles से triangles का shape same सिद्ध होता है
```

#### SSS similarity

तीनों corresponding sides proportional हों:

$$\frac{AB}{PQ}=\frac{BC}{QR}=\frac{CA}{RP}$$

#### SAS similarity

दो corresponding sides proportional और included angle equal हो।

### Congruence और similarity का comparison

| Property | Congruent | Similar |
|---|---|---|
| Shape | same | same |
| Size | same | अलग हो सकता है |
| Corresponding sides | equal | proportional |
| Corresponding angles | equal | equal |
| Scale factor | $1$ | कोई भी positive ratio |

---

## 35.6 :icon-ruler: Scale factor, perimeter और area

यदि similar triangles का side scale factor $k$ है, तो:

$$\frac{\text{corresponding side}_2}{\text{corresponding side}_1}=k$$

Perimeter भी $k$ times होता है:

$$\frac{P_2}{P_1}=k$$

Area square ratio में बदलता है:

$$\frac{A_2}{A_1}=k^2$$

```figure
type: scale-factor
k: 2
small: 3
caption: side और perimeter k times, area k² times बदलता है
```

**उदाहरण 4.** Similar triangles का side ratio $2:3$ है। Perimeter ratio और area ratio?

- perimeter ratio $=\mathbf{2:3}$
- area ratio $=2^2:3^2=\mathbf{4:9}$

**उदाहरण 5.** छोटे triangle की side $5$ cm और corresponding बड़े triangle की side $15$ cm है। Scale factor?

$$k=15/5=\mathbf{3}$$

यदि छोटे triangle का area $20$ cm² है, तो बड़े का area:

$$A_2=20\times3^2=\mathbf{180\text{ cm}^2}$$

### Similar triangles में missing side

**उदाहरण 6.** $\triangle ABC\sim\triangle PQR$, $AB=6$, $PQ=9$, $BC=8$। $QR$?

Scale factor $=9/6=3/2$।

$$QR=8\times\frac{3}{2}=\mathbf{12}$$

---

## 35.7 :icon-divide: Basic Proportionality Theorem (BPT)

यदि triangle की एक side के parallel line बाकी दो sides को काटती है, तो वह sides को proportional segments में divide करती है।

Triangle $ABC$ में $D$ on $AB$, $E$ on $AC$ और $DE\parallel BC$ हो, तो:

$$\frac{AD}{DB}=\frac{AE}{EC}$$

```figure
type: bpt-parallel
caption: DE parallel BC होने पर AD/DB = AE/EC
```

### Converse of BPT

यदि:

$$\frac{AD}{DB}=\frac{AE}{EC}$$

तो $DE\parallel BC$ सिद्ध किया जा सकता है।

**उदाहरण 7.** $AD=4$, $DB=6$, $AE=6$, $EC=9$। क्या $DE\parallel BC$?

$$\frac{AD}{DB}=\frac{4}{6}=\frac{2}{3}$$

$$\frac{AE}{EC}=\frac{6}{9}=\frac{2}{3}$$

Ratios equal हैं, इसलिए converse BPT से $\mathbf{DE\parallel BC}$।

**उदाहरण 8.** $AD=3$, $DB=5$, $AE=6$, $EC=x$ और $DE\parallel BC$। $x$?

$$\frac{3}{5}=\frac{6}{x}\quad\Rightarrow\quad3x=30\quad\Rightarrow\quad x=\mathbf{10}$$

### BPT का similarity connection

$DE\parallel BC$ होने पर:

$$\triangle ADE\sim\triangle ABC$$

इसलिए corresponding sides proportional होती हैं।

---

## 35.8 :icon-chart: Height, shadow और practical similarity

एक vertical object और उसकी shadow, तथा एक known object और उसकी shadow, समान sun angle के कारण similar right triangles बनाते हैं।

```figure
type: shadow-similarity
height: 6
shadow: 4
known_height: 1.5
known_shadow: 1
caption: height/shadow ratio समान रखकर अनजान height या shadow निकालिए
```

**उदाहरण 9.** $1.5$ m stick की shadow $1$ m है। एक tower की shadow $20$ m है। tower की height?

$$\frac{\text{height}}{\text{shadow}}=\frac{1.5}{1}$$

$$\text{tower height}=20\times1.5=\mathbf{30\text{ m}}$$

**उदाहरण 10.** एक pole की height $6$ m और shadow $4$ m है। उसी समय $1.5$ m stick की shadow?

$$\frac{6}{4}=\frac{1.5}{x}\quad\Rightarrow\quad6x=6\quad\Rightarrow\quad x=\mathbf{1\text{ m}}$$

### Distance from inaccessible object

Similarity का प्रयोग river width, tower height, pole distance और map scale में होता है। Diagram में parallel ground और equal angle identify कीजिए।

---

## 35.9 :icon-brain: Proof strategy और shortcuts

### :icon-timer: Congruence proof order

1. Corresponding vertices की order लिखें।
2. Given equal sides/angles list करें।
3. Included angle है या नहीं जाँचें।
4. SSS, SAS, ASA, AAS या RHS लिखें।
5. केवल उसके बाद CPCTC से required part निकालें।

### :icon-timer: Similarity proof order

1. दो equal angles खोजें ⟹ AA।
2. या तीन side ratios compare करें ⟹ SSS similarity।
3. Included angle equal और two ratios equal हों ⟹ SAS similarity।
4. Correspondence order सही रखें।

### :icon-timer: Shortcut 1 — AAA और AA

Triangles में दो angles equal होने पर तीसरा angle स्वतः equal होता है:

$$C=180-A-B$$

इसलिए AA पर्याप्त है।

### :icon-timer: Shortcut 2 — scale factor

यदि one side pair से $k$ मिल जाए:

- side: $k$
- perimeter: $k$
- area: $k^2$

### :icon-timer: Shortcut 3 — CPCTC

Congruent triangles के matching parts के लिए अलग calculation की जरूरत नहीं; correspondence से answer copy करें।

### :icon-timer: Shortcut 4 — BPT ratio

Parallel segment दिखते ही:

$$\frac{\text{upper segment}}{\text{lower segment}}=\frac{\text{other upper}}{\text{other lower}}$$

### :icon-timer: Shortcut 5 — shadow

$$\frac{H_1}{S_1}=\frac{H_2}{S_2}$$

एक ही समय की shadows में sun angle same होता है।

### :icon-timer: Shortcut 6 — invalid data पहचानिए

- SSS valid
- SAS valid only included angle
- ASA/AAS valid
- RHS valid
- AAA gives similarity
- SSA generally insufficient

---

## 35.10 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Congruent और similar को same मानना।
> Congruent में size equal; similar में size अलग हो सकता है।

> :icon-cross: **जाल 2.** Congruence criteria का order गलत लिखना।
> $\triangle ABC\cong\triangle PQR$ में A↔P, B↔Q, C↔R।

> :icon-cross: **जाल 3.** SAS में non-included angle लगाना।
> Angle दो given sides के बीच का होना चाहिए।

> :icon-cross: **जाल 4.** AAA को congruence criterion मानना।
> AAA केवल similarity देता है।

> :icon-cross: **जाल 5.** Similar triangles में area ratio को side ratio मानना।
> Area ratio $k^2$ होता है।

> :icon-cross: **जाल 6.** CPCTC पहले लिख देना।
> पहले congruence prove करें, फिर corresponding part निकालें।

> :icon-cross: **जाल 7.** BPT में segments का order उलटना।
> $AD/DB$ के सामने $AE/EC$ ही रखें।

> :icon-cross: **जाल 8.** Shadow problem में height ratio को shadow ratio का inverse कर देना।
> Corresponding height/shadow ratios समान होते हैं।

> :icon-cross: **जाल 9.** Similarity में corresponding vertices की order बदलना।
> Side ratio बनाने से पहले matching angles/vertices mark करें।

---

## 35.11 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* तीन corresponding sides equal हों तो criterion?

**हल:** **SSS congruence**।

**PYQ 2.** *(SSC CHSL)* दो angles equal हों तो triangles?

**हल:** **AA similarity**।

**PYQ 3.** *(RRB NTPC)* Similar triangles का side ratio $2:3$। Area ratio?

**हल:** $\mathbf{4:9}$।

**PYQ 4.** *(IBPS Clerk)* $AD=4,DB=6,AE=6,EC=9$। क्या $DE\parallel BC$?

**हल:** $4/6=6/9=2/3$ ⟹ **हाँ, converse BPT**।

**PYQ 5.** *(UP Police SI)* $1.5$ m stick shadow $1$ m, tower shadow $20$ m। height?

**हल:** $\mathbf{30}$ m।

**PYQ 6.** *(SSC MTS)* Congruent triangles में one corresponding side $8$ cm है। दूसरी?

**हल:** CPCTC से $\mathbf{8}$ cm।

---

## 35.12 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | 3 corresponding sides equal | SSS | congruence |
| 2 | 2 sides + included angle | SAS | congruence |
| 3 | 2 angles + included side | ASA | congruence |
| 4 | right angle + hypotenuse + side | RHS | congruence |
| 5 | AAA gives | similarity, not congruence | size may differ |
| 6 | $\triangle ABC\cong\triangle PQR$, AB=8 | PQ=8 | CPCTC |
| 7 | same congruence, angle B=55° | angle Q=55° | CPCTC |
| 8 | side ratio similar triangles $2:3$ | perimeter $2:3$ | scale $k$ |
| 9 | side ratio $2:3$ | area $4:9$ | square ratio |
| 10 | side 5 to corresponding 15 | scale factor 3 | ratio |
| 11 | small area 20, scale 3 | large area 180 | $20×9$ |
| 12 | AB=6,PQ=9, BC=8 similar | QR=12 | scale $3/2$ |
| 13 | $AD=4,DB=6,AE=6,EC=9$ | parallel | converse BPT |
| 14 | $AD=3,DB=5,AE=6,DE||BC$ | EC=10 | proportion |
| 15 | stick 1.5m/shadow1m, tower shadow20m | tower 30m | similar shadows |
| 16 | pole6m/shadow4m, stick1.5m | shadow1m | ratio |
| 17 | same shape, sides 4 and10 | scale $5/2$ | similarity |
| 18 | scale factor 4 | area factor 16 | $k^2$ |
| 19 | two right triangles hypotenuse equal + side equal | RHS | congruence |
| 20 | $DE||BC$ in triangle | $AD/DB=AE/EC$ | BPT |
| 21 | $2$ equal angles in triangles | AA similarity | angle sum |
| 22 | SSA data | not generally sufficient | ambiguous |
| 23 | $AB/ PQ=3/5$, BC=12 | QR=20 | proportional sides |
| 24 | congruent triangles side ratio | $1:1$ | equal size |
| 25 | side ratio $3:4$, small perimeter 27 | large perimeter 36 | scale $4/3$ |

---

## 35.13 :icon-trophy: अध्याय का सार

```
━━━ Congruence ━━━
same shape + same size
corresponding sides equal
corresponding angles equal

Criteria:
SSS, SAS, ASA, AAS, RHS
AAA → similarity only
SSA → generally insufficient

━━━ CPCTC ━━━
congruence prove होने के बाद
corresponding parts equal

━━━ Similarity ━━━
same shape, sides proportional
angles equal
criteria: AA, SSS proportional, SAS proportional

side ratio = k
perimeter ratio = k
area ratio = k²

━━━ BPT ━━━
DE || BC
AD/DB = AE/EC
converse भी true

━━━ Shadow ━━━
height/shadow ratios equal

━━━ Proof order ━━━
correspondence
matching data
criterion
CPCTC or proportional conclusion

━━━ Traps ━━━
AAA congruence नहीं
SAS included angle
area ratio k²
BPT segment order
```

> :icon-trophy: **Chapter 34 के triangle properties अब congruence, similarity और proportionality में बदल गए।** यही tools height, shadow, inaccessible distance और mensuration applications में काम आएँगे।
>
> **आगे:** Chapter 36 — **चतुर्भुज व बहुभुज (Quadrilaterals & Polygons)**।
