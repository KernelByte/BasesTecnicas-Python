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
