class Fatura:
    def __init__(self, numFatura, descricao, quantidade, precoItem):
        self.numFatura = numFatura
        self.descricao = descricao
        self.quantidade = quantidade if quantidade > 0 else 0
        self.precoItem = precoItem if precoItem > 0 else 0.0

    def calcular_fatura(self):
        return self.quantidade * self.precoItem

    def __str__(self):
        return (f"Número da fatura: {self.numFatura}\n"
                f"Descrição: {self.descricao}\n"
                f"Quantidade: {self.quantidade}\n"
                f"Preço por item: R$ {self.precoItem:.2f}\n"
                f"Valor total da fatura: R$ {self.calcular_fatura():.2f}")