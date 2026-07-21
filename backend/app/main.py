#..\venv\Scripts\Activate.ps1
#uvicorn app.main:app --reload

from fastapi import FastAPI

from app.api import health
from app.api import projects
from app.api import documents
from app.api import chat

app = FastAPI(
    title="ForgeMind AI",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(projects.router)
app.include_router(documents.router)
app.include_router(chat.router)