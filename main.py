from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "online", "message": "API FastAPI rodando com CI/CD!"}
