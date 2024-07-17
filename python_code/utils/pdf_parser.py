import pdfplumber

class pdf_parser():

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.pages = []



    def parse_pdf(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            self.pages = [page.extract_text() for page in pdf.pages]

        return self.pages