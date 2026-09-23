from pypdf import PdfReader
from docx import Document

def extract_text_from_pdf(file):

    text = ""
    reader = PdfReader(file)  # Creates a PdfReader object and opens the uploaded pdf which can be acessed

    # iterating through pages in the pdf
    for page in reader.pages:
        page_text = page.extract_text()

        # If the page extracted "None"
        if page_text:
            text += page_text +"\n"

    return text

def extract_text_from_docx(file):

    text = ""
    document = Document(file)  # Opens the uploaded document and gives access to paragraphs.

    # iterating through each paragraph in the docx
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text

def extract_resume_text(file):
    file_name = file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif file_name.endswith(".docx"):
        return extract_text_from_docx(file)
    else:
        raise ValueError(
            "Unsupported file format. Please upload a PDF or DOCX file."
        )