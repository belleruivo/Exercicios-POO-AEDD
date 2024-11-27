'''Implemente um sistema de Banco com seus 3 tipos de contas (corrente, poupança e
investimento), evidenciando a classe Account como uma classe abstrata.'''

from abc import ABC, abstractmethod

# Interface Base
class Account(ABC):
    @abstractmethod
    def saque(self, valor):
        pass

    @abstractmethod
    def deposito(self, valor):
        pass

    @abstractmethod
    def extrato(self):
        pass

class Rendimento(ABC):
    @abstractmethod
    def aplicar_rendimento(self):
        pass

class ContaCorrente(Account):
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def saque(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def deposito(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso!"

    def extrato(self):
        return f"Titular: {self.titular}, Saldo: R${self.saldo:.2f}, Limite: R${self.limite:.2f}"


class ContaPoupança(Account, Rendimento):
    def __init__(self, titular, saldo, taxa_juros):
        self.titular = titular
        self.saldo = saldo
        self.taxa_juros = taxa_juros

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def deposito(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso!"

    def extrato(self):
        return f"Titular: {self.titular}, Saldo: R${self.saldo:.2f}, Taxa de Juros: {self.taxa_juros:.2f}%"

    def aplicar_rendimento(self):
        juros = self.saldo * self.taxa_juros / 100
        self.saldo += juros
        return f"Juros aplicados: R${juros:.2f}"


class ContaInvestimento(Account, Rendimento):
    def __init__(self, titular, saldo, tipo_investimento):
        self.titular = titular
        self.saldo = saldo
        self.tipo_investimento = tipo_investimento

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def deposito(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso!"

    def extrato(self):
        return f"Titular: {self.titular}, Saldo: R${self.saldo:.2f}, Tipo de Investimento: {self.tipo_investimento}"

    def aplicar_rendimento(self):
        rendimento = self.saldo * (0.10 if self.tipo_investimento == "1" else 0.03)
        self.saldo += rendimento
        return f"Rendimento aplicado: R${rendimento:.2f}"


