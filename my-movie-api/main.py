from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "My movie app"
app.version = 1.0

@app.get("/",tags=["Home url"],response_class=HTMLResponse)
def get_message():
    return "<h1>Hello world</h1>"


@app.get("/person",tags=["Person url"])
def get_person():
    return [
        {
            "name" : "Yoniher Melendez",
            "age"  : 23
        },

        {
            "name" : "Oscar Martinez",
            "age"  : 34
        }
    ]