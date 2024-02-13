from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    color: str


@app.post("/check")
def check_cat(item: Item):
    if(item.color == "black"):
        return {"result": "Claire"}
    elif(item.color == "gray"):
        return {"result": "Muta"}
    elif(item.color == "brown"):
        return {"result": "Leon"}
    else:
        return {"result": "humm.. human?"}