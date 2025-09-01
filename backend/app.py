# FastAPI entrypoint (API routes)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, MedQueryBot is running!"}