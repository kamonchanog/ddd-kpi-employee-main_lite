#!/usr/bin/env python3
"""Convert a PDF in input/ to Markdown. Tries markitdown → pymupdf → pypdf in order."""

import sys
from pathlib import Path


def _try_markitdown(pdf: Path) -> str:
    from markitdown import MarkItDown
    return MarkItDown().convert(str(pdf)).text_content


def _try_pymupdf(pdf: Path) -> str:
    import fitz
    doc = fitz.open(str(pdf))
    return "\n\n".join(page.get_text() for page in doc)


def _try_pypdf(pdf: Path) -> str:
    from pypdf import PdfReader
    reader = PdfReader(str(pdf))
    return "\n\n".join(p.extract_text() or "" for p in reader.pages)


CONVERTERS = [_try_markitdown, _try_pymupdf, _try_pypdf]
INSTALL_HINT = "pip install markitdown   # or: pip install pymupdf   # or: pip install pypdf"


def convert(pdf_path: str) -> None:
    pdf = Path(pdf_path)
    if not pdf.exists():
        sys.exit(f"Error: file not found — {pdf_path}")
    if pdf.suffix.lower() != ".pdf":
        sys.exit(f"Error: expected a .pdf file, got {pdf.suffix}")

    text = None
    for fn in CONVERTERS:
        try:
            text = fn(pdf)
            break
        except ImportError:
            continue

    if text is None:
        sys.exit(f"Error: no PDF library installed.\n{INSTALL_HINT}")

    md_path = pdf.with_suffix(".md")
    md_path.write_text(text.strip(), encoding="utf-8")
    print(f"Converted : {pdf.name} -> {md_path.name}")
    pdf.unlink()
    print(f"Removed   : {pdf.name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 scripts/pdf_to_md.py <path/to/file.pdf>")
    convert(sys.argv[1])
