from pagamento import Pagamento

class PagamentoCartaoCredito(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R$ {valor:.2f} no cartão de crédito...")