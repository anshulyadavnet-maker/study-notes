#!/usr/bin/env bash
# build-all.sh — regenerate every PDF from the markdown sources.
# usage:  bash pdf-system/build-all.sh
set -e
cd "$(dirname "$0")"
PY="python3 md2pdf.py"
OUT="$HOME/PDF"
mkdir -p "$OUT"

M="$HOME/supertet-maths"
R="$HOME/reasoning-book"

echo "── SUPER TET MATHS ─────────────────────────────"
$PY "$M/01-Primary-Level-Maths-Notes.md" -o "$OUT/SuperTET-Maths-Primary-Notes.pdf" \
   --title "गणित नोट्स — प्राथमिक स्तर" --subtitle "SUPER TET · कक्षा 1–5" --badge "22 अध्याय" --toc

$PY "$M/02-Junior-Level-Maths-Notes.md" -o "$OUT/SuperTET-Maths-Junior-Notes.pdf" \
   --title "गणित नोट्स — जूनियर स्तर" --subtitle "SUPER TET · कक्षा 6–8" --badge "19 अध्याय" --toc

$PY "$M/03-Primary-Solved-Question-Bank.md" -o "$OUT/SuperTET-Maths-Primary-QuestionBank.pdf" \
   --title "हल प्रश्न-पत्र — प्राथमिक" --subtitle "SUPER TET · 221 हल प्रश्न" --badge "20 अध्याय" --toc --qcols --flow

$PY "$M/04-Junior-Solved-Question-Bank.md" -o "$OUT/SuperTET-Maths-Junior-QuestionBank.pdf" \
   --title "हल प्रश्न-पत्र — जूनियर" --subtitle "SUPER TET · 210 हल प्रश्न" --badge "17 अध्याय" --toc --qcols --flow

# complete maths book (all four merged)
$PY "$M/00-Syllabus-aur-Strategy.md" "$M/01-Primary-Level-Maths-Notes.md" \
    "$M/03-Primary-Solved-Question-Bank.md" "$M/02-Junior-Level-Maths-Notes.md" \
    "$M/04-Junior-Solved-Question-Bank.md" \
   -o "$OUT/SuperTET-Maths-COMPLETE.pdf" \
   --title "SUPER TET गणित" --subtitle "सम्पूर्ण पुस्तक — नोट्स + 431 हल प्रश्न" \
   --badge "प्राथमिक + जूनियर" --toc --qcols --flow

echo "── REASONING ───────────────────────────────────"
$PY "$R/00-MASTER-Syllabus-Blueprint.md" -o "$OUT/Reasoning-Syllabus-Blueprint.pdf" \
   --title "Reasoning ब्लूप्रिंट" --subtitle "SSC · UP Police · RRB · Banking · TET" --badge "40 अध्याय"

$PY "$R" -o "$OUT/Reasoning-COMPLETE.pdf" \
   --title "सम्पूर्ण Reasoning" --subtitle "सभी सरकारी परीक्षाओं हेतु एकीकृत पुस्तक" \
   --badge "40 अध्याय · 6 भाग" --toc --flow

echo
echo "── DONE ────────────────────────────────────────"
ls -lh "$OUT"/*.pdf | awk '{printf "  %-52s %s\n",$9,$5}'
