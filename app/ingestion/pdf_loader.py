import fitz
import easyocr
from PIL import Image
import io
import json
from pathlib import Path
import numpy as np


# Initialize OCR reader
reader = easyocr.Reader(['en'])


def is_scanned_pdf(text):

    """
    Detect if PDF page is scanned/image-based.
    """

    return len(text.strip()) < 30


def ocr_page(page):

    """
    Apply OCR on scanned PDF page.
    """

    pix = page.get_pixmap()

    img_bytes = pix.tobytes("png")

    image = Image.open(io.BytesIO(img_bytes))

    image_np = np.array(image)

    results = reader.readtext(image_np, detail=0)

    text = " ".join(results)

    return text


def extract_document(pdf_path):

    """
    Extract text from PDF with OCR fallback.
    """

    doc = fitz.open(pdf_path)

    pages = []

    for page_num in range(len(doc)):

        page = doc[page_num]

        text = page.get_text()

        scanned = is_scanned_pdf(text)

        if scanned:

            print(f"OCR applied on page {page_num + 1}")

            text = ocr_page(page)

        page_data = {

            "document_name": Path(pdf_path).name,

            "page_number": page_num + 1,

            "text": text,

            "is_scanned": scanned
        }

        pages.append(page_data)

    return pages


if __name__ == "__main__":

    pdf_path = "data/raw/Basic_Hydraulic_And_Components.pdf"

    pages = extract_document(pdf_path)

    output_path = "data/processed/output.json"

    with open(output_path, "w", encoding="utf-8") as f:

        json.dump(pages, f, indent=2, ensure_ascii=False)

    print(f"\nExtraction completed successfully!")
    print(f"Output saved to: {output_path}")