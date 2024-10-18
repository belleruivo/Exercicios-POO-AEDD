from imposto import Imposto

class ImpostoSimples(Imposto):
    def calcular(self, valor):
        return valor * 0.10  # 10% de imposto sobre o valor