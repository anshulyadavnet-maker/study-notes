# अध्याय 25 — रेलगाड़ी सम्बन्धी प्रश्न (Problems on Trains)

## 25.1 :icon-target: परिचय व वेटेज

अध्याय 24 में हमने relative speed सीखी थी। Train problems उसी idea का सबसे महत्वपूर्ण प्रयोग हैं। जब train किसी pole, व्यक्ति, platform या दूसरी train को पार करती है, तो train का अगला सिरा और पिछला सिरा दोनों अपनी पूरी दूरी तय करते हैं।

> *"180 m लम्बी train 54 km/h की चाल से एक pole को कितने समय में पार करेगी?"*

Pole की लम्बाई शून्य है, इसलिए distance केवल train की length $180$ m होगी। लेकिन $54$ km/h को पहले $15$ m/s में बदलना पड़ेगा। समय $=180/15=12$ seconds।

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **SSC CGL Tier-1** | **1–2** | pole, platform, two trains |
| **SSC CGL Tier-2** | **2–3** | relative speed और unknown length |
| SSC CHSL / MTS / GD | 1–2 | fixed object crossing |
| **SSC CPO** | **2** | platform और overtaking |
| **IBPS / SBI PO** | 1–2 | moving person, two trains |
| IBPS / SBI Clerk | 1 | basic train length |
| **RRB NTPC / ALP** | **2–3** | train crossing का उच्च वेटेज |
| UP Police SI / Constable | 1–2 | pole और platform |
| UPSSSC PET | 1 | direct formula |
| Super TET / UPTET | 1 | relative speed application |

> :icon-key: **पूरे अध्याय का एक वाक्य:** train crossing में **समय = पार की जाने वाली कुल दूरी ÷ relative speed**।

---

## 25.2 :icon-number: मूल अवधारणा — train की length ही दूरी है

जब एक train किसी fixed pole को पार करती है, तो train का पिछला सिरा pole तक पहुँचने तक train अपनी पूरी length के बराबर चलती है।

$$\text{time}=\frac{\text{train length}}{\text{speed}}$$

```figure
type: train-pole
length: 180
speed_kmh: 54
caption: fixed pole के लिए crossing distance केवल train length होती है
```

**उदाहरण 1.** $180$ m train $54$ km/h की चाल से pole को कितने seconds में पार करेगी?

- $54$ km/h $=54\times5/18=15$ m/s
- दूरी $=180$ m

$$T=\frac{180}{15}=\mathbf{12}\text{ seconds}$$

**उदाहरण 2.** एक train $72$ km/h की चाल से pole को $15$ seconds में पार करती है। train की length?

$72$ km/h $=20$ m/s।

$$L=20\times15=\mathbf{300}\text{ m}$$

> :icon-bulb: Pole, tree, signal या stationary person की effective length $0$ होती है। इसलिए इन मामलों में train की length ही distance है।

### Train के दोनों सिरों को समझिए

- सामने का सिरा pole तक पहुँचता है: crossing शुरू
- पिछला सिरा pole को पार करता है: crossing समाप्त
- इस दौरान train ने अपनी पूरी length जितनी दूरी तय की

यही कारण है कि “train passes a pole” में platform की length नहीं जोड़ते।

---

## 25.3 :icon-ruler: Platform, bridge और tunnel

Platform, bridge या tunnel को पूरी तरह पार करने के लिए train को अपनी length के अतिरिक्त उस object की length भी तय करनी होती है।

$$\text{crossing distance}=L+P$$

जहाँ $L$ train की length और $P$ platform/bridge/tunnel की length है।

```figure
type: train-platform
length: 150
platform: 250
speed_kmh: 72
caption: platform पार करने के लिए train length और platform length दोनों जुड़ते हैं
```

**उदाहरण 3.** $150$ m train $250$ m platform को $72$ km/h से कितने समय में पार करेगी?

- कुल दूरी $=150+250=400$ m
- $72$ km/h $=20$ m/s

$$T=\frac{400}{20}=\mathbf{20}\text{ seconds}$$

**उदाहरण 4.** एक train $90$ km/h की चाल से $30$ seconds में $500$ m bridge पार करती है। train की length?

- $90$ km/h $=25$ m/s
- कुल distance $=25\times30=750$ m
- train length $=750-500=\mathbf{250}$ m

**उदाहरण 5.** $120$ m train $54$ km/h से एक platform को $20$ seconds में पार करती है। platform length?

- speed $=15$ m/s
- कुल दूरी $=15\times20=300$ m
- platform $=300-120=\mathbf{180}$ m

> :icon-key: Platform, bridge और tunnel की समस्या में पहले “कुल दूरी” लिखिए: $L+P$, $L+B$ या $L+T$।

---

## 25.4 :icon-steps: प्रकार-वार हल किए उदाहरण

### :icon-calc: प्रकार 1 — pole, tree या stationary person

**उदाहरण 6.** $240$ m train $72$ km/h से pole को पार करती है। समय?

$72$ km/h $=20$ m/s।

$$T=\frac{240}{20}=\mathbf{12}\text{ seconds}$$

**उदाहरण 7.** एक train pole को $8$ seconds में और $54$ km/h की चाल से पार करती है। length?

$54$ km/h $=15$ m/s।

$$L=15\times8=\mathbf{120}\text{ m}$$

### :icon-chart: प्रकार 2 — platform, bridge या tunnel

**उदाहरण 8.** $180$ m train $54$ km/h से $270$ m platform को पार करती है। समय?

- speed $=15$ m/s
- distance $=180+270=450$ m

$$T=\frac{450}{15}=\mathbf{30}\text{ seconds}$$

**उदाहरण 9.** $200$ m train $72$ km/h की चाल से $400$ m tunnel को पार करती है।

कुल दूरी $=200+400=600$ m और speed $=20$ m/s।

$$T=\frac{600}{20}=\mathbf{30}\text{ seconds}$$

### :icon-divide: प्रकार 3 — train की length और speed निकालना

यदि train pole को $t_1$ seconds और platform $P$ m को $t_2$ seconds में पार करती है, तो —

$$v=\frac{P}{t_2-t_1}$$

और —

$$L=v\times t_1$$

```figure
type: train-data
platform: 200
pole_seconds: 20
platform_seconds: 30
caption: pole और platform crossing times के अन्तर से speed, फिर train length निकालिए
```

**उदाहरण 10.** एक train pole को $20$ seconds और $200$ m platform को $30$ seconds में पार करती है। speed और length?

Platform के कारण अतिरिक्त दूरी $200$ m है और अतिरिक्त समय $30-20=10$ seconds।

$$v=\frac{200}{10}=20\text{ m/s}=\mathbf{72\text{ km/h}}$$

Train length $=20\times20=\mathbf{400}$ m।

**उदाहरण 11.** एक train pole को $12$ seconds और $360$ m platform को $30$ seconds में पार करती है।

- extra time $=30-12=18$ s
- speed $=360/18=20$ m/s $=72$ km/h
- length $=20\times12=\mathbf{240}$ m

### :icon-brain: प्रकार 4 — दो trains opposite direction

दो trains को पूरी तरह पार करने के लिए उनकी lengths जुड़ती हैं। Opposite direction में relative speed भी जुड़ती है।

$$T=\frac{L_1+L_2}{v_1+v_2}$$

```figure
type: two-trains
l1: 100
l2: 200
s1: 54
s2: 36
direction: opposite
caption: विपरीत दिशाओं में lengths और speeds दोनों जुड़ते हैं
```

**उदाहरण 12.** $100$ m और $200$ m की दो trains क्रमशः $54$ और $36$ km/h की चाल से विपरीत दिशाओं में चलती हैं। वे एक-दूसरे को कितने समय में पार करेंगी?

- कुल distance $=100+200=300$ m
- relative speed $=54+36=90$ km/h $=25$ m/s

$$T=\frac{300}{25}=\mathbf{12}\text{ seconds}$$

**उदाहरण 13.** $150$ m और $250$ m trains $72$ और $54$ km/h से opposite दिशा में हैं।

- distance $=400$ m
- relative speed $=126$ km/h $=35$ m/s

$$T=\frac{400}{35}=\mathbf{\frac{80}{7}}\text{ seconds}$$

### :icon-timer: प्रकार 5 — दो trains same direction

Same direction में तेज train धीमी train को overtake करती है। Relative speed = speeds का अन्तर।

$$T=\frac{L_1+L_2}{v_{fast}-v_{slow}}$$

```figure
type: two-trains
l1: 150
l2: 100
s1: 72
s2: 54
direction: same
caption: एक ही दिशा में relative speed speeds का अन्तर होती है
```

**उदाहरण 14.** $150$ m train $72$ km/h से और $100$ m train $54$ km/h से same direction में चलती हैं। तेज train धीमी train को कितने समय में पार करेगी?

- distance $=150+100=250$ m
- relative speed $=72-54=18$ km/h $=5$ m/s

$$T=\frac{250}{5}=\mathbf{50}\text{ seconds}$$

**उदाहरण 15.** एक train $120$ m की है और $54$ km/h से चल रही cyclist को same direction में $18$ km/h पर overtake करती है। time?

- relative speed $=54-18=36$ km/h $=10$ m/s
- cyclist की length नगण्य

$$T=\frac{120}{10}=\mathbf{12}\text{ seconds}$$

### :icon-number: प्रकार 6 — moving person या cyclist

Moving person को fixed pole न मानें। Train और person की relative speed लगाएँ।

```figure
type: moving-person
length: 200
train_kmh: 72
person_kmh: 18
direction: same
caption: same direction में train की speed से person की speed घटती है
```

**उदाहरण 16 — same direction।** $200$ m train $72$ km/h से चल रही है और cyclist $18$ km/h से उसी दिशा में। train cyclist को कितने समय में पार करेगी?

- relative speed $=72-18=54$ km/h $=15$ m/s
- distance $=200$ m

$$T=\frac{200}{15}=\mathbf{13\frac{1}{3}}\text{ seconds}$$

**उदाहरण 17 — opposite direction।** वही train cyclist की ओर $18$ km/h से आ रहा है।

- relative speed $=72+18=90$ km/h $=25$ m/s

$$T=\frac{200}{25}=\mathbf{8}\text{ seconds}$$

> :icon-warn: Moving person की speed को same direction में घटाना और opposite direction में जोड़ना है। Pole वाले प्रश्न में person की speed $0$ मानी जाती है।

### :icon-ruler: प्रकार 7 — train और platform time का अन्तर

किसी train को pole और platform पार करने के समय का अन्तर platform की length तय करने में लगता है।

**उदाहरण 18.** एक train pole को $10$ s और $210$ m platform को $24$ s में पार करती है। train की speed और length?

- extra time $=24-10=14$ s
- speed $=210/14=15$ m/s $=54$ km/h
- train length $=15\times10=\mathbf{150}$ m

### :icon-list: प्रकार 8 — crossing comparison

```figure
type: crossing-table
length: 180
platform: 270
bridge: 420
speed_kmh: 54
caption: pole, platform और bridge के लिए distance क्रमशः L, L+P और L+B होती है
```

**उदाहरण 19.** $180$ m train $54$ km/h से pole, $270$ m platform और $420$ m bridge को पार करती है। तीनों समय?

Speed $=15$ m/s।

- pole: $180/15=\mathbf{12}$ s
- platform: $(180+270)/15=\mathbf{30}$ s
- bridge: $(180+420)/15=\mathbf{40}$ s

### :icon-steps: प्रकार 9 — train की crossing speed से length

**उदाहरण 20.** एक train $90$ km/h की चाल से $500$ m bridge को $30$ s में पार करती है। train length?

- speed $=25$ m/s
- total distance $=25\times30=750$ m
- train length $=750-500=\mathbf{250}$ m

### :icon-star: प्रकार 10 — length ratio और time ratio

यदि दो trains एक ही speed से pole को पार करती हैं, तो उनके crossing times उनकी lengths के अनुपात में होंगे।

**उदाहरण 21.** दो trains की lengths $3:5$ हैं और speeds समान हैं। pole पार करने के समय का अनुपात?

$$T_1:T_2=L_1:L_2=\mathbf{3:5}$$

यदि lengths समान हों और speeds का ratio $4:5$ हो, तो time ratio $5:4$ होगा।

---

## 25.5 :icon-bulb: शॉर्टकट व उनके प्रमाण

### :icon-timer: शॉर्टकट 1 — fixed object

Pole/tree/stationary person के लिए —

$$T=\frac{L}{v}$$

जहाँ $L$ metres में और $v$ m/s में हो।

### :icon-timer: शॉर्टकट 2 — platform/bridge/tunnel

$$T=\frac{L+P}{v}$$

Train की length और object की length जोड़ना न भूलें।

### :icon-timer: शॉर्टकट 3 — two trains

Opposite direction:

$$T=\frac{L_1+L_2}{v_1+v_2}$$

Same direction:

$$T=\frac{L_1+L_2}{|v_1-v_2|}$$

### :icon-timer: शॉर्टकट 4 — moving person

Train और person के लिए भी वही relative speed:

$$v_{relative}=v_{train}+v_{person}\quad\text{(opposite)}$$

$$v_{relative}=|v_{train}-v_{person}|\quad\text{(same)}$$

### :icon-timer: शॉर्टकट 5 — pole/platform time difference

यदि pole time $t_1$, platform time $t_2$ और platform length $P$ हो —

$$v=\frac{P}{t_2-t_1}$$

फिर —

$$L=v\times t_1$$

**प्रमाण:** platform crossing distance $L+P$ और pole crossing distance $L$ है। दूरी का अन्तर केवल $P$ और समय का अन्तर $t_2-t_1$ है।

### :icon-timer: शॉर्टकट 6 — speed conversion

$$54\text{ km/h}=15\text{ m/s},\quad 72\text{ km/h}=20\text{ m/s},\quad 90\text{ km/h}=25\text{ m/s}$$

इन तीन values को याद करने से train questions तेज़ होते हैं।

### :icon-timer: शॉर्टकट 7 — distance और time ratio

समान speed पर —

$$T_1:T_2=D_1:D_2$$

समान train length पर —

$$T_1:T_2=v_2:v_1$$

---

## 25.6 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** km/h को सीधे m/s की तरह इस्तेमाल करना।
> Train length metres में हो और time seconds में, तो speed m/s में बदलिए।

> :icon-cross: **जाल 2.** platform की length न जोड़ना।
> Platform, bridge और tunnel के लिए distance $L+P$ होती है।

> :icon-cross: **जाल 3.** दो trains की lengths घटाना।
> दोनों trains को पूरी तरह पार करना है, इसलिए lengths हमेशा जुड़ती हैं।

> :icon-cross: **जाल 4.** same direction में speeds जोड़ना।
> Overtaking में relative speed = faster speed − slower speed।

> :icon-cross: **जाल 5.** moving person को pole मानना।
> Person की speed direction के अनुसार add/subtract होगी।

> :icon-cross: **जाल 6.** pole और platform times का अन्तर गलत लेना।
> Extra distance platform length है; इसलिए $P/(t_2-t_1)$ speed होगी।

> :icon-cross: **जाल 7.** train length को platform length समझ लेना।
> Total distance $=$ train length + object length; फिर दिए object को घटाकर train length निकालिए।

> :icon-cross: **जाल 8.** bridge और tunnel को pole जैसा मानना।
> Bridge/tunnel की अपनी length होती है, इसलिए उसे जोड़ना जरूरी है।

> :icon-cross: **जाल 9.** crossing का अर्थ train का front object तक पहुँचना मानना।
> Crossing तब समाप्त होता है जब train का पिछला सिरा object पार कर लेता है।

---

## 25.7 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(SSC CGL)* $180$ m train $54$ km/h से pole को पार करती है। समय?

**हल:** $54=15$ m/s; $180/15=\mathbf{12}$ s।

**PYQ 2.** *(SSC CHSL)* $150$ m train $250$ m platform को $72$ km/h से पार करती है। समय?

**हल:** distance $400$ m, speed $20$ m/s ⟹ $\mathbf{20}$ s।

**PYQ 3.** *(RRB NTPC)* $100$ m और $200$ m trains $54$ और $36$ km/h से opposite direction में।

**हल:** distance $300$ m, relative $25$ m/s ⟹ $\mathbf{12}$ s।

**PYQ 4.** *(IBPS Clerk)* train pole को $20$ s और $200$ m platform को $30$ s में पार करती है। speed और length?

**हल:** speed $=200/10=20$ m/s $=\mathbf{72}$ km/h; length $=20\times20=\mathbf{400}$ m।

**PYQ 5.** *(UP Police SI)* $150$ m train $72$ km/h से $100$ m train को $54$ km/h पर same direction में पार करती है।

**हल:** distance $250$ m, relative $5$ m/s ⟹ $\mathbf{50}$ s।

**PYQ 6.** *(SSC MTS)* $200$ m train $72$ km/h से $18$ km/h cyclist को same direction में पार करती है।

**हल:** relative $54$ km/h $=15$ m/s; समय $=\mathbf{13\frac{1}{3}}$ s।

---

## 25.8 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | $180$ m train, $54$ km/h, pole | $12$ s | $180/15$ |
| 2 | $72$ km/h, pole in $15$ s | $300$ m | $20\times15$ |
| 3 | train $150$ m + platform $250$ m, $72$ km/h | $20$ s | $400/20$ |
| 4 | bridge $500$ m, $90$ km/h, $30$ s | train $250$ m | $750-500$ |
| 5 | train $120$ m, $54$ km/h, platform $20$ s | platform $180$ m | $300-120$ |
| 6 | trains $100,200$ m; $54,36$ km/h opposite | $12$ s | $300/25$ |
| 7 | trains $150,100$ m; $72,54$ km/h same | $50$ s | $250/5$ |
| 8 | train $200$ m at $72$, cyclist $18$ same direction | $13\frac{1}{3}$ s | relative $15$ m/s |
| 9 | train $200$ m at $72$, person $18$ opposite | $8$ s | relative $25$ m/s |
| 10 | pole $20$ s, platform $200$ m in $30$ s | speed $72$ km/h, length $400$ m | extra time |
| 11 | train $120$ m, speed $72$, platform $20$ s | platform $280$ m | $400-120$ |
| 12 | train $240$ m, $54$ km/h, pole | $16$ s | $240/15$ |
| 13 | trains $120,180$ m; $54,36$ opposite | $12$ s | $300/25$ |
| 14 | train $180$ m; platform $270$; $54$ km/h | $30$ s | $450/15$ |
| 15 | train $240$ m; pole $12$ s; platform $360$ | $30$ s | speed $20$ m/s |
| 16 | train $120$ m, $54$ km/h; cyclist $18$ same | $12$ s | relative $10$ m/s |
| 17 | train $200$ m, $72$ km/h; person $18$ opposite | $8$ s | relative $25$ m/s |
| 18 | pole $10$ s, platform $210$ m in $24$ s | speed $54$ km/h, length $150$ m | $210/14$ |
| 19 | train $180$ m, $54$ km/h: pole/platform $270$/bridge $420$ | $12,30,40$ s | compare distances |
| 20 | bridge $500$ m, train $90$ km/h, time $30$ s | train $250$ m | total $750$ |
| 21 | lengths ratio $3:5$, same speed | time ratio $3:5$ | $T\propto L$ |
| 22 | same train length, speeds ratio $4:5$ | time ratio $5:4$ | inverse speed |
| 23 | trains $200,100$ m; $36,54$ opposite | $12$ s | $300/25$ |
| 24 | train $240$ m, platform $360$ m, speed $72$ | $30$ s | $600/20$ |
| 25 | train $250$ m crosses $350$ m platform in $30$ s | $72$ km/h | total $600$ m; speed $20$ m/s |

---

## 25.9 :icon-trophy: अध्याय का सार

```
━━━ Fixed object ━━━
pole/tree/stationary person:
distance = train length L
time = L / speed

180 m train at 54 km/h = 15 m/s
pole time = 180/15 = 12 s

━━━ Platform / bridge / tunnel ━━━
distance = train length + object length
T = (L + P) / v

150 m train + 250 m platform at 72 km/h
= 400/20 = 20 s

━━━ Two trains ━━━
distance = L₁ + L₂
opposite: relative speed = v₁ + v₂
same direction: relative speed = |v₁ − v₂|

100 m and 200 m, 54 and 36 opposite
= 300/25 = 12 s

━━━ Moving person ━━━
same direction → train speed − person speed
opposite → train speed + person speed

━━━ Pole/platform data ━━━
speed = platform length / (platform time − pole time)
train length = speed × pole time

200 m platform; times 20 s and 30 s
speed = 200/10 = 20 m/s = 72 km/h
length = 20×20 = 400 m

━━━ Ratios ━━━
same speed → time ratio = length ratio
same length → time ratio = inverse speed ratio

━━━ Conversion ━━━
54 km/h = 15 m/s
72 km/h = 20 m/s
90 km/h = 25 m/s

━━━ जाल ━━━
km/h को m/s में बदलिए
platform/object length जोड़िए
train lengths हमेशा जुड़ती हैं
same direction में speeds घटती हैं
moving person को fixed pole मत मानिए
```

> :icon-trophy: **अध्याय 24 का relative-speed आधार अब train problems में पूरा हुआ।**
>
> **आगे:** अध्याय 26 — **नाव व धारा (Boats & Streams)**। वहाँ पानी की धारा को एक moving medium मानकर upstream और downstream की effective speed निकाली जाएगी।
