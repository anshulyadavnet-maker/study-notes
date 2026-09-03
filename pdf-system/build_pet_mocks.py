#!/usr/bin/env python3
"""
build_pet_mocks.py — Build print-ready PDFs for UPSSSC PET Mock Tests.
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

MCQ2PDF = HERE / "mcqmdtopdf.py"
MOCK_DIR = REPO_ROOT / "pet" / "mock"

def run_mcq(cmd_args):
    cmd = [sys.executable, str(MCQ2PDF)] + cmd_args
    print(f"\n[RUN MCQ] {' '.join(cmd_args)}")
    res = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if res.returncode != 0:
        print(f"  [ERROR] Command failed with code {res.returncode}")
    return res.returncode

def main():
    print("==================================================")
    print("       BUILDING UPSSSC PET MOCK TEST PDFS         ")
    print("==================================================")

    if not MOCK_DIR.exists():
        print(f"Directory not found: {MOCK_DIR}")
        return 1

    # Individual Mock Tests 01-05
    for i in range(1, 6):
        mock_file = MOCK_DIR / f"{i:02d}-UPSSSC-PET-Mock-Test.md"
        out_file = OUT_DIR / f"UPSSSC-PET-Mock-Test-{i:02d}.pdf"
        sub = "100 प्रश्न · व्याख्या सहित हल (आधिकारिक ब्लूप्रिंट)" if i == 1 else "100 मिश्रित प्रश्न · व्याख्या सहित हल"
        if mock_file.exists():
            run_mcq([
                str(mock_file),
                "-o", str(out_file),
                "--title", f"UPSSSC PET 2026 — मॉक टेस्ट {i:02d}",
                "--subtitle", sub,
                "--badge", f"Mock Test {i:02d}",
                "--toc"
            ])

    # Combined 5-Mock Complete Book
    all_mocks = [str(MOCK_DIR / f"{i:02d}-UPSSSC-PET-Mock-Test.md") for i in range(1, 6) if (MOCK_DIR / f"{i:02d}-UPSSSC-PET-Mock-Test.md").exists()]
    if all_mocks:
        run_mcq(all_mocks + [
            "-o", str(OUT_DIR / "UPSSSC-PET-5-Mock-Tests-COMPLETE.pdf"),
            "--title", "UPSSSC PET 2026 सम्पूर्ण मॉक टेस्ट सीरीज",
            "--subtitle", "5 पूर्ण मॉक टेस्ट · 500 प्रश्न (विस्तृत व्याख्या सहित हल)",
            "--badge", "500 MCQs · 5 Mocks",
            "--toc", "--flow"
        ])

    print("\n==================================================")
    print("            PET MOCKS BUILD COMPLETE              ")
    print("==================================================")
    for p in sorted(OUT_DIR.glob("UPSSSC-PET-Mock-Test-*.pdf")):
        mb = p.stat().st_size / (1024 * 1024)
        print(f"  [PDF] {p.name:<45} {mb:6.2f} MB")
    
    complete_pdf = OUT_DIR / "UPSSSC-PET-5-Mock-Tests-COMPLETE.pdf"
    if complete_pdf.exists():
        mb = complete_pdf.stat().st_size / (1024 * 1024)
        print(f"  [PDF] {complete_pdf.name:<45} {mb:6.2f} MB")

if __name__ == "__main__":
    main()
