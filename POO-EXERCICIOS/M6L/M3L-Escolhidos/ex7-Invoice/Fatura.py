class Fatura:
    def __init__(self, numFatura, cliente, produto, quantidade):
        self.numFatura = numFatura
        self.cliente = cliente  # Associação com Cliente
        self.produto = produto  # Associação com Produto
        self.quantidade = quantidade if quantidade > 0 else 0

    def get_numFatura(self):
        return self.numFatura

    def get_cliente(self):
        return self.cliente

    def get_produto(self):
        return self.produto

    def get_quantidade(self):
        return self.quantidade

    def calcular_fatura(self):
        return self.quantidade * self.produto.preco