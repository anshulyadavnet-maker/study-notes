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
NOTES2PDF = HERE / "ctet-notes-md2pdf.py"
PET2PDF = HERE / "pet-notes-md2pdf.py"

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

def run_notes(cmd_args):
    runner = NOTES2PDF if NOTES2PDF.exists() else MD2PDF
    cmd = [sys.executable, str(runner)] + cmd_args
    print(f"\n[RUN NOTES] {' '.join(cmd_args)}")
    res = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if res.returncode != 0:
        print(f"  [ERROR] Command failed with code {res.returncode}")
    return res.returncode

def run_pet(cmd_args):
    runner = PET2PDF if PET2PDF.exists() else MD2PDF
    cmd = [sys.executable, str(runner)] + cmd_args
    print(f"\n[RUN PET] {' '.join(cmd_args)}")
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
            "--badge", "25 अध्याय", "--toc"
        ])
        run([
            str(M / '02-Junior-Level-Maths-Notes.md'),
            "-o", str(OUT_DIR / 'SuperTET-Maths-Junior-Notes.pdf'),
            "--title", "गणित नोट्स — जूनियर स्तर",
            "--subtitle", "SUPER TET · कक्षा 6–8",
            "--badge", "21 अध्याय", "--toc"
        ])
        run([
            str(M / '03-Primary-Solved-Question-Bank.md'),
            "-o", str(OUT_DIR / 'SuperTET-Maths-Primary-QuestionBank.pdf'),
            "--title", "हल प्रश्न-पत्र — प्राथमिक",
            "--subtitle", "SUPER TET · हल प्रश्न-बैंक",
            "--badge", "23 अध्याय", "--toc", "--qcols", "--flow"
        ])
        run([
            str(M / '04-Junior-Solved-Question-Bank.md'),
            "-o", str(OUT_DIR / 'SuperTET-Maths-Junior-QuestionBank.pdf'),
            "--title", "हल प्रश्न-पत्र — जूनियर",
            "--subtitle", "SUPER TET · हल प्रश्न-बैंक",
            "--badge", "19 अध्याय", "--toc", "--qcols", "--flow"
        ])
        run([
            str(M / '00-Syllabus-aur-Strategy.md'),
            "-o", str(OUT_DIR / 'Syllabus-aur-Strategy.pdf'),
            "--title", "पाठ्यक्रम एवं रणनीति",
            "--subtitle", "SUPER TET प्राथमिक एवं जूनियर स्तर",
            "--badge", "रणनीति", "--toc"
        ])
        run([
            str(M / '00-Syllabus-aur-Strategy.md'),
            str(M / '01-Primary-Level-Maths-Notes.md'),
            str(M / '03-Primary-Solved-Question-Bank.md'),
            str(M / '02-Junior-Level-Maths-Notes.md'),
            str(M / '04-Junior-Solved-Question-Bank.md'),
            "-o", str(OUT_DIR / 'SuperTET-Maths-COMPLETE.pdf'),
            "--title", "SUPER TET गणित",
            "--subtitle", "सम्पूर्ण पुस्तक — नोट्स + हल प्रश्न",
            "--badge", "प्राथमिक + जूनियर", "--toc", "--qcols", "--flow"
        ])

    # 1.1 SUPER TET IT (INFORMATION TECHNOLOGY)
    IT = REPO_ROOT / "supertet-it"
    if IT.exists():
        print("\n--- 1.1 SUPER TET IT -------------------------------")
        run([
            str(IT / '01-Primary-Level-IT-Notes.md'),
            "-o", str(OUT_DIR / 'SuperTET-IT-Primary-Notes.pdf'),
            "--title", "सूचना तकनीकी — प्राथमिक स्तर",
            "--subtitle", "SUPER TET · कक्षा 1–5 सम्पूर्ण IT नोट्स",
            "--badge", "8 अध्याय", "--toc", "--flow"
        ])
        run([
            str(IT / '02-Primary-IT-Solved-Question-Bank.md'),
            "-o", str(OUT_DIR / 'SuperTET-IT-Primary-QuestionBank.pdf'),
            "--title", "सूचना तकनीकी — प्रश्न-बैंक",
            "--subtitle", "SUPER TET प्राथमिक स्तर · 114 हल प्रश्न",
            "--badge", "8 अध्याय", "--toc", "--qcols", "--flow"
        ])
        run([
            str(IT / '00-IT-Syllabus-aur-Strategy.md'),
            str(IT / '01-Primary-Level-IT-Notes.md'),
            str(IT / '02-Primary-IT-Solved-Question-Bank.md'),
            "-o", str(OUT_DIR / 'SuperTET-IT-COMPLETE.pdf'),
            "--title", "SUPER TET सूचना तकनीकी",
            "--subtitle", "सम्पूर्ण अध्ययन सामग्री — नोट्स + 114 हल प्रश्न",
            "--badge", "प्राथमिक स्तर", "--toc", "--qcols", "--flow"
        ])

    # 1.2 SUPER TET REASONING
    STR = REPO_ROOT / "supertet_reasoning.md"
    if STR.exists():
        print("\n--- 1.2 SUPER TET REASONING ------------------------")
        run([
            str(STR),
            "-o", str(OUT_DIR / 'SuperTET-Reasoning-Notes.pdf'),
            "--title", "तार्किक ज्ञान — SUPER TET",
            "--subtitle", "Primary (18 टॉपिक्स) + Junior (8 टॉपिक्स) सम्पूर्ण अध्ययन गाइड",
            "--badge", "18 टॉपिक्स", "--toc", "--flow"
        ])

    # 1.3 SUPER TET SCIENCE
    SCI = REPO_ROOT / "supertet-science"
    if SCI.exists():
        print("\n--- 1.3 SUPER TET SCIENCE --------------------------")
        run([
            str(SCI / '01-Primary-Level-Science-Notes.md'),
            "-o", str(OUT_DIR / 'SuperTET-Science-Primary-Notes.pdf'),
            "--title", "विज्ञान नोट्स — प्राथमिक स्तर",
            "--subtitle", "SUPER TET · कक्षा 1–5 सम्पूर्ण विज्ञान अध्ययन सामग्री",
            "--badge", "10 अध्याय", "--toc", "--flow"
        ])
        run([
            str(SCI / '02-Junior-Level-Science-Notes.md'),
            "-o", str(OUT_DIR / 'SuperTET-Science-Junior-Notes.pdf'),
            "--title", "विज्ञान नोट्स — जूनियर स्तर",
            "--subtitle", "SUPER TET · कक्षा 6–8 विज्ञान एवं गणित शिक्षक",
            "--badge", "22 अध्याय", "--toc", "--flow"
        ])
        run([
            str(SCI / '00-Syllabus-aur-Strategy.md'),
            str(SCI / '01-Primary-Level-Science-Notes.md'),
            str(SCI / '02-Junior-Level-Science-Notes.md'),
            "-o", str(OUT_DIR / 'SuperTET-Science-COMPLETE.pdf'),
            "--title", "SUPER TET विज्ञान",
            "--subtitle", "सम्पूर्ण अध्ययन सामग्री — प्राथमिक (1–5) एवं जूनियर (6–8) स्तर",
            "--badge", "प्राथमिक + जूनियर", "--toc", "--flow"
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

    # 7. CTET REVISION NOTES
    CN = REPO_ROOT / "ctet-notes"
    if CN.exists():
        print("\n--- 7. CTET REVISION NOTES ------------------------")
        # Blueprint
        run_notes([
            str(CN / '00-CTET-Revision-Notes-Blueprint.md'),
            "-o", str(OUT_DIR / 'CTET-Revision-Notes-Blueprint.pdf'),
            "--title", "CTET Revision Notes Blueprint",
            "--subtitle", "पाठ्यक्रम एवं सम्पूर्ण नोट्स रूपरेखा",
            "--badge", "CTET", "--toc"
        ])
        # Paper I Subjects
        run_notes([
            str(CN / '01-CDP-Revision-Notes.md'),
            "-o", str(OUT_DIR / 'CTET-01-CDP-Revision-Notes.pdf'),
            "--title", "बाल विकास एवं शिक्षाशास्त्र (CDP) — Paper I",
            "--subtitle", "CTET Paper I (प्राथमिक स्तर) · सम्पूर्ण रिवीज़न नोट्स",
            "--badge", "CDP", "--toc"
        ])
        if (CN / '01-CDP-Revision-Notes-Pure-Hindi.md').exists():
            run_notes([
                str(CN / '01-CDP-Revision-Notes-Pure-Hindi.md'),
                "-o", str(OUT_DIR / 'CTET-01-CDP-Revision-Notes-Pure-Hindi.pdf'),
                "--title", "बाल विकास एवं शिक्षाशास्त्र — शुद्ध हिंदी",
                "--subtitle", "CTET Paper I (प्राथमिक स्तर) · सम्पूर्ण शुद्ध हिंदी रिवीज़न नोट्स",
                "--badge", "शुद्ध हिंदी", "--toc"
            ])
        run_notes([
            str(CN / '02-Paper-I-Mathematics-Revision-Notes.md'),
            "-o", str(OUT_DIR / 'CTET-02-Paper-I-Mathematics-Revision-Notes.pdf'),
            "--title", "गणित (Mathematics) — Paper I",
            "--subtitle", "CTET Paper I · सम्पूर्ण रिवीज़न नोट्स",
            "--badge", "गणित", "--toc"
        ])
        if (CN / '02-Paper-I-Mathematics-Revision-Notes-Pure-Hindi.md').exists():
            run_notes([
                str(CN / '02-Paper-I-Mathematics-Revision-Notes-Pure-Hindi.md'),
                "-o", str(OUT_DIR / 'CTET-02-Paper-I-Mathematics-Revision-Notes-Pure-Hindi.pdf'),
                "--title", "गणित — शुद्ध हिंदी",
                "--subtitle", "CTET Paper I (प्राथमिक स्तर) · सम्पूर्ण शुद्ध हिंदी रिवीज़न नोट्स",
                "--badge", "शुद्ध हिंदी", "--toc"
            ])
        run_notes([
            str(CN / '03-Paper-I-EVS-Revision-Notes.md'),
            "-o", str(OUT_DIR / 'CTET-03-Paper-I-EVS-Revision-Notes.pdf'),
            "--title", "पर्यावरण अध्ययन (EVS) — Paper I",
            "--subtitle", "CTET Paper I · सम्पूर्ण रिवीज़न नोट्स",
            "--badge", "EVS", "--toc"
        ])
        if (CN / '03-Paper-I-EVS-Revision-Notes-Pure-Hindi.md').exists():
            run_notes([
                str(CN / '03-Paper-I-EVS-Revision-Notes-Pure-Hindi.md'),
                "-o", str(OUT_DIR / 'CTET-03-Paper-I-EVS-Revision-Notes-Pure-Hindi.pdf'),
                "--title", "पर्यावरण अध्ययन — शुद्ध हिंदी",
                "--subtitle", "CTET Paper I (प्राथमिक स्तर) · सम्पूर्ण शुद्ध हिंदी रिवीज़न नोट्स",
                "--badge", "शुद्ध हिंदी", "--toc"
            ])
        run_notes([
            str(CN / '04-Language-I-Hindi-Revision-Notes.md'),
            "-o", str(OUT_DIR / 'CTET-04-Language-I-Hindi-Revision-Notes.pdf'),
            "--title", "हिन्दी भाषा (Language I)",
            "--subtitle", "CTET Paper I & II · सम्पूर्ण रिवीज़न नोट्स",
            "--badge", "हिन्दी", "--toc"
        ])
        run_notes([
            str(CN / '05-Language-II-English-Revision-Notes.md'),
            "-o", str(OUT_DIR / 'CTET-05-Language-II-English-Revision-Notes.pdf'),
            "--title", "English Language (Language II)",
            "--subtitle", "CTET Paper I & II · Comprehensive Revision Notes",
            "--badge", "English", "--toc"
        ])
        if (CN / '06-Language-II-Sanskrit-Revision-Notes.md').exists():
            run_notes([
                str(CN / '06-Language-II-Sanskrit-Revision-Notes.md'),
                "-o", str(OUT_DIR / 'CTET-06-Language-II-Sanskrit-Revision-Notes.pdf'),
                "--title", "संस्कृत भाषा (Language II)",
                "--subtitle", "CTET Paper I & II · सम्पूर्ण रिवीज़न नोट्स",
                "--badge", "संस्कृत", "--toc"
            ])
        # Paper II Subjects
        run_notes([
            str(CN / '07-Paper-II-CDP-Revision-Notes.md'),
            "-o", str(OUT_DIR / 'CTET-07-Paper-II-CDP-Revision-Notes.pdf'),
            "--title", "बाल विकास एवं शिक्षाशास्त्र (CDP) — Paper II",
            "--subtitle", "CTET Paper II (उच्च प्राथमिक स्तर 11–14 वर्ष) · सम्पूर्ण रिवीज़न नोट्स",
            "--badge", "Paper II CDP", "--toc"
        ])
        run_notes([
            str(CN / '08-Paper-II-Mathematics-Revision-Notes.md'),
            "-o", str(OUT_DIR / 'CTET-08-Paper-II-Mathematics-Revision-Notes.pdf'),
            "--title", "गणित (Mathematics) — Paper II",
            "--subtitle", "CTET Paper II (कक्षा 6–8) · सम्पूर्ण रिवीज़न नोट्स",
            "--badge", "Paper II Maths", "--toc"
        ])
        run_notes([
            str(CN / '09-Paper-II-Science-Revision-Notes.md'),
            "-o", str(OUT_DIR / 'CTET-09-Paper-II-Science-Revision-Notes.pdf'),
            "--title", "विज्ञान (Science) — Paper II",
            "--subtitle", "CTET Paper II (कक्षा 6–8) · सम्पूर्ण रिवीज़न नोट्स",
            "--badge", "Paper II Science", "--toc"
        ])
        run_notes([
            str(CN / '10-Paper-II-Social-Science-Revision-Notes.md'),
            "-o", str(OUT_DIR / 'CTET-10-Paper-II-Social-Science-Revision-Notes.pdf'),
            "--title", "सामाजिक अध्ययन / सामाजिक विज्ञान — Paper II",
            "--subtitle", "CTET Paper II (इतिहास, भूगोल, नागरिक शास्त्र + शिक्षाशास्त्र)",
            "--badge", "Paper II SST", "--toc"
        ])
        run_notes([
            str(CN / '11-Last-Minute-CTET-Revision-Sheets.md'),
            "-o", str(OUT_DIR / 'CTET-11-Last-Minute-Revision-Sheets.pdf'),
            "--title", "CTET Last-Minute Quick Revision Sheets",
            "--subtitle", "Paper I & II · Tag Words, Formulas, Key Points & Mindmaps",
            "--badge", "Last-Minute", "--toc"
        ])

        # Unified Complete Books
        run_notes([
            str(CN / '00-CTET-Revision-Notes-Blueprint.md'),
            str(CN / '01-CDP-Revision-Notes.md'),
            str(CN / '02-Paper-I-Mathematics-Revision-Notes.md'),
            str(CN / '03-Paper-I-EVS-Revision-Notes.md'),
            str(CN / '04-Language-I-Hindi-Revision-Notes.md'),
            str(CN / '05-Language-II-English-Revision-Notes.md'),
            str(CN / '11-Last-Minute-CTET-Revision-Sheets.md'),
            "-o", str(OUT_DIR / 'CTET-Paper-I-Complete-Revision-Notes.pdf'),
            "--title", "CTET Paper I सम्पूर्ण रिवीज़न नोट्स",
            "--subtitle", "CDP · गणित · EVS · हिन्दी · English + Last-Minute Sheets",
            "--badge", "Paper I Complete", "--toc", "--flow"
        ])
        run_notes([
            str(CN / '00-CTET-Revision-Notes-Blueprint.md'),
            str(CN / '07-Paper-II-CDP-Revision-Notes.md'),
            str(CN / '08-Paper-II-Mathematics-Revision-Notes.md'),
            str(CN / '09-Paper-II-Science-Revision-Notes.md'),
            str(CN / '04-Language-I-Hindi-Revision-Notes.md'),
            str(CN / '05-Language-II-English-Revision-Notes.md'),
            str(CN / '11-Last-Minute-CTET-Revision-Sheets.md'),
            "-o", str(OUT_DIR / 'CTET-Paper-II-Maths-Science-Complete-Notes.pdf'),
            "--title", "CTET Paper II गणित एवं विज्ञान सम्पूर्ण नोट्स",
            "--subtitle", "CDP · गणित · विज्ञान · हिन्दी · English + Last-Minute Sheets",
            "--badge", "Paper II Maths-Science", "--toc", "--flow"
        ])
        run_notes([
            str(CN / '00-CTET-Revision-Notes-Blueprint.md'),
            str(CN / '07-Paper-II-CDP-Revision-Notes.md'),
            str(CN / '10-Paper-II-Social-Science-Revision-Notes.md'),
            str(CN / '04-Language-I-Hindi-Revision-Notes.md'),
            str(CN / '05-Language-II-English-Revision-Notes.md'),
            str(CN / '11-Last-Minute-CTET-Revision-Sheets.md'),
            "-o", str(OUT_DIR / 'CTET-Paper-II-Social-Science-Complete-Notes.pdf'),
            "--title", "CTET Paper II सामाजिक विज्ञान सम्पूर्ण नोट्स",
            "--subtitle", "CDP · SST · हिन्दी · English + Last-Minute Sheets",
            "--badge", "Paper II SST", "--toc", "--flow"
        ])

    # 8. UPSSSC PET REVISION NOTES
    PET = REPO_ROOT / "pet"
    if PET.exists():
        print("\n--- 8. UPSSSC PET REVISION NOTES ------------------")
        if (PET / '00-PET-Complete-Syllabus.md').exists():
            run_pet([
                str(PET / '00-PET-Complete-Syllabus.md'),
                "-o", str(OUT_DIR / 'UPSSSC-PET-Complete-Syllabus.pdf'),
                "--title", "UPSSSC PET सम्पूर्ण पाठ्यक्रम एवं रणनीति",
                "--subtitle", "आधिकारिक पाठ्यक्रम एवं विषयवार अंक विभाजन (100 अंक · 15 विषय)",
                "--badge", "PET 2026", "--toc"
            ])
        ENG = PET / "09-General-English"
        if ENG.exists():
            run_pet([
                str(ENG / '01-Basic-Grammar.md'),
                "-o", str(OUT_DIR / 'PET-09-General-English-01-Basic-Grammar.pdf'),
                "--title", "General English — Basic Grammar",
                "--subtitle", "UPSSSC PET 2026 Detailed Notes · Part A to E",
                "--badge", "General English", "--toc"
            ])
            run_pet([
                str(ENG / '02-Vocabulary.md'),
                "-o", str(OUT_DIR / 'PET-09-General-English-02-Vocabulary.pdf'),
                "--title", "General English — Vocabulary",
                "--subtitle", "UPSSSC PET 2026 Detailed Notes · Synonyms, Antonyms, Idioms & OWS",
                "--badge", "General English", "--toc"
            ])
            run_pet([
                str(ENG / '03-Sentence-Ability.md'),
                "-o", str(OUT_DIR / 'PET-09-General-English-03-Sentence-Ability.pdf'),
                "--title", "General English — Sentence Ability",
                "--subtitle", "UPSSSC PET 2026 Detailed Notes · Spotting Errors, Improvement & Fillers",
                "--badge", "General English", "--toc"
            ])
            run_pet([
                str(ENG / '04-Reading-Comprehension.md'),
                "-o", str(OUT_DIR / 'PET-09-General-English-04-Reading-Comprehension.pdf'),
                "--title", "General English — Reading Comprehension",
                "--subtitle", "UPSSSC PET 2026 Detailed Notes · Unseen Passages & PYQ Strategy",
                "--badge", "General English", "--toc"
            ])
            # Unified Complete English Book
            run_pet([
                str(ENG / '01-Basic-Grammar.md'),
                str(ENG / '02-Vocabulary.md'),
                str(ENG / '03-Sentence-Ability.md'),
                str(ENG / '04-Reading-Comprehension.md'),
                "-o", str(OUT_DIR / 'UPSSSC-PET-General-English-COMPLETE.pdf'),
                "--title", "UPSSSC PET General English",
                "--subtitle", "सम्पूर्ण अंग्रेजी नोट्स — Grammar, Vocabulary, Sentence Ability & Comprehension",
                "--badge", "PET English Complete", "--toc", "--flow"
            ])
        MOCK = PET / "mock"
        if MOCK.exists():
            run_mcq([
                str(MOCK / '01-UPSSSC-PET-Mock-Test.md'),
                "-o", str(OUT_DIR / 'UPSSSC-PET-Mock-Test-01.pdf'),
                "--title", "UPSSSC PET 2026 — मॉक टेस्ट 01",
                "--subtitle", "100 प्रश्न · व्याख्या सहित हल (आधिकारिक ब्लूप्रिंट)",
                "--badge", "Mock Test 01", "--toc"
            ])
            run_mcq([
                str(MOCK / '02-UPSSSC-PET-Mock-Test.md'),
                "-o", str(OUT_DIR / 'UPSSSC-PET-Mock-Test-02.pdf'),
                "--title", "UPSSSC PET 2026 — मॉक टेस्ट 02",
                "--subtitle", "100 मिश्रित प्रश्न · व्याख्या सहित हल",
                "--badge", "Mock Test 02", "--toc"
            ])
            run_mcq([
                str(MOCK / '03-UPSSSC-PET-Mock-Test.md'),
                "-o", str(OUT_DIR / 'UPSSSC-PET-Mock-Test-03.pdf'),
                "--title", "UPSSSC PET 2026 — मॉक टेस्ट 03",
                "--subtitle", "100 मिश्रित प्रश्न · व्याख्या सहित हल",
                "--badge", "Mock Test 03", "--toc"
            ])
            run_mcq([
                str(MOCK / '04-UPSSSC-PET-Mock-Test.md'),
                "-o", str(OUT_DIR / 'UPSSSC-PET-Mock-Test-04.pdf'),
                "--title", "UPSSSC PET 2026 — मॉक टेस्ट 04",
                "--subtitle", "100 मिश्रित प्रश्न · व्याख्या सहित हल",
                "--badge", "Mock Test 04", "--toc"
            ])
            run_mcq([
                str(MOCK / '05-UPSSSC-PET-Mock-Test.md'),
                "-o", str(OUT_DIR / 'UPSSSC-PET-Mock-Test-05.pdf'),
                "--title", "UPSSSC PET 2026 — मॉक टेस्ट 05",
                "--subtitle", "100 मिश्रित प्रश्न · व्याख्या सहित हल",
                "--badge", "Mock Test 05", "--toc"
            ])
            # Unified Complete Mock Test Series
            run_mcq([
                str(MOCK / '01-UPSSSC-PET-Mock-Test.md'),
                str(MOCK / '02-UPSSSC-PET-Mock-Test.md'),
                str(MOCK / '03-UPSSSC-PET-Mock-Test.md'),
                str(MOCK / '04-UPSSSC-PET-Mock-Test.md'),
                str(MOCK / '05-UPSSSC-PET-Mock-Test.md'),
                "-o", str(OUT_DIR / 'UPSSSC-PET-5-Mock-Tests-COMPLETE.pdf'),
                "--title", "UPSSSC PET 2026 सम्पूर्ण मॉक टेस्ट सीरीज",
                "--subtitle", "5 पूर्ण मॉक टेस्ट · 500 प्रश्न (विस्तृत व्याख्या सहित हल)",
                "--badge", "500 MCQs · 5 Mocks", "--toc", "--flow"
            ])

    # 9. RAILWAY EXAM NOTES
    RW = REPO_ROOT / "railway"
    if RW.exists():
        print("\n--- 9. RAILWAY EXAM NOTES -------------------------")
        if (RW / '01-Statistics-Notes.md').exists():
            run([
                str(RW / '01-Statistics-Notes.md'),
                "-o", str(OUT_DIR / 'Railway-Statistics-Notes.pdf'),
                "--title", "Railway Maths — Statistics",
                "--subtitle", "RRB NTPC • Group D • ALP • Technician • RPF",
                "--badge", "Exam-Oriented Notes", "--toc", "--flow"
            ])

    # 10. DEMOS & EXAMPLES
    if (HERE / 'figure-demo.md').exists():
        print("\n--- 10. DEMOS & EXAMPLES --------------------------")
        run([
            str(HERE / 'figure-demo.md'),
            "-o", str(OUT_DIR / '00-FIGURE-DEMO.pdf'),
            "--title", "Figure Demo — ज्यामिति आकृति",
            "--subtitle", "Vector Diagrams & Callouts Demo",
            "--badge", "Demo"
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
