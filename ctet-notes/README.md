# CTET Notes — folder README (developer / printing instructions)

> 🖨️ **Students को दी जाने वाली notes में printing/tooling instructions नहीं हैं।**
> यह README केवल तैयारी (content-creation, build, print) के लिए है।

## Folder contents

- `00-CTET-Revision-Notes-Blueprint.md` — मास्टर योजना: exam snapshot, notes format, revision content का outline (Part A–E)। Students भी इसकी संरचना देख सकते हैं; कोई build-निर्देश इसमें नहीं है।
- `01-CDP-Revision-Notes.md` (+ `Pure-Hindi` variant) — Paper I CDP revision notes
- `02-Paper-I-Mathematics-Revision-Notes.md` (+ `Pure-Hindi` variant)
- `03-Paper-I-EVS-Revision-Notes.md` (+ `Pure-Hindi` variant)
- `04-Language-I-Hindi-Revision-Notes.md`
- `05-Language-II-English-Revision-Notes.md`
- `06-Language-II-Punjabi-Revision-Notes.md` — planned
- `07-Paper-II-CDP-Revision-Notes.md`
- `08-Paper-II-Mathematics-Revision-Notes.md`
- `09-Paper-II-Science-Revision-Notes.md`
- `10-Paper-II-Social-Science-Revision-Notes.md`
- `11-Last-Minute-CTET-Revision-Sheets.md`

## MCQ practice source map (authoring के समय use करें)

| Subject bank | Available practice |
|---|---|
| CDP (`01-CDP-MCQ-Part-1/2.md`) | 200 CDP MCQs |
| Paper I Mathematics (`02-Paper-I-Mathematics-MCQ-Part-1/2.md`) | 200 Paper I Mathematics MCQs |
| Paper I EVS (`03-Paper-I-EVS-MCQ-Part-1/2.md`) | 200 Paper I EVS MCQs |
| Language I Hindi (`04-Language-I-Hindi-MCQ-Part-1/2.md`) | 200 Hindi Language I MCQs |
| Language II English (`05-Language-II-English-MCQ-Part-1/2.md`) | 200 English Language II MCQs |
| Language II Punjabi (`05-Language-II-Punjabi-MCQ-Part-1/2.md`) | 200 Punjabi + Hindi-help MCQs |
| Paper II Mathematics (`06-Paper-II-Mathematics-*`) | English + Hindi Mathematics MCQs |
| Paper II Science (`07-Paper-II-Science-*`) | English + Hindi Science MCQs |
| Paper II Social Science (`08-Paper-II-Social-Science-*`) | English + Hindi SST MCQs |

## Print / PDF (केवल local env में)

PDFs इस repo से नहीं बनाई जातीं — अपने local env में बनाएँ:

```bash
# Revision notes / books
python3 pdf-system/md2pdf.py <notes-file> -o PDF/<name>.pdf --title "..." --toc --flow

# CTET MCQ question banks
python3 pdf-system/mcqmdtopdf.py <mcq-file> -o PDF/<name>.pdf

# पुराना CTET-notes-specific script (SECTION_STYLES mapping control करता है)
python3 pdf-system/ctet-notes-md2pdf.py ctet-notes/<file>.md \
  -o PDF/<name>.pdf --title "CTET Revision Notes" \
  --subtitle "Hindi-medium exam revision" --badge "CTET" --toc --flow
```

- `ctet-notes-md2pdf.py` में `SECTION_STYLES` mapping section keywords और colours control करती है। जब कोई नया notes section बनाया जाए, उसकी keyword और preferred colour उसी mapping में add करें; unknown headings के लिए generic style automatically लागू रहेगी।
- Students को दी जाने वाली `.md` notes कभी भी build commands / file names / folder structure expose न करें — internal tooling सिर्फ़ READMEs में।
