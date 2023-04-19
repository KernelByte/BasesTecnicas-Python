#--------- modulos ------------

# modulo para el manejo del sistema
import sys

# ubicacion donde se ejecuta el archivo actual
print(sys.path)
# --> ['/home/runner/coursepythonbasic', '/home/runner/coursepythonbasic/venv/lib/python3.10/site-packages',

# modulo de expresiones regulares
import re

# obtener los numeros de un texto
text = 'mi numero telefonico es 310 234 999. El codigo delpais es 57. Mi numero de la suerte es 7'

result = re.findall('[0-9]+', text)
print(result)
# --> ['310', '234', '999', '57', '7']

# Modulo para el manejo de horas y fechas
import time

# hora y fecha actual en el formato de la computadora
timestamp = time.time()
print(timestamp)
# --> 1669896713.8403738

# hora y fecha actual con formato de hora
local = time.localtime()
hora_actual = time.asctime(local)
print(hora_actual) # hora en el que corre el servidor
# --> Thu Dec  1 12:11:53 2022

# modulo para el manejo de listas
import collections

# frecuencia de los numeros de una lista en un diccionario
numbers = [1,2,4,5,5,5,7,1,3,8,5,5]
counter = collections.Counter(numbers)
print(counter)
# --> Counter({5: 5, 1: 2, 2: 1, 4: 1, 7: 1, 3: 1, 8: 1})