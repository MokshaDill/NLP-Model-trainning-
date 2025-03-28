import os
import pdfplumber

# Define input and output paths
INPUT_FOLDER = "dataset"
OUTPUT_FILE = "trainning/processed_data.txt"

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def process_pdfs():
    all_text = ""
    pdf_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".pdf")]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(INPUT_FOLDER, pdf_file)
        extracted_text = extract_text_from_pdf(pdf_path)
        all_text += extracted_text + "\n"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(all_text)

    print(f"Processed text saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    process_pdfs()
