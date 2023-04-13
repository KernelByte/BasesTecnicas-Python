def fu_potenciador(numero) :
    return numero * 2

# Higher order function - Funcion que recibe otra como parametro
def  fu_sumaValores(valor, fu_potenciador ):
    return valor + fu_potenciador(valor)

resultado = fu_sumaValores(10,fu_potenciador)

print("El valor calculado es: ", resultado)

# Ejemplo haciendo uso de una lambda
resultado2 = fu_sumaValores(10, lambda numero : numero * 5)
print("El valor calculado es: ", resultado2)
