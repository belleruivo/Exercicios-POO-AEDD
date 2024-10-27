from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calcular_desconto(self, preco):
        pass

class DiscountPercentage(Discount):
    def __init__(self, valor):
        self.valor = valor

    def calcular_desconto(self, preco):
        return preco * (self.valor / 100)

class DiscountFixed(Discount):
    def __init__(self, valor):
        self.valor = valor

    def calcular_desconto(self, preco):
        return self.valor
    
class DiscountManager:
    def __init__(self):
        self.desconto = None

    def definir_desconto(self, desconto: Discount):
        self.desconto = desconto

    def aplicar_desconto(self, total):
        if self.desconto:
            return total - self.desconto.calcular_desconto(total)
        return total