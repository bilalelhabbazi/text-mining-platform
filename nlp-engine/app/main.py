
from fastapi import FastAPI

app = FastAPI(
    title="Text Mining Platform API",
    description="NLP and Topic Discovery Engine",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Text Mining NLP Engine is running",
        "status": "OK"
    }

@app.get("/health")
def health():
    return {
        "service": "nlp-engine",
        "status": "healthy"
    }
