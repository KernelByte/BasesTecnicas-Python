text = 'Ella sabe programar en python'

# Operador para buscar un subtext
operacion = 'programar' in text
print(operacion)

# Operador para contar el numero de caracteres
conteo = len(text)
print(conteo)

# Metodo para pasar texto a mayusculas
print(text.upper())

# Metodo para pasar texto a minusculas
print(text.lower())

# Metodo contar el numero de veces de una letra
print(text.count("a"))

# Metodo transformar caracteres en mayusculas y minusculas
print(text.swapcase())

# Metodo para preguntar si un texto inicia con una palabra
print(text.startswith("Ella"))

# Metodo para preguntar si un texto finaliza con una palabra
print(text.endswith("Ella"))

# Metodo para remplazar texto
print(text.replace("programar","desarrollar"))

# Metado para poner la primera letra en mayuscula
text2 = "este es un titulo"
print(text2.capitalize())

# Metodo para poner la primera letra de cada palabra en mayucula
print(text2.title())

# Metodo para saber si esta variable es un digito
print(text2.isdigit())