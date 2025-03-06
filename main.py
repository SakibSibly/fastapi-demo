from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
async def details():
    return {"data": "FastAPI Implementation basics"}


@app.get("/number/{number}")
async def getNumber(number: int):
    return {"data": f"You entered {number}"}
