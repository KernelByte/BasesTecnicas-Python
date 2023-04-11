def increment(x):
    return x + 1
result = increment(10)
print(result)

#Funcion lambda debemos definir parametros de entrada y de salida

fun = lambda x : x + 2
print(fun(10))

full_name = lambda name,last_name: f'el nombre es {name} {last_name} '
print(full_name('Yoniher','Melendez'))