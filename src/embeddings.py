import os
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def load_pdf_text(pdf_folder):
    docs = []
    filenames = []
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join(pdf_folder, file))
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            docs.append(text)
            filenames.append(file)
    return docs, filenames

def generate_embeddings(text_list):
    embeddings = model.encode(text_list, show_progress_bar=True)
    return embeddings

if __name__ == "__main__":
    docs, files = load_pdf_text("sample_docs/")
    embeddings = generate_embeddings(docs)
    print("Generated embeddings for", len(docs), "documents")
