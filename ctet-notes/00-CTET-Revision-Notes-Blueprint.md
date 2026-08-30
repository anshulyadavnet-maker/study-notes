# CTET Revision Notes — Master Blueprint

> **Audience:** Hindi-medium CTET students
>
> **Source of truth:** [CTET Detailed Syllabus & Exam Blueprint](../ctet-mcq/00-CTET-Detailed-Syllabus.md)
>
> यह folder syllabus को दोहराने के लिए नहीं, बल्कि exam से पहले fast, concept-based और print-friendly revision के लिए बनाया जा रहा है। Detailed syllabus में कोई official change हो तो पहले उसी file और latest CTET bulletin को update/check किया जाएगा।

---

## 1. Revision Notes का उद्देश्य

CTET revision notes में हर topic को short लेकिन complete form में दिया जाएगा:

1. **Core concept / definition**
2. **Important facts and rules**
3. **Classroom application**
4. **Common misconception / trap**
5. **PYQ-concept संकेत**
6. **Mini examples**
7. **Diagram, timeline, map या flowchart** जहाँ useful हो
8. **One-page quick revision box**
9. **Self-check questions**

> **Medium rule:** Main explanation Hindi में होगी। जरूरी exam terms English में brackets के साथ दिए जाएंगे, जैसे *assessment (मूल्यांकन)*, *scaffolding (सहारा)* और *inquiry (खोज-आधारित सीखना)*।

---

## 2. CTET Exam Snapshot

### Paper I — Primary Stage (Classes I–V)

| Section | Questions | Marks |
|---|---:|---:|
| Child Development and Pedagogy | 30 | 30 |
| Mathematics | 30 | 30 |
| Environmental Studies | 30 | 30 |
| Language I | 30 | 30 |
| Language II | 30 | 30 |
| **Total** | **150** | **150** |

### Paper II — Elementary Stage (Classes VI–VIII)

| Section | Questions | Marks |
|---|---:|---:|
| Child Development and Pedagogy | 30 | 30 |
| Mathematics & Science **or** Social Studies/Social Science | 60 | 60 |
| Language I | 30 | 30 |
| Language II | 30 | 30 |
| **Total** | **150** | **150** |

### Common official points

- प्रत्येक paper में 150 MCQs और 150 marks होते हैं।
- प्रत्येक सही answer 1 mark का होता है।
- Wrong या unattempted answer के लिए negative marking नहीं है।
- Paper की duration 2 hours 30 minutes है।
- Language II, Language I से अलग language होनी चाहिए।
- Paper I का content मुख्यतः NCERT Classes I–V और Paper II का content NCERT Classes VI–VIII से linked है।
- Questions facts के साथ concepts, application, problem-solving और pedagogy को भी test करते हैं।

---

## 3. Notes बनाने का Standard Format

हर revision chapter/file का format:

```text
1. Topic overview
2. Syllabus checklist
3. Core theory
4. Important terms
5. Rules / facts / tables
6. Diagram or flowchart (if useful)
7. Classroom examples
8. Common mistakes and traps
9. PYQ-concept patterns
10. Quick revision sheet
11. 10–20 self-check questions
```

### Print-friendly rules

- छोटे paragraphs और clear headings
- Important facts के लिए tables
- Long theory को bullet points में बदलना
- Hindi explanation के साथ standard English terms
- Figures केवल learning value होने पर
- हर topic के अंत में **Last-Minute Revision Box**
- Revision notes के लिए `pdf-system/ctet-notes-md2pdf.py`
- MCQ banks के लिए `pdf-system/mcqmdtopdf.py`

### Revision notes PDF command

```bash
python3 pdf-system/ctet-notes-md2pdf.py \\
  ctet-notes/00-CTET-Revision-Notes-Blueprint.md \\
  -o PDF/CTET-Revision-Notes-Blueprint.pdf \\
  --title "CTET Revision Notes" \\
  --subtitle "Hindi-medium exam revision" \\
  --badge "CTET" --toc --flow
```

`ctet-notes-md2pdf.py` में `SECTION_STYLES` mapping section keywords और colours control करती है। जब कोई नया notes section बनाया जाए, उसकी keyword और preferred colour उसी mapping में add करें; unknown headings के लिए generic style automatically लागू रहेगी।

---

# PART A — Paper I Revision Notes

## 4. Child Development and Pedagogy — Paper I

### Main note units

1. Child development और learning का relationship
2. Development के principles
3. Heredity और environment
4. Socialisation: family, peers और teacher
5. Piaget, Vygotsky, Kohlberg और अन्य thinkers
6. Child-centred और progressive education
7. Intelligence और individual differences
8. Language and thought
9. Gender, diversity और inclusion
10. Assessment for learning / assessment of learning
11. CCE और School-Based Assessment
12. Learning difficulties और Children with Special Needs
13. Motivation, cognition और emotions
14. Errors as learning evidence
15. Diagnostic और remedial teaching

### Revision lens

> **Most appropriate teacher response:** Child को label, punish या compare करने के बजाय उसकी thinking समझें, evidence लें, scaffold दें और अगला learning step plan करें।

## 5. Paper I Mathematics

### Content units

- Numbers और number sense
- Addition, subtraction, multiplication और division
- Fractions और decimals
- Shapes और spatial understanding
- Solids around us
- Measurement, weight, time और volume
- Money, patterns और data handling

### Pedagogy units

- Nature of Mathematics
- Logical thinking
- Children की strategies
- Multiple methods
- Language of Mathematics
- Community Mathematics
- Error analysis
- Diagnostic और remedial teaching
- Activity-based learning
- Assessment और feedback

## 6. Paper I EVS

### Content themes

- Family and Friends
- Food
- Shelter
- Water
- Travel
- Things We Make and Do

### Pedagogy lens

- EVS का integrated nature
- Observation और inquiry
- Discussion और questioning
- Activity, experiment और field visit
- Local knowledge और community resources
- Project work
- Assessment और remedial teaching

---

# PART B — Paper II Revision Notes

## 7. Common CDP — Elementary Stage

Paper II CDP notes में 11–14 years learners पर focus रहेगा:

- Development and learning
- Inclusive education
- Learning difficulties and impairments
- Adolescence-related classroom needs
- Piaget, Vygotsky, Kohlberg
- Intelligence, motivation और self-efficacy
- Constructivism और social learning
- Errors, misconceptions और assessment
- Learner diversity और differentiated support

## 8. Paper II Mathematics

### Content

- Number System
- Integers और fractions
- Algebra
- Ratio and proportion
- Geometry और elementary shapes
- Symmetry
- Construction: scale, straight edge, protractor और compass
- Perimeter, area और volume
- Tables, pictorial data और bar graphs

### Pedagogy

- Mathematical reasoning
- Child strategies और alternative methods
- Concrete–representational–abstract progression
- Mathematical language
- Curriculum और progression
- Community Mathematics
- Error analysis
- Diagnostic/remedial teaching
- Evaluation और feedback

## 9. Paper II Science

### Content

- Food
- Materials और separation
- The World of the Living
- Plants, animals और human body
- Moving Things, People and Ideas
- How Things Work: electricity, circuits और magnets
- Light, shadows और reflection
- Natural phenomena और sky
- Air, water, soil और natural resources

### Pedagogy

- Nature and aims of Science
- Scientific inquiry
- Observation, prediction और experimentation
- Variables और fair test
- Evidence और explanation
- Integrated Science
- Teaching aids और models
- Cognitive, psychomotor और affective assessment
- Misconceptions, inclusion और remedial teaching

## 10. Paper II Social Studies/Social Science

### Content

- **History:** early societies से India after Independence तक
- **Geography:** Earth, globe, environment, air, water, resources, agriculture, settlement, transport और communication
- **Social and Political Life/Civics:** diversity, government, local government, livelihood, democracy, State Government, media, gender, Constitution, Parliament, judiciary और social justice

### Pedagogy

- Nature and concept of Social Science
- Classroom processes, activities और discourse
- Critical thinking
- Enquiry और empirical evidence
- Primary और secondary sources
- Timelines, maps और local resources
- Projects और fieldwork
- Multiple perspectives
- Democratic classroom
- Evaluation, inclusion और remedial teaching

> **SST revision rule:** History में chronology + cause/effect, Geography में map/scale + human-environment relation, और Civics में institution + rights + accountability को साथ revise करें।

---

# PART C — Language Revision Notes

## 11. Language I — Hindi

- Unseen prose और poetry comprehension
- Main idea, title, fact, inference
- शब्दार्थ, पर्यायवाची, विलोम
- Grammar और verbal ability
- Language acquisition और learning
- Listening, speaking, reading और writing
- Multilingual classroom
- Language errors और remedial teaching
- Assessment, textbook और teaching-learning materials

## 12. Language II — English

- Unseen prose/poetry comprehension
- Vocabulary और grammar in context
- Listening-speaking activities
- Reading strategies
- Process writing
- English as an additional language
- Multilingual and inclusive classroom
- Language assessment and remediation

## 13. Language II — Punjabi (Optional Bank)

यदि learner ने Punjabi चुनी है तो notes और practice bank में:

- Punjabi Gurmukhi comprehension
- Hindi सहायता / bridge explanation
- Punjabi grammar और vocabulary
- Listening-speaking-reading-writing
- Punjabi language pedagogy
- Multilingual classroom support
- Language errors, assessment और remedial teaching

---

# PART D — Existing MCQ Source Map

Revision notes बनाते समय existing question banks को application practice के लिए use किया जाएगा:

| Source bank | Available practice |
|---|---|
| `ctet-mcq/01-CDP-MCQ-Part-1.md` और `Part-2.md` | 200 CDP MCQs |
| `ctet-mcq/02-Paper-I-Mathematics-*` | 200 Paper I Mathematics MCQs |
| `ctet-mcq/03-Paper-I-EVS-*` | 200 Paper I EVS MCQs |
| `ctet-mcq/04-Language-I-Hindi-*` | 200 Hindi Language I MCQs |
| `ctet-mcq/05-Language-II-English-*` | 200 English Language II MCQs |
| `ctet-mcq/05-Language-II-Punjabi-*` | 200 Punjabi + Hindi-help MCQs |
| `ctet-mcq/06-Paper-II-Mathematics-*` | English + Hindi Mathematics MCQs |
| `ctet-mcq/07-Paper-II-Science-*` | English + Hindi Science MCQs |
| `ctet-mcq/08-Paper-II-Social-Science-*` | English + Hindi SST MCQs |

> MCQs और revision notes अलग resources हैं: **notes concept समझाएँगे; MCQs recall, application और exam decision-making practise कराएँगे।**

---

# PART E — Planned Revision-Notes Files

```text
ctet-notes/
├── 00-CTET-Revision-Notes-Blueprint.md   ← यह file
├── 01-CDP-Revision-Notes.md              ← first completed revision notes file
├── 02-Paper-I-Mathematics-Revision-Notes.md
├── 03-Paper-I-EVS-Revision-Notes.md
├── 04-Language-I-Hindi-Revision-Notes.md     ← completed revision notes file
├── 05-Language-II-English-Revision-Notes.md  ← completed revision notes file
├── 06-Language-II-Punjabi-Revision-Notes.md
├── 07-Paper-II-CDP-Revision-Notes.md          ← completed revision notes file
├── 08-Paper-II-Mathematics-Revision-Notes.md
├── 09-Paper-II-Science-Revision-Notes.md
├── 10-Paper-II-Social-Science-Revision-Notes.md
└── 11-Last-Minute-CTET-Revision-Sheets.md
```

### Recommended creation order

1. Paper II CDP
2. Paper II Social Science / Science / Mathematics — learner’s chosen option
3. Paper I CDP
4. Mathematics and EVS
5. Language notes
6. Last-minute mixed revision sheets

---

# Final Revision Strategy

```text
Step 1: Read the short concept note
Step 2: Study the diagram/table/example
Step 3: Solve related MCQs
Step 4: Analyse the wrong answer
Step 5: Revise the common trap
Step 6: Attempt a timed mixed set
Step 7: Make a one-page final revision sheet
```

> **Golden rule:** CTET में केवल “क्या” याद करना पर्याप्त नहीं है। यह भी समझना है कि **बच्चा कैसे सोचता है, teacher को क्या करना चाहिए, evidence कैसे पढ़ना है और concept को नई situation में कैसे apply करना है।**
