class FinanciavelMixin:
    def calcular_financiamento(self, meses):
        valor_base = 50000  
        juros = 0.02
        total = valor_base * (1 + juros) ** meses
        valor_mensal = total / meses
        return f"Valor do financiamento por mês: R$ {valor_mensal:.2f}"

class SeguroMixin:
    def avaliar_seguro(self):
        return f"Avaliando seguro para {self.__class__.__name__} {self.marca} de {self.ano}."