import Product

class Clothing(Product):
    def __init__(self, code: int, name: str, category: str, price: float, brand: str, size: str) -> None:
        super(Clothing, self).__init__(code, name, category, price)
        self.__brand = brand # Encapsulated
        self.size = size

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, new_brand: str):
        self.__brand = new_brand
    
    def __str__(self) -> str:
        return super(Clothing, self).__str__() + f"\nBrand: {self.__brand} \nSize: {self.size}"