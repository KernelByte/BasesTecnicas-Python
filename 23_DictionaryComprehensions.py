names = ['nico','zule','santi']
ages = [12, 56, 98]

dict2 = dict(zip(names,ages))
print(dict2)

new_dict = {name:age for (name,age) in zip(names,ages)}
print(new_dict)

# Dictionary condictions
text = "Hola a todos, esta es una cadena de texto de prueba."
unique = { c: text.count(c) for c in text if c in 'aeiou' }
print(unique)