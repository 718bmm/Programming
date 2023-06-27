from pypdf import PdfReader, PdfWriter, PdfMerger  
from pathlib import Path 

# Reading PDF Files With PdfReader
pdf_path = Path().absolute() / "practice_files" /"Pride_and_Prejudice.pdf"
print(pdf_path)

# PdfReader opens loads asnd closes file on its own
pdf_reader = PdfReader(pdf_path)

# print(pdf_reader)
# print(len(pdf_reader.pages))
# print(pdf_reader.metadata)
# print(pdf_reader.metadata.title)

# Extracting Text From a Page
first_page = pdf_reader.pages[0]
print('type',type(first_page))
print(first_page.extract_text())

for page in pdf_reader.pages[:5]: # iterator
    print(page.extract_text())
