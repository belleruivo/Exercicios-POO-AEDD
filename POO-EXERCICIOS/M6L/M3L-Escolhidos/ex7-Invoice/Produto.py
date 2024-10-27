class Produto:
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco if preco > 0 else 0.0

    def __str__(self):
        return f"{self.descricao} - R$ {self.preco:.2f}"