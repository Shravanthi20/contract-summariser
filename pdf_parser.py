import fitz  

def extract_text_from_pdf(file_bytes):
    """Extract all text from a PDF file given as bytes."""
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text
