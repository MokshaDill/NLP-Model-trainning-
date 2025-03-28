import re

INPUT_FILE = "trainning\processed_data.txt"  #C:\Users\moksh\OneDrive\Documents\GitHub\NLP-Model-trainning-\trainning\processed_data.txt, 
OUTPUT_FILE = "cleaned_data.txt"

def clean_text(text):
    text = re.sub(r"\n+", "\n", text)  # Remove multiple new lines
    text = re.sub(r"[^\x00-\x7F]+", " ", text)  # Remove non-ASCII characters
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    return text.strip()

def clean_file():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    cleaned_text = clean_text(text)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(f"Cleaned text saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    clean_file()
