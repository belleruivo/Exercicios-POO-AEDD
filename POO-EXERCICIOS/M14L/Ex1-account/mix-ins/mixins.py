class LimiteCreditoMixIn:
    def __init__(self, limite=0):
        self.limite = limite

    def set_limite(self, limite):
        self.limite = limite

    def get_limite(self):
        return self.limite


class JurosMixIn:
    def __init__(self, taxa_juros=0):
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        self.saldo += self.saldo * self.taxa_juros
        return f"Juros aplicados. Novo saldo: R${self.saldo:.2f}"
    
class InvestimentoMixIn:
    def __init__(self, rendimento=0.05):
        self.rendimento = rendimento

    def aplicar_rendimento(self):
        self.saldo += self.saldo * self.rendimento
        return f"Rendimento aplicado. Novo saldo: R${self.saldo:.2f}"