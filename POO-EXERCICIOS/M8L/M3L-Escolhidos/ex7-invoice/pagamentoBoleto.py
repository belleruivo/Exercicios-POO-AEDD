from pagamento import Pagamento

class PagamentoBoleto(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Gerando boleto no valor de R$ {valor:.2f}...")