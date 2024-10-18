from fatura import Fatura

class FaturaComDesconto(Fatura):
    def __init__(self, numFatura, descricao, quantidade, precoItem, desconto):
        super().__init__(numFatura, descricao, quantidade, precoItem)
        self.desconto = desconto if desconto > 0 else 0.0

    def calcular_fatura(self):
        valor_total = super().calcular_fatura()
        return valor_total - (valor_total * (self.desconto / 100))