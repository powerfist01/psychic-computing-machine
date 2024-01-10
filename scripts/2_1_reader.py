import fitz  # imports the pymupdf library


path = '2_1.pdf'  # path to the pdf file
doc = fitz.open(path)

text = ""
for page in doc:
    text += page.get_text()()

print(text)
doc.close()  # close the document