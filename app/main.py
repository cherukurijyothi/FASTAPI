from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello everyone. This is jyothi! How are you doing? "}

@app.get("/health")
def health():
    return {"status": "ok"}
