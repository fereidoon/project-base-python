from PyPDF2 import PdfReader

def get_pdf_text(doc_path):
    pdf_text = ""
    try:
        reader = PdfReader(doc_path)
        texts = []
        for page in reader.pages:
            t = page.extract_text()
            if t:
                texts.append(t)
        pdf_text = "\n\n".join(texts)
    except Exception as e:
        pdf_text = ""
        print(f"Error reading PDF: {e}")
    return pdf_text

if __name__ == "__main__":
    sample_pdf_path = "src/data/resume.pdf"
    resume_text = get_pdf_text(sample_pdf_path)
    print(resume_text)
    