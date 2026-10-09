import os

from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI(title="API Lambda")


class Item(BaseModel):
    nome: str
    preco: float


# Memória volátil: não persiste entre instâncias do Lambda
itens: list[Item] = []


@app.get("/")
def raiz():
    return {"mensagem": "FastAPI rodando no AWS Lambda"}


@app.get("/info")
def info():
    return {"ambiente": os.getenv("AMBIENTE", "local")}


@app.get("/itens")
def listar():
    return itens


@app.post("/itens", status_code=201)
def criar(item: Item):
    itens.append(item)
    return item


@app.get("/itens/{item_id}")
def obter(item_id: int):
    if not 0 <= item_id < len(itens):
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return itens[item_id]


handler = Mangum(app)
