class SistemaPagamento:
    def __init__(self):
        self.saldo = 0.0

    def inserir_dinheiro(self, valor):
        if valor <= 0:
            print("Valor inválido. O valor deve ser positivo.")
            return
        self.saldo += valor
        print(f"R$ {valor:.2f} inserido. Saldo atual: R$ {self.saldo:.2f}")

    def processar_pagamento(self, valor):
        if self.saldo < valor:
            print(f"Saldo insuficiente. O preço do produto é R$ {valor:.2f}.")
            return False
        self.saldo -= valor
        return True

    def retornar_troco(self):
        if self.saldo > 0:
            troco = self.saldo
            self.saldo = 0
            print(f"Retornando troco: R$ {troco:.2f}")
        else:
            print("Não há troco a ser retornado.")