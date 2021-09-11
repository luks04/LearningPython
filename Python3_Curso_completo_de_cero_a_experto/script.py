import random

def example_dict():
    cadena = 'Cualquier cosa'
    cadena_al_reves = cadena[::-1]
    print(cadena_al_reves)

    diccionario = {1: "Rojo", 2: "Azul", 3: "Morado"}
    print(diccionario)
    print(diccionario[2])
    print(diccionario.keys())

    diccionario.items()

def example_enumerate():
    animales = ["perro", "gato", "caballo", "jirafa"]

    for index, animal in enumerate(animales):
        print(index, animal)

def foo_args(*args):
    print(args) 

def foo_kwargs(**kwargs):
    for key in kwargs:
        print(str(key) + " : " + str(kwargs[key]))

def dictionary_from_arrays_example():
    array1 = ['A', 'B', 'C', 'D']
    array2 = [10, 20, 30, 40]
    tuple_list = zip(array1, array2)
    dictionary = dict(tuple_list)
    print(dictionary)

def lambda_function():
    # Mala practica
    doblar = lambda num: num * 2
    print(doblar(35))
    sumar = lambda x, y: x + y
    print(sumar(7, 13))

def files():
    # 'r' antes de definir una cadena de texto indica que esta debe interpretarse como un texto crudo
    with open(r'/Users/lucaspatino/Documents/Luks_Learning/Learning_Projects/example_file.txt', 'w') as file:
        file.write("Primera linea")
        file.write("\nSegunda linea")
        file.write("\nTercera linea")
    with open(r'/Users/lucaspatino/Documents/Luks_Learning/Learning_Projects/example_file.txt', 'r') as file:
        print(file.read())
    with open(r'/Users/lucaspatino/Documents/Luks_Learning/Learning_Projects/example_file.txt', 'r') as file:
        print(file.readlines())
    with open(r'/Users/lucaspatino/Documents/Luks_Learning/Learning_Projects/example_file.txt', 'r') as file:
        for linea in file:
            print(linea)
    with open(r'/Users/lucaspatino/Documents/Luks_Learning/Learning_Projects/example_file.txt', 'r') as file:
        palabras = list()
        for linea in file:
            palabras_linea = linea.split()
            palabras.extend(palabras_linea[:])
        print(palabras)

def exepciones():
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

if __name__ == "__main__":
    # example_dict()
    # print("#################################################################################")
    # example_enumerate()
    # print("#################################################################################")
    # foo_args("Param", 105, ['A', 'B', 'C'], {"f": 25, "s": 30})
    # print("#################################################################################")
    # foo_kwargs(param_1 = "something", other_name = 55)
    # print("#################################################################################")
    # dictionary_from_arrays_example()
    # lambda_function()
    # files()
    exepciones()
