# Agregar elementos de forma clasica
days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
newlist = []

for i in days:
  if "a" in i:
    newlist.append(i)

print(newlist) #["martes", "sabado"]


# Uso de list Comprehensions
days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
newlist = [i for i in days if "a" in i]
print(newlist) # ["martes", "sabado"]