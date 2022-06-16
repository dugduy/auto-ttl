from docx import Document
doc = Document('./Bản sao của T10-004-04.docx')
f=open('T10-004-04.txt','w',encoding='utf-8')
for para in doc.paragraphs:
    print(para.text)
    f.write(para.text)