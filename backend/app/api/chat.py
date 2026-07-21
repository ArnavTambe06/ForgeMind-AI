from fastapi import APIRouter

from app.ai.embeddings import get_embedding
from app.ai.vector_store import search_documents
from app.ai.rag import generate_answer

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/")
async def chat(question: dict):

    query = question["question"]

    query_embedding = get_embedding(query)

    context_chunks = search_documents(
        query_embedding,
        k=3
    )

    context = "\n\n".join(context_chunks)

    answer = generate_answer(query, context)

    return {
        "question": query,
        "answer": answer
    }