from fastapi import FastAPI
import wikipedia

app = FastAPI()

@app.get("/summary/{title}")
def path(title):
    return wikipedia.summary(f"{title}")

@app.get("/search")
def query(q):
    qs = wikipedia.search(q)
    if len(qs) == 0:
        return  "No results"
    return qs

from pydantic import BaseModel

class Request(BaseModel):
    query: str


@app.post("/pages")
def body(data: Request):
    return wikipedia.search(data.query)

#uvicorn prac:app --reload
