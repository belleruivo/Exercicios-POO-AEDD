class Discount:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def calcular_desconto(self, preco):
        if self.tipo == "percentual":
            return preco * (self.valor / 100)
        elif self.tipo == "fixo":
            return self.valor
        else:
            return 0