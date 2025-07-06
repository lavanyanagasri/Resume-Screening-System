import os
from pdfminer.high_level import extract_text
import docx2txt

def extract_text_from_pdf(file_path):
    try:
        return extract_text(file_path)
    except Exception as e:
        print(f"❌ Error reading PDF: {file_path} — {e}")
        return ""

def extract_text_from_docx(file_path):
    try:
        return docx2txt.process(file_path)
    except Exception as e:
        print(f"❌ Error reading DOCX: {file_path} — {e}")
        return ""

def extract_text_from_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"❌ Error reading TXT: {file_path} — {e}")
        return ""

def parse_resume(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        print(f"⚠️ Unsupported file type: {file_path}")
        return ""

