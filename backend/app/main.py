from fastapi import FastAPI

app = FastAPI(
    title="ForgeMind AI API",
    version="1.0.0",
    description="Industrial Knowledge Intelligence Platform"
)


@app.get("/")
def root():
    return {
        "message": "ForgeMind AI Backend Running 🚀"
    }