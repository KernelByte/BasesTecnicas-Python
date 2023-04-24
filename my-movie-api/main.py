from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_init():
    return "Hello world"