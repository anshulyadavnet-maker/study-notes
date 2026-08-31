# StudyHub Point — PET Notes Authoring & PDF Style Guide

> **यह file PET notes लिखने का fixed content + formatting contract है।**
> सभी `/pet/*.md` files इसी structure का पालन करें ताकि `pdf-system/pet-notes-md2pdf.py` एक consistent PDF theme दे।

## 1. Core design rules

- Language: मुख्यतः सरल Hindi; आवश्यक exam terminology English में brackets में।
- Tone: concise, exam-focused, factual; अनावश्यक कहानी/लंबी भूमिका नहीं।
- Hierarchy: `#` = major subject/chapter, `##` = subtopic, `###` = concept, `####` = micro-point.
- एक heading में एक ही मुख्य concept रखें।
- पहले concept, फिर example/application, फिर exam point/trap।
- बड़े paragraphs से बचें; bullets, tables और short examples को प्राथमिकता दें।
- हर subject में एक जैसा structure रखें।
- Actual PYQ को newly-created practice questions से अलग रखें।

## 2. Fixed file naming

```text
pet/
├── 00-PET-Complete-Syllabus.md
├── 00-PET-Notes-Style-Guide.md
├── 01-History.md
├── 02-National-Movement.md
├── 03-Geography.md
├── 04-Indian-Economy.md
├── 05-Constitution-Public-Administration.md
├── 06-General-Science.md
├── 07-Arithmetic.md
├── 08-General-Hindi.md
├── 09-General-English.md
├── 10-Reasoning.md
├── 11-Current-Affairs.md
├── 12-General-Awareness.md
├── 13-Hindi-Passage.md
├── 14-Graph-Analysis.md
├── 15-Table-Analysis.md
├── 16-PET-Mixed-Revision.md
├── 17-PET-MCQ.md
└── 18-PET-PYQ.md
```

## 3. Standard subject structure

हर subject file का recommended skeleton:

```markdown
# 01. भारतीय इतिहास

> PET Focus: 5 अंक | High Priority

## 1. प्राचीन भारत

### 1.1 सिन्धु घाटी सभ्यता

#### प्रमुख तथ्य
- ...

#### परीक्षा में क्या याद रखें?
- ...

::: concept मूल अवधारणा
...
:::

::: example उदाहरण
...
:::

::: trick याद रखने की Trick
...
:::

::: tip परीक्षा Tip
...
:::

::: warning सावधानी
...
:::

::: formula सूत्र
...
:::

::: remember याद रखें
...
:::

::: pyq PYQ Focus
...
:::

## Quick Revision

| Point | Fact |
|---|---|
| ... | ... |

## Practice Check

1. ...
```

## 4. Semantic boxes — fixed vocabulary

**Box का नाम content के अर्थ के अनुसार चुनें; केवल decoration के लिए box न लगाएँ।**

| Syntax | उपयोग | Theme intent |
|---|---|---|
| `::: concept` | मूल अवधारणा | Core concept |
| `::: note` | अतिरिक्त clarification | Neutral note |
| `::: trick` | shortcut/mnemonic | Trick box |
| `::: tip` | exam strategy | Exam tip |
| `::: warning` | सावधानी | Warning |
| `::: trap` | common exam trap | Trap |
| `::: example` | solved/example case | Example |
| `::: formula` | formula/rule | Formula |
| `::: remember` | must-remember fact | Memory box |
| `::: pyq` | वास्तविक PYQ/theme | PYQ focus |
| `::: practice` | practice prompt | Practice |
| `::: fact` | one important fact | Fact |

### Example

```markdown
::: concept मौलिक अवधारणा
1857 का विद्रोह केवल एक सैन्य विद्रोह नहीं था; इसके पीछे अनेक राजनीतिक, आर्थिक, सामाजिक और सैन्य कारण थे।
:::

::: trick याद रखने की Trick
कारणों को **राजनीतिक → आर्थिक → सामाजिक → सैन्य** क्रम में याद करें।
:::

::: warning Exam Warning
किसी एक कारण को 1857 के विद्रोह का एकमात्र कारण न मानें।
:::

::: tip PET Tip
प्रश्न में “तात्कालिक कारण” और “दीर्घकालिक कारण” को अलग पहचानें।
:::
```

## 5. Heading colour system

Renderer subject heading के keywords देखकर accent लागू करेगा:

- History → brick/red
- National Movement → deeper brick/red
- Geography → green
- Economy → amber/gold
- Constitution/Public Administration → indigo
- General Science → red
- Arithmetic → blue
- Hindi → magenta/pink
- English → slate/indigo
- Reasoning → purple
- Current Affairs → red-orange
- General Awareness → teal
- Hindi Passage → blue-slate
- Graph Analysis → blue
- Table Analysis → blue

**इसलिए headings में subject का नाम स्पष्ट रखें।**

## 6. Colour meaning for boxes

रंग केवल semantic meaning बताएँ:

- 🔵 **Concept / Formula** — knowledge/structure
- 🟦 **Note** — neutral clarification
- 🟠 **Trick** — shortcut/mnemonic
- 🟢 **Tip / Remember** — exam action or memory
- 🔴 **Warning / Trap** — error/misconception/common confusion
- 🟣 **Example / PYQ** — application/evidence
- 🔷 **Practice** — student action
- 🟡 **Fact** — high-value factual recall

PDF renderer background/border/typography तय करेगा; Markdown author को inline colour codes या HTML colours नहीं लिखने हैं।

## 7. Icons

जहाँ common visual cue उपयोगी हो, renderer-compatible icon syntax इस्तेमाल करें:

```text
:icon-book:
:icon-lightbulb:
:icon-warning:
:icon-check:
```

**सिर्फ supported icons का प्रयोग करें।** Emoji की जगह SVG icon बेहतर है जहाँ renderer library में icon उपलब्ध हो।

## 8. SVG figures

Conceptual diagram के लिए common figure block इस्तेमाल करें:

```markdown
```figure
type: india-map-pet
caption: भारत का भौगोलिक क्षेत्र — PET revision figure
```
```

Figure का `type` केवल `figlib` में उपलब्ध renderer से होना चाहिए। नए figure types बनाते समय उन्हें पहले `pdf-system/figlib/` में register करें।

## 9. Tables

- 2–4 columns सामान्यतः बेहतर।
- बहुत चौड़ी tables को छोटे sub-tables में बाँटें।
- एक cell में बहुत लंबा paragraph न रखें।
- Comparison को table में दें।
- Facts के लिए `Point | Answer/Fact` format उपयोगी है।

## 10. Mathematics

- Formula को अलग `::: formula` box में रखें।
- Formula के बाद कम-से-कम एक short example दें।
- Calculation में units स्पष्ट रखें।
- बहुत लंबी calculation को steps में बाँटें।

## 11. Current Affairs

Current affairs में हर item के लिए:

```markdown
### घटना / विषय
- Date:
- Place:
- Organisation/Person:
- What happened:
- Why important for PET:

::: fact PET Fact
एक-line exam fact.
:::
```

पुरानी जानकारी को बिना date/source context के current affair के रूप में न लिखें।

## 12. PYQ policy

- **Actual PYQ:** year + exam/source उपलब्ध हो तो दें।
- **PYQ Theme:** यदि केवल theme/प्रश्न-पैटर्न लिया गया है तो उसे actual PYQ न लिखें।
- **Practice MCQ:** स्पष्ट रूप से Practice लिखें।

## 13. Content quality rules

1. तथ्य publish करने से पहले verify करें।
2. Ambiguous textbook terminology में छोटा clarification दें।
3. “सबसे महत्वपूर्ण” जैसे claims सीमित रखें।
4. Current information को static fact के रूप में freeze न करें।
5. एक ही fact की contradictory versions अलग files में न रखें।
6. Hindi spelling और terminology consistent रखें।
7. हर chapter के अंत में **Quick Revision** होना चाहिए।
8. बड़े chapter में **Common Traps** और **Exam Strategy** जोड़ें।

## 14. PDF rendering contract

`pet-notes-md2pdf.py` को ये जिम्मेदारियाँ निभानी हैं:

- A4 readable layout
- StudyHub Point cover
- fixed subject heading accents
- semantic box colours
- consistent margins/spacing
- tables kept readable
- page-break-inside avoidance for boxes/figures/tables जहाँ संभव हो
- Markdown → HTML → PDF
- existing `md2pdf.py` pipeline से SVG icons और figures reuse
- Devanagari-friendly font pipeline reuse
- no author-written inline CSS required

**Content author का काम:** semantic Markdown लिखना।  
**Renderer का काम:** colour, spacing, typography, borders, SVG placement और PDF print styling।

## 15. Final pre-commit checklist

- [ ] Heading hierarchy सही है
- [ ] Subject heading में पहचान योग्य keyword है
- [ ] Concept/Tip/Warning/Trick सही semantic box में है
- [ ] Actual PYQ और practice अलग हैं
- [ ] Tables बहुत चौड़ी नहीं हैं
- [ ] Figures के type supported हैं
- [ ] Icons supported हैं
- [ ] कोई inline colour/CSS नहीं है
- [ ] Hindi spelling check की गई है
- [ ] Facts verified हैं
- [ ] Chapter में Quick Revision है
- [ ] Chapter PDF में readable रहेगा

---

**StudyHub Point — PET Notes Standard**
