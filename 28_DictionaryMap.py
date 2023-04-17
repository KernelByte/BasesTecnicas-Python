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
    # Se realiza copia del diccionario original para no alterar al original pór su referencia en memoria
    new_items = values.copy();
    new_items["taxes"] = new_items["price"] * 0.19
    return new_items

new_list = list(map(convert,items))
print(new_list)