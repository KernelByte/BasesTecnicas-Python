#file = open("./text.txt")

# Leer todo el archivo
#print(file.read())

# Forma de leer linea a linea
'''
print(file.readline())
print(file.readline())
print(file.readline())
'''

#for line in file:
#    print(line)


#file.close()


with open("./text.txt") as file:
  print(file.read())