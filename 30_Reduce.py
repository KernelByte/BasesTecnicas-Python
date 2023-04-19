import functools

numbers = [1, 2, 7, 4]

def accum(counter, item):
  print(f'Counter: {counter}')
  print(f'item: {item}')
  return counter + item

'''
iteration counter item return
   1         0      1    1
   2         1      2    3
   3         3      3    6
   4         6      4    10
'''

result = functools.reduce(lambda counter, item: counter + item, numbers)
#result = functools.reduce(accum, numbers)

print(result)