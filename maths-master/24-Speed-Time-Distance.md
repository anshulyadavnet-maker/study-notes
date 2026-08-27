# अध्याय 24 — चाल, समय व दूरी (Speed, Time & Distance)

## 24.1 :icon-target: परिचय व वेटेज

अध्याय 21 में हमने काम को दर और समय से जोड़ा था। चाल, समय व दूरी में भी वही विचार चलता है — यहाँ कार्य-दर की जगह **चाल** है और काम की जगह **दूरी**।

> *"एक car 60 km/h की चाल से 2.5 घंटे चले तो कितनी दूरी तय करेगी?"*

सिर्फ एक सूत्र पूरे अध्याय की नींव है:

$$\text{distance}=\text{speed}\times\text{time}$$

दूरी, चाल और समय की units सही रख ली जाएँ तो प्रश्न सीधा हो जाता है। इसके बाद average speed, relative speed, meeting, catch-up और trains जैसे प्रकार उसी सूत्र के विस्तार हैं।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | चाल–समय, relative speed |
| **SSC CGL Tier-2** | **2–3** | average speed, trains |
| SSC CHSL / MTS / GD | 1–2 | conversion और direct formula |
| **SSC CPO** | **2** | relative speed और train crossing |
| **IBPS / SBI PO** | **2–3** | average speed, catch-up |
| IBPS / SBI Clerk | 1–2 | सरल TSD |
| **RRB NTPC / ALP** | **2–3** | train, meeting, speed ratio |
| UP Police SI / Constable | 1–2 | basic speed questions |
| UPSSSC PET | 1 | चाल और समय |
| Super TET / UPTET | 1 | ऐकिक नियम आधारित |

> :icon-key: **पूरे अध्याय का एक वाक्य:** $D=S\times T$; इसलिए $S=D/T$ और $T=D/S$।

---

## 24.2 :icon-number: मूल अवधारणा — दूरी, चाल और समय

तीन राशियों का सम्बन्ध —

$$\text{distance}=\text{speed}\times\text{time}$$

या —

$$D=S\times T,\qquad S=\frac{D}{T},\qquad T=\frac{D}{S}$$

```figure
type: distance-triangle
distance: 150
speed: 60
caption: D ऊपर और S, T नीचे — जिस राशि को निकालना हो उसे ढककर formula याद रखें
```

| पूछा गया | सूत्र |
|---|---|
| दूरी | $D=S\times T$ |
| चाल | $S=D/T$ |
| समय | $T=D/S$ |

**उदाहरण 1.** एक car $60$ km/h की चाल से $2.5$ घंटे चले। दूरी?

$$D=60\times2.5=\mathbf{150}\text{ km}$$

**उदाहरण 2.** एक bus $240$ km दूरी $60$ km/h की चाल से तय करती है। समय?

$$T=\frac{240}{60}=\mathbf{4}\text{ hours}$$

**उदाहरण 3.** एक cyclist $3$ घंटे में $45$ km जाता है। चाल?

$$S=\frac{45}{3}=\mathbf{15}\text{ km/h}$$

> :icon-bulb: दूरी और चाल की unit एक-दूसरे से मेल खानी चाहिए। km और hour के साथ km/h, metre और second के साथ m/s रखिए।

### :icon-star: चाल का अर्थ

$60$ km/h का अर्थ है — समान चाल पर $1$ घंटे में $60$ km, $30$ मिनट में $30$ km और $15$ मिनट में $15$ km।

यदि चाल बदलती है, तो हर हिस्से की दूरी अलग निकालिए और अन्त में कुल दूरी/कुल समय से average speed निकालिए।

---

## 24.3 :icon-ruler: Unit conversion और speed ratio

Competitive exams में सबसे जरूरी conversion —

$$1\text{ km}=1000\text{ m},\qquad 1\text{ hour}=3600\text{ s}$$

इसलिए —

$$1\text{ km/h}=\frac{1000}{3600}=\frac{5}{18}\text{ m/s}$$

और —

$$1\text{ m/s}=\frac{18}{5}\text{ km/h}$$

```figure
type: unit-conversion
kmh: 72
ms: 15
caption: km/h से m/s में 5/18 और m/s से km/h में 18/5 गुणा कीजिए
```

**उदाहरण 4.** $72$ km/h को m/s में बदलें।

$$72\times\frac{5}{18}=\mathbf{20}\text{ m/s}$$

**उदाहरण 5.** $15$ m/s को km/h में बदलें।

$$15\times\frac{18}{5}=\mathbf{54}\text{ km/h}$$

### चाल और समय का अनुपात

समान दूरी के लिए चाल और समय व्युत्क्रमानुपाती हैं।

$$S_1:S_2=T_2:T_1$$

**उदाहरण 6.** किसी समान दूरी को A और B क्रमशः $3:4$ की चाल के अनुपात में तय करते हैं। उनके समय का अनुपात?

$$T_A:T_B=4:3$$

समान समय में दूरी चाल के समान अनुपात में होगी:

$$D_1:D_2=S_1:S_2$$

> :icon-warn: $72$ km/h को सीधे $72$ m/s मत लिखिए। पहले $5/18$ लगाइए; $72$ km/h वास्तव में $20$ m/s है।

---

## 24.4 :icon-steps: प्रकार-वार हल किए उदाहरण

### :icon-calc: प्रकार 1 — औसत चाल

औसत चाल का मूल सूत्र —

$$\text{average speed}=\frac{\text{total distance}}{\text{total time}}$$

यह **total distance ÷ total time** है, चालों का साधारण average नहीं।

```figure
type: average-speed
u: 40
v: 60
distance: 120
caption: समान दूरी पर average speed harmonic form 2uv/(u+v) होती है
```

**उदाहरण 7 — समान दूरी।** एक व्यक्ति $120$ km दूरी $40$ km/h और अगली $120$ km दूरी $60$ km/h से तय करता है। औसत चाल?

- कुल दूरी $=240$ km
- समय $=120/40+120/60=3+2=5$ घंटे

$$\text{average}=\frac{240}{5}=\mathbf{48}\text{ km/h}$$

समान दूरी के लिए shortcut —

$$\text{average speed}=\frac{2uv}{u+v}$$

**उदाहरण 8 — समान समय।** कोई व्यक्ति आधे समय $40$ km/h और आधे समय $60$ km/h से चले। औसत चाल?

समान समय में साधारण average चलेगा:

$$\text{average}=\frac{40+60}{2}=\mathbf{50}\text{ km/h}$$

**उदाहरण 9 — अलग-अलग दूरी।** एक bus $120$ km को $40$ km/h और $180$ km को $60$ km/h से तय करती है। औसत चाल?

- कुल दूरी $=300$ km
- कुल समय $=120/40+180/60=3+3=6$ घंटे

$$\text{average}=\frac{300}{6}=\mathbf{50}\text{ km/h}$$

> :icon-key: समान दूरी में harmonic formula, समान समय में arithmetic average, और सामान्य प्रश्न में total distance/total time लगाइए।

### :icon-divide: प्रकार 2 — Relative speed

दो वस्तुओं की relative speed दिशा पर निर्भर करती है:

- विपरीत दिशाओं में: speeds **जोड़ें**
- एक ही दिशा में: speeds का **अन्तर** लें

```figure
type: relative-speed
s1: 45
s2: 55
direction: opposite
caption: विपरीत दिशा में relative speed = speeds का योग
```

**उदाहरण 10 — विपरीत दिशाएँ।** दो व्यक्ति $45$ km/h और $55$ km/h से एक-दूसरे की ओर चल रहे हैं। उनके बीच $600$ m दूरी है। मिलने का समय?

- relative speed $=45+55=100$ km/h
- $100$ km/h $=100\times5/18=250/9$ m/s

$$T=\frac{600}{250/9}=\mathbf{\frac{108}{5}}\text{ s}=21.6\text{ s}$$

**उदाहरण 11 — एक ही दिशा।** A की चाल $72$ km/h और B की $54$ km/h है। A, B से $270$ km पीछे है। A कितने समय में पकड़ेगा?

- relative speed $=72-54=18$ km/h
- समय $=270/18=\mathbf{15}$ घंटे

**उदाहरण 12.** दो trains विपरीत दिशाओं में $54$ और $36$ km/h से चल रही हैं। Relative speed?

$$54+36=90\text{ km/h}=\mathbf{25\text{ m/s}}$$

> :icon-bulb: “एक-दूसरे की ओर” दिखे तो add; “पीछा कर रहा है” या “same direction” दिखे तो subtract।

### :icon-chart: प्रकार 3 — Meeting और catch-up

Meeting में प्रारम्भिक दूरी relative speed से घटती है। Catch-up में आगे चल रहे व्यक्ति की lead भी वही दूरी है।

```figure
type: catch-up
lead: 30
fast: 60
slow: 45
caption: initial lead को relative speed से divide करने पर catch-up time मिलता है
```

**उदाहरण 13.** एक bus $45$ km/h से चल रही है। $30$ km पीछे से car $60$ km/h पर शुरू होती है। car कितने घंटे में bus को पकड़ेगी?

$$\text{relative speed}=60-45=15\text{ km/h}$$

$$T=\frac{30}{15}=\mathbf{2}\text{ hours}$$

**उदाहरण 14.** दो towns के बीच दूरी $420$ km है। दो buses $60$ और $80$ km/h से आमने-सामने चलती हैं। मिलने का समय?

$$T=\frac{420}{60+80}=\frac{420}{140}=\mathbf{3}\text{ hours}$$

पहली bus की meeting तक दूरी $=60\times3=180$ km और दूसरी की $=240$ km; योग $420$ km।

### :icon-timer: प्रकार 4 — चाल बदलने पर समय का अन्तर

यदि समान दूरी को $u$ और $v$ चाल से तय करने पर समय का अन्तर $t$ हो, तो —

$$D\left(\frac{1}{u}-\frac{1}{v}\right)=t$$

**उदाहरण 15.** कोई व्यक्ति $5$ km/h से चले तो $12$ मिनट late और $6$ km/h से चले तो $10$ मिनट early पहुँचता है। दूरी?

दोनों समय का अन्तर $=12+10=22$ मिनट $=22/60=11/30$ घंटे।

$$D\left(\frac{1}{5}-\frac{1}{6}\right)=\frac{11}{30}$$

$$D\times\frac{1}{30}=\frac{11}{30}\quad\Rightarrow\quad D=\mathbf{11}\text{ km}$$

**उदाहरण 16.** चाल $40$ km/h से दूरी तय करने में $30$ मिनट अधिक लगते हैं, जबकि $50$ km/h पर समय कम है। दूरी?

$$D\left(\frac{1}{40}-\frac{1}{50}\right)=\frac{1}{2}$$

$$D\times\frac{1}{200}=\frac{1}{2}\quad\Rightarrow\quad D=\mathbf{100}\text{ km}$$

### :icon-number: प्रकार 5 — चाल में प्रतिशत परिवर्तन

समान दूरी के लिए समय चाल के व्युत्क्रम में बदलता है। यदि चाल $p\%$ बढ़े, तो नया समय —

$$T_2=T_1\times\frac{100}{100+p}$$

और समय में कमी —

$$\frac{p}{100+p}\times100\%$$

**उदाहरण 17.** चाल $20\%$ बढ़ा दी जाए तो समान दूरी के लिए समय कितने प्रतिशत घटेगा?

$$\text{time decrease}=\frac{20}{120}\times100=\mathbf{16\frac{2}{3}\%}$$

**उदाहरण 18.** किसी journey में चाल $25\%$ घट जाती है। समय में कितने प्रतिशत वृद्धि होगी?

नई चाल $=75\%$।

$$\text{time increase}=\frac{100}{75}-1=\frac{1}{3}=\mathbf{33\frac{1}{3}\%}$$

### :icon-ruler: प्रकार 6 — circular track और races

Circular track पर —

- विपरीत दिशा में पहली meeting time $=\text{track length}/(u+v)$
- समान दिशा में catch-up time $=\text{track length}/(u-v)$
- एक lap पूरा करने का समय $=\text{track length}/\text{speed}$

**उदाहरण 19.** $400$ m circular track पर दो runners $8$ m/s और $6$ m/s से विपरीत दिशा में दौड़ते हैं। पहली बार कब मिलेंगे?

$$T=\frac{400}{8+6}=\frac{400}{14}=\mathbf{\frac{200}{7}}\text{ s}$$

**उदाहरण 20.** उसी track पर दोनों same direction में दौड़ें, तो faster runner कितने समय में एक lap से catch करेगा?

$$T=\frac{400}{8-6}=\mathbf{200}\text{ s}$$

### :icon-steps: प्रकार 7 — मिश्रित journey

**उदाहरण 21.** एक car कुल $300$ km चलती है। पहले $100$ km $50$ km/h और अगले $200$ km $100$ km/h से। औसत चाल?

- पहला समय $=100/50=2$ घंटे
- दूसरा समय $=200/100=2$ घंटे
- कुल दूरी $=300$ km, कुल समय $=4$ घंटे

$$\text{average speed}=\frac{300}{4}=\mathbf{75}\text{ km/h}$$

> :icon-warn: अलग-अलग हिस्सों की चालों का average $((50+100)/2=75)$ यहाँ संयोग से सही आया; सामान्यतः total distance/total time ही भरोसेमंद विधि है।

---

## 24.5 :icon-bulb: शॉर्टकट व उनके प्रमाण

### :icon-timer: शॉर्टकट 1 — D-S-T triangle

$$D=S\times T,\qquad S=D/T,\qquad T=D/S$$

एक ही relation से तीनों प्रकार हल हो जाते हैं।

### :icon-timer: शॉर्टकट 2 — km/h और m/s

$$\text{km/h}\to\text{m/s}:\times\frac{5}{18}$$

$$\text{m/s}\to\text{km/h}:\times\frac{18}{5}$$

$54$ km/h $=15$ m/s और $90$ km/h $=25$ m/s जैसे मान याद रखना उपयोगी है।

### :icon-timer: शॉर्टकट 3 — average speed

समान दूरी $u,v$ पर —

$$\bar S=\frac{2uv}{u+v}$$

**प्रमाण:** दूरी $d$ की दो यात्राओं के लिए कुल दूरी $2d$ और कुल समय $d/u+d/v$।

$$\bar S=\frac{2d}{d/u+d/v}=\frac{2uv}{u+v}$$

### :icon-timer: शॉर्टकट 4 — relative speed

$$S_{relative}=u+v\quad\text{(opposite)}$$

$$S_{relative}=|u-v|\quad\text{(same direction)}$$

फिर —

$$T=\frac{\text{initial separation}}{S_{relative}}$$

### :icon-timer: शॉर्टकट 5 — train crossing

Train की लंबाई $L$ m और speed $v$ m/s हो —

- pole/person: $T=L/v$
- platform की लंबाई $P$: $T=(L+P)/v$
- दूसरी train की लंबाई $L_2$: $T=(L+L_2)/v_{relative}$

```figure
type: train-crossing
train: 180
platform: 250
speed_kmh: 72
caption: platform पार करने में train और platform दोनों की लंबाई तय होती है
```

**अगले अध्याय में** train crossing के सभी प्रकार विस्तार से आएँगे।

### :icon-timer: शॉर्टकट 6 — speed percentage

समान दूरी पर speed ratio और time ratio उल्टे होते हैं:

$$S_1:S_2=m:n\quad\Rightarrow\quad T_1:T_2=n:m$$

Speed $p\%$ बढ़े:

$$\text{time decrease}=\frac{p}{100+p}\times100\%$$

Speed $p\%$ घटे:

$$\text{time increase}=\frac{p}{100-p}\times100\%$$

### :icon-timer: शॉर्टकट 7 — late/early

यदि $u$ चाल पर $a$ समय late और $v$ चाल पर $b$ समय early हो, तो —

$$D\left(\frac{1}{u}-\frac{1}{v}\right)=a+b$$

दोनों समय एक ही unit में बदलिए।

---

## 24.6 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** km/h और m/s को बिना conversion के साथ इस्तेमाल करना।
> Distance metre और time seconds हों तो speed m/s में रखिए।

> :icon-cross: **जाल 2.** समान दूरी की चालों का साधारण average लेना।
> सही formula $2uv/(u+v)$ है।

> :icon-cross: **जाल 3.** Relative speed में दिशा भूलना।
> Opposite में add, same direction में subtract।

> :icon-cross: **जाल 4.** Train और platform crossing में केवल train length लेना।
> Platform पार करने के लिए $L+P$ distance तय होती है।

> :icon-cross: **जाल 5.** pole/person की length जोड़ना।
> Pole की length zero मानी जाती है; distance केवल train length है।

> :icon-cross: **जाल 6.** catch-up में slower speed से divide करना।
> Lead को relative speed से divide करना है।

> :icon-cross: **जाल 7.** speed $20\%$ बढ़ने पर time भी $20\%$ घटा देना।
> Time inverse है; $20\%$ speed increase पर time reduction $16\frac{2}{3}\%$ होती है।

> :icon-cross: **जाल 8.** late और early का अन्तर लेना।
> Scheduled time के दोनों ओर होने पर total difference $=$ late $+$ early।

> :icon-cross: **जाल 9.** circular track में opposite और same direction को एक जैसा मानना।
> Opposite में track length को sum speed से, same में difference speed से भाग दें।

---

## 24.7 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* $72$ km/h को m/s में बदलें।

**हल:** $72\times5/18=\mathbf{20}$ m/s।

**PYQ 2.** *(SSC CHSL)* समान दूरी $40$ और $60$ km/h से तय की गई। औसत चाल?

**हल:** $2\times40\times60/(40+60)=\mathbf{48}$ km/h।

**PYQ 3.** *(RRB NTPC)* दो व्यक्ति $45$ और $55$ km/h से आमने-सामने हैं; दूरी $600$ m। समय?

**हल:** relative $=100$ km/h $=250/9$ m/s; समय $=\mathbf{21.6}$ s।

**PYQ 4.** *(IBPS Clerk)* bus $45$ km/h और car $60$ km/h, lead $30$ km। catch-up time?

**हल:** relative $15$ km/h; time $=\mathbf{2}$ घंटे।

**PYQ 5.** *(SSC CPO)* $5$ km/h पर $12$ min late और $6$ km/h पर $10$ min early। दूरी?

**हल:** $D(1/5-1/6)=22/60$ ⟹ $\mathbf{11}$ km।

**PYQ 6.** *(UP Police SI)* $400$ m track पर $8$ और $6$ m/s opposite direction। पहली meeting?

**हल:** $400/(8+6)=\mathbf{200/7}$ s।

---

## 24.8 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | $60$ km/h, $2.5$ घंटे | $150$ km | $S\times T$ |
| 2 | $240$ km at $60$ km/h | $4$ घंटे | $D/S$ |
| 3 | $72$ km/h in m/s | $20$ m/s | $\times5/18$ |
| 4 | $15$ m/s in km/h | $54$ km/h | $\times18/5$ |
| 5 | speed ratio $3:4$, same distance | time $4:3$ | inverse |
| 6 | $100$ km at $40$, $100$ at $60$ | $48$ km/h | equal-distance average |
| 7 | equal time at $40$ and $60$ | $50$ km/h | arithmetic average |
| 8 | $120$ km at $40$, $180$ at $60$ | $50$ km/h | total $D/T$ |
| 9 | opposite $45,55$ km/h; $600$ m | $21.6$ s | relative sum |
| 10 | $72,54$ km/h; lead $270$ km | $15$ घंटे | relative difference |
| 11 | train $180$ m at $54$ km/h; pole | $12$ s | $180/15$ |
| 12 | train $150$ m + platform $250$ m at $72$ km/h | $20$ s | $400/20$ |
| 13 | trains $120,180$ m; speeds $54,36$ opposite | $12$ s | $300/25$ |
| 14 | $400$ m track; $8,6$ m/s opposite | $200/7$ s | sum speed |
| 15 | lead $30$ km; speeds $60,45$ | $2$ घंटे | $30/15$ |
| 16 | $5$ km/h: 12 min late; $6$: 10 min early | $11$ km | late + early |
| 17 | speed increases $20\%$ | time decreases $16\frac{2}{3}\%$ | $20/120$ |
| 18 | speed ratio $5:4$, same distance | time $4:5$ | inverse ratio |
| 19 | $100$ km at $50$, $200$ at $100$ | $75$ km/h | $300/4$ |
| 20 | half distance at $30$, half at $60$ | $40$ km/h | $2uv/(u+v)$ |
| 21 | $180$ m separation; $90,72$ km/h same direction | $36$ s | relative $18$ km/h |
| 22 | trains $200,100$ m; $36,54$ opposite | $12$ s | $300/25$ |
| 23 | $300$ km at $60$ and $90$ for equal times | $75$ km/h | equal-time average |
| 24 | $180$ km: $60$ at $30$, $120$ at $60$ | $45$ km/h | total $D/T$ |
| 25 | $40$ km/h takes 30 min more than $50$ km/h | $100$ km | time difference |

---

## 24.9 :icon-trophy: अध्याय का सार

```
━━━ मूल सूत्र ━━━
D = S × T
S = D/T
T = D/S

━━━ Conversion ━━━
km/h → m/s : × 5/18
m/s → km/h : × 18/5
72 km/h = 20 m/s
54 km/h = 15 m/s
90 km/h = 25 m/s

━━━ Ratio ━━━
समान दूरी: speed ratio = inverse time ratio
S₁:S₂ = m:n → T₁:T₂ = n:m
समान समय: distance ratio = speed ratio

━━━ Average speed ━━━
औसत = total distance / total time
समान दूरी at u,v → 2uv/(u+v)
समान समय at u,v → (u+v)/2

40 और 60, समान दूरी → 48
40 और 60, समान समय → 50

━━━ Relative speed ━━━
opposite → u+v
same direction → |u−v|
meeting/catch-up time = separation / relative speed

━━━ Late/Early ━━━
D(1/u − 1/v) = late + early
5 और 6 km/h; 12 min late, 10 min early → D = 11 km

━━━ Percentage ━━━
speed p% बढ़े → time decrease = p/(100+p) × 100%
speed p% घटे → time increase = p/(100−p) × 100%

━━━ Circular track ━━━
opposite → track/(u+v)
same direction → track/(u−v)

━━━ Train foundation ━━━
pole: L/v
platform: (L+P)/v
next chapter में train questions का पूरा विस्तार

━━━ जाल ━━━
units पहले मिलाइए
समान दूरी पर साधारण average नहीं
relative direction देखिए
catch-up में relative speed
late + early
speed और time inverse
```

> :icon-trophy: **भाग 3 आगे बढ़ा।** चाल, समय और दूरी का आधार तैयार है।
>
> **आगे:** अध्याय 25 — **रेलगाड़ी सम्बन्धी प्रश्न (Problems on Trains)**। वहाँ train length, pole, platform और दो trains के crossing questions को इसी relative-speed आधार पर विस्तार से हल करेंगे।
