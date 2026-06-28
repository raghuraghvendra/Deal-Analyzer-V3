import fitz


class PDFParser:

    def extract_text(self, pdf_path: str) -> str:
        doc = fitz.open(pdf_path)

        full_text = ""

        for page in doc:
            full_text += page.get_text()

        doc.close()

        return full_text