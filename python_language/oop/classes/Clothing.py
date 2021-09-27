import Product

class Clothing(Product):
    def __init__(self, code: int, name: str, category: str, price: float, brand: str, size: str) -> None:
        super(Clothing, self).__init__(code, name, category, price)
        self.brand = brand
        self.size = size
    
    def __str__(self) -> str:
        return super(Clothing, self).__str__() + f"\nBrand: {self.brand} \nSize: {self.size}"