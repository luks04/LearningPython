x = 20

def foo():
    global x
    x = 100

print(x)
foo()
print(x)

print("----------------------------------------------------------------")

def lambda_function():
    # Bad practice
    doblar = lambda num: num * 2
    print(doblar(35))
    sumar = lambda x, y: x + y
    print(sumar(7, 13))

print("----------------------------------------------------------------")

def showEmployee(name, salary = 2000):
    print("Employee", name, "salary is:", salary)

showEmployee("bob", 2000)
showEmployee("bob")

print("----------------------------------------------------------------")

def foo_args(*args):
    print(args) 

print("----------------------------------------------------------------")

def foo_kwargs(**kwargs):
    for key in kwargs:
        print(str(key) + " : " + str(kwargs[key]))
