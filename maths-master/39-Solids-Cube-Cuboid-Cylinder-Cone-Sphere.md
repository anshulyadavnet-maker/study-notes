# अध्याय 39 — ठोस आकृतियाँ (Cube, Cuboid, Cylinder, Cone, Sphere & Hemisphere)

## 39.1 :icon-target: परिचय व वेटेज

Chapter 38 में flat 2-D regions का area और perimeter निकाला। अब figures में length, breadth और height तीन dimensions होंगी। Solid questions में सबसे पहले यह पहचानना जरूरी है कि पूछा गया है—volume, curved/lateral surface area, total surface area या capacity।

> *"Cylinder की curved surface paint करनी है या पूरा closed cylinder?"*

Curved surface में circular bases नहीं आते; total surface में bases भी जुड़ते हैं। यही distinction exam में सबसे अधिक गलती कराता है।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **2–3** | cube, cuboid, cylinder |
| **SSC CGL Tier-2** | **3–5** | cone, sphere, composite solids |
| SSC CHSL / MTS / GD | 1–2 | volume और surface |
| **SSC CPO** | **2–3** | cylinder/cone and capacity |
| **IBPS / SBI PO** | 1–2 | arithmetic mensuration |
| IBPS / SBI Clerk | 1 | direct solid formula |
| **RRB NTPC / ALP** | **2–3** | cuboid, cylinder, sphere |
| UP Police SI / Constable | 1–2 | capacity and volume |
| UPSSSC PET | 1 | basic 3-D formula |
| Super TET / UPTET | 1–2 | visual solids |

> :icon-key: **पूरे अध्याय का एक वाक्य:** Solid पहचानिए, required surface/volume formula चुनिए और cubic units को capacity units में सही बदलें।

---

## 39.2 :icon-number: 3-D measures और surface labels

### Volume

Solid के अन्दर की जगह volume है। Units cubic होती हैं: cm³, m³।

### Surface area

- Curved Surface Area (CSA): केवल curved part
- Lateral Surface Area (LSA): sides का area, bases नहीं
- Total Surface Area (TSA): सभी exposed surfaces

### Unit conversion

$$1\text{ m}=100\text{ cm}$$

$$1\text{ m}^3=1000000\text{ cm}^3$$

Capacity:

$$1\text{ litre}=1000\text{ cm}^3$$

$$1\text{ m}^3=1000\text{ litres}$$

| Question wording | Quantity |
|---|---|
| holds, contains, capacity | volume |
| paint curved wall | CSA |
| wrap side surface | LSA |
| closed solid polish/paint | TSA |
| open container | TSA minus open base/top as appropriate |

---

## 39.3 :icon-calc: Cube और cuboid

### Cube

Side $a$ वाले cube के:

$$V=a^3$$

$$LSA=4a^2$$

$$TSA=6a^2$$

$$\text{space diagonal}=a\sqrt{3}$$

```figure
type: cube3d
side: 6
caption: cube में छह equal square faces और space diagonal होती है
```

**उदाहरण 1.** Cube की side $6$ cm।

- Volume $=6^3=\mathbf{216\text{ cm}^3}$
- LSA $=4\times6^2=\mathbf{144\text{ cm}^2}$
- TSA $=6\times6^2=\mathbf{216\text{ cm}^2}$
- diagonal $=\mathbf{6\sqrt{3}\text{ cm}}$

### Cuboid / rectangular parallelepiped

Length $l$, breadth $b$, height $h$:

$$V=lbh$$

$$LSA=2h(l+b)$$

$$TSA=2(lb+bh+hl)$$

$$d=\sqrt{l^2+b^2+h^2}$$

```figure
type: cuboid3d
length: 8
breadth: 5
height: 4
caption: cuboid की तीन dimensions volume, surface और space diagonal देती हैं
```

**उदाहरण 2.** Cuboid $l=8$, $b=5$, $h=4$ cm।

- Volume $=8\times5\times4=\mathbf{160\text{ cm}^3}$
- TSA $=2(40+20+32)=\mathbf{184\text{ cm}^2}$
- LSA $=2\times4(8+5)=\mathbf{104\text{ cm}^2}$
- diagonal $=\sqrt{64+25+16}=\mathbf{\sqrt{105}\text{ cm}}$

---

## 39.4 :icon-chart: Cylinder

Radius $r$ और height $h$ वाले cylinder के:

$$V=\pi r^2h$$

$$CSA=2\pi rh$$

$$TSA=2\pi r(h+r)$$

```figure
type: cylinder3d
radius: 4
height: 10
caption: cylinder में two circular bases और एक curved surface होती है
```

**उदाहरण 3.** Cylinder $r=4$ cm, $h=10$ cm।

- Volume $=\pi(4)^2(10)=\mathbf{160\pi\text{ cm}^3}$
- CSA $=2\pi(4)(10)=\mathbf{80\pi\text{ cm}^2}$
- TSA $=2\pi(4)(10+4)=\mathbf{112\pi\text{ cm}^2}$

### Open cylinder

- दोनों bases closed: $TSA=2\pi r(h+r)$
- एक base open: $CSA+\pi r^2$
- दोनों ends open pipe: $CSA$

**उदाहरण 4.** Open cylindrical tank की inside radius $7$ cm और height $20$ cm है। अंदर का capacity?

$$V=\pi r^2h=\frac{22}{7}\times49\times20=\mathbf{3080\text{ cm}^3}=\mathbf{3.08\text{ litres}}$$

> :icon-warn: Open/closed wording surface area बदलता है, volume नहीं—यदि dimensions same हों।

---

## 39.5 :icon-ruler: Cone

Cone में radius $r$, perpendicular height $h$ और slant height $l$ होते हैं।

$$l^2=r^2+h^2$$

$$V=\frac{1}{3}\pi r^2h$$

$$CSA=\pi rl$$

$$TSA=\pi r(l+r)$$

```figure
type: cone3d
radius: 5
height: 12
caption: cone की slant height l, radius और perpendicular height से बनती है
```

**उदाहरण 5.** Cone $r=5$ cm, $h=12$ cm।

$$l=\sqrt{5^2+12^2}=\mathbf{13\text{ cm}}$$

- Volume $=\frac{1}{3}\pi(25)(12)=\mathbf{100\pi\text{ cm}^3}$
- CSA $=\pi(5)(13)=\mathbf{65\pi\text{ cm}^2}$
- TSA $=\pi(5)(13+5)=\mathbf{90\pi\text{ cm}^2}$

### Cone और cylinder relation

Same $r,h$ वाले cone का volume उसी cylinder का one-third होता है:

$$V_{cone}=\frac{1}{3}V_{cylinder}$$

**उदाहरण 6.** Same radius और height में cylinder volume $300\pi$ cm³ है। Cone volume?

$$V=\mathbf{100\pi\text{ cm}^3}$$

---

## 39.6 :icon-chart: Sphere और hemisphere

### Sphere

Radius $r$:

$$V=\frac{4}{3}\pi r^3$$

$$SA=4\pi r^2$$

```figure
type: sphere3d
radius: 6
caption: sphere में surface का हर point centre से समान radius पर होता है
```

**उदाहरण 7.** Sphere radius $6$ cm।

- Surface area $=4\pi(36)=\mathbf{144\pi\text{ cm}^2}$
- Volume $=\frac{4}{3}\pi(216)=\mathbf{288\pi\text{ cm}^3}$

### Hemisphere

Radius $r$:

$$V=\frac{2}{3}\pi r^3$$

$$CSA=2\pi r^2$$

$$TSA=3\pi r^2$$

```figure
type: hemisphere3d
radius: 6
caption: hemisphere का CSA curved half है और TSA में circular base भी शामिल है
```

**उदाहरण 8.** Hemisphere radius $6$ cm।

- Volume $=\frac{2}{3}\pi(216)=\mathbf{144\pi\text{ cm}^3}$
- CSA $=2\pi(36)=\mathbf{72\pi\text{ cm}^2}$
- TSA $=3\pi(36)=\mathbf{108\pi\text{ cm}^2}$

> :icon-key: Hemisphere में “curved surface” और “total surface” अलग हैं। TSA = CSA + base circle।

---

## 39.7 :icon-chart: Solids की तुलना और capacity

```figure
type: solid-comparison
caption: समान volume वाले solids की surface area shape के अनुसार बदलती है
```

**उदाहरण 9.** Cube side $6$ cm और cuboid $3\times6\times12$ cm। दोनों का volume?

- Cube $=6^3=216$ cm³
- Cuboid $=3\times6\times12=216$ cm³

Volume equal है, लेकिन TSA अलग:

- Cube TSA $=216$ cm²
- Cuboid TSA $=2(18+72+36)=252$ cm²

### Capacity conversion

```figure
type: capacity-container
radius: 5
height: 12
caption: cylindrical container का inside volume litres में capacity देता है
```

**उदाहरण 10.** Cylinder $r=5$ cm और $h=12$ cm की capacity litres में?

$$V=\pi(5)^2(12)=300\pi\text{ cm}^3$$

यदि $\pi=3.14$:

$$V=942\text{ cm}^3=\mathbf{0.942\text{ litres}}$$

---

## 39.8 :icon-steps: Melting, recasting और composite solids

### Melting and recasting

जब solid melt करके नए shape में recast होता है और wastage नहीं है:

$$\text{old volume}=\text{new volume}$$

```figure
type: melt-recast
radius: 3
height: 8
side: 2
caption: melting और recasting में volume conserve रहता है
```

**उदाहरण 11.** Radius $3$ cm और height $8$ cm cylinder melt करके side $2$ cm cubes बनाए गए। Cubes की संख्या?

Cylinder volume:

$$V=\pi(3)^2(8)=72\pi\text{ cm}^3$$

One cube volume $=2^3=8$ cm³।

$$n=\frac{72\pi}{8}=\mathbf{9\pi}$$

यदि $\pi=22/7$, $n=198/7$ आएगा; practical integer question में dimensions/values सामान्यतः integer count देने के लिए चुने जाते हैं।

> :icon-warn: Recasting में surface area conserve नहीं होता; केवल volume conserve होता है।

### Composite solid

Cuboid और cylinder/cone जैसे components अलग करके volumes जोड़ें या hollow part subtract करें।

```figure
type: composite-solid
caption: composite solid को natural boundary पर अलग करके component volumes जोड़िए
```

**उदाहरण 12.** A solid में cuboid और उसके ऊपर cylinder जुड़ा है। Total volume:

$$V_{total}=V_{cuboid}+V_{cylinder}$$

यदि hole हो:

$$V_{remaining}=V_{outer}-V_{hole}$$

---

## 39.9 :icon-ruler: Surface area applications

### Painting a cylinder

- curved wall paint: $CSA=2\pi rh$
- closed cylinder paint: $TSA=2\pi r(h+r)$
- open top tank: $CSA+\pi r^2$

**उदाहरण 13.** Cylinder का curved surface area $80\pi$ cm² है, $r=4$ cm। Height?

$$2\pi rh=80\pi\quad\Rightarrow\quad2(4)h=80\quad\Rightarrow\quad h=\mathbf{10\text{ cm}}$$

### Cuboid box

- closed box: TSA
- open-top box: TSA minus top rectangle $lb$
- four walls: LSA $=2h(l+b)$

**उदाहरण 14.** $8\times5\times4$ cuboid का four-wall area?

$$LSA=2(4)(8+5)=\mathbf{104\text{ cm}^2}$$

### Cone sheet

Cone के लिए curved sheet/cloth: $\pi rl$; base सहित closed: $\pi r(l+r)$।

---

## 39.10 :icon-bulb: Formula map और shortcuts

### :icon-timer: Cube/cuboid

$$V_{cube}=a^3,\quad TSA=6a^2,\quad d=a\sqrt{3}$$

$$V_{cuboid}=lbh,\quad TSA=2(lb+bh+hl)$$

### :icon-timer: Cylinder

$$V=\pi r^2h,\quad CSA=2\pi rh,\quad TSA=2\pi r(h+r)$$

### :icon-timer: Cone

$$l=\sqrt{r^2+h^2}$$

$$V=\frac{1}{3}\pi r^2h,\quad CSA=\pi rl,\quad TSA=\pi r(l+r)$$

### :icon-timer: Sphere/hemisphere

$$V_{sphere}=\frac{4}{3}\pi r^3,\quad SA=4\pi r^2$$

$$V_{hemi}=\frac{2}{3}\pi r^3,\quad CSA=2\pi r^2,\quad TSA=3\pi r^2$$

### :icon-timer: Shortcut 1 — radius factor

Radius $k$ times:

- sphere volume $k^3$ times
- sphere surface $k^2$ times
- cylinder volume $k^2$ times if height same

### :icon-timer: Shortcut 2 — volume equality

Melt/recast, water transfer and combined capacity questions में:

$$\sum V_{input}=\sum V_{output}$$

### :icon-timer: Shortcut 3 — litres

$$1000\text{ cm}^3=1\text{ litre}$$

### :icon-timer: Shortcut 4 — open surface

Open container में absent face का area subtract करें।

---

## 39.11 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** CSA, LSA और TSA को interchange करना।
> Question में curved, lateral या total शब्द ध्यान से पढ़िए।

> :icon-cross: **जाल 2.** Cone में height को slant height समझना।
> $l^2=r^2+h^2$ से slant height निकालिए।

> :icon-cross: **जाल 3.** Cone volume में $1/3$ भूलना।
> Cone का volume same cylinder का one-third है।

> :icon-cross: **जाल 4.** Hemisphere TSA में base circle भूलना।
> CSA $2\pi r^2$, TSA $3\pi r^2$।

> :icon-cross: **जाल 5.** Cuboid space diagonal में केवल $l^2+b^2$ लेना।
> Height का $h^2$ भी जोड़ना है।

> :icon-cross: **जाल 6.** Cubic unit को square unit लिखना।
> Volume cm³/m³ में होता है।

> :icon-cross: **जाल 7.** $1$ litre को $100$ cm³ लिखना।
> सही conversion $1000$ cm³ = $1$ litre।

> :icon-cross: **जाल 8.** Recasting में surface area conserve मानना।
> Recasting में volume conserve होता है, surface area नहीं।

> :icon-cross: **जाल 9.** Open container में missing base/top को include करना।
> केवल exposed surfaces का area लें।

> :icon-cross: **जाल 10.** Composite solid में overlapping boundary को दो बार surface area में जोड़ना।
> Internal joining surface exposed नहीं होती।

---

## 39.12 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* Cube side $6$ cm का volume और TSA?

**हल:** $\mathbf{216\text{ cm}^3}$ और $\mathbf{216\text{ cm}^2}$।

**PYQ 2.** *(SSC CHSL)* Cuboid $8\times5\times4$ का volume?

**हल:** $\mathbf{160\text{ cm}^3}$।

**PYQ 3.** *(RRB NTPC)* Cylinder $r=4,h=10$ का volume?

**हल:** $\mathbf{160\pi\text{ cm}^3}$।

**PYQ 4.** *(IBPS Clerk)* Cone $r=5,h=12$ की slant height?

**हल:** $\mathbf{13}$ cm।

**PYQ 5.** *(UP Police SI)* Sphere radius $6$ का volume?

**हल:** $\mathbf{288\pi\text{ cm}^3}$।

**PYQ 6.** *(SSC MTS)* Hemisphere radius $6$ का TSA?

**हल:** $\mathbf{108\pi\text{ cm}^2}$।

---

## 39.13 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | Cube side $6$ volume | $216$ | $a^3$ |
| 2 | Cube side $6$ TSA | $216$ | $6a^2$ |
| 3 | Cube side $6$ diagonal | $6\sqrt{3}$ | space diagonal |
| 4 | Cuboid $8,5,4$ volume | $160$ | $lbh$ |
| 5 | Cuboid $8,5,4$ TSA | $184$ | formula |
| 6 | Cylinder $r=4,h=10$ volume | $160\pi$ | $\pi r^2h$ |
| 7 | Cylinder $r=4,h=10$ CSA | $80\pi$ | $2\pi rh$ |
| 8 | Cone $r=5,h=12$ slant height | $13$ | Pythagoras |
| 9 | Cone $r=5,h=12$ volume | $100\pi$ | one-third |
| 10 | Cone $r=5,l=13$ CSA | $65\pi$ | $\pi rl$ |
| 11 | Sphere $r=6$ surface area | $144\pi$ | $4\pi r^2$ |
| 12 | Sphere $r=6$ volume | $288\pi$ | $4/3\pi r^3$ |
| 13 | Hemisphere $r=6$ volume | $144\pi$ | $2/3\pi r^3$ |
| 14 | Hemisphere $r=6$ TSA | $108\pi$ | $3\pi r^2$ |
| 15 | Cylinder capacity $r=5,h=12$ | $300\pi$ cm³ | volume |
| 16 | $300\pi$ cm³ in litres | $0.3\pi$ litres | divide 1000 |
| 17 | Cylinder CSA $80\pi$, r=4 | h=10 | solve $2\pi rh$ |
| 18 | Cuboid four walls $8,5,4$ | $104$ | LSA |
| 19 | Cube side doubled | volume 8 times | cube factor |
| 20 | Sphere radius tripled | surface 9 times | square factor |
| 21 | Cone volume vs same cylinder | one-third | relation |
| 22 | Cylinder melt to cubes | volume conserved | recasting |
| 23 | Cuboid + cylinder | add volumes | composite |
| 24 | Open cylinder | omit open base/top | surface selection |
| 25 | $l=6,b=4,h=3$ four walls | $60$ | $2h(l+b)$ |

---

## 39.14 :icon-trophy: अध्याय का सार

```
━━━ Cube ━━━
V=a³
LSA=4a²
TSA=6a²
diagonal=a√3

━━━ Cuboid ━━━
V=lbh
LSA=2h(l+b)
TSA=2(lb+bh+hl)
diagonal=√(l²+b²+h²)

━━━ Cylinder ━━━
V=πr²h
CSA=2πrh
TSA=2πr(h+r)

━━━ Cone ━━━
l²=r²+h²
V=1/3πr²h
CSA=πrl
TSA=πr(l+r)

━━━ Sphere ━━━
SA=4πr²
V=4/3πr³

━━━ Hemisphere ━━━
V=2/3πr³
CSA=2πr²
TSA=3πr²

━━━ Capacity ━━━
1000 cm³ = 1 litre
1 m³ = 1000 litres

━━━ Recasting ━━━
old volume = new volume
surface area is not conserved

━━━ Composite ━━━
component volumes add
holes/internal parts subtract
```

> :icon-trophy: **3-D mensuration complete।** Cube, cuboid, cylinder, cone, sphere और hemisphere की volume/surface/capacity system अब तैयार है।
>
> **आगे:** Chapter 40 — **Prism, Pyramid और Frustum**।
