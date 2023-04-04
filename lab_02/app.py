import docx

doc = docx.Document("laba.docx")

for paragraph in doc.paragraphs:
    print(paragraph.text)
