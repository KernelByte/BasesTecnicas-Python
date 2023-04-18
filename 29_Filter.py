# Lista de numeros
numbers = [1,2,3,4,5,6,7,8]

# Se aplica filtro haciendo uso de una funcion
new_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(new_numbers)