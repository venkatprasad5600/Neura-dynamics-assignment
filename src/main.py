import os
from embeddings import load_pdf_text, generate_embeddings
from vector_db import create_faiss_index, save_index, load_index, search_index
from rag_pipeline import answer_question
import numpy as np

# Step 1: Load documents
docs, files = load_pdf_text("sample_docs")
embeddings = generate_embeddings(docs)
embeddings = np.array(embeddings).astype('float32')

# Step 2: Create FAISS index
index = create_faiss_index(embeddings)
save_index(index, "faiss_index.index")

# Step 3: Ask questions
while True:
    question = input("Enter your question (or 'exit' to quit): ")
    if question.lower() == 'exit':
        break
    answer = answer_question(question)
    print("Answer:", answer)
