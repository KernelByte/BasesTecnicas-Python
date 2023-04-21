foot = ["chiken","Apple","rice","Otro"]
number = ["1","2","3"]

# El map permite la conversion de datos haciendo uso de funciones
result = list(map(lambda numbers, foots  : "#" + numbers +" - "+ foots,number,foot))
print(result)