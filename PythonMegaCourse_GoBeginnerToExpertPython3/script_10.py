var = "Hello"
print(var[1:3])
print(var[1:])
print(var[:2])
print(var[:])

print("-----------------------------------------")

var2 = "Hello world"
print(var[-3])
print(var[-3:])
print(var[:-3])
print(var[:-21])
print(var[-7:-1])

print("-----------------------------------------")

s1 = slice(3)
s2 = slice(1, 3, 2)
print(var2[s1])
print(var2[s2])