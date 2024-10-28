class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def reduzir_estoque(self):
        if self.quantidade > 0:
            self.quantidade -= 1
            return True
        else:
            return False

    def __str__(self):
        return f"{self.nome}: R$ {self.preco:.2f} - Quantidade: {self.quantidade}"