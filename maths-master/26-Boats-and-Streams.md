# अध्याय 26 — नाव व धारा (Boats & Streams)

## 26.1 :icon-target: परिचय व वेटेज

अध्याय 24 में हमने चाल, समय व दूरी और अध्याय 25 में relative speed सीखी। नाव व धारा में नदी की धारा स्वयं एक moving medium है। नाव की अपनी चाल और पानी की चाल मिलकर downstream speed बनाती हैं, जबकि upstream में धारा नाव की चाल को कम करती है।

> *"शांत जल में नाव की चाल 12 km/h और धारा की चाल 3 km/h है। downstream और upstream चाल क्या होगी?"*

Downstream में $12+3=15$ km/h और upstream में $12-3=9$ km/h। यही दो operations पूरे अध्याय की नींव हैं।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1** | downstream/upstream |
| **SSC CGL Tier-2** | **1–2** | round trip और relative speed |
| SSC CHSL / MTS / GD | 1 | मूल boat speed |
| SSC CPO | 1–2 | धारा और समय |
| **IBPS / SBI PO** | **1–2** | boat–stream ratio |
| IBPS / SBI Clerk | 1 | speed from two effective speeds |
| **RRB NTPC / ALP** | **1–2** | upstream, downstream, raft |
| UP Police SI / Constable | 1–2 | direct formula |
| UPSSSC PET | 1 | सरल चाल–समय |
| Super TET / UPTET | 1 | गति का अनुप्रयोग |

> :icon-key: **पूरे अध्याय का एक वाक्य:** downstream में boat speed और stream speed **जुड़ते** हैं; upstream में stream speed **घटती** है।

---

## 26.2 :icon-number: मूल अवधारणा — शांत जल और धारा

मान लीजिए —

- शांत जल में नाव की चाल $=b$
- धारा की चाल $=s$

तब —

$$\text{downstream speed}=b+s$$

$$\text{upstream speed}=b-s$$

```figure
type: speed-components
still: 12
current: 3
caption: धारा downstream में नाव को तेज और upstream में धीमा करती है
```

| स्थिति | प्रभावी चाल |
|---|---|
| downstream | $b+s$ |
| upstream | $b-s$ |
| floating object | केवल $s$ |
| still water boat speed | $b$ |

**उदाहरण 1.** शांत जल में नाव की चाल $12$ km/h और धारा $3$ km/h है।

- downstream $=12+3=\mathbf{15}$ km/h
- upstream $=12-3=\mathbf{9}$ km/h

**उदाहरण 2.** downstream speed $15$ km/h और upstream speed $9$ km/h है। शांत जल की नाव और धारा की चाल?

$$b=\frac{15+9}{2}=\mathbf{12}\text{ km/h}$$

$$s=\frac{15-9}{2}=\mathbf{3}\text{ km/h}$$

```figure
type: up-downstream
down: 15
up: 9
caption: downstream और upstream speeds का योग और अन्तर boat तथा stream speed देते हैं
```

### दो महत्वपूर्ण सूत्र

यदि downstream speed $D$ और upstream speed $U$ दी हों, तो —

$$\text{boat speed in still water}=\frac{D+U}{2}$$

$$\text{stream speed}=\frac{D-U}{2}$$

> :icon-warn: Upstream speed तभी धनात्मक होगी जब boat की still-water speed stream speed से अधिक हो।

---

## 26.3 :icon-formula: दूरी और समय

Downstream या upstream की effective speed मिलने के बाद Chapter 24 का मूल सूत्र लगाइए:

$$D=S\times T,\qquad T=\frac{D}{S}$$

**उदाहरण 3.** एक नाव downstream $120$ km दूरी $15$ km/h की चाल से तय करती है। समय?

$$T=\frac{120}{15}=\mathbf{8}\text{ hours}$$

**उदाहरण 4.** वही नाव upstream $9$ km/h की चाल से $120$ km जाती है। समय?

$$T=\frac{120}{9}=\mathbf{13\frac{1}{3}}\text{ hours}$$

**उदाहरण 5.** शांत जल में boat speed $20$ km/h और current speed $5$ km/h है। $60$ km upstream जाने का समय?

Upstream speed $=20-5=15$ km/h।

$$T=\frac{60}{15}=\mathbf{4}\text{ hours}$$

> :icon-bulb: Boat questions में पहले effective speed लिखिए, फिर दूरी को उससे भाग दीजिए। Directly still-water speed से time निकालना सामान्य गलती है।

---

## 26.4 :icon-steps: प्रकार-वार हल किए उदाहरण

### :icon-calc: प्रकार 1 — downstream और upstream का round trip

एक ही दूरी downstream और upstream तय की जाए, तो दोनों legs के समय जोड़िए।

```figure
type: round-trip
distance: 120
down: 15
up: 9
caption: समान दूरी पर downstream और upstream समय जोड़कर total time मिलता है
```

**उदाहरण 6.** नाव $120$ km downstream $15$ km/h और वापस upstream $9$ km/h से जाती है। कुल समय?

- downstream time $=120/15=8$ घंटे
- upstream time $=120/9=13\frac{1}{3}$ घंटे

कुल समय $=\mathbf{21\frac{1}{3}}$ घंटे।

कुल distance $=240$ km, इसलिए average speed —

$$\text{average speed}=\frac{240}{21\frac{1}{3}}=\mathbf{11\frac{1}{4}}\text{ km/h}$$

समान दूरी के लिए shortcut —

$$\text{average speed}=\frac{2DU}{D+U}$$

जहाँ $D$ downstream और $U$ upstream speed हैं।

### :icon-divide: प्रकार 2 — boat और stream speed निकालना

**उदाहरण 7.** एक नाव downstream $18$ km/h और upstream $10$ km/h से चलती है।

- still-water boat speed $=(18+10)/2=\mathbf{14}$ km/h
- stream speed $=(18-10)/2=\mathbf{4}$ km/h

```figure
type: boat-data
down: 18
up: 10
caption: दो effective speeds का योग boat speed और अन्तर stream speed देता है
```

**उदाहरण 8.** Downstream speed upstream speed की $3/2$ गुनी है और stream speed $4$ km/h है। boat speed?

मान लें upstream speed $=2x$, downstream $=3x$।

$$\frac{D-U}{2}=\frac{3x-2x}{2}=4\quad\Rightarrow\quad x=8$$

अतः upstream $=16$, downstream $=24$ और boat speed —

$$b=\frac{24+16}{2}=\mathbf{20}\text{ km/h}$$

### :icon-chart: प्रकार 3 — raft या floating object

Floating object की अपनी कोई चाल नहीं होती। वह पानी के साथ current speed से बहता है।

```figure
type: floating-object
current: 4
distance: 120
caption: raft या floating object stream की चाल से ही आगे बढ़ता है
```

**उदाहरण 9.** धारा की चाल $4$ km/h है। एक raft $120$ km कितने समय में बहेगा?

$$T=\frac{120}{4}=\mathbf{30}\text{ hours}$$

**उदाहरण 10.** एक floating log $3$ घंटे में $18$ km बहता है। stream speed?

$$s=\frac{18}{3}=\mathbf{6}\text{ km/h}$$

> :icon-key: Raft के लिए still-water boat speed $0$ है; downstream speed सिर्फ stream speed होगी।

### :icon-timer: प्रकार 4 — समय का अन्तर

समान दूरी $d$ के लिए downstream और upstream समय का अन्तर —

$$\Delta T=\frac{d}{b-s}-\frac{d}{b+s}$$

**उदाहरण 11.** नाव की still-water speed $12$ km/h और current $3$ km/h है। $120$ km downstream और upstream समय का अन्तर?

- downstream time $=120/15=8$ घंटे
- upstream time $=120/9=13\frac{1}{3}$ घंटे

अन्तर $=\mathbf{5\frac{1}{3}}$ घंटे।

**उदाहरण 12.** एक boat $30$ km downstream $2$ घंटे और वही दूरी upstream $3$ घंटे में तय करती है। boat और stream speed?

- downstream speed $=30/2=15$ km/h
- upstream speed $=30/3=10$ km/h
- boat speed $=(15+10)/2=\mathbf{12.5}$ km/h
- stream speed $=(15-10)/2=\mathbf{2.5}$ km/h

### :icon-ruler: प्रकार 5 — speed ratio और stream ratio

यदि boat की still-water speed और stream speed का ratio दिया हो, तो सीधे मान लेकर downstream/upstream निकालिए।

**उदाहरण 13.** Boat speed : stream speed $=3:1$ है। Downstream और upstream speed का ratio?

मान लें boat $=3x$, stream $=x$।

- downstream $=4x$
- upstream $=2x$

अतः ratio $=\mathbf{2:1}$।

**उदाहरण 14.** Boat speed stream speed की $4$ गुनी है और stream $3$ km/h है।

- boat speed $=12$ km/h
- downstream $=15$ km/h
- upstream $=9$ km/h

### :icon-brain: प्रकार 6 — दो boats का मिलना

यदि नदी की दिशा के अनुसार एक boat downstream और दूसरी upstream एक-दूसरे की ओर चलें, तो उनके बीच gap relative speed से घटेगा।

```figure
type: meeting-boats
distance: 120
down: 15
up: 9
caption: downstream और upstream दिशा में आती boats का relative speed योग होता है
```

**उदाहरण 15.** दो points के बीच नदी की दूरी $120$ km है। एक boat downstream $15$ km/h और दूसरी upstream $9$ km/h से एक-दूसरे की ओर चलती हैं। meeting time?

Relative speed $=15+9=24$ km/h।

$$T=\frac{120}{24}=\mathbf{5}\text{ hours}$$

**उदाहरण 16.** दो boats एक ही दिशा में चलती हैं। तेज boat की speed $18$ km/h और धीमी की $12$ km/h है; gap $30$ km है। catch-up time?

$$T=\frac{30}{18-12}=\mathbf{5}\text{ hours}$$

### :icon-list: प्रकार 7 — total journey time

**उदाहरण 17.** Boat speed in still water $15$ km/h और current $3$ km/h है। $60$ km downstream और वापस upstream जाने में total time?

- downstream speed $=18$, time $=60/18=3\frac{1}{3}$ घंटे
- upstream speed $=12$, time $=60/12=5$ घंटे

कुल समय $=\mathbf{8\frac{1}{3}}$ घंटे।

**उदाहरण 18.** Boat $90$ km downstream और $90$ km upstream जाती है। downstream speed $18$ और upstream speed $12$ km/h हैं।

$$T=\frac{90}{18}+\frac{90}{12}=5+7.5=\mathbf{12.5}\text{ hours}$$

### :icon-star: प्रकार 8 — given total time से दूरी

**उदाहरण 19.** Boat speed $15$ km/h और stream speed $3$ km/h है। downstream और upstream बराबर दूरी तय करने में total time $10$ घंटे है। प्रत्येक दिशा की दूरी?

Effective speeds $18$ और $12$ km/h। यदि प्रत्येक दूरी $d$ हो —

$$\frac{d}{18}+\frac{d}{12}=10$$

$$d\left(\frac{2+3}{36}\right)=10\quad\Rightarrow\quad d\times\frac{5}{36}=10$$

अतः $d=\mathbf{72}$ km।

### :icon-steps: प्रकार 9 — वापस आने का समय

**उदाहरण 20.** Boat की still-water speed $20$ km/h और stream $5$ km/h है। Boat $75$ km downstream जाकर वापस उसी point पर आती है। कुल समय?

- downstream speed $=25$, समय $=75/25=3$ घंटे
- upstream speed $=15$, समय $=75/15=5$ घंटे
- कुल $=\mathbf{8}$ घंटे

---

## 26.5 :icon-bulb: शॉर्टकट व उनके प्रमाण

### :icon-timer: शॉर्टकट 1 — four basic formulas

$$S_d=b+s$$

$$S_u=b-s$$

$$b=\frac{S_d+S_u}{2}$$

$$s=\frac{S_d-S_u}{2}$$

यहाँ $S_d$ downstream और $S_u$ upstream speed हैं; इन्हें distance $D$ से अलग समझिए।

### :icon-timer: शॉर्टकट 2 — round-trip average

समान दूरी downstream speed $D$ और upstream speed $U$ पर —

$$\bar S=\frac{2DU}{D+U}$$

**प्रमाण:** समान दूरी $d$ के लिए total distance $2d$ और total time $d/D+d/U$।

### :icon-timer: शॉर्टकट 3 — same distance time ratio

एक ही दूरी पर —

$$T_{down}:T_{up}=U:D$$

यदि downstream $15$ और upstream $9$ हो, तो time ratio $=9:15=3:5$।

### :icon-timer: शॉर्टकट 4 — stream को cancel करना

यदि boat downstream जाकर upstream वापस आती है, तो —

$$T=\frac{d}{b+s}+\frac{d}{b-s}$$

दोनों fractions जोड़ने पर —

$$T=\frac{2bd}{b^2-s^2}$$

इससे round trip में stream के प्रभाव को जल्दी जाँचा जा सकता है।

### :icon-timer: शॉर्टकट 5 — raft

Floating object:

$$S_{raft}=s$$

इसलिए $d$ दूरी के लिए —

$$T=\frac{d}{s}$$

### :icon-timer: शॉर्टकट 6 — ratio method

Boat : stream $=m:n$ हो, तो boat $=mx$, stream $=nx$ मानिए।

- downstream $=(m+n)x$
- upstream $=(m-n)x$

यदि boat speed stream से $k$ गुनी हो, तो boat $=kx$, stream $=x$ रखिए।

### :icon-timer: शॉर्टकट 7 — meeting/catch-up

दो boats की effective speeds $v_1,v_2$ और separation $d$ हो —

$$T=\frac{d}{v_1+v_2}\quad\text{(towards each other)}$$

$$T=\frac{d}{|v_1-v_2|}\quad\text{(same direction)}$$

---

## 26.6 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Downstream में stream speed घटाना।
> Flow की दिशा में boat को धारा मदद करती है: $b+s$।

> :icon-cross: **जाल 2.** Upstream में speeds जोड़ना।
> धारा के विरुद्ध जाने पर $b-s$ लगेगा।

> :icon-cross: **जाल 3.** Downstream और upstream speeds का साधारण average लेना।
> Equal-distance round trip में $2DU/(D+U)$ लगेगा।

> :icon-cross: **जाल 4.** Raft को boat की still-water speed देना।
> Floating object stream के साथ $s$ speed से चलता है।

> :icon-cross: **जाल 5.** Downstream और upstream की समान दूरी के लिए equal time मान लेना।
> Downstream तेज है, इसलिए उसका समय कम होगा।

> :icon-cross: **जाल 6.** Effective speed की जगह still-water speed से time निकालना।
> पहले $b+s$ या $b-s$ निकालिए।

> :icon-cross: **जाल 7.** Meeting boats में relative speed घटाना जबकि वे आमने-सामने हों।
> Opposite direction में relative speeds जुड़ती हैं।

> :icon-cross: **जाल 8.** Boat speed stream speed से कम या बराबर दे देना।
> तब upstream motion सम्भव नहीं होगा; प्रश्न में सामान्यतः $b>s$ होगा।

> :icon-cross: **जाल 9.** Speed units को दूरी और समय units से न मिलाना।
> km के साथ km/h, metre के साथ m/s रखिए।

---

## 26.7 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* Boat speed $12$ km/h, stream $3$ km/h। downstream और upstream?

**हल:** $\mathbf{15}$ और $\mathbf{9}$ km/h।

**PYQ 2.** *(SSC CHSL)* Downstream speed $15$ और upstream $9$ km/h। boat और stream speed?

**हल:** boat $\mathbf{12}$, stream $\mathbf{3}$ km/h।

**PYQ 3.** *(RRB NTPC)* Boat $120$ km downstream $15$ और upstream $9$ km/h। total time?

**हल:** $8+13\frac{1}{3}=\mathbf{21\frac{1}{3}}$ घंटे।

**PYQ 4.** *(IBPS Clerk)* Boat downstream $18$ और upstream $10$ km/h। still-water और stream speed?

**हल:** $\mathbf{14}$ और $\mathbf{4}$ km/h।

**PYQ 5.** *(UP Police SI)* Stream $4$ km/h; raft $120$ km बहती है। time?

**हल:** $120/4=\mathbf{30}$ घंटे।

**PYQ 6.** *(SSC MTS)* दो boats $120$ km gap पर $15$ और $9$ km/h से आमने-सामने। meeting time?

**हल:** relative $24$ km/h ⟹ $\mathbf{5}$ घंटे।

---

## 26.8 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | boat $12$, stream $3$ km/h | down $15$, up $9$ | $b\pm s$ |
| 2 | down $15$, up $9$ km/h | boat $12$, stream $3$ | sum/difference half |
| 3 | $120$ km downstream at $15$ | $8$ घंटे | $D/S$ |
| 4 | $120$ km upstream at $9$ | $13\frac{1}{3}$ घंटे | $D/S$ |
| 5 | down $18$, up $10$ | boat $14$, stream $4$ | formulas |
| 6 | boat $20$, stream $5$ | down $25$, up $15$ | $b\pm s$ |
| 7 | $120$ km each way; down $15$, up $9$ | $21\frac{1}{3}$ घंटे | times जोड़ें |
| 8 | equal distance at $15$ and $9$ | $11\frac{1}{4}$ km/h | harmonic average |
| 9 | raft, current $4$, distance $120$ | $30$ घंटे | raft speed $=s$ |
| 10 | boat $20$, stream $5$; $60$ km up | $4$ घंटे | upstream $15$ |
| 11 | $90$ km each way; down $18$, up $12$ | $12.5$ घंटे | $5+7.5$ |
| 12 | down/up $15,10$; distance $30$ | boat $12.5$, stream $2.5$ | $D/S$ then half |
| 13 | boat:stream $3:1$ | down:up $2:1$ | $4x:2x$ |
| 14 | stream $3$, boat $4$ times stream | down $15$, up $9$ | boat $12$ |
| 15 | $60$ km each way; down $18$, up $10$ | $9\frac{1}{3}$ घंटे | $10/3+6$ |
| 16 | $120$ km; down $15$, up $9$ | time difference $5\frac{1}{3}$ घंटे | $13\frac{1}{3}-8$ |
| 17 | $30$ km: down $2$ h, up $3$ h | boat $12.5$, stream $2.5$ | speeds $15,10$ |
| 18 | raft current $4$, distance $80$ | $20$ घंटे | $80/4$ |
| 19 | boats gap $120$, speeds down $15$, up $9$ | $5$ घंटे | relative $24$ |
| 20 | boat:stream $3:1$ | down $4x$, up $2x$ | ratio method |
| 21 | boat is $4$ times stream; stream $3$ | boat $12$, down $15$, up $9$ | ratio |
| 22 | upstream $8$, stream $2$ | boat $10$, down $12$ | add/subtract |
| 23 | $48$ km down at $16$, boat $12$, stream $4$ | total $9$ घंटे | up $8$ |
| 24 | boat $15$, stream $3$; equal distance each way total $10$ h | each $72$ km | equation in $d$ |
| 25 | equal distance; down time $4$ h, up time $6$ h, distance $120$ km | boat $25$, stream $5$ | speeds $30,20$ |

---

## 26.9 :icon-trophy: अध्याय का सार

```
━━━ मूल speed formulas ━━━
boat speed in still water = b
stream speed = s

downstream = b + s
upstream = b − s

यदि downstream D और upstream U दिए हों:
boat = (D+U)/2
stream = (D−U)/2

D=15, U=9
boat = 12, stream = 3

━━━ दूरी और समय ━━━
T = distance / effective speed
120 km downstream at 15 → 8 h
120 km upstream at 9 → 13 1/3 h

━━━ Round trip ━━━
equal distance average = 2DU/(D+U)
15 और 9 → 11 1/4 km/h

━━━ Raft ━━━
floating object speed = stream speed
120 km at stream 4 → 30 h

━━━ Ratio ━━━
boat:stream = 3:1
boat = 3x, stream = x
down = 4x, up = 2x

a boat k times stream:
boat=kx, stream=x
down=(k+1)x, up=(k−1)x

━━━ Meeting boats ━━━
towards each other → relative speeds add
same direction → speeds subtract
T = separation / relative speed

━━━ जाल ━━━
downstream में जोड़ना है
upstream में घटाना है
raft की own speed zero
round trip में साधारण average नहीं
पहले effective speed, फिर D/S
units मिलाइए
```

> :icon-trophy: **भाग 3 पूर्ण।** अध्याय 21 से 26 तक समय, कार्य, मजदूरी, चाल, दूरी, trains और boats की पूरी rate-based नींव तैयार है।
>
> **आगे:** अध्याय 27 — **बीजगणित की नींव व बहुपद (Algebra Foundations & Polynomials)**। अब arithmetic rates के बाद algebraic expressions और equations की व्यवस्थित शुरुआत होगी।
