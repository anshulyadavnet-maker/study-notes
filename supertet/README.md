# SUPER TET 2026 Notes

यह folder UP के प्राथमिक और उच्च प्राथमिक सहायक अध्यापक भर्ती परीक्षा के लिए बनाया जा रहा है। नए UPESSC syllabus update के बाद Primary और Junior/Upper Primary को अलग-अलग files में रखा गया है।

## अलग-अलग syllabus

1. 📄 **Primary — आधिकारिक UPESSC विषयवस्तु (शब्दशः):** [UP_Primary_1_5_Syllabus_2026.md](./UP_Primary_1_5_Syllabus_2026.md)
2. 📝 **Primary Level — व्याख्या + तैयारी (कक्षा 1–5):** [00-Primary-Level-Syllabus-2026.md](./00-Primary-Level-Syllabus-2026.md)
3. 📄 **Junior — आधिकारिक UPESSC विषयवस्तु (शब्दशः):** [UP_Junior_6_8_New_Syllabus_2026.md](./UP_Junior_6_8_New_Syllabus_2026.md)
4. 📝 **Junior / Upper Primary Level — व्याख्या + तैयारी (कक्षा 6–8):** [00-Junior-Level-Syllabus-2026.md](./00-Junior-Level-Syllabus-2026.md)
5. [Primary और Junior comparison index](./00-SUPER-TET-2026-Syllabus-and-Pattern.md)

> ✅ **Status (3 सितम्बर 2026):** Primary और Junior — **दोनों levels की आधिकारिक संरचना व विषयवस्तु प्राप्त है**; दोनों की files उसी से अद्यतन हैं।

## ✅ बन चुका है — सूचना तकनीकी (IT) — Primary Level

Primary के **सूचना तकनीकी (4 प्रश्न / 12 अंक)** section की पूरी सामग्री तैयार है:

| सामग्री | File | PDF |
|---|---|---|
| Syllabus + रणनीति | [supertet-it/00-IT-Syllabus-aur-Strategy.md](./supertet-it/00-IT-Syllabus-aur-Strategy.md) | — |
| पूर्ण नोट्स (8 अध्याय + 9 आकृतियाँ) | [supertet-it/01-Primary-Level-IT-Notes.md](./supertet-it/01-Primary-Level-IT-Notes.md) | [PDF/SuperTET-IT-Primary-Notes.pdf](../PDF/SuperTET-IT-Primary-Notes.pdf) |
| Solved Question Bank (114 प्रश्न) | [supertet-it/02-Primary-IT-Solved-Question-Bank.md](./supertet-it/02-Primary-IT-Solved-Question-Bank.md) | [PDF/SuperTET-IT-Primary-QuestionBank.pdf](../PDF/SuperTET-IT-Primary-QuestionBank.pdf) |
| सब एक साथ (COMPLETE) | — | [PDF/SuperTET-IT-COMPLETE.pdf](../PDF/SuperTET-IT-COMPLETE.pdf) |

> 📌 Notes में अब आकृतियाँ (` ```figure ` blocks — figlib) हैं, इसलिए IT के PDF **`pdf-system/md2pdf.py`** से बनाएँ (WeasyPrint + figlib — आकृतियाँ सहित)। पुराने PDF (md2pdf-hb से बने) में आकृतियाँ नहीं हैं — नए notes से दोबारा बनाएँ।

## ✅ बन चुका है — तार्किक ज्ञान (Logical Reasoning) — Primary + Junior

Reasoning की SuperTET-केंद्रित सामग्री तैयार है (आधिकारिक 18 topics की अपनी file — generic reasoning-book से अलग):

| सामग्री | File |
|---|---|
| **SuperTET Reasoning guide** (Primary 18 + Junior 8 official topics, हर topic: सूत्र + हल उदाहरण + आकृतियाँ, 10 प्रश्न TET अभ्यास, 5-प्रश्नों की 5/5 रणनीति) | [supertet_reasoning.md](../supertet_reasoning.md) |
| गहन स्रोत — सभी परीक्षाओं वाला generic reasoning-book (40 अध्याय) | [reasoning-book/](../reasoning-book/) |

> 📌 reasoning-book में जो SuperTET topics के लिए अलग अध्याय नहीं थे (Binary Logic, Grouping & Selections, TET-स्तरीय DI) — वे `supertet_reasoning.md` में पूरे हैं। आकृतियाँ ` ```figure ` blocks से हैं → PDF के लिए `pdf-system/md2pdf.py` (WeasyPrint/figlib) चाहिए, `md2pdf-hb.py` figures को placeholder दिखाता है।

## ✅ बन चुका है — विज्ञान (Science) — Primary + Junior

| सामग्री | File |
|---|---|
| Syllabus + रणनीति | [supertet-science/00-Syllabus-aur-Strategy.md](./supertet-science/00-Syllabus-aur-Strategy.md) |
| Primary विज्ञान Notes (10 अध्याय — 12 आधिकारिक अंश) | [supertet-science/01-Primary-Level-Science-Notes.md](./supertet-science/01-Primary-Level-Science-Notes.md) |
| Junior विज्ञान Notes (22 अध्याय — 22 आधिकारिक बिंदु, 1:1) | [supertet-science/02-Junior-Level-Science-Notes.md](./supertet-science/02-Junior-Level-Science-Notes.md) |

> 📌 Primary: **8 प्रश्न / 24 अंक**। Junior: "विज्ञान एवं गणित" 90-खण्ड में विज्ञान-भाग (official split नहीं; ~40–50 मानें)। Solved QB इस चरण में नहीं (बाद में बन सकता है); **PDFs इस repo से नहीं बनतीं — local env में `md2pdf.py` से बनाएँ**।

## Revised working pattern — दोनों levels

- 120 objective questions
- 360 total marks
- प्रत्येक सही उत्तर: 3 marks
- प्रत्येक गलत उत्तर: 1 mark negative marking
- समय: 2 घंटे / 120 मिनट
- 4 options और 1 correct answer
- Paper Hindi और English दोनों में

## सबसे महत्वपूर्ण अंतर

| Level | Pattern |
|---|---|
| **Primary (कक्षा 1–5)** | सभी subjects का fixed distribution: GK 25, Reasoning 5, Language 30, Science 8, Maths 16, EVS/Social Studies 8, Teaching Skills 8, Child Psychology 8, IT 4, Life Skills 8 |
| **Junior (कक्षा 6–8)** | एक प्रश्न पत्र, दो खण्ड — प्रथम खण्ड: GK/समसामयिक/तार्किक 30 (अनिवार्य) + द्वितीय खण्ड: चयनित subject 90 |

### Junior subject selection

- Language Teacher: हिन्दी, English या Sanskrit में से कोई एक
- Social Studies Teacher: Social Studies
- Science & Mathematics Teacher: Science और Mathematics

## Planned notes

1. Level-wise syllabus और exam strategy
2. Hindi, English और Sanskrit language notes
3. Mathematics और Science notes
4. Environment & Social Studies notes
5. Teaching Skills और Child Psychology
6. General Knowledge, UP GK और Current Affairs
7. ✅ Logical Knowledge → [supertet_reasoning.md](../supertet_reasoning.md) • Information Technology → [supertet-it/](./supertet-it/)
8. Life Skills, Management & Attitude
9. Level-wise PYQ, practice sets और full mocks

> **Verification note (3 सितम्बर 2026):** Primary व Junior — **दोनों levels की files UPESSC की आधिकारिक संरचना व विषयवस्तु** पर आधारित हैं (शब्दशः: `UP_Primary_1_5_Syllabus_2026.md` व `UP_Junior_6_8_New_Syllabus_2026.md`)। Final UPESSC recruitment notification/PDF में कोई बदलाव हो तो वही अंतिम मान्य होगा। पुराने 150-question/150-mark pattern को नए 120-question/360-mark pattern के साथ mix न करें।

## 🖨️ PDF कैसे बनाएँ (केवल तैयारी/developer के लिए — students को दी जाने वाली notes में ये instructions नहीं हैं)

- सभी SuperTET subjects की notes/QB को **अपने local env में** `python3 pdf-system/md2pdf.py` (WeasyPrint + figlib) से PDF बनाएँ — इसी engine से ` ```figure ` आकृतियाँ सही आती हैं।
- **Maths:** मौजूदा `PDF/SuperTET-Maths-*.pdf` पुराने (pre-overhaul) Markdown से बने हैं — maths की नई md files से दोबारा बनाएँ।
- `md2pdf-hb.py` (HarfBuzz) केवल तब है जब system में WeasyPrint न हो; उसमें figures placeholder दिखती हैं — final print के लिए उपयुक्त नहीं।
- सभी notes/QB/strategy files content-ही-content हैं; build commands, file names या folder structure कहीं student-facing content में नहीं दिखती।

### Sources checked

- [UPESSC official portal](https://upessc.up.gov.in/) — Primary व Junior official विषयवस्तु (आधार)
