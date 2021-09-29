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

print("----------------------------------------------------------------")

try:
    number = "Anything"
    if type(number) is not int:
        raise TypeError
except TypeError:
    print("Error, it must be a number")
finally:
    print("It will be printed anyway")

print("----------------------------------------------------------------")

class CustomException(Exception):
    def __init__(self):
        super()

def foo_custom_exception():
    while True:
        try:
            something = input("Enter a word that not starts with 'Z': \n")
            if something.startswith("Z"):
                raise CustomException
        except CustomException:
            # Example
            print(f"ERROR: It should not start with 'Z'")
        except Exception as error:
            print(f"ERROR: Try again \n{error}")
        else:
            print("Good word!")
            break
        finally:
            print("End of cycle")

foo_custom_exception()

print("----------------------------------------------------------------")

def foo_exception_example():
    while True:
        try:
            num = int(input("Enter a number:\n"))
            if num:
                number = str(num)
                half = str(num / 2)
                print(f"The number is {number} and its half is {half}")
        except ValueError:
            print(f"ERROR: It cannot divide a text by 2")
        except Exception as error:
            print(f"ERROR: Try again \n{error}")
        else:
            print("Successful calculation")
            break
        finally:
            print("End of cycle")

#foo_exception_example()
