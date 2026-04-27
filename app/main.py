from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello everyone. This is jyothi! How are you doing? and testing the digital ocean droplet as well"}

@app.get("/health")
def health():
    return {"status": "ok"}
