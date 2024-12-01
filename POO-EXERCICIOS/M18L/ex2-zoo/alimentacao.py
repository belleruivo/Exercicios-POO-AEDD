class Alimentacao:
    
    def __init__(self, tipo, quantidade):
        self.tipo = tipo
        self.quantidade = quantidade
    
    def get_dieta(self):
        return f'Tipo: {self.tipo}, Quantidade: {self.quantidade}'
