#!/usr/bin/env python3
"""
build_all.py — Regenerate every PDF from markdown sources across all subjects.
Usage: python pdf-system/build_all.py
"""

import sys, os, subprocess
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
OUT_DIR = REPO_ROOT / "PDF"
OUT_DIR.mkdir(parents=True, exist_ok=True)

MD2PDF = HERE / "md2pdf.py"
MCQ2PDF = HERE / "mcqmdtopdf.py"

def run(cmd_args):
    cmd = [sys.executable, str(MD2PDF)] + cmd_args
    print(f"\n[RUN] {' '.join(cmd_args)}")
    res = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if res.returncode != 0:
        print(f"  [ERROR] Command failed with code {res.returncode}")
    return res.returncode

def run_mcq(cmd_args):
    runner = MCQ2PDF if MCQ2PDF.exists() else MD2PDF
    cmd = [sys.executable, str(runner)] + cmd_args
    print(f"\n[RUN MCQ] {' '.join(cmd_args)}")
    res = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if res.returncode != 0:
        print(f"  [ERROR] Command failed with code {res.returncode}")
    return res.returncode

def main():
    print("==================================================")
    print("       BUILDING ALL STUDY NOTES PDFS              ")
    print("==================================================")

    # 1. SUPER TET MATHS
    M = REPO_ROOT / "supertet-maths"
    if M.exists():
        print("\n--- 1. SUPER TET MATHS -----------------------------")
        run([
            str(M / '01-Primary-Level-Maths-Notes.md'),
            "-o", str(OUT_DIR / 'SuperTET-Maths-Primary-Notes.pdf'),
            "--title", "गणित नोट्स — प्राथमिक स्तर",
            "--subtitle", "SUPER TET · कक्षा 1–5",
            "--badge", "22 अध्याय", "--toc"
        ])
        run([
            str(M / '02-Junior-Level-Maths-Notes.md'),
            "-o", str(OUT_DIR / 'SuperTET-Maths-Junior-Notes.pdf'),
            "--title", "गणित नोट्स — जूनियर स्तर",
            "--subtitle", "SUPER TET · कक्षा 6–8",
            "--badge", "19 अध्याय", "--toc"
        ])
        run([
            str(M / '03-Primary-Solved-Question-Bank.md'),
            "-o", str(OUT_DIR / 'SuperTET-Maths-Primary-QuestionBank.pdf'),
            "--title", "हल प्रश्न-पत्र — प्राथमिक",
            "--subtitle", "SUPER TET · 221 हल प्रश्न",
            "--badge", "20 अध्याय", "--toc", "--qcols", "--flow"
        ])
        run([
            str(M / '04-Junior-Solved-Question-Bank.md'),
            "-o", str(OUT_DIR / 'SuperTET-Maths-Junior-QuestionBank.pdf'),
            "--title", "हल प्रश्न-पत्र — जूनियर",
            "--subtitle", "SUPER TET · 210 हल प्रश्न",
            "--badge", "17 अध्याय", "--toc", "--qcols", "--flow"
        ])
        run([
            str(M / '00-Syllabus-aur-Strategy.md'),
            str(M / '01-Primary-Level-Maths-Notes.md'),
            str(M / '03-Primary-Solved-Question-Bank.md'),
            str(M / '02-Junior-Level-Maths-Notes.md'),
            str(M / '04-Junior-Solved-Question-Bank.md'),
            "-o", str(OUT_DIR / 'SuperTET-Maths-COMPLETE.pdf'),
            "--title", "SUPER TET गणित",
            "--subtitle", "सम्पूर्ण पुस्तक — नोट्स + 431 हल प्रश्न",
            "--badge", "प्राथमिक + जूनियर", "--toc", "--qcols", "--flow"
        ])

    # 2. REASONING BOOK
    R = REPO_ROOT / "reasoning-book"
    if R.exists():
        print("\n--- 2. REASONING BOOK -----------------------------")
        run([
            str(R / '00-MASTER-Syllabus-Blueprint.md'),
            "-o", str(OUT_DIR / 'Reasoning-Syllabus-Blueprint.pdf'),
            "--title", "Reasoning ब्लूप्रिंट",
            "--subtitle", "SSC · UP Police · RRB · Banking · TET",
            "--badge", "40 अध्याय"
        ])
        run([
            str(R),
            "-o", str(OUT_DIR / 'Reasoning-COMPLETE.pdf'),
            "--title", "सम्पूर्ण Reasoning",
            "--subtitle", "सभी सरकारी परीक्षाओं हेतु एकीकृत पुस्तक",
            "--badge", "40 अध्याय · 6 भाग", "--toc", "--flow"
        ])

    # 3. MATHS MASTER
    MM = REPO_ROOT / "maths-master"
    if MM.exists():
        print("\n--- 3. MATHS MASTER -----------------------------")
        run([
            str(MM / '00-MASTER-Syllabus-Blueprint.md'),
            "-o", str(OUT_DIR / 'Maths-Master-Blueprint.pdf'),
            "--title", "गणित मास्टरी ब्लूप्रिंट",
            "--subtitle", "सभी प्रतियोगी परीक्षाओं के लिए",
            "--badge", "मास्टर सिलेबस"
        ])
        run([
            str(MM),
            "-o", str(OUT_DIR / 'Maths-Master-COMPLETE.pdf'),
            "--title", "सम्पूर्ण गणित मास्टरी",
            "--subtitle", "UPSC · SSC · RRB · Banking · State Exams",
            "--badge", "46 अध्याय", "--toc", "--flow"
        ])

    # 4. POLITY
    P = REPO_ROOT / "polity"
    if P.exists():
        print("\n--- 4. INDIAN POLITY -----------------------------")
        run([
            str(P),
            "-o", str(OUT_DIR / 'Indian-Polity-COMPLETE.pdf'),
            "--title", "भारतीय राजव्यवस्था",
            "--subtitle", "UPSC · State PSC · SSC · Railways",
            "--badge", "संवैधानिक ढांचा व मौलिक अधिकार", "--toc", "--flow"
        ])

    # 5. CTET MCQ
    C = REPO_ROOT / "ctet-mcq"
    if C.exists():
        print("\n--- 5. CTET MCQ -----------------------------------")
        run([
            str(C / '00-CTET-Detailed-Syllabus.md'),
            "-o", str(OUT_DIR / 'CTET-Detailed-Syllabus.pdf'),
            "--title", "CTET विस्तृत पाठ्यक्रम व परीक्षा योजना",
            "--subtitle", "Paper I व Paper II · CTET 2026",
            "--badge", "Official Blueprint", "--toc"
        ])
        run_mcq([
            str(C / '01-CDP-MCQ-Part-1.md'),
            str(C / '01-CDP-MCQ-Part-2.md'),
            "-o", str(OUT_DIR / 'CTET-CDP-MCQ.pdf'),
            "--title", "CTET बाल विकास एवं शिक्षाशास्त्र",
            "--subtitle", "सम्पूर्ण 200 अभ्यास प्रश्न (Part 1 + 2) · PYQ पैटर्न",
            "--badge", "200 MCQs", "--toc", "--flow"
        ])
        run_mcq([
            str(C / '02-Paper-I-Mathematics-MCQ-Part-1.md'),
            str(C / '02-Paper-I-Mathematics-MCQ-Part-2.md'),
            "-o", str(OUT_DIR / 'CTET-Paper-I-Mathematics-MCQ.pdf'),
            "--title", "CTET गणित (Paper I)",
            "--subtitle", "सम्पूर्ण 200 अभ्यास प्रश्न (Part 1 + 2) · PYQ पैटर्न",
            "--badge", "200 MCQs", "--toc", "--flow"
        ])
        run_mcq([
            str(C / '03-Paper-I-EVS-MCQ-Part-1.md'),
            str(C / '03-Paper-I-EVS-MCQ-Part-2.md'),
            "-o", str(OUT_DIR / 'CTET-Paper-I-EVS-MCQ.pdf'),
            "--title", "CTET पर्यावरण अध्ययन (EVS)",
            "--subtitle", "सम्पूर्ण 200 अभ्यास प्रश्न (Part 1 + 2) · PYQ पैटर्न",
            "--badge", "200 MCQs", "--toc", "--flow"
        ])
        run_mcq([
            str(C / '04-Language-I-Hindi-MCQ-Part-1.md'),
            str(C / '04-Language-I-Hindi-MCQ-Part-2.md'),
            "-o", str(OUT_DIR / 'CTET-Language-I-Hindi-MCQ.pdf'),
            "--title", "CTET भाषा I (हिन्दी)",
            "--subtitle", "सम्पूर्ण 200 अभ्यास प्रश्न (Part 1 + 2) · PYQ पैटर्न",
            "--badge", "200 MCQs", "--toc", "--flow"
        ])
        run_mcq([
            str(C / '05-Language-II-English-MCQ-Part-1.md'),
            str(C / '05-Language-II-English-MCQ-Part-2.md'),
            "-o", str(OUT_DIR / 'CTET-Language-II-English-MCQ.pdf'),
            "--title", "CTET Language II (English)",
            "--subtitle", "Complete 200 Practice MCQs (Part 1 + 2) · PYQ Pattern",
            "--badge", "200 MCQs", "--toc", "--flow"
        ])
        run_mcq([
            str(C / '05-Language-II-Punjabi-MCQ-Part-1.md'),
            str(C / '05-Language-II-Punjabi-MCQ-Part-2.md'),
            "-o", str(OUT_DIR / 'CTET-Language-II-Punjabi-MCQ.pdf'),
            "--title", "CTET Language II (ਪੰਜਾਬੀ Punjabi)",
            "--subtitle", "200 Practice MCQs (Part 1 + 2) · Gurmukhi + Hindi Clues",
            "--badge", "200 MCQs", "--toc", "--flow"
        ])
        run_mcq([
            str(C / '00-CTET-Detailed-Syllabus.md'),
            str(C / '01-CDP-MCQ-Part-1.md'),
            str(C / '01-CDP-MCQ-Part-2.md'),
            str(C / '02-Paper-I-Mathematics-MCQ-Part-1.md'),
            str(C / '02-Paper-I-Mathematics-MCQ-Part-2.md'),
            str(C / '03-Paper-I-EVS-MCQ-Part-1.md'),
            str(C / '03-Paper-I-EVS-MCQ-Part-2.md'),
            str(C / '04-Language-I-Hindi-MCQ-Part-1.md'),
            str(C / '04-Language-I-Hindi-MCQ-Part-2.md'),
            str(C / '05-Language-II-English-MCQ-Part-1.md'),
            str(C / '05-Language-II-English-MCQ-Part-2.md'),
            "-o", str(OUT_DIR / 'CTET-Paper-I-COMPLETE.pdf'),
            "--title", "CTET Paper I सम्पूर्ण प्रश्न बैंक",
            "--subtitle", "पाठ्यक्रम + CDP, गणित, EVS, हिन्दी, English (1000 MCQs)",
            "--badge", "1000 MCQs", "--toc", "--flow"
        ])

        # Paper II subjects
        run_mcq([
            str(C / '06-Paper-II-Mathematics-MCQ-Part-1.md'),
            str(C / '06-Paper-II-Mathematics-MCQ-Part-2.md'),
            "-o", str(OUT_DIR / 'CTET-Paper-II-Mathematics-MCQ.pdf'),
            "--title", "CTET Paper II Mathematics (English)",
            "--subtitle", "Complete 200 Practice MCQs (Content + Pedagogy)",
            "--badge", "200 MCQs", "--toc", "--flow"
        ])
        run_mcq([
            str(C / '06-Paper-II-Mathematics-Hindi-MCQ-Part-1.md'),
            str(C / '06-Paper-II-Mathematics-Hindi-MCQ-Part-2.md'),
            "-o", str(OUT_DIR / 'CTET-Paper-II-Mathematics-Hindi-MCQ.pdf'),
            "--title", "CTET गणित (Paper II हिन्दी)",
            "--subtitle", "सम्पूर्ण 200 अभ्यास प्रश्न (विषय + शिक्षाशास्त्र)",
            "--badge", "200 MCQs", "--toc", "--flow"
        ])
        run_mcq([
            str(C / '07-Paper-II-Science-MCQ-Part-1.md'),
            str(C / '07-Paper-II-Science-MCQ-Part-2.md'),
            "-o", str(OUT_DIR / 'CTET-Paper-II-Science-MCQ.pdf'),
            "--title", "CTET Paper II Science (English)",
            "--subtitle", "Complete 200 Practice MCQs (Content + Pedagogy)",
            "--badge", "200 MCQs", "--toc", "--flow"
        ])
        run_mcq([
            str(C / '07-Paper-II-Science-Hindi-MCQ-Part-1.md'),
            str(C / '07-Paper-II-Science-Hindi-MCQ-Part-2.md'),
            "-o", str(OUT_DIR / 'CTET-Paper-II-Science-Hindi-MCQ.pdf'),
            "--title", "CTET विज्ञान (Paper II हिन्दी)",
            "--subtitle", "सम्पूर्ण 200 अभ्यास प्रश्न (विषय + शिक्षाशास्त्र)",
            "--badge", "200 MCQs", "--toc", "--flow"
        ])
        run_mcq([
            str(C / '08-Paper-II-Social-Science-MCQ-Part-1.md'),
            str(C / '08-Paper-II-Social-Science-MCQ-Part-2.md'),
            "-o", str(OUT_DIR / 'CTET-Paper-II-Social-Science-MCQ.pdf'),
            "--title", "CTET Paper II Social Science (English)",
            "--subtitle", "Complete 200 Practice MCQs (History, Geo, Civics + Pedagogy)",
            "--badge", "200 MCQs", "--toc", "--flow"
        ])
        run_mcq([
            str(C / '08-Paper-II-Social-Science-Hindi-MCQ-Part-1.md'),
            str(C / '08-Paper-II-Social-Science-Hindi-MCQ-Part-2.md'),
            str(C / '08-Paper-II-Social-Science-Hindi-MCQ-Part-3.md'),
            str(C / '08-Paper-II-Social-Science-Hindi-MCQ-Part-4.md'),
            "-o", str(OUT_DIR / 'CTET-Paper-II-Social-Science-Hindi-MCQ.pdf'),
            "--title", "CTET सामाजिक अध्ययन / सामाजिक विज्ञान (Paper II)",
            "--subtitle", "सम्पूर्ण 400 अभ्यास प्रश्न (इतिहास, भूगोल, नागरिक शास्त्र + शिक्षाशास्त्र)",
            "--badge", "400 MCQs", "--toc", "--flow"
        ])

    print("\n==================================================")
    print("            BUILD COMPLETE                        ")
    print("==================================================")
    pdf_files = list(OUT_DIR.glob("*.pdf"))
    for pdf in sorted(pdf_files):
        mb = pdf.stat().st_size / 1024 / 1024
        print(f"  [PDF] {pdf.name:<45} {mb:6.2f} MB")

if __name__ == "__main__":
    main()
