# अध्याय 37 — वृत्त, जीवा व स्पर्श रेखाएँ (Circles, Chords & Tangents)

## 37.1 :icon-target: परिचय व वेटेज

Part 5 का सबसे theorem-heavy topic circles है। Chapter 36 के cyclic quadrilateral और Chapter 33 के angles यहाँ सीधे काम आएँगे। Circle questions में figure markings—centre, radius, chord, tangent, contact point—को सही पढ़ना calculation जितना ही महत्वपूर्ण है।

> *"एक tangent और chord के बीच angle 45° है। Circle के alternate segment में angle कितना होगा?"*

Tangent–chord theorem से answer $45°$ होगा। इसी तरह chord, central angle, inscribed angle और common tangents के rules competitive exams में बार-बार आते हैं।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **2–3** | chords, tangents, angles |
| **SSC CGL Tier-2** | **3–5** | circle theorems और common tangents |
| SSC CHSL / MTS / GD | 1–2 | radius, diameter, semicircle |
| **SSC CPO** | **2–3** | tangent और cyclic angles |
| **IBPS / SBI PO** | 1–2 | geometry reasoning |
| IBPS / SBI Clerk | 1 | direct theorem |
| **RRB NTPC / ALP** | **2–3** | chord, tangent, circle measure |
| UP Police SI / Constable | 1–2 | tangent and angles |
| UPSSSC PET | 1 | area/circumference |
| Super TET / UPTET | 1–2 | visual circle geometry |

> :icon-key: **पूरे अध्याय का एक वाक्य:** Centre से chord/tangent तक perpendicular, centre angle और circumference angle का $2:1$ relation, और tangent lengths की equality—ये circle chapter के core rules हैं।

---

## 37.2 :icon-number: Circle के parts और measures

Circle के मुख्य parts:

- Centre $O$
- Radius $r$: centre से circumference तक
- Diameter $d=2r$: centre से गुजरने वाली chord
- Chord: circumference के दो points को join करने वाला segment
- Arc: circumference का भाग
- Sector: दो radii और एक arc से घिरा region
- Segment: chord और arc से घिरा region
- Tangent: circle को केवल एक point पर touch करने वाली line

```figure
type: circle-parts37
caption: radius, diameter, chord, arc और sector को एक ही diagram में पहचानिए
```

### Circumference और area

$$\text{circumference}=2\pi r=\pi d$$

$$\text{area}=\pi r^2$$

**उदाहरण 1.** Radius $7$ cm के circle की circumference और area।

$$C=2\times\frac{22}{7}\times7=\mathbf{44\text{ cm}}$$

$$A=\frac{22}{7}\times7^2=\mathbf{154\text{ cm}^2}$$

### Arc और sector

यदि central angle $\theta$ हो:

$$\text{arc length}=\frac{\theta}{360°}\times2\pi r$$

$$\text{sector area}=\frac{\theta}{360°}\times\pi r^2$$

**उदाहरण 2.** $r=14$ cm और $\theta=90°$ वाले sector का arc और area।

$$\text{arc}=\frac{90}{360}\times2\pi(14)=\mathbf{7\pi\text{ cm}}$$

$$\text{area}=\frac{90}{360}\times\pi(14)^2=\mathbf{49\pi\text{ cm}^2}$$

```figure
type: circle-measure
radius: 7
angle: 90
caption: circumference, area, arc और sector formulas को साथ compare कीजिए
```

---

## 37.3 :icon-ruler: Chord के theorems

### Perpendicular from centre bisects chord

यदि centre $O$ से chord $AB$ पर perpendicular $OM$ खींचें, तो:

$$OM\perp AB\quad\Rightarrow\quad AM=MB$$

```figure
type: chord-perpendicular
caption: centre से chord पर perpendicular chord को दो equal parts में बाँटता है
```

**उदाहरण 3.** Chord $AB=18$ cm है। Centre से perpendicular chord को $M$ पर काटता है। $AM$?

$$AM=MB=\frac{18}{2}=\mathbf{9\text{ cm}}$$

### Equal chords

Circle में equal chords centre से equal distance पर होती हैं।

```figure
type: equal-chords
caption: equal chords की centre से perpendicular distances समान होती हैं
```

यदि $AB=CD$, तो centre से $AB$ और $CD$ की दूरी equal होगी। Converse भी true है।

### Longer chord

- Centre के closer chord की length अधिक
- Centre से farther chord की length कम
- Centre से गुजरने वाली diameter सबसे बड़ी chord है

**उदाहरण 4.** एक circle में chord $AB$ centre से $4$ cm और chord $CD$ centre से $7$ cm दूर है। कौन-सी chord बड़ी?

$AB$ centre के closer है, इसलिए $\mathbf{AB>CD}$।

### Chord और radius relation

यदि radius $r$ और centre से chord की perpendicular distance $d$ हो, तो half chord:

$$\left(\frac{c}{2}\right)^2=r^2-d^2$$

**उदाहरण 5.** Circle radius $13$ cm और centre से chord की दूरी $5$ cm। Chord length?

$$\frac{c}{2}=\sqrt{13^2-5^2}=\sqrt{144}=12$$

अतः chord $c=\mathbf{24\text{ cm}}$।

---

## 37.4 :icon-chart: Central और inscribed angles

### Angle at centre और circumference

एक ही arc पर centre का angle, circumference के angle का double होता है:

$$\angle AOB=2\angle ACB$$

```figure
type: center-angle
caption: same arc पर central angle inscribed angle का double होता है
```

**उदाहरण 6.** Centre angle $AOB=100°$ है। Same arc पर circumference angle $ACB$?

$$\angle ACB=\frac{100}{2}=\mathbf{50°}$$

**उदाहरण 7.** Circumference angle $35°$ है। Centre angle?

$$\angle AOB=2\times35=\mathbf{70°}$$

### Same segment theorem

एक ही chord के same segment में बने angles equal होते हैं।

```figure
type: same-segment
caption: same chord AB पर खड़े angles बराबर होते हैं
```

$$\angle APB=\angle AQB$$

**उदाहरण 8.** Same segment में एक angle $42°$ है। दूसरा?

उत्तर $\mathbf{42°}$।

### Angle in a semicircle

Diameter द्वारा circumference पर subtended angle हमेशा right angle होता है:

$$\angle APB=90°$$

```figure
type: semicircle-angle
caption: diameter AB द्वारा semicircle पर बना angle 90° होता है
```

**उदाहरण 9.** $AB$ diameter है और $\angle A=35°$ in triangle $APB$। $\angle B$?

$$B=180-90-35=\mathbf{55°}$$

### Equal chords and angles

- Equal chords equal central angles subtend करती हैं।
- Equal central angles equal arcs subtend करते हैं।
- Same arc पर inscribed angles equal।

---

## 37.5 :icon-steps: Cyclic quadrilateral और circle angles

यदि quadrilateral के चारों vertices circle पर हों, तो वह cyclic quadrilateral है।

Properties:

$$\angle A+\angle C=180°$$

$$\angle B+\angle D=180°$$

**उदाहरण 10.** Cyclic quadrilateral में opposite angles $(3x+10)°$ और $(5x-30)°$ हैं।

$$3x+10+5x-30=180\quad\Rightarrow\quad x=\mathbf{25}$$

Angles $85°$ और $95°$।

### Exterior angle of cyclic quadrilateral

Cyclic quadrilateral का exterior angle opposite interior angle के बराबर होता है।

**उदाहरण 11.** Exterior angle $110°$ है। Opposite interior angle?

उत्तर $\mathbf{110°}$।

### Intersecting chords inside circle

यदि chords $AB$ और $CD$ circle के अन्दर $P$ पर intersect करें, तो:

$$PA\times PB=PC\times PD$$

**उदाहरण 12.** $PA=4$, $PB=9$, $PC=6$। $PD$?

$$4\times9=6\times PD\quad\Rightarrow\quad PD=\mathbf{6}$$

---

## 37.6 :icon-timer: Tangent और radius

Tangent circle को केवल एक point पर touch करती है। Touch point को point of contact कहते हैं।

### Radius–tangent theorem

Point of contact पर radius tangent के perpendicular होती है:

$$OT\perp\text{tangent}$$

```figure
type: tangent-radius
caption: point of contact T पर radius OT tangent के perpendicular होती है
```

**उदाहरण 13.** Tangent और radius के बीच angle?

उत्तर $\mathbf{90°}$।

### Tangents from an external point

यदि external point $P$ से circle पर दो tangents $PA$ और $PB$ draw हों, तो:

$$PA=PB$$

```figure
type: two-tangents
caption: एक external point से खींची गई दोनों tangents की lengths equal होती हैं
```

**उदाहरण 14.** $PA=3x+2$ और $PB=5x-10$ tangents हैं। $x$?

$$3x+2=5x-10\quad\Rightarrow\quad x=\mathbf{6}$$

Tangent length $=20$ units।

### Tangent length और power

यदि $P$ से tangent length $PT$ और secant के external/internal parts $PA,PB$ हों:

$$PT^2=PA\times PB$$

**उदाहरण 15.** $PA=4$, $PB=16$। Tangent $PT$?

$$PT=\sqrt{4\times16}=\mathbf{8}$$

---

## 37.7 :icon-ruler: Tangent–chord theorem

Tangent और chord के बीच का angle, alternate segment में उसी chord द्वारा subtended angle के बराबर होता है।

```figure
type: tangent-chord
caption: tangent-chord angle alternate segment के inscribed angle के बराबर होता है
```

**उदाहरण 16.** Tangent और chord का angle $48°$ है। Alternate segment angle?

उत्तर $\mathbf{48°}$।

**उदाहरण 17.** Alternate segment angle $35°$ है। Tangent-chord angle?

उत्तर $\mathbf{35°}$।

### Tangent और chord angle chase

यदि radius और chord से triangle बने, तो radius–tangent $90°$ और isosceles radii का उपयोग कर missing angles निकालिए।

**उदाहरण 18.** $OT$ radius है, tangent पर $90°$ angle है और chord $TA$ के साथ tangent angle $40°$ है। Alternate segment में chord $TA$ का angle?

Tangent-chord theorem से answer $\mathbf{40°}$।

---

## 37.8 :icon-chart: Two circles और common tangents

दो circles के बीच common tangent दोनों circles को touch करती है। Blueprint में “two or more circles की common tangents” विशेष रूप से महत्वपूर्ण है।

### Direct common tangent

Direct/common external tangent दोनों circles के एक ही side से touch करती है।

```figure
type: common-direct-tangent
caption: direct common tangent circles के एक ही side पर रहती है
```

यदि centre distance $d$, radii $R,r$ हों, तो tangent segment length:

$$L=\sqrt{d^2-(R-r)^2}$$

### Transverse common tangent

Transverse/internal tangent circles के बीच से cross करती है।

```figure
type: common-transverse-tangent
caption: transverse common tangents circles के बीच cross करती हैं
```

Length:

$$L=\sqrt{d^2-(R+r)^2}$$

### Common tangents की संख्या

दो separate non-overlapping circles के लिए सामान्यतः चार common tangents:

- 2 direct/external
- 2 transverse/internal

यदि circles touch/intersect करें तो number बदल सकता है।

**उदाहरण 19.** Two circles के centres की distance $13$ cm और radii $5$ cm तथा $2$ cm हैं। Direct common tangent length?

$$L=\sqrt{13^2-(5-2)^2}=\sqrt{169-9}=\mathbf{4\sqrt{10}\text{ cm}}$$

**उदाहरण 20.** वही circles के transverse tangent की length?

$$L=\sqrt{13^2-(5+2)^2}=\sqrt{169-49}=\mathbf{2\sqrt{30}\text{ cm}}$$

> :icon-warn: Direct tangent में $R-r$ और transverse tangent में $R+r$ आता है। यही सबसे common advanced trap है।

---

## 37.9 :icon-divide: Circle measures और composite regions

**उदाहरण 21.** $r=7$ cm circle का area और circumference।

$$A=\pi r^2=49\pi$$

$$C=2\pi r=14\pi$$

**उदाहरण 22.** $r=14$ cm और sector angle $90°$। Sector area?

$$A=\frac{90}{360}\pi(14)^2=49\pi\text{ cm}^2$$

### Ring या annulus

Outer radius $R$ और inner radius $r$:

$$\text{area}=\pi(R^2-r^2)$$

```figure
type: circle-measure
radius: 14
angle: 180
caption: arc और sector measures में central angle का fraction लगाइए
```

**उदाहरण 23.** Ring के radii $7$ cm और $3$ cm हैं। Area?

$$A=\pi(7^2-3^2)=\mathbf{40\pi\text{ cm}^2}$$

---

## 37.10 :icon-bulb: Theorem map और shortcuts

### :icon-timer: Chord checklist

- Centre perpendicular chord ⟹ chord bisected
- Equal chords ⟹ equal distance from centre
- Equal chords ⟹ equal central angles
- Diameter largest chord

### :icon-timer: Angle checklist

- Centre angle $=2\times$ circumference angle on same arc
- Same segment angles equal
- Semicircle angle $90°$
- Cyclic opposite angles sum $180°$

### :icon-timer: Tangent checklist

- radius ⟂ tangent at contact
- external point से tangent lengths equal
- tangent-chord angle = alternate segment angle
- direct common tangent: $R-r$
- transverse common tangent: $R+r$

### :icon-timer: Chord intersection

$$PA\times PB=PC\times PD$$

### :icon-timer: Tangent-secant

$$PT^2=PA\times PB$$

### :icon-timer: Measure formulas

$$C=2\pi r,\quad A=\pi r^2$$

$$L_{arc}=\frac{\theta}{360}\times2\pi r$$

$$A_{sector}=\frac{\theta}{360}\times\pi r^2$$

---

## 37.11 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Diameter को chord से अलग completely मानना।
> Diameter centre से गुजरने वाली सबसे बड़ी chord है।

> :icon-cross: **जाल 2.** Centre angle और circumference angle equal लिखना।
> Same arc पर centre angle double होता है।

> :icon-cross: **जाल 3.** Chord पर perpendicular को tangent समझना।
> Tangent circle को एक point पर touch करती है और radius contact पर perpendicular होता है।

> :icon-cross: **जाल 4.** Equal chords को centre से अलग distances पर रखना।
> Equal chords centre से equal distance पर होती हैं।

> :icon-cross: **जाल 5.** Cyclic quadrilateral में adjacent angles का sum $180°$ लेना।
> Opposite angles supplementary होते हैं।

> :icon-cross: **जाल 6.** Tangent length from external point unequal लेना।
> Same external point से दोनों tangent segments equal होते हैं।

> :icon-cross: **जाल 7.** Tangent-chord theorem में wrong segment चुनना।
> Chord के opposite arc/alternate segment का angle देखिए।

> :icon-cross: **जाल 8.** Direct common tangent में $R+r$ लगाना।
> Direct में radius difference; transverse में radius sum।

> :icon-cross: **जाल 9.** Sector area में $\theta/180$ लगाना।
> Full circle $360°$ है; fraction $\theta/360$।

> :icon-cross: **जाल 10.** Ring area में inner circle को जोड़ना।
> Annulus area outer area minus inner area है।

---

## 37.12 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* Radius $7$ cm circle की circumference और area?

**हल:** $\mathbf{44}$ cm और $\mathbf{154}$ cm²।

**PYQ 2.** *(SSC CHSL)* Centre angle $100°$। Same arc circumference angle?

**हल:** $\mathbf{50°}$।

**PYQ 3.** *(RRB NTPC)* Radius $13$ और chord distance $5$। Chord length?

**हल:** $\mathbf{24}$ cm।

**PYQ 4.** *(IBPS Clerk)* External point से tangent lengths $3x+2$ और $5x-10$। $x$?

**हल:** $\mathbf{6}$।

**PYQ 5.** *(UP Police SI)* Cyclic opposite angles $72°$ और $x$। $x$?

**हल:** $\mathbf{108°}$।

**PYQ 6.** *(SSC CPO)* Direct common tangent formula?

**हल:** $\mathbf{\sqrt{d^2-(R-r)^2}}$।

---

## 37.13 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | Radius $7$ circle circumference | $44$ | $2\pi r$ |
| 2 | Radius $7$ circle area | $154$ | $\pi r^2$ |
| 3 | Chord $18$; perpendicular from centre | half $9$ | bisects chord |
| 4 | Radius $13$, chord distance $5$ | chord $24$ | Pythagoras |
| 5 | Equal chords property | equal centre distances | theorem |
| 6 | Central angle $100°$ | inscribed $50°$ | half |
| 7 | Inscribed angle $35°$ | central $70°$ | double |
| 8 | Same segment one angle $42°$ | other $42°$ | equal |
| 9 | Diameter triangle angle | $90°$ | semicircle |
| 10 | Cyclic opposite $72°$ | $108°$ | supplementary |
| 11 | Chords intersect: $4,9,6,x$ | $x=6$ | products |
| 12 | Tangent-radius angle | $90°$ | perpendicular |
| 13 | Tangents $3x+2$, $5x-10$ | $x=6$ | equal tangents |
| 14 | Tangent-secant parts $4,16$ | tangent $8$ | square relation |
| 15 | Tangent-chord angle $48°$ | alternate $48°$ | theorem |
| 16 | Sector $r=14,\theta=90°$ area | $49\pi$ | sector formula |
| 17 | Sector $r=14,\theta=90°$ arc | $7\pi$ | arc formula |
| 18 | Ring radii $7,3$ area | $40\pi$ | difference squares |
| 19 | Direct tangent: $d=13,R=5,r=2$ | $4\sqrt{10}$ | $R-r$ |
| 20 | Transverse same circles | $2\sqrt{30}$ | $R+r$ |
| 21 | Common tangents for separate circles | 4 | 2 direct + 2 transverse |
| 22 | Exterior cyclic angle $110°$ | opposite $110°$ | theorem |
| 23 | Diameter $20$ | radius $10$ | $d=2r$ |
| 24 | $r=7$, sector $180°$ area | $49\pi/2$ | half circle |
| 25 | Circle area $154$ | radius $7$ | reverse formula |

---

## 37.14 :icon-trophy: अध्याय का सार

```
━━━ Circle parts ━━━
centre O, radius r, diameter d=2r
chord, arc, sector, segment, tangent

━━━ Measures ━━━
C=2πr=πd
A=πr²
arc=(θ/360)×2πr
sector=(θ/360)×πr²
ring=π(R²−r²)

━━━ Chords ━━━
perpendicular from centre bisects chord
equal chords are equidistant from centre
longer chord is closer to centre
diameter is longest chord

━━━ Angles ━━━
central angle = 2×inscribed angle
same segment angles equal
semicircle angle = 90°
cyclic opposite angles sum 180°

━━━ Tangents ━━━
radius ⟂ tangent at contact
external tangents equal
PT² = PA×PB
tangent-chord = alternate segment angle

━━━ Common tangents ━━━
direct: sqrt(d²−(R−r)²)
transverse: sqrt(d²−(R+r)²)
separate circles: 2 direct + 2 transverse

━━━ Traps ━━━
centre angle double
opposite cyclic angles
R−r versus R+r
θ/360 in sector formulas
```

> :icon-trophy: **Chapter 37 में circle geometry की पूरी theorem-map तैयार है।** Chords, central angles, cyclic quadrilaterals, tangents और common tangents अब एक connected visual system के रूप में काम करेंगे।
>
> **आगे:** Chapter 38 — **क्षेत्रफल व परिमाप (2-D Area & Perimeter)**।
