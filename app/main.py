from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "running"}

@app.get("/visitors")
def visitors():
    return {"total_visitors": 71}