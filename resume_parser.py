import pdfplumber
from docx import Document

def extract_pdf_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content
    return text

def extract_docx_text(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def parse_resume(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        return extract_pdf_text(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return extract_docx_text(uploaded_file)
    else:
        return uploaded_file.read().decode("utf-8")
