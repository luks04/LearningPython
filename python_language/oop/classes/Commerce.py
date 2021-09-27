import Product

class Commerce:
    def __init__(self, products: list = list()) -> None:
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