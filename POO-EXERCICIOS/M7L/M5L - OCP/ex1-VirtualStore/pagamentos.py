class Pagamento:
    def __init__(self, total):
        self.total = total

    def processar_pagamento(self):
        raise NotImplementedError("Este método deve ser implementado na subclasse.")


class PagamentoCartao(Pagamento):
    def processar_pagamento(self):
        print(f"Pagamento de R$ {self.total:.2f} realizado com cartão.")


class PagamentoDinheiro(Pagamento):
    def processar_pagamento(self):
        print(f"Pagamento de R$ {self.total:.2f} realizado em dinheiro.")