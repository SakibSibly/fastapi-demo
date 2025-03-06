from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
async def details():
    return {"data": "FastAPI Implementation basics"}
