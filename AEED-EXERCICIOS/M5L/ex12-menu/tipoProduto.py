class TipoProduto:
    def __init__(self, tipo, percentual_imposto):
        self.tipo = tipo
        self.percentual_imposto = percentual_imposto

    def __str__(self):
        return f"Tipo: {self.tipo}, Imposto: {self.percentual_imposto}%"