from sentence_transformers import SentenceTransformer

# Load the model once when the app starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str):
    """
    Returns the embedding vector for a single text chunk.
    """
    embedding = model.encode(text)
    return embedding.tolist()


def get_embeddings(texts: list[str]):
    """
    Returns embeddings for multiple text chunks.
    """
    embeddings = model.encode(texts)
    return embeddings.tolist()