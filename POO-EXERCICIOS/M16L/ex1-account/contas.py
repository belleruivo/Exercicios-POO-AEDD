from interfaces import InterfaceConta

# Implementação da classe base de Conta
class Conta(InterfaceConta):
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def extrato(self):
        return f"Extrato de {self.titular}: R${self.saldo:.2f}"


# Conta Corrente
class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=1000):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."


# Conta Poupança
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."


# Conta Investimento
class ContaInvestimento(Conta):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."


