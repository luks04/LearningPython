x = 20

def foo():
    global x
    x = 100

print(x)
foo()
print(x)
