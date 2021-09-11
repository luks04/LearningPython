import random

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