class Fatura:
    def __init__(self, numFatura, descricao, quantidade, precoItem):
        self.numFatura = numFatura
        self.descricao = descricao
        self.quantidade = quantidade if quantidade > 0 else 0
        self.precoItem = precoItem if precoItem > 0 else 0.0
        self.pedido = None  # A fatura é associada a um pedido posteriormente

    def calcular_fatura(self):
        return self.quantidade * self.precoItem

    def exibir_fatura(self):
        print(f"\nFatura {self.numFatura}:")
        print(f"Descrição: {self.descricao}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Preço por item: R$ {self.precoItem:.2f}")
        print(f"Valor total: R$ {self.calcular_fatura():.2f}")