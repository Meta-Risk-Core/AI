
from fastapi import FastAPI, Query
from core.engine import Engine
from typing import List

app = FastAPI()
engine = Engine()

@app.get("/analyze")
def analyze(wallet: str):
    return engine.analyze_wallet(wallet)

@app.post("/batch-analyze")
def batch_analyze(wallets: List[str]):
    return {w: engine.analyze_wallet(w) for w in wallets}
