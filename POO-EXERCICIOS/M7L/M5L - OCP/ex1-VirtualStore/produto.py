class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, desconto):
        self.preco -= desconto.calcular_desconto(self.preco)

    def __str__(self):
        return f"{self.nome}: R$ {self.preco:.2f}"
