class Produto:
    def __init__(self, numero, preco, tipo):
        self.numero = numero
        self.preco = preco
        self.tipo = tipo

    def __str__(self):
        return f"Produto {self.numero}, Preço: {self.preco}, Tipo: {self.tipo}"