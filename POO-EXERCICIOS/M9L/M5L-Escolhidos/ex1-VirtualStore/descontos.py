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

