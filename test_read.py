from docx import Document

def read_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

file_path = "uploads/ds practical.docx"
print(read_docx(file_path))
