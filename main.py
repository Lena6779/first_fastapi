from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my first API"}

class EchoRequest(BaseModel):
    message: str
    shout: bool = False


@app.get("/about")
def about():
    return {
        "name": "Lena",
        "module": "Module 4: REST API Fundamentals",
        "fun_fact": "I can play the flute and guitar!",
    }


@app.get("/greet/{name}")
def greet(name: str):
    return {"greeting": f"Hello, {name}! Nice to meet you."}


@app.post("/echo")
def echo(body: EchoRequest):
    if body.shout:
        return {"message": body.message.upper()}
    return {"message": body.message}