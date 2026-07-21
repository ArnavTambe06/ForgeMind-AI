import faiss
import numpy as np

# MiniLM embedding dimension
DIMENSION = 384

index = faiss.IndexFlatL2(DIMENSION)

documents = []


def add_documents(chunks, embeddings):
    """
    Store document chunks and their embeddings.
    """

    vectors = np.array(embeddings).astype("float32")

    index.add(vectors)

    documents.extend(chunks)


def search_documents(query_embedding, k=3):
    """
    Search similar document chunks.
    """

    query = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query, k)

    results = []

    for idx in indices[0]:
        if idx != -1 and idx < len(documents):
            results.append(documents[idx])

    return results