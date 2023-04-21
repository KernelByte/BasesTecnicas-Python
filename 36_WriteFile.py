# leer archivo
with open('./text.txt', 'r+') as file:
  # leer archivo
  for line in file:
    print(line)

  # agregar nuevo contenido al existente
  file.write('\n')  # salto de linea
  file.write('una nueva linea\n')