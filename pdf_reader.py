from PyPDF2 import PdfFileReader
class pdf_reader:
    def __init__(self, path):
        self.pdf = PdfFileReader(path)
    def extractor(self):
        print(self.pdf.getDocumentInfo())