from conta import Conta

class Poupanca(Conta):
    def __init__(self, nome, pin, saldo, taxa_juros):
        super().__init__(nome, pin)
        self.saldo = saldo
        self.taxa_juros = taxa_juros

    def calcularJuros(self):
        return self.saldo * self.taxa_juros

    def __str__(self):
        return f"Conta Poupança: {self.nome}, Saldo: R${self.saldo:.2f}, PIN: {self.pin}"