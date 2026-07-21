from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil
from uuid import uuid4

from app.ai.pdf_loader import extract_text
from app.ai.chunker import chunk_text
from app.ai.embeddings import get_embeddings
from app.ai.vector_store import add_documents



router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    # Save PDF
    pdf_path = UPLOAD_FOLDER / file.filename

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = extract_text(str(pdf_path))

    # Chunk text
    chunks = chunk_text(text)

    # Generate embeddings
    embeddings = get_embeddings(chunks)

    # Store in ChromaDB
    add_documents(
    chunks,
    embeddings
)

    return {
        "filename": file.filename,
        "chunks": len(chunks),
        "message": "Document indexed successfully"
    }