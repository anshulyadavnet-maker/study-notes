#!/usr/bin/env python3
"""
watermark.py — PDF Image Watermarking Tool and Pipeline Helper.

Applies a semi-transparent logo watermark centered on every page of generated PDFs.
Default settings: logo.png (fallback to C:\\Users\\ram-s\\OneDrive\\Documents\\logo.png), scale=1.0, opacity=0.08.
"""

import os
import sys
import glob
import io
import argparse
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
FALLBACK_LOGO_PATH = r"C:\Users\ram-s\OneDrive\Documents\logo.png"


def resolve_logo_path(custom_logo=None):
    """
    Resolves the logo path with priority:
    1. If a custom logo path was explicitly specified and exists, use it.
    2. Check 'logo.png' in current working directory.
    3. Check 'logo.png' in repository root.
    4. Check 'logo.png' in pdf-system directory.
    5. Fall back to 'C:\\Users\\ram-s\\OneDrive\\Documents\\logo.png'.
    """
    if custom_logo and custom_logo != "logo.png":
        if os.path.exists(custom_logo):
            return os.path.abspath(custom_logo)
        raise FileNotFoundError(f"Specified logo file not found: {custom_logo}")

    candidates = [
        os.path.abspath("logo.png"),
        str(REPO_ROOT / "logo.png"),
        str(HERE / "logo.png"),
        FALLBACK_LOGO_PATH,
    ]

    for p in candidates:
        if p and os.path.exists(p):
            return os.path.abspath(p)

    raise FileNotFoundError(
        f"Logo not found in local directory ({os.path.abspath('logo.png')}) "
        f"or fallback location ({FALLBACK_LOGO_PATH})."
    )


def process_watermark_image(image_path, opacity=0.08):
    """
    Load image, ensure RGBA format, adjust alpha channel to the target opacity,
    and return PNG bytes along with aspect ratio (h/w).
    """
    from PIL import Image

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Watermark image not found: {image_path}")

    with Image.open(image_path) as img:
        img = img.convert("RGBA")
        r, g, b, alpha = img.split()
        alpha = alpha.point(lambda p: int(p * opacity))
        img.putalpha(alpha)

        buf = io.BytesIO()
        img.save(buf, format="PNG")
        img_bytes = buf.getvalue()
        w, h = img.size

    aspect_ratio = h / w if w > 0 else 1.0
    return img_bytes, aspect_ratio


def apply_watermark_to_pdf(pdf_path, img_bytes=None, aspect_ratio=None, scale=1.0, opacity=0.08, logo_path=None):
    """
    Apply watermark image to every page in the given PDF file.
    If img_bytes is not provided, prepares it on the fly using logo_path and opacity.
    """
    import fitz  # PyMuPDF

    pdf_path = str(pdf_path)
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Target PDF file not found: {pdf_path}")

    if img_bytes is None or aspect_ratio is None:
        if logo_path is None:
            logo_path = resolve_logo_path()
        img_bytes, aspect_ratio = process_watermark_image(logo_path, opacity=opacity)

    doc = fitz.open(pdf_path)
    total_pages = len(doc)

    for idx in range(total_pages):
        page = doc[idx]
        rect = page.rect

        wm_w = rect.width * scale
        wm_h = wm_w * aspect_ratio

        # Center position on page
        cx, cy = rect.width * 0.5, rect.height * 0.5
        target_rect = fitz.Rect(
            cx - wm_w / 2,
            cy - wm_h / 2,
            cx + wm_w / 2,
            cy + wm_h / 2,
        )

        page.insert_image(
            target_rect,
            stream=img_bytes,
            overlay=True,
        )

    temp_output = pdf_path + ".tmp"
    doc.save(temp_output, deflate=True)
    doc.close()

    os.replace(temp_output, pdf_path)
    return total_pages


def auto_watermark_pdf(pdf_path, scale=1.0, opacity=0.08, logo_path=None):
    """
    Helper for automated post-processing in PDF pipelines.
    Gracefully applies watermark to all pages of the generated PDF file.
    """
    try:
        pages = apply_watermark_to_pdf(
            pdf_path,
            scale=scale,
            opacity=opacity,
            logo_path=logo_path,
        )
        return pages
    except Exception as e:
        print(f"  ! Watermark skipped or failed ({e})")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Apply image watermark to all PDF files in a directory or a specific PDF."
    )
    parser.add_argument(
        "--file",
        default=None,
        help="Path to a single PDF file to watermark"
    )
    parser.add_argument(
        "--logo",
        default="logo.png",
        help=f"Path to watermark image (default: logo.png, fallback: {FALLBACK_LOGO_PATH})"
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=1.0,
        help="Scale ratio relative to page width (default: 1.0)"
    )
    parser.add_argument(
        "--opacity",
        type=float,
        default=0.08,
        help="Watermark opacity from 0.0 to 1.0 (default: 0.08)"
    )
    parser.add_argument(
        "--dir",
        default=".",
        help="Target directory containing PDFs (default: current directory)"
    )

    args = parser.parse_args()

    try:
        logo_path = resolve_logo_path(args.logo)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    if args.file:
        pdf_files = [os.path.abspath(args.file)]
        target_desc = f"Single File: {args.file}"
    else:
        target_dir = os.path.abspath(args.dir)
        target_desc = f"Directory  : {target_dir}"
        pdf_files = sorted(glob.glob(os.path.join(target_dir, "*.pdf")))
        pdf_files = [f for f in pdf_files if not f.endswith(".tmp.pdf") and not f.endswith(".tmp")]

    print("=" * 60)
    print("             BATCH PDF WATERMARK TOOL                       ")
    print("=" * 60)
    print(target_desc)
    print(f"Logo Image : {logo_path}")
    print(f"Scale      : {args.scale}")
    print(f"Opacity    : {args.opacity}")
    print("-" * 60)

    if not pdf_files:
        print("No PDF files found to process.")
        return

    print(f"Found {len(pdf_files)} PDF file(s) to process.\n")

    try:
        img_bytes, aspect_ratio = process_watermark_image(logo_path, opacity=args.opacity)
    except Exception as e:
        print(f"Error preparing watermark image: {e}")
        sys.exit(1)

    total_watermarked_pages = 0
    success_count = 0

    for i, pdf_path in enumerate(pdf_files, 1):
        filename = os.path.basename(pdf_path)
        print(f"[{i}/{len(pdf_files)}] Processing: {filename} ...", end=" ", flush=True)
        try:
            pages = apply_watermark_to_pdf(pdf_path, img_bytes, aspect_ratio, scale=args.scale)
            total_watermarked_pages += pages
            success_count += 1
            print(f"Done ({pages} pages)")
        except Exception as e:
            print(f"Failed: {e}")

    print("-" * 60)
    print(f"Completed! {success_count}/{len(pdf_files)} files watermarked ({total_watermarked_pages} total pages).")
    print("=" * 60)


if __name__ == "__main__":
    main()
