# Railway Maths — सांख्यिकी (Statistics)

## 1.1 :icon-target: परिचय और Railway परीक्षा में उपयोग

Statistics (सांख्यिकी) data को collect, arrange, represent और interpret करने की mathematics है। Railway exams में raw numbers, frequency tables और graphs से mean, median, mode, range, percentage और comparison पूछे जाते हैं। पहले data को साफ़ तरीके से पढ़ें, फिर पूछा गया measure या graph-formula चुनें।

> *"किसी data set का सबसे representative value कौन-सा है—mean, median या mode?"*

Mean सभी observations को use करता है, median middle position बताता है और mode सबसे अधिक बार आने वाला value। Data की nature और outliers देखकर सही measure चुनना जरूरी है।

| Railway परीक्षा | Statistics में उपयोगी क्षेत्र | तैयारी का फोकस |
|---|---|---|
| **RRB NTPC** | average, table/graph और basic data | speed + calculation accuracy |
| **RRB Group D** | mean, median, mode और सरल graph | formula recognition |
| **RRB ALP / Technician** | arithmetic-based statistics | units और approximation |
| **RRB JE** | data interpretation और grouped data | concept + multi-step calculation |
| **RPF Constable / SI** | average, percentage और chart | short methods |

> Railway भर्ती के अलग-अलग notifications में प्रश्नों का weightage बदल सकता है। ऊपर की table topic-priority guide है, official question-count guarantee नहीं।

> :icon-key: **Railway exam का one-line rule:** Data को पहले order/frequency table में व्यवस्थित करें, फिर central tendency या graph का सही formula चुनें।

---

## 1.2 :icon-number: Data और frequency table

### Data

Numbers या observations का collection data है।

- Ungrouped data: $4,7,7,9,12$
- Discrete data: अलग-अलग count values
- Continuous data: intervals जैसे $0-10,10-20$

### Frequency

किसी observation के repeat होने की संख्या frequency $f$ है।

```figure
type: data-table
caption: frequency table repeated observations को compact form में बदलती है
```

| Value $x$ | Frequency $f$ | Product $xf$ |
|---:|---:|---:|
| 10 | 2 | 20 |
| 20 | 5 | 100 |
| 30 | 8 | 240 |
| 40 | 4 | 160 |
| 50 | 1 | 50 |
| **Total** | **20** | **570** |

Total observations:

$$N=\sum f$$

Weighted total:

$$\sum xf$$

> :icon-bulb: Frequency table में mean निकालने के लिए केवल values का average नहीं; हर value को उसकी frequency से multiply करना पड़ता है।

---

## 1.3 :icon-calc: Mean (माध्य)

### Individual data

$n$ observations $x_1,x_2,\ldots,x_n$:

$$\bar{x}=\frac{\sum x}{n}$$

**उदाहरण 1.** $8,10,12,15,15$ का mean?

$$\bar{x}=\frac{8+10+12+15+15}{5}=\mathbf{12}$$

### Discrete frequency data

$$\bar{x}=\frac{\sum xf}{\sum f}$$

**उदाहरण 2.** ऊपर की table में:

$$\bar{x}=\frac{570}{20}=\mathbf{28.5}$$

```figure
type: mean-bars
caption: weighted total को total frequency से divide करने पर mean मिलता है
```

### Assumed mean method

यदि values बड़ी हों, तो assumed mean $A$ लें:

$$\bar{x}=A+\frac{\sum fd}{\sum f},\qquad d=x-A$$

**उदाहरण 3.** Values $20,30,40$ की frequencies $2,5,3$ हैं। $A=30$ लें:

| $x$ | $f$ | $d=x-30$ | $fd$ |
|---:|---:|---:|---:|
| 20 | 2 | -10 | -20 |
| 30 | 5 | 0 | 0 |
| 40 | 3 | 10 | 30 |

$$\sum f=10,\quad\sum fd=10$$

$$\bar{x}=30+10/10=\mathbf{31}$$

### Weighted mean

अलग-अलग groups के means $\bar{x}_1,\bar{x}_2$ और sizes $n_1,n_2$ हों:

$$\bar{x}=\frac{n_1\bar{x}_1+n_2\bar{x}_2}{n_1+n_2}$$

**उदाहरण 4.** 20 students का mean 60 और 30 students का mean 70। Combined mean?

$$\bar{x}=\frac{20(60)+30(70)}{50}=\mathbf{66}$$

---

## 1.4 :icon-steps: Median (मध्यका)

Median ordered data का middle value है। Data को पहले ascending/descending order में लगाएँ।

### Odd number of observations

यदि $n$ odd:

$$\text{median position}=\frac{n+1}{2}$$

```figure
type: median-position
caption: ordered data में middle position median को दिखाती है
```

**उदाहरण 5.** $3,5,6,8,10,12,15,18,20$।

$n=9$:

$$\text{position}=\frac{9+1}{2}=5$$

Median $=\mathbf{10}$।

### Even number of observations

यदि $n$ even, बीच के दो observations का average:

$$\text{median}=\frac{(n/2)th+(n/2+1)th}{2}$$

**उदाहरण 6.** $4,7,9,12,15,18$।

Middle values $9,12$:

$$\text{median}=\frac{9+12}{2}=\mathbf{10.5}$$

### Discrete frequency median

Cumulative frequency बनाइए और middle observation locate करें।

यदि $N$ odd, position $(N+1)/2$; यदि even, $N/2$ और $N/2+1$ positions।

---

## 1.5 :icon-chart: Mode और empirical relation

Mode वह observation है जिसकी frequency सबसे अधिक हो।

```figure
type: mode-bar
caption: सबसे ऊँचा frequency bar mode observation बताता है
```

**उदाहरण 7.** Values $10,20,30,40,50$ की frequencies $3,6,12,5,2$ हैं।

Highest frequency $12$ value $30$ पर है। Mode $=\mathbf{30}$।

### Empirical relation

Moderately symmetric distribution में:

$$\mathbf{Mode=3Median-2Mean}$$

या:

$$\mathbf{Mean-Mode=3(Mean-Median)}$$

**उदाहरण 8.** Mean $25$ और Median $27$ है। Mode?

$$Mode=3(27)-2(25)=81-50=\mathbf{31}$$

> :icon-warn: Empirical relation exact universal law नहीं; exam में जब explicitly use/appropriate distribution हो, तब लगाएँ।

---

## 1.6 :icon-ruler: Grouped data — class mark और median/mode

Continuous class interval $10-20$ का class mark:

$$x=\frac{10+20}{2}=15$$

Mean के लिए हर class का midpoint लेकर $xf$ बनाइए।

### Grouped median

Formula:

$$Median=l+\left(\frac{N/2-cf}{f}\right)h$$

जहाँ:

- $l$: median class की lower boundary
- $N$: total frequency
- $cf$: median class से पहले cumulative frequency
- $f$: median class frequency
- $h$: class width

### Grouped mode

यदि modal class की frequency $f_1$, previous $f_0$, next $f_2$:

$$Mode=l+\left(\frac{f_1-f_0}{2f_1-f_0-f_2}\right)h$$

> :icon-key: Grouped formula में class boundary और class width एक ही unit में रखिए।

---

## 1.7 :icon-chart: Histogram और frequency polygon

### Histogram

Continuous class intervals के frequency bars histogram में **touch** करते हैं।

```figure
type: histogram
caption: histogram में continuous intervals होने के कारण bars के बीच gaps नहीं होते
```

यदि class widths unequal हों, तो frequency density:

$$\text{frequency density}=\frac{f}{\text{class width}}$$

और bar area frequency represent करता है।

### Frequency polygon

Class midpoints पर frequencies plot करके straight segments से join करें।

```figure
type: frequency-polygon
caption: frequency polygon class midpoints को straight lines से join करता है
```

**उदाहरण 9.** Classes $0-10,10-20,20-30$ के midpoints $5,15,25$ हैं। Frequency polygon में x-coordinates $5,15,25$ लगेंगे, class boundaries नहीं।

### Histogram और bar diagram difference

| Feature | Histogram | Bar diagram |
|---|---|---|
| Data | continuous intervals | discrete categories |
| Bars | touching | separated |
| Width | class width | visual category width |
| Area | frequency | usually height comparison |

---

## 1.8 :icon-list: Bar diagram, pie chart और ogive

### Bar diagram

Discrete categories में bars के बीच gap होता है।

```figure
type: bar-chart
caption: discrete categories के bar diagram में bars अलग-अलग रहते हैं
```

### Pie chart

पूरे circle का angle $360°$ है। Category frequency $f$ और total $N$:

$$\text{sector angle}=\frac{f}{N}\times360°$$

```figure
type: pie-chart
caption: pie chart में category frequency के अनुपात में sector angle बनता है
```

**उदाहरण 10.** Total 200 students में 50 Science group में हैं। Pie angle?

$$\frac{50}{200}\times360=\mathbf{90°}$$

### Ogive (cumulative-frequency curve)

Cumulative frequency classes को upper class boundaries के against plot करके curve बनता है।

```figure
type: ogive
caption: less-than ogive cumulative frequency को continuously बढ़ते curve में दिखाता है
```

Ogive से median, quartiles और percentile approximate पढ़े जा सकते हैं।

### Pie chart reverse questions

यदि sector angle $72°$ और total 250 है:

$$f=\frac{72}{360}\times250=\mathbf{50}$$

---

## 1.9 :icon-divide: Missing frequency और data checks

**उदाहरण 11.** Values $10,20,30,40$ की frequencies $2,x,5,3$ हैं और mean $25$ है। $x$?

Total frequency:

$$N=2+x+5+3=x+10$$

Total $xf$:

$$\sum xf=10(2)+20x+30(5)+40(3)=20x+290$$

Mean condition:

$$\frac{20x+290}{x+10}=25$$

$$20x+290=25x+250\quad\Rightarrow\quad x=\mathbf{8}$$

```figure
type: missing-frequency
caption: known mean को frequency equation में रखकर missing frequency निकालिए
```

### Mean change

यदि $n$ observations का mean $M$ है और हर observation में $k$ जोड़ें:

$$\text{new mean}=M+k$$

यदि हर observation $k$ से multiply हो:

$$\text{new mean}=kM$$

यदि एक गलत value $a$ को $b$ से correct करें:

$$\text{corrected mean}=\frac{nM-a+b}{n}$$

**उदाहरण 12.** 10 numbers का mean 25 है। एक number 18 की जगह 28 होना चाहिए था। Correct mean?

$$\frac{10(25)-18+28}{10}=\mathbf{26}$$

---

## 1.10 :icon-bulb: Shortcuts और method map

### :icon-timer: Mean

$$Mean=\frac{\sum x}{n}$$

Frequency:

$$Mean=\frac{\sum xf}{\sum f}$$

### :icon-timer: Median position

- Odd $n$: $(n+1)/2$
- Even $n$: average of $n/2$ and $n/2+1$

### :icon-timer: Mode

Highest frequency वाली value।

### :icon-timer: Empirical relation

$$Mode=3Median-2Mean$$

### :icon-timer: Pie chart

$$angle=\frac{frequency}{total}\times360°$$

### :icon-timer: Mean correction

$$M_{new}=\frac{nM-old+new}{n}$$

### :icon-timer: Grouped mean

Class mark $=(lower+upper)/2$। फिर $xf$ table बनाइए।

### :icon-timer: Graph choice

- continuous data: histogram
- discrete categories: bar diagram
- cumulative data: ogive
- parts of whole: pie chart
- class midpoint trend: frequency polygon

---

## 1.11 :icon-warn: जाल (Traps)

> :icon-cross: **जाल 1.** Mean में frequencies ignore करना।
> Frequency data में $\sum xf/\sum f$ लगाइए।

> :icon-cross: **जाल 2.** Median निकालने से पहले data order न करना।
> Median हमेशा ordered position पर आधारित है।

> :icon-cross: **जाल 3.** Even data में एक middle value लेना।
> दो middle values का average लें।

> :icon-cross: **जाल 4.** Mode को सबसे बड़ा number मानना।
> Mode highest frequency वाला observation है।

> :icon-cross: **जाल 5.** Histogram में gaps छोड़ना।
> Continuous intervals के bars touch करते हैं।

> :icon-cross: **जाल 6.** Bar diagram और histogram को same मानना।
> Categories discrete हों तो bars separated होते हैं।

> :icon-cross: **जाल 7.** Pie chart angle में total frequency से divide न करना।
> $f/N\times360°$।

> :icon-cross: **जाल 8.** Class mark की जगह class upper limit लेना।
> Midpoint $(lower+upper)/2$ लें।

> :icon-cross: **जाल 9.** Missing frequency में total $N$ बदलना भूलना।
> Unknown frequency total में भी शामिल होगी।

> :icon-cross: **जाल 10.** Empirical relation को हर distribution पर exact मानना।
> यह approximate relation है; question context देखें।

---

## 1.12 :icon-exam: PYQ-pattern प्रश्न

> ये solved examples Railway परीक्षाओं में पूछे जाने वाले सामान्य patterns पर आधारित हैं; इन्हें किसी वर्ष के प्रश्नपत्र की verbatim copy न मानें। वास्तविक भर्ती का syllabus और question pattern संबंधित RRB notification से मिलाएँ।

**PYQ-pattern 1.** *(RRB NTPC)* $8,10,12,15,15$ का mean?

**हल:** $\mathbf{12}$।

**PYQ-pattern 2.** *(RRB Group D)* Ordered data $3,5,6,8,10,12,15,18,20$ का median?

**हल:** $\mathbf{10}$।

**PYQ-pattern 3.** *(RRB ALP)* Frequencies $3,6,12,5,2$ values $10,20,30,40,50$। Mode?

**हल:** $\mathbf{30}$।

**PYQ-pattern 4.** *(RPF SI)* Mean 25, median 27। Empirical mode?

**हल:** $3(27)-2(25)=\mathbf{31}$।

**PYQ-pattern 5.** *(RRB Technician)* Pie chart में total 200 और category 50। Angle?

**हल:** $\mathbf{90°}$।

**PYQ-pattern 6.** *(RRB NTPC)* 10 values का mean25; wrong18 को28 से replace करें। Correct mean?

**हल:** $\mathbf{26}$।

---

## 1.13 :icon-pencil: Railway अभ्यास प्रश्न (25 प्रश्न)

| # | प्रश्न | उत्तर | विधि |
|---:|---|---|---|
| 1 | $8,10,12,15,15$ mean | 12 | sum/5 |
| 2 | Ordered $3,5,6,8,10,12,15,18,20$ median | 10 | position 5 |
| 3 | Even data $4,7,9,12,15,18$ median | 10.5 | middle average |
| 4 | highest frequency value | mode | frequency |
| 5 | mean 25, median27 | mode31 | empirical relation |
| 6 | values 10,20,30; f 2,3,5 | mean23 | $\sum xf/\sum f$ |
| 7 | class $10-20$ midpoint | 15 | average limits |
| 8 | total 200, frequency50 pie angle | 90° | $f/N×360$ |
| 9 | pie angle72°, total250 | frequency50 | reverse formula |
| 10 | 10 values mean25; 18→28 | corrected mean26 | correction |
| 11 | histogram data type | continuous | touching bars |
| 12 | bar diagram data type | discrete | separated bars |
| 13 | polygon uses | class midpoints | join points |
| 14 | less-than ogive uses | cumulative frequency | curve |
| 15 | values 10,20,30,40,50; f 2,5,8,4,1 | mean28.5 | table |
| 16 | same table total frequency | 20 | sum f |
| 17 | same table sum xf | 570 | product sum |
| 18 | $f=2,x,5,3$, mean25 | x=8 | missing frequency |
| 19 | every value +5, mean20 | new mean25 | shift |
| 20 | every value ×3, mean12 | new mean36 | scale |
| 21 | mean of group 20 size60, group 30 mean70 | combined66 | weighted mean |
| 22 | class width $10$, f=20 | density2 | f/width |
| 23 | mode formula needs | modal, previous, next f | grouped mode |
| 24 | median formula needs | l, N/2, cf, f, h | grouped median |
| 25 | total frequency 40 median position | 20th/21st | even position |

---

## 1.14 :icon-trophy: अध्याय का सार

```
━━━ Mean ━━━
individual = sum x / n
frequency = sum xf / sum f
assumed mean = A + sum fd / sum f

━━━ Median ━━━
order data first
odd position = (n+1)/2
even = average of n/2 and n/2+1

grouped median = l + [(N/2−cf)/f]h

━━━ Mode ━━━
highest-frequency observation
Mode = 3 Median − 2 Mean (empirical)

━━━ Graphs ━━━
histogram: continuous, touching bars
bar diagram: discrete, gaps
frequency polygon: class midpoints joined
pie chart: f/N×360°
ogive: cumulative frequency

━━━ Corrections ━━━
new mean = (nM−old+new)/n
values +k → mean +k
values ×k → mean ×k

━━━ Missing frequency ━━━
mean condition:
sum xf = mean × sum f
```

> :icon-trophy: **Railway Statistics complete।** Mean, median, mode, frequency tables और सभी प्रमुख statistical diagrams अब एक connected exam system में covered हैं।
>
> **अगला Railway Maths topic:** Data Interpretation, Caselets, Data Sufficiency, P&C और Probability।
