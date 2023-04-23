import requests

def get_categories() :
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(r.text)

    names = r.json()
    for data in names:
        print(data["name"])