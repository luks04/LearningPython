cars = {
    "BMW": 2012,
    "Honda": 2019,
    "Ford": 2020
}

try:
    print(cars)
    del cars["Honda"]
    print(cars)

    if "Ford" in cars:
        print("Yes, it is available")
    else:
        print("No, it is not available in the cars dictionary")

    cars.clear()
    print(cars)
    del cars
    print(cars) # -> NameError: name 'cars' is not defined
except Exception:
    print("Ups, there is an exeption but your program will continue running")


try:
    number = "Anything"
    if type(number) is not int:
        raise TypeError
except TypeError:
    print("Error, it must be a number")
finally:
    print("It will be printed anyway")