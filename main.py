from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from pydantic import BaseModel
from utils import load_data, search_similar

app = FastAPI()
business_data = load_data()

class QueryRequest(BaseModel):
    query: str

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("ui.html") as f:
        return f.read()

@app.post("/search")
async def search(request: QueryRequest):
    results = search_similar(request.query, business_data)

    follow_up = "Would you like directions or want me to book a table?"

    return JSONResponse(content={
        "results": results,
        "follow_up": follow_up
    })
