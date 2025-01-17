!pip install PyMuPDF
!pip install PyPDF2
import fitz
import PyPDF2

def check_for_material_number(material_no):
    n1= "94-1234-001"    #Files taken here are for example
    n2 = "94-5678-001"
    n3 = "94-4321-001"
    if material_no == n1:
      return "/content/TECHNICAL LIBRARY/94-1234-001_LPI.pdf"
    elif material_no == n2:
      return "/content/TECHNICAL LIBRARY/94-5678-001_LPI.pdf"
    elif material_no == n3:
      return "/content/TECHNICAL LIBRARY/94-4321-001_LPI.pdf"


def extract_lpi(keyword, pdf_path):
    keyword = keyword.upper()
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if keyword in line:
                    print(f"Keyword '{keyword}' found on page {page_num}, line {i}: {lines[i + 1]}")
                    line = lines[i + 1]
                    return line


def find_and_print_part_numbers(description):
    description = description.upper()
    found = False
    numbers_found = []

    for desc, numbers in parts_list:
        if desc == description:
            print(f"Part number(s) for '{description}': {', '.join(numbers)}")
            found = True
            numbers_found.extend(numbers)

    if not found:
        print(f"No part number found for the description '{description}'.")

    return numbers_found
