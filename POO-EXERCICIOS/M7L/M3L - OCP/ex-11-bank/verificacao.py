from conta import Conta

class Verificacao(Conta):
    def __init__(self, nome, pin, saldo):
        super().__init__(nome, pin)
        self.saldo = saldo

    def calcularJuros(self):
        return 0  # Conta corrente não gera juros

    def __str__(self):
        return f"Conta Corrente: {self.nome}, Saldo: R${self.saldo:.2f}, PIN: {self.pin}"