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

def run(cmd_args):
    cmd = [sys.executable, str(MD2PDF)] + cmd_args
    print(f"\n[RUN] {' '.join(cmd_args)}")
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

    print("\n==================================================")
    print("            BUILD COMPLETE                        ")
    print("==================================================")
    pdf_files = list(OUT_DIR.glob("*.pdf"))
    for pdf in sorted(pdf_files):
        mb = pdf.stat().st_size / 1024 / 1024
        print(f"  [PDF] {pdf.name:<45} {mb:6.2f} MB")

if __name__ == "__main__":
    main()
