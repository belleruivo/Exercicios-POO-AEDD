class Pagamento:
    def __init__(self, tipo, total):
        self.tipo = tipo 
        self.total = total

    def processar_pagamento(self):
        if self.tipo in ['cartao', 'cartão']:
            print(f"Pagamento de R$ {self.total:.2f} realizado com cartão.")
        elif self.tipo == 'dinheiro':
            print(f"Pagamento de R$ {self.total:.2f} realizado em dinheiro.")
        else:
            print("Tipo de pagamento inválido!")