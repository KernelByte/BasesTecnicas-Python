# Definicion de una funcion
# Agregamos valores por defecto
def suma(a = 1,b = 2):
    return print("La suma de los numeros es: ",a+b)

suma(2,8)

# Retornar mas de un valor
def mensaje():
    return 34,2,"Hola"

resultado = mensaje()
print(resultado)