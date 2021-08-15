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

class Product:
    def __init__(self, code: int, name: str, category: str, price: float) -> None:
        self.code = code
        self.name = name
        self.category = category
        self.price = price
    
    def get_stock(self):
        return random.randint(0, 200)
    
    def __str__(self) -> str:
        return f"\nCode: {self.code} \nName: {self.name} \nCategory: {self.category} \nPrice: {self.price}"

class Clothing(Product):
    def __init__(self, code: int, name: str, category: str, price: float, brand: str, size: str) -> None:
        super(Clothing, self).__init__(code, name, category, price)
        self.brand = brand
        self.size = size
    
    def __str__(self) -> str:
        return super(Clothing, self).__str__() + f"\nBrand: {self.brand} \nSize: {self.size}"

class Commerce:
    def __init__(self, products: list[Product] = list()) -> None:
        self.__products = products
    
    def get_product_by_code(self, code: int = None) -> Product or None:
        for product in self.__products:
            if product.code == code:
                return product
        return None
    
    def get_products(self):
        return self.__products
    
    def remove_product_by_code(self, code: int = None) -> Product or None:
        for index, product in enumerate(self.__products):
            if product.code == code:
                del(self.__products[index])
                return product
        return None

def oop_example():
    lemon = Product(10001, "Lemon", "Fruit", 1800.0)
    cookie = Product(name = "Cookie", price = 800.5, code = 20002, category = "Junk Food")
    shirt1 = Clothing(30003, "Shirt", "Clothing", 25000, "Koaj", "S")
    commerce = Commerce(products = [lemon, cookie, shirt1])
    lemon_product = commerce.get_product_by_code(10001)
    cookie_product = commerce.get_product_by_code(20002)
    shirt1_product = commerce.get_product_by_code(30003)
    print("--------------------------------------------")
    print(lemon_product)
    print(cookie_product)
    print(shirt1_product)
    print("--------------------------------------------")
    commerce.remove_product_by_code(20002)
    cookie_product = commerce.get_product_by_code(20002)
    if cookie_product is not None:
        print(cookie_product)
    else:
        print("\nERROR: There is not that product")
    all_products = commerce.get_products()
    for product in all_products:
        print(f"Stock - {product.name}: " + str(product.get_stock()))

class A:
    def __init__(self):
        print("Class A constructor")
    
    def method_a(self):
        print("Class A method")

class B:
    def __init__(self):
        print("Class B constructor")
    
    def method_b(self):
        print("Class B method")

class C(A, B):
    def __init__(self):
        print("Class C constructor")
        super(C, self).__init__()
    
    def method_c(self):
        print("Class C method")

def multi_inheritance():
    a = A()
    b = B()
    new_c = C()
    new_c.method_a()
    new_c.method_b()
    new_c.method_c()
    print(f"new_c is instance of Product: {str(isinstance(new_c, Product))}")
    print(f"new_c is instance of A: {str(isinstance(new_c, A))}")
    print(f"new_c is instance of B: {str(isinstance(new_c, A))}")
    print(f"new_c is instance of C: {str(isinstance(new_c, A))}")

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
    # exepciones()
    # oop_example()
    multi_inheritance()
