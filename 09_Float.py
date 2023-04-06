x = 3.3
y = 3.30098089

print(x == y)

# Transformacion con str
y_str = format(y,".2g")
print(y_str)

# Transformar matematica
print("*" * 50)

tolerance = 0.00001
print(abs(x - y) < tolerance)