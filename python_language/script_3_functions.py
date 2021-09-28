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
    print(">>> Default args")
    print("Employee", name, "salary is:", salary)

showEmployee("bob", 4000)
showEmployee("bob")

print("----------------------------------------------------------------")

def foo_args(*args):
    print(">>> *args")
    print(type(args), args)
    print("args[1] -> ", args[1])

foo_args(123, "example arg", {"obj1": [1, 2, 3, 4, 5]})

print("----------------------------------------------------------------")

def foo_kwargs(**kwargs):
    print(">>> *kwargs")
    for key in kwargs:
        print(str(key) + " : " + str(kwargs[key]))

foo_kwargs(number = 123, string = "example arg")

def foo_all_args_example(a, b, c = 100, *args, **kwargs):
    print("\n\n-----------------------------------------------------")
    print(f"a -> {a}, b -> {b}, c -> {c}")
    print(">>> *args")
    print(type(args), args)
    print("\n")
    print(">>> *kwargs")
    for key in kwargs:
        print(str(key) + " : " + str(kwargs[key]))

foo_all_args_example("val for a", "val for b", 300, ["a", "b", "c"], 5.2, number = 999, string = "example arg")
