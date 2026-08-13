# अध्याय 40 — प्रिज़्म, पिरामिड व फ्रस्टम (Prism, Pyramid & Frustum)

## 40.1 :icon-target: परिचय व वेटेज

Chapter 39 में cube, cuboid, cylinder, cone, sphere और hemisphere पढ़े। अब syllabus में दिए गए अधिक advanced solids—right prism, regular right pyramid और frustum—को व्यवस्थित करेंगे।

> *"एक ही base और height वाले prism और pyramid में किसका volume अधिक होगा?"*

Same base area $B$ और height $h$ पर prism का volume $Bh$ और pyramid का $Bh/3$ होता है। इसलिए pyramid, matching prism का one-third है।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | prism/pyramid basics |
| **SSC CGL Tier-2** | **2–4** | advanced surface and frustum |
| SSC CHSL / MTS / GD | 1 | volume comparison |
| **SSC CPO** | **2** | pyramid and frustum |
| **IBPS / SBI PO** | 1–2 | 3-D arithmetic |
| IBPS / SBI Clerk | 1 | direct volume |
| **RRB NTPC / ALP** | **2–3** | prism and pyramid |
| UP Police SI / Constable | 1 | solid volume |
| UPSSSC PET | 1 | basic prism |
| Super TET / UPTET | 1 | visual solids |

> :icon-key: **पूरे अध्याय का एक वाक्य:** Prism में $B\times h$, pyramid में $\frac{1}{3}B\times h$, और frustum में बड़े और छोटे parallel bases दोनों को formula में शामिल करें।

---

## 40.2 :icon-number: Prism की मूल अवधारणा

Prism में एक ही आकार और area के दो parallel bases होते हैं, जिन्हें rectangular/parallelogram faces जोड़ते हैं।

यदि base area $B$, base perimeter $P$ और prism height $h$ हो:

$$V=B h$$

$$LSA=P h$$

$$TSA=Ph+2B$$

```figure
type: prism-general
base_area: 24
base_perimeter: 20
height: 10
caption: prism का वही base ऊपर तक repeat होता है
```

**उदाहरण 1.** Prism का base area $24$ cm², base perimeter $20$ cm और height $10$ cm।

- Volume $=24\times10=\mathbf{240\text{ cm}^3}$
- LSA $=20\times10=\mathbf{200\text{ cm}^2}$
- TSA $=200+2(24)=\mathbf{248\text{ cm}^2}$

### Right prism

Right prism में lateral edges bases के perpendicular होती हैं। Triangular prism, rectangular prism और square prism इसके examples हैं।

---

## 40.3 :icon-chart: Triangular prism

Triangular prism में triangular base दो बार और तीन rectangular lateral faces होते हैं।

यदि triangle base $b$, triangle height $t$ और prism length $L$:

$$B=\frac{1}{2}bt$$

$$V=\frac{1}{2}btL$$

```figure
type: triangular-prism
base: 6
base_height: 4
length: 10
caption: triangular base को length के along extrude करने पर triangular prism बनता है
```

**उदाहरण 2.** Triangular prism में triangle base $6$ cm, triangle height $4$ cm और length $10$ cm।

Base area:

$$B=\frac{1}{2}\times6\times4=12\text{ cm}^2$$

Volume:

$$V=12\times10=\mathbf{120\text{ cm}^3}$$

यदि triangular base की तीन sides $6,5,5$ cm हों, base perimeter $16$ cm:

$$LSA=16\times10=\mathbf{160\text{ cm}^2}$$

और TSA $=160+2(12)=\mathbf{184\text{ cm}^2}$।

---

## 40.4 :icon-chart: Pyramid की मूल अवधारणा

Pyramid में एक base और एक apex होता है। Apex को base के सभी vertices से join किया जाता है।

यदि base area $B$ और perpendicular height $h$:

$$V=\frac{1}{3}Bh$$

```figure
type: square-pyramid
side: 8
height: 12
caption: square pyramid में apex base के centre के ऊपर होता है
```

### Square pyramid

Square base side $a$:

$$B=a^2$$

$$V=\frac{1}{3}a^2h$$

Square right pyramid में face slant height $l$:

$$l^2=h^2+\left(\frac{a}{2}\right)^2$$

$$LSA=2al$$

$$TSA=a^2+2al$$

**उदाहरण 3.** Square pyramid side $8$ cm और height $12$ cm।

$$l=\sqrt{12^2+4^2}=\sqrt{160}=\mathbf{4\sqrt{10}\text{ cm}}$$

$$V=\frac{1}{3}(8^2)(12)=\mathbf{256\text{ cm}^3}$$

### Triangular pyramid

यदि triangular base area $B$ और height $h$:

$$V=\frac{1}{3}Bh$$

```figure
type: triangular-pyramid
base: 6
base_height: 4
height: 9
caption: triangular pyramid का volume one-third base area times height है
```

**उदाहरण 4.** Triangular base area $12$ cm² और pyramid height $9$ cm।

$$V=\frac{1}{3}\times12\times9=\mathbf{36\text{ cm}^3}$$

> :icon-warn: Pyramid की slant height volume formula में नहीं, surface-area formula में आती है। Volume में perpendicular vertical height $h$ लगेगी।

---

## 40.5 :icon-chart: Prism और pyramid comparison

Same base area $B$ और same height $h$ के लिए:

$$V_{prism}=Bh$$

$$V_{pyramid}=\frac{1}{3}Bh$$

```figure
type: solid-comparison40
caption: same base और height पर pyramid volume prism का one-third है
```

**उदाहरण 5.** Same base और height वाले prism का volume $600$ cm³ है। Matching pyramid का volume?

$$V_{pyramid}=600/3=\mathbf{200\text{ cm}^3}$$

**उदाहरण 6.** Pyramid volume $160$ cm³ और same base/height वाला prism?

$$V_{prism}=3\times160=\mathbf{480\text{ cm}^3}$$

यह relation किसी भी polygonal base पर लागू होता है।

---

## 40.6 :icon-ruler: Frustum की अवधारणा

किसी cone या pyramid को base के parallel plane से काटकर ऊपर का छोटा भाग हटाएँ, तो बचा हुआ solid frustum है। इसमें दो parallel bases होते हैं—एक बड़ा और एक छोटा।

### Conical frustum

- बड़ा radius $R$
- छोटा radius $r$
- perpendicular height $h$
- slant height $l$

$$l^2=h^2+(R-r)^2$$

$$V=\frac{1}{3}\pi h(R^2+r^2+Rr)$$

$$CSA=\pi(R+r)l$$

$$TSA=\pi(R+r)l+\pi R^2+\pi r^2$$

```figure
type: cone-frustum
R: 7
r: 3
height: 8
caption: conical frustum में दो radii, height और slant height होती हैं
```

**उदाहरण 7.** Conical frustum में $R=7$, $r=3$, $h=8$ cm।

$$l=\sqrt{8^2+(7-3)^2}=\sqrt{80}=\mathbf{4\sqrt{5}\text{ cm}}$$

Volume:

$$V=\frac{1}{3}\pi(8)(49+9+21)=\mathbf{\frac{632\pi}{3}\text{ cm}^3}$$

CSA:

$$CSA=\pi(7+3)(4\sqrt{5})=\mathbf{40\pi\sqrt{5}\text{ cm}^2}$$

```figure
type: frustum-slant
R: 7
r: 3
height: 8
caption: slant height के लिए radius difference और perpendicular height का right triangle बनता है
```

> :icon-key: Frustum में volume के अंदर $R^2+r^2+Rr$ आता है—सिर्फ $R^2-r^2$ नहीं।

---

## 40.7 :icon-chart: Square pyramid frustum

Square frustum में बड़े square base side $a$, छोटे square base side $b$ और height $h$ हों।

Base areas:

$$B_1=a^2,\qquad B_2=b^2$$

General frustum volume:

$$V=\frac{h}{3}\left(B_1+B_2+\sqrt{B_1B_2}\right)$$

Square bases के लिए:

$$V=\frac{h}{3}(a^2+b^2+ab)$$

```figure
type: square-frustum
bottom: 10
top: 4
height: 6
caption: square frustum में बड़े और छोटे square bases parallel होते हैं
```

### Lateral surface area

यदि square frustum की slant height $l$:

$$LSA=2(a+b)l$$

$$TSA=2(a+b)l+a^2+b^2$$

**उदाहरण 8.** Square frustum में $a=10$, $b=4$, $h=6$ और slant height $l=\sqrt{45}$ cm। Volume?

$$V=\frac{6}{3}(100+16+40)=\mathbf{312\text{ cm}^3}$$

---

## 40.8 :icon-steps: Nets और surface area

Solid का net उसे flat faces में खोलकर दिखाता है। Net से faces की संख्या और surface area समझना आसान होता है।

```figure
type: pyramid-net
caption: square pyramid net में one square base और four triangular faces होते हैं
```

### Prism net

Triangular prism net:

- 2 congruent triangles
- 3 rectangles

Square prism/cuboid net में 6 rectangular/square faces होते हैं।

### Pyramid net

Square pyramid net:

- 1 square base
- 4 congruent triangles

**उदाहरण 9.** Square pyramid base side $8$ cm और face slant height $5$ cm। TSA?

$$TSA=8^2+2(8)(5)=64+80=\mathbf{144\text{ cm}^2}$$

### Open solids

- Open prism: missing base का area subtract करें
- Open pyramid: missing base/face के अनुसार subtract करें
- Frustum container: inside volume capacity; outside TSA नहीं

---

## 40.9 :icon-ruler: Mixed volume और composite solids

**उदाहरण 10.** A solid में cuboid और उसके ऊपर triangular prism जुड़ा है।

```figure
type: prism-area
base_area: 24
height: 10
caption: prism volume को base area और prism height से निकालिए
```

यदि components overlap नहीं करते:

$$V_{total}=V_{cuboid}+V_{triangular\ prism}$$

यदि बीच में hollow part हो:

$$V_{remaining}=V_{outer}-V_{hollow}$$

**उदाहरण 11.** A prism का base area $24$ cm² और length $10$ cm है। Volume?

$$V=24\times10=\mathbf{240\text{ cm}^3}$$

### Capacity

**उदाहरण 12.** A prism-shaped container का base area $250$ cm² और height $40$ cm है। Capacity litres?

$$V=250\times40=10000\text{ cm}^3$$

$$\text{capacity}=\mathbf{10\text{ litres}}$$

---

## 40.10 :icon-bulb: Formula map और shortcuts

### :icon-timer: Prism

$$V=Bh,\quad LSA=Ph,\quad TSA=Ph+2B$$

### :icon-timer: Pyramid

$$V=\frac{1}{3}Bh$$

Regular right pyramid:

$$LSA=\frac{1}{2}Pl$$

$$TSA=\frac{1}{2}Pl+B$$

### :icon-timer: Conical frustum

$$l=\sqrt{h^2+(R-r)^2}$$

$$V=\frac{1}{3}\pi h(R^2+r^2+Rr)$$

$$CSA=\pi(R+r)l$$

### :icon-timer: Square frustum

$$V=\frac{h}{3}(a^2+b^2+ab)$$

$$LSA=2(a+b)l$$

### :icon-timer: Shortcut 1 — prism/pyramid

Same base and height:

$$V_{pyramid}:V_{prism}=1:3$$

### :icon-timer: Shortcut 2 — frustum as difference

Conical frustum को बड़े cone से छोटे similar cone subtract करके भी समझ सकते हैं।

### :icon-timer: Shortcut 3 — surface selection

- Prism side paint: $Ph$
- Pyramid side sheet: $Pl/2$
- Cone side sheet: $\pi rl$
- Frustum side sheet: $\pi(R+r)l$

### :icon-timer: Shortcut 4 — capacity

$$1\text{ litre}=1000\text{ cm}^3$$

### :icon-timer: Shortcut 5 — net

Net में exposed faces जोड़ें; hidden joining faces को surface area में शामिल न करें।

---

## 40.11 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Prism और pyramid volume में same formula लगाना।
> Prism $Bh$, pyramid $Bh/3$।

> :icon-cross: **जाल 2.** Pyramid volume में slant height लेना।
> Volume में perpendicular vertical height $h$ होती है।

> :icon-cross: **जाल 3.** Frustum में radius difference/sum गलत चुनना।
> Slant height में $R-r$; volume में $R^2+r^2+Rr$।

> :icon-cross: **जाल 4.** Frustum को पूरा cone मान लेना।
> दो bases और truncated height को formula में शामिल करें।

> :icon-cross: **जाल 5.** Pyramid TSA में base छोड़ देना या double जोड़ना।
> TSA = LSA + one base area।

> :icon-cross: **जाल 6.** Net में hidden faces को exposed surface मानना।
> Solid के बाहर दिखाई देने वाली surfaces ही paint/sheet area हैं।

> :icon-cross: **जाल 7.** Volume और surface units बदलना।
> Volume cubic units में, surface square units में।

> :icon-cross: **जाल 8.** Capacity conversion में $1$ litre = $100$ cm³ लिखना।
> सही $1000$ cm³ = $1$ litre।

> :icon-cross: **जाल 9.** Composite solids में overlapping volume दो बार जोड़ना।
> Natural boundary पर components अलग करिए और overlap check करें।

---

## 40.12 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* Prism base area $24$ और height $10$। Volume?

**हल:** $\mathbf{240}$ cm³।

**PYQ 2.** *(SSC CHSL)* Same base/height pyramid का volume prism का कितना?

**हल:** $\mathbf{one-third}$।

**PYQ 3.** *(RRB NTPC)* Square pyramid side $8$, height $12$। Volume?

**हल:** $\mathbf{256}$ cm³।

**PYQ 4.** *(IBPS Clerk)* Cone frustum $R=7,r=3,h=8$ की slant height?

**हल:** $\mathbf{4\sqrt{5}}$ cm।

**PYQ 5.** *(UP Police SI)* Square frustum sides $10,4$, height $6$। Volume?

**हल:** $\mathbf{312}$ cm³।

**PYQ 6.** *(SSC MTS)* Square pyramid base $8$, slant height $5$। TSA?

**हल:** $\mathbf{144}$ cm²।

---

## 40.13 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | Prism $B=24,h=10$ volume | $240$ | $Bh$ |
| 2 | Prism $B=24,P=20,h=10$ LSA | $200$ | $Ph$ |
| 3 | Prism same data TSA | $248$ | $Ph+2B$ |
| 4 | Triangular prism $b=6,t=4,L=10$ volume | $120$ | $1/2btL$ |
| 5 | Pyramid $B=60,h=9$ volume | $180$ | $Bh/3$ |
| 6 | Square pyramid $a=8,h=12$ volume | $256$ | $a²h/3$ |
| 7 | Square pyramid $a=8,h=12$ slant | $4\sqrt{10}$ | Pythagoras |
| 8 | Square pyramid $a=8,l=5$ TSA | $144$ | $a²+2al$ |
| 9 | Triangular pyramid $B=12,h=9$ | $36$ | $Bh/3$ |
| 10 | Frustum $R=7,r=3,h=8$ slant | $4\sqrt{5}$ | $(R-r)$ |
| 11 | Frustum square sides $10,4,h=6$ | $312$ | frustum volume |
| 12 | Conical frustum CSA | $\pi(R+r)l$ | formula |
| 13 | Pyramid net faces | 1 base + 4 triangles | net |
| 14 | Same base/height prism:pyramid volume | $3:1$ | relation |
| 15 | Base area $250$, height $40$ prism capacity | $10$ litres | cm³/1000 |
| 16 | Prism base area $30$, height $12$ | $360$ cm³ | $Bh$ |
| 17 | Pyramid $B=45,h=12$ | $180$ cm³ | one-third |
| 18 | Frustum $R=5,r=2,h=9$ slant | $\sqrt{90}$ | right triangle |
| 19 | Prism side paint | LSA $Ph$ | surface selection |
| 20 | Square pyramid side paint | LSA $2al$ | four triangles |
| 21 | Frustum with $R=r$ becomes | cylinder | limiting case |
| 22 | Recast prism into pyramid | volume conserved | conservation |
| 23 | Cube/prism same B,h relation | pyramid one-third | comparison |
| 24 | Square frustum V formula | $h(a²+b²+ab)/3$ | formula |
| 25 | Open pyramid surface | omit missing base | exposed faces |

---

## 40.14 :icon-trophy: अध्याय का सार

```
━━━ Prism ━━━
V = B h
LSA = P h
TSA = P h + 2B

triangular prism:
B=1/2 b t
V=1/2 b t L

━━━ Pyramid ━━━
V=1/3 B h
regular right pyramid:
LSA=1/2 P l
TSA=1/2 P l+B

square pyramid:
V=1/3 a²h
LSA=2al
TSA=a²+2al

━━━ Cone frustum ━━━
l²=h²+(R−r)²
V=1/3πh(R²+r²+Rr)
CSA=π(R+r)l
TSA=CSA+πR²+πr²

━━━ Square frustum ━━━
V=h/3(a²+b²+ab)

━━━ Comparison ━━━
same base and height:
pyramid volume = prism volume/3

━━━ Nets ━━━
prism: 2 bases + lateral rectangles
square pyramid: 1 square + 4 triangles

━━━ Capacity ━━━
1000 cm³ = 1 litre
```

> :icon-trophy: **Prism, pyramid और frustum complete।** Chapter 39 के basic solids से आगे बढ़कर syllabus में दिए गए right prism, regular pyramid और frustum अब formulas, nets और visual diagrams के साथ covered हैं।
>
> **आगे:** Chapter 41 — **निर्देशांक ज्यामिति (Coordinate Geometry)**।
