import fitz  # PyMuPDF
import pandas as pd

def extract_text_from_pdf(file_path):
    document = fitz.open(file_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def load_csv(file_path):
    return pd.read_csv(file_path)

def load_xls(file_path):
    return pd.read_excel(file_path)

def process_file(file_path):
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.csv'):
        text = load_csv(file_path).to_string()
    elif file_path.endswith('.xls') or file_path.endswith('.xlsx'):
        text = load_xls(file_path).to_string()
    else:
        raise ValueError("Unsupported file type")
    return text
