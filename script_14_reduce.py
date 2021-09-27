from functools import reduce

def sum(a, b):
    return a + b

print(reduce(sum, [1, 2, 3, 10, 11, 12]))
