# app/main.py

from fastapi import FastAPI
# из lib что-то импортируем, если надо
# from lib.something import do_something

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": "ok"}