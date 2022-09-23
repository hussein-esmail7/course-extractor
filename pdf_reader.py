from PyPDF2 import PdfFileReader
import re

class pdf_reader:
    def __init__(self, path):
        self.pdf = PdfFileReader(path)

    def extractor(self):
        print(self.pdf.getPage(0).extractText())
        course_code = re.findall(r'[a-zA-Z]+[0-9]+', self.pdf.getPage(0).extractText())

        print(course_code)