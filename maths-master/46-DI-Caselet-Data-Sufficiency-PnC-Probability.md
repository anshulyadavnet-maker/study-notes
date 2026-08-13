# अध्याय 46 — DI, Caselet, Data Sufficiency, P&C व Probability

## 46.1 :icon-target: परिचय व वेटेज

यह Maths Master syllabus का अंतिम chapter है और Banking तथा advanced aptitude के लिए बहुत महत्वपूर्ण है। इसमें calculation से अधिक **data reading, condition selection और counting logic** काम आता है।

इस chapter में पाँच connected skills हैं:

1. Data Interpretation (DI)
2. Caselet DI
3. Data Sufficiency
4. Permutation & Combination (P&C)
5. Probability

> *"Table में दिए numbers को पढ़कर ratio, percentage, average और difference निकालना है—लेकिन पहले यह तय करना है कि कौन-सी information relevant है।"*

| परीक्षा | सीधे प्रश्न | टिप्पणी |
|---|---:|---|
| **IBPS / SBI PO Prelims** | **5–10** | table, bar, line, pie DI |
| **IBPS / SBI PO Mains** | **10–20** | caselet, missing data, P&C |
| IBPS / SBI Clerk | 5–10 | arithmetic DI |
| **SSC CGL Tier-2** | **3–8** | DI और probability |
| SSC CPO / CHSL | 2–5 | table and graph |
| **RRB NTPC / ALP** | 2–5 | chart interpretation |
| UP Police SI | 2–5 | data and probability |
| State Banking Exams | 5–15 | mixed sets |

> :icon-key: **पूरे अध्याय का एक वाक्य:** Data को structure में बदलें, question की exact demand निकालें, और answer को total/condition से verify करें।

---

## 46.2 :icon-number: Data Interpretation की नींव

DI में चार steps:

1. Units और labels पढ़ें।
2. Total, ratio और percentage जैसे base values निकालें।
3. हर sub-question के लिए केवल जरूरी data लें।
4. Approximation/option check से calculation तेज करें।

```figure
type: di-table
caption: table DI में rows, columns और units पहले identify कीजिए
```

### Table example

| Year | Company A | Company B |
|---:|---:|---:|
| 2021 | 120 | 100 |
| 2022 | 150 | 140 |
| 2023 | 180 | 160 |
| 2024 | 200 | 220 |

**उदाहरण 1.** 2021–24 में A का total production?

$$120+150+180+200=\mathbf{650}$$

**उदाहरण 2.** A का 2021 से 2024 percentage increase?

$$\frac{200-120}{120}\times100=\mathbf{66\frac{2}{3}\%}$$

**उदाहरण 3.** 2023 में A:B ratio?

$$180:160=\mathbf{9:8}$$

**उदाहरण 4.** B का average production?

$$\frac{100+140+160+220}{4}=\mathbf{155}$$

> :icon-bulb: DI में percentage change का denominator initial value होता है, final value नहीं।

---

## 46.3 :icon-chart: Bar, line और pie DI

### Bar diagram

Bar chart में categories या periods compare किए जाते हैं।

```figure
type: di-bars
caption: grouped bars में दो series को category-wise compare कीजिए
```

Useful calculations:

- difference $=A-B$
- ratio $=A/B$
- percentage more $=(A-B)/B\times100$
- percentage less $=(B-A)/B\times100$

**उदाहरण 5.** यदि category C में A=15 और B=20, तो A, B से कितने प्रतिशत कम?

$$\frac{20-15}{20}\times100=\mathbf{25\%}$$

### Line graph

Line graph ordered time/data trend दिखाता है। Maximum, minimum, consecutive change और average पूछे जा सकते हैं।

```figure
type: di-line
caption: line trend से increase, decrease, maximum और average पढ़िए
```

**उदाहरण 6.** Values $20,35,30,50,45$ का maximum और total?

- maximum $=\mathbf{50}$
- total $=20+35+30+50+45=\mathbf{180}$
- average $=180/5=\mathbf{36}$

### Pie chart

Pie chart का full angle $360°$ होता है:

$$\text{sector angle}=\frac{f}{N}\times360°$$

```figure
type: di-pie
caption: pie chart में percentage को sector angle में बदलें
```

**उदाहरण 7.** Total 200 students में 50 Science group में हैं। Sector angle?

$$\frac{50}{200}\times360=\mathbf{90°}$$

Reverse:

$$f=\frac{\text{sector angle}}{360°}\times N$$

---

## 46.4 :icon-steps: Caselet DI

Caselet में table नहीं, paragraph में information छिपी होती है। पहले paragraph को mini-table या flow में बदलें।

```figure
type: caselet-flow
caption: caselet की language को total, ratio और percentage steps में बदलिए
```

**Caselet:** एक school में 720 students हैं। Boys:girls $=5:4$। 60% boys और 50% girls sports में हैं।

- Total parts $=9$
- Boys $=720\times5/9=400$
- Girls $=720\times4/9=320$
- Sports boys $=60\%$ of $400=240$
- Sports girls $=50\%$ of $320=160$
- Total sports students $=\mathbf{400}$

**उदाहरण 8.** Sports में boys:girls ratio?

$$240:160=\mathbf{3:2}$$

**उदाहरण 9.** Non-sports students?

$$720-400=\mathbf{320}$$

> :icon-key: Caselet में हर sentence को एक variable, ratio या percentage statement में बदलें। Mental reading पर भरोसा करने से numerator/denominator बदल सकता है।

---

## 46.5 :icon-ruler: Data Sufficiency

Data sufficiency में question का answer निकालना मुख्य उद्देश्य नहीं; यह तय करना है कि दी गई statements answer के लिए sufficient हैं या नहीं।

Typical format:

- Statement I
- Statement II
- options: I alone, II alone, both together, either alone, neither

```figure
type: sufficiency-flow
caption: statements को अलग-अलग और फिर साथ test करके sufficiency तय करें
```

**उदाहरण 10.** What is $x$?

I. $x+y=10$

II. $x-y=4$

- I alone: x निश्चित नहीं; y बदल सकता है।
- II alone: x निश्चित नहीं।
- दोनों: जोड़ने पर $2x=14$, इसलिए $x=7$।

अतः **both statements together sufficient**।

### Sufficiency method

1. Statement I को अकेले use करें।
2. क्या answer unique है? यदि हाँ, I sufficient।
3. Statement II अकेले test करें।
4. दोनों साथ use करें।
5. Unnecessary exact calculation न करें।

**उदाहरण 11.** क्या $n$ even है?

I. $n$ को 2 से divide करने पर remainder 0 आता है।

I alone ही answer देता है, इसलिए sufficient।

**उदाहरण 12.** $x$ का value?

I. $x+y=12$

II. $y=5$

दोनों साथ $x=7$ देते हैं; individually insufficient।

---

## 46.6 :icon-calc: Fundamental Counting Principle

यदि एक काम के पहले step के $m$ choices और दूसरे step के $n$ choices हों, total outcomes:

$$m\times n$$

```figure
type: counting-tree
caption: independent choices multiply होकर total outfits/outcomes बनाते हैं
```

**उदाहरण 13.** 3 shirts और 2 trousers से outfits?

$$3\times2=\mathbf{6}$$

### Factorial

$$n!=n(n-1)(n-2)\cdots3\times2\times1$$

और $0!=1$।

**उदाहरण 14.** $5!=\mathbf{120}$।

### Repetition allowed

$n$ symbols से $r$ places भरें और repetition allowed:

$$n^r$$

**उदाहरण 15.** 5 digits से 3-place code, repetition allowed:

$$5^3=\mathbf{125}$$

---

## 46.7 :icon-list: Permutation और Combination

### Permutation: arrangement

Order matters:

$$nP_r=\frac{n!}{(n-r)!}$$

**उदाहरण 16.** 5 students में से 3 को first, second, third positions में arrange करें:

$$5P_3=5\times4\times3=\mathbf{60}$$

```figure
type: arrangement
caption: permutation में order matters, combination में केवल selection
```

### Combination: selection

Order does not matter:

$$nC_r=\frac{n!}{r!(n-r)!}$$

**उदाहरण 17.** 8 students में से 3 की team?

$$8C_3=\frac{8\times7\times6}{3\times2\times1}=\mathbf{56}$$

### Relation

$$nP_r=nC_r\times r!$$

### Useful properties

$$nC_r=nC_{n-r}$$

$$nC_0=nC_n=1$$

**उदाहरण 18.** $10C_8=10C_2=\mathbf{45}$।

### Repeated objects

यदि total $n$ objects में $p,q$ identical objects हों:

$$\text{arrangements}=\frac{n!}{p!q!}$$

**उदाहरण 19.** Word “LEVEL” के distinct arrangements:

L दो और E दो:

$$\frac{5!}{2!2!}=\mathbf{30}$$

---

## 46.8 :icon-brain: Probability basics

Sample space $S$ सभी possible outcomes का set है। Event $E$ favourable outcomes का set है। Equally likely outcomes में:

$$P(E)=\frac{n(E)}{n(S)}$$

```figure
type: probability-box
caption: probability favourable outcomes को total sample space से compare करती है
```

Probability की range:

$$0\leq P(E)\leq1$$

- impossible event: $P=0$
- certain event: $P=1$

**उदाहरण 20.** Fair die में even number आने की probability?

Sample space $\{1,2,3,4,5,6\}$; favourable $\{2,4,6\}$।

$$P(E)=\frac{3}{6}=\mathbf{\frac{1}{2}}$$

### Complement

$$P(\text{not }E)=1-P(E)$$

**उदाहरण 21.** Die में 6 न आने की probability:

$$1-\frac{1}{6}=\mathbf{\frac{5}{6}}$$

### Addition rule

Mutually exclusive events:

$$P(A\text{ or }B)=P(A)+P(B)$$

**उदाहरण 22.** Die में 2 या 5 आने की probability:

$$\frac{1}{6}+\frac{1}{6}=\mathbf{\frac{1}{3}}$$

General events में overlap subtract करना होता है:

$$P(A\cup B)=P(A)+P(B)-P(A\cap B)$$

---

## 46.9 :icon-steps: Sequential probability और tree

Independent events में multiplication:

$$P(A\text{ and }B)=P(A)P(B)$$

Without replacement में second probability बदलती है।

**उदाहरण 23.** Bag में 5 red और 3 blue balls हैं। बिना replacement दो red balls निकलने की probability?

```figure
type: probability-tree
caption: बिना replacement दूसरी branch में denominator और favourable count बदलते हैं
```

$$P(RR)=\frac{5}{8}\times\frac{4}{7}=\mathbf{\frac{5}{14}}$$

With replacement होता तो:

$$P(RR)=\frac{5}{8}\times\frac{5}{8}=\frac{25}{64}$$

### At least one

“At least one” questions में complement fastest:

$$P(\text{at least one})=1-P(\text{none})$$

**उदाहरण 24.** Coin को 3 बार toss करने पर कम से कम एक head:

$$P(\text{no head})=P(TTT)=\left(\frac{1}{2}\right)^3=\frac{1}{8}$$

$$P(\text{at least one H})=1-\frac{1}{8}=\mathbf{\frac{7}{8}}$$

---

## 46.10 :icon-chart: Mixed exam strategy

**उदाहरण 25.** एक class में 40 students हैं। 24 Maths पसंद करते हैं, 18 Science और 10 दोनों। कम से कम एक subject पसंद करने वाले?

$$n(M\cup S)=24+18-10=\mathbf{32}$$

Neither:

$$40-32=\mathbf{8}$$

यह DI, set counting और probability की boundary पर आने वाला mixed reasoning है।

### Time strategy

| Question type | First move |
|---|---|
| table/bar DI | totals और units लिखें |
| caselet | paragraph को mini-table बनाएं |
| sufficiency | statements individually test करें |
| P&C | order matters? decide करें |
| probability | sample space और event लिखें |
| at least one | complement देखें |
| without replacement | denominator बदलें |

---

## 46.11 :icon-bulb: Shortcuts और formula map

### :icon-timer: DI

$$\%\text{ change}=\frac{new-old}{old}\times100$$

$$\text{average}=\frac{total}{number\ of\ periods}$$

### :icon-timer: Pie

$$angle=\frac{f}{N}\times360°$$

### :icon-timer: Sufficiency

I alone, II alone, both together—तीनों अलग test करें।

### :icon-timer: Counting

$$nP_r=\frac{n!}{(n-r)!}$$

$$nC_r=\frac{n!}{r!(n-r)!}$$

$$nP_r=nC_r\times r!$$

### :icon-timer: Probability

$$P(E)=\frac{favourable}{total}$$

$$P(\bar E)=1-P(E)$$

$$P(A\cap B)=P(A)P(B)\quad\text{if independent}$$

### :icon-timer: Complement shortcut

At least one $=1-$ none।

### :icon-timer: Approximation

DI options बहुत अलग हों तो rounded values से eliminate करें; close options में exact calculation करें।

---

## 46.12 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** DI में wrong denominator से percentage निकालना।
> Increase/decrease percentage initial value के against होता है।

> :icon-cross: **जाल 2.** Caselet के ratio को total पर सीधे apply करना।
> पहले total ratio parts में बाँटिए।

> :icon-cross: **जाल 3.** Data sufficiency में statement I और II को अलग test न करना।
> दोनों साथ sufficient हों तो individually sufficient नहीं मानें।

> :icon-cross: **जाल 4.** P&C और combination को interchange करना।
> Order matters = permutation; order ignored = combination।

> :icon-cross: **जाल 5.** Repeated objects को अलग-अलग मानकर factorial लगाना।
> Identical objects के factorial से divide करें।

> :icon-cross: **जाल 6.** Probability का denominator बदलना भूलना।
> Without replacement में total objects घटता है।

> :icon-cross: **जाल 7.** At least one में direct cases बहुत गिनना।
> Complement $1-P(none)$ तेज और सुरक्षित है।

> :icon-cross: **जाल 8.** Pie chart में percentage को angle समझ लेना।
> Percentage × $3.6$ = degrees।

> :icon-cross: **जाल 9.** Histogram और bar graph में gaps गलत लगाना।
> Continuous classes touch; categories separate।

> :icon-cross: **जाल 10.** Probability को 1 से बड़ा या negative लिखना।
> हर probability $0$ और $1$ के बीच होती है।

---

## 46.13 :icon-exam: विगत वर्ष प्रश्न (PYQ)

**PYQ 1.** *(IBPS PO)* Table DI में A total 650 और B total 620। Combined total?

**हल:** $\mathbf{1270}$।

**PYQ 2.** *(SBI Clerk)* Total 200 में category 50। Pie angle?

**हल:** $\mathbf{90°}$।

**PYQ 3.** *(IBPS PO)* I: $x+y=10$, II: $x-y=4$; x निकालने को कौन-सी statements?

**हल:** **Both together**।

**PYQ 4.** *(RRB PO)* $5P_3$।

**हल:** $\mathbf{60}$।

**PYQ 5.** *(SSC CGL)* $8C_3$।

**हल:** $\mathbf{56}$।

**PYQ 6.** *(IBPS Clerk)* Die में even number की probability?

**हल:** $\mathbf{1/2}$।

---

## 46.14 :icon-pencil: अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | A table total $120+150+180+200$ | 650 | sum |
| 2 | A 120 से 200 percentage increase | $66\frac{2}{3}\%$ | change/initial |
| 3 | B values $100,140,160,220$ average | 155 | total/4 |
| 4 | 15 vs 20; first कितने % less? | 25% | difference/20 |
| 5 | caselet total720, ratio5:4 | 400,320 | parts |
| 6 | 60% of400 +50% of320 | 400 | caselet |
| 7 | pie frequency50,total200 | 90° | angle |
| 8 | pie angle72,total250 | 50 | reverse |
| 9 | $3$ shirts, $2$ trousers | 6 | multiplication |
| 10 | $5!$ | 120 | factorial |
| 11 | $5P_3$ | 60 | order |
| 12 | $8C_3$ | 56 | selection |
| 13 | $10C_8$ | 45 | symmetry |
| 14 | 5 symbols, 3 code places repetition | 125 | $5^3$ |
| 15 | LEVEL arrangements | 30 | repeated factorial |
| 16 | die even probability | $1/2$ | 3/6 |
| 17 | die not 6 | $5/6$ | complement |
| 18 | die 2 or5 | $1/3$ | addition |
| 19 | 5 red,3 blue; two red no replacement | $5/14$ | multiply branches |
| 20 | 3 coin toss at least one head | $7/8$ | complement |
| 21 | total40, M24,S18,both10 | union32 | inclusion-exclusion |
| 22 | neither in previous | 8 | subtract union |
| 23 | data sufficiency I $x+y=10$, II $x-y=4$ | both together | unique x |
| 24 | mean correction: n10,M25,18→28 | 26 | correction |
| 25 | class intervals $0-10$ etc. graph | histogram | continuous data |

---

## 46.15 :icon-trophy: अध्याय का सार

```
━━━ DI ━━━
read units and labels
percentage = change/initial ×100
average = total/periods
pie angle = f/N ×360

━━━ Caselet ━━━
paragraph → ratio parts → actual counts → question

━━━ Data sufficiency ━━━
I alone
II alone
both together
unique answer required

━━━ Counting ━━━
fundamental principle: multiply choices
nPr = n!/(n−r)!
nCr = n!/[r!(n−r)!]
nPr = nCr × r!
order matters → P
order ignored → C

━━━ Probability ━━━
P(E)=favourable/total
P(not E)=1−P(E)
independent events multiply
mutually exclusive events add
at least one = 1−none
without replacement: denominator changes

━━━ Graphs ━━━
histogram: continuous, touching bars
bar: discrete, gaps
pie: parts of whole
line: trend
caselet: build a table first
```

> :icon-trophy: **Maths Master के सभी 46 planned chapters complete।** Chapter 1 से 46 तक arithmetic, algebra, geometry, trigonometry, statistics, DI, P&C और probability की integrated exam-focused foundation तैयार है।
>
> **आगे:** Full Maths Master book assembly, final revision sheets, mock tests और PDF build/indexing।
