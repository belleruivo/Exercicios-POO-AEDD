from product import Product

class ItemOrder:
    
    def __init__(self, product: Product, quantify: int):
        self.product = product
        self.quantify = quantify
    
    def get_total(self):
        return self.product.value * self.quantify
