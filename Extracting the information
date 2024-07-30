def search_part_number_in_pdf(pdf_path, part_number):
    doc = fitz.open(pdf_path)  # Open the PDF file
    found = False
    print(f"\nSearching for part number: {part_number}")
    for page_num in range(len(doc)):  # Iterate through each page
        page = doc.load_page(page_num)
        text_instances = page.search_for(part_number)  # Search for the part number

        if text_instances:  # Check if the part number is found
                # Attempting to capture a larger context assuming tables are not split across pages
                print(f"Found in page {page_num + 1}:")
                text = page.get_text("text")  # Extract text from the page
                # Trying to find a broader context for the found 'zcode'
                # This part needs customization based on your document structure.
                start_index = text.find(part_number)  # Start from the found 'zcode'
                # Look backwards for a newline to try and find the beginning of the table
                table_start = text.rfind('\n', 0, start_index)
                # Look forward for double newlines which might indicate the end of the table
                table_end = text.find('\n\n', start_index)
                if table_start == -1:  # If start isn't found, default to the start of the page text
                    table_start = 0
                if table_end == -1:  # If end isn't found, default to the end of the page text
                    table_end = len(text)
                # Extracting the supposed table's text
                table_text = text[table_start:table_end]
                print(table_text)
                found = True
                break  # Assuming only the first occurrence is needed
        if not found:
            print(f"Part number '{part_number}' not found in the document.")
    doc.close()

# Example usage

material_no = input("Please enter the part number: ")
path = check_for_material_number(material_no)
user_description = input("Please enter the Keyword to be searched: ")
if user_description == "sealant":
  pdf_path = r"/content/TECHNICAL LIBRARY/prepreg.pdf"
else:
  pdf_path = r"/content/TECHNICAL LIBRARY/prepreg.pdf"
y_code = extract_lpi(user_description, path)
result = search_part_number_in_pdf(pdf_path, y_code)

if result:
    search_part_number_in_pdf(pdf_path, part_numbers[0])  # Pass the first part number in the list
