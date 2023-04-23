import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3,4,5,6,7,8,9]

@app.get("/contact")
def get_contact():
    return [{
        "name" : "Yoniher Melendez",
        "age" : 29
    }, 
    {
        "name" : "Oscar Martinez",
        "age" : 20
    }]

@app.get("/bodyhtml",response_class=HTMLResponse)
def get_body():
    return '''
    <h1>Hola mundo</h1>
    <p>Parrafo de ejemplo</p>
    '''

def run():
    store.get_categories()

if __name__ == "__main__":
    run()