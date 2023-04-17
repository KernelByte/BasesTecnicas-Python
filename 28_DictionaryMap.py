items = [
    {
        "product": "camisa",
        "price": 100,
    },

    {
        "product": "pantalon",
        "price": 200
    },

    {
        "product": "medias",
        "price": 50
    }
]

prices = list(map(lambda item : item["price"], items))
print(prices)

# Conversion de diccionario añadiendo nuevo campo

def convert (values) :
    values["taxes"] = values["price"] * 0.19
    return values

new_list = list(map(convert,items))
print(new_list)