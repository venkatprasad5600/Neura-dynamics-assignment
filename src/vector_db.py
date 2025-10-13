import faiss
import numpy as np
import pickle

def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def save_index(index, filepath):
    faiss.write_index(index, filepath)

def load_index(filepath):
    return faiss.read_index(filepath)

def search_index(index, query_embedding, k=3):
    distances, indices = index.search(query_embedding, k)
    return distances, indices

if __name__ == "__main__":
    # Example usage
    embeddings = np.random.rand(10, 384).astype('float32')  # placeholder
    index = create_faiss_index(embeddings)
    save_index(index, "../outputs/faiss_index.index")
    loaded_index = load_index("../outputs/faiss_index.index")
    query = np.random.rand(1, 384).astype('float32')
    distances, indices = search_index(loaded_index, query)
    print("Nearest docs indices:", indices)
