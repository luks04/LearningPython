from .classes import Product
from .classes import Clothing
from .classes import Commerce

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
    oop_example()
    multi_inheritance()