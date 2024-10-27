from imposto import Imposto
from pagamento import Pagamento
from invoice import Invoice

class Faturamento:
    def __init__(self, imposto: Imposto, pagamento: Pagamento):
        self.imposto = imposto
        self.pagamento = pagamento

    def processar_fatura(self, invoice: Invoice):
        # Exibe a fatura original
        invoice.exibir_fatura()
        valor_total = invoice.calcular_fatura()

        # Calcula o imposto
        valor_imposto = self.imposto.calcular(valor_total)
        valor_final = valor_total + valor_imposto

        # Exibe valores com imposto
        print(f"\nImposto aplicado: R$ {valor_imposto:.2f}")
        print(f"Valor final com imposto: R$ {valor_final:.2f}")

        # Processa o pagamento
        self.pagamento.processar_pagamento(valor_final)