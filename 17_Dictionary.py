# En Python, los diccionarios son una estructura de datos que te permiten almacenar pares clave-valor.
Person = {"name": "Yoniher Melendez",
          "age": 20,
          "country": "Colombia"
          }

print(Person)
print(len(Person))

# Preguntar por la llave
print(Person["name"])
print(Person.get("name")) # En este caso envia none si no existe

# Otra opcion para validar la llave dentro del diccionario
print("age" in Person)

# Formas para modificacion de datos:
Person["name"] = "Oscar Lopez"
print(Person)

# Delete
# Person.pop("age")
del Person["age"]
print(Person)

# Impresion de datos
print("items = ", Person.items())
print("keys = ", Person.keys())
print("values = ", Person.values())
