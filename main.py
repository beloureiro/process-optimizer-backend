from fastapi import FastAPI
from pydantic import BaseModel
from optimization import optimize_process

app = FastAPI()

class ProcessFlow(BaseModel):
    data: dict  # Estrutura do fluxo de processo

@app.post("/optimize")
async def optimize_flow(flow: ProcessFlow):
    result = optimize_process(flow.data)
    return result
