'''
course-extractor.py
Hussein Esmail
Created: 2022 09 19
Updated: 2022 09 19
Description: [DESCRIPTION]
'''

# This part is used for https://github.com/hussein-esmail7/template-maker
# templateDescription: Python Programming Document

import os
import sys
import platform
from PyPDF2 import PdfFileReader

# ========= VARIABLES ===========

# ========= COLOR CODES =========
from pdf_reader import pdf_reader

color_end               = '\033[0m'
color_darkgrey          = '\033[90m'
color_red               = '\033[91m'
color_green             = '\033[92m'
color_yellow            = '\033[93m'
color_blue              = '\033[94m'
color_pink              = '\033[95m'
color_cyan              = '\033[96m'
color_white             = '\033[97m'
color_grey              = '\033[98m'

# ========= COLORED STRINGS =========
str_prefix_q            = f"[{color_pink}Q{color_end}]\t "
str_prefix_y_n          = f"[{color_pink}y/n{color_end}]"
str_prefix_err          = f"[{color_red}ERROR{color_end}]\t "
str_prefix_done         = f"[{color_green}DONE{color_end}]\t "
str_prefix_info         = f"[{color_cyan}INFO{color_end}]\t "


def yes_or_no(str_ask):
    while True:
        y_n = input(f"{str_prefix_q} {str_prefix_y_n} {str_ask}").lower()
        if y_n[0] == "y":
            return True
        elif y_n[0] == "n":
            return False
        if y_n[0] == "q":
            sys.exit()
        else:
            print(f"{str_prefix_err} {error_neither_y_n}")

def get_platform():
    string = platform.platform().split("-")
    print(string)
    if "macOS" in string:
        return "macOS"
        # TODO: Account for Windows
        # TODO: Account for Linux
    else:
        return "UNKOWN"
def course_extractor(path):
    pdf = pdf_reader(path)
    pdf.extractor()
    course_code = ""
    return course_code


def main():
    # CODE HERE
    #print(get_platform())
    #sys.exit()
    path = '/Users/hrutikmehta0/My Drive/Programming/Course_Extractor/declaration.pdf'
    print(course_extractor(path))



if __name__ == "__main__":
    main()
