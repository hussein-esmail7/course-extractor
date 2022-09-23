from PyPDF2 import PdfFileReader
import re

class pdf_reader:
    def __init__(self, path):
        self.pdf = PdfFileReader(path)

    def extractor(self):
        for i in range(0, self.pdf.getNumPages()):
            course_code = re.findall(r'[a-zA-Z]+[0-9]+', self.pdf.getPage(0).extractText())
        return course_code