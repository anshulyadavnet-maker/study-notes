# Railway Exam Notes

यह folder Railway भर्ती परीक्षाओं के लिए chapter-wise, exam-oriented notes के लिए है। सामग्री मुख्यतः RRB NTPC, RRB Group D, RRB ALP/Technician, RRB JE और RPF जैसे exams में उपयोगी common concepts पर केन्द्रित होगी। अलग-अलग notifications में syllabus और question weightage बदल सकता है, इसलिए आवेदन से पहले संबंधित RRB की official notification अवश्य देखें।

## उपलब्ध notes

1. [Statistics / सांख्यिकी](./01-Statistics-Notes.md) — data और frequency table, mean, median, mode, grouped data, histogram, bar diagram, pie chart, ogive, missing frequency, shortcuts, traps और Railway-pattern solved practice.

## आगे जोड़े जाने वाले Railway Maths chapters

> **स्पष्टता:** नीचे दिए गए topics Statistics के हिस्से नहीं हैं। ये Railway Maths के अलग-अलग chapters हैं।

- Number System और Simplification
- Percentage, Ratio और Average
- Profit-Loss, Simple/Compound Interest
- Time and Work, Time-Speed-Distance
- Data Interpretation और Probability

### Statistics में क्या-क्या शामिल है?

`01-Statistics-Notes.md` में Statistics के मुख्य topics हैं:

- Data, observation और frequency distribution
- Mean (माध्य), Median (मध्यका) और Mode (बहुलक)
- Grouped data, class mark और cumulative frequency
- Histogram, bar diagram, pie chart, ogive और frequency polygon
- Missing frequency और mean correction
- Statistical graphs की reading और comparison

> **Data Interpretation** Statistics से जुड़ा हुआ है, लेकिन Railway Maths में इसे अलग chapter रखना अधिक उपयोगी है। **Probability** Statistics से संबंधित mathematics है, पर इसका अलग concept और formula-set होता है।

## PDF में print करने का सही तरीका

यह chapter **notes** है, इसलिए इसके लिए general notes renderer इस्तेमाल करें:

```bash
python3 pdf-system/md2pdf.py \
  railway/01-Statistics-Notes.md \
  -o PDF/Railway-Statistics-Notes.pdf \
  --title "Railway Maths — Statistics" \
  --subtitle "RRB NTPC • Group D • ALP • Technician • RPF" \
  --badge "Exam-Oriented Notes" \
  --toc --flow
```

- `pdf-system/md2pdf.py` formulas, tables, callout boxes और vector SVG figures के लिए सबसे उपयुक्त है।
- `pdf-system/mcqmdtopdf.py` MCQ question banks के लिए है; इस notes chapter के लिए इसे इस्तेमाल न करें।
- `--qcols` न लगाएँ—notes को one-column layout में print करना formulas, tables और figures के लिए अधिक साफ़ रहेगा।

> Notes को सरल Hindi-English मिश्रित भाषा, formulas, tables, examples और quick-revision format में तैयार किया जा रहा है।
