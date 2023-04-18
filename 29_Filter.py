# Lista de numeros
numbers = [1,2,3,4,5,6,7,8]

# Se aplica filtro haciendo uso de una funcion
new_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(new_numbers)

# Filtro lista de diccionarios
persons = [
    {
        "name" : "Yoniher",
        "age" : 23
    },

    {
        "name" : "Oscar Martinez",
        "age" : 34
    },

    {
        "name" : "Luis mario",
        "age" : 56
    }
]

new_persons = list(filter(lambda x : x["age"] > 30, persons))
print(new_persons)