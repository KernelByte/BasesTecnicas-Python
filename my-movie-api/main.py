from fastapi import FastAPI

app = FastAPI()
app.title = "My movie app"
app.version = 1.0

@app.get("/",tags=["Home url"])
def get_message():
    return "Hello world"


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