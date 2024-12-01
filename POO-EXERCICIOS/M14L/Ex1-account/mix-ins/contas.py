from abc import ABC, abstractmethod
from mixins import *

class Conta(ABC):
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    def extrato(self):
        return f"Extrato de {self.titular}: R${self.saldo:.2f}"

class ContaCorrente(Conta, LimiteCreditoMixIn):
    def __init__(self, titular, saldo=0, limite=1000):
        Conta.__init__(self, titular, saldo)
        LimiteCreditoMixIn.__init__(self, limite)
    
    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."
    
    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."

class ContaPoupanca(Conta, JurosMixIn):
    def __init__(self, titular, saldo=0, taxa_juros=0.01):
        Conta.__init__(self, titular, saldo)
        JurosMixIn.__init__(self, taxa_juros)
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."

class ContaInvestimento(Conta, InvestimentoMixIn):
    def __init__(self, titular, saldo=0, rendimento=0.05):
        Conta.__init__(self, titular, saldo)
        InvestimentoMixIn.__init__(self, rendimento)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."
    
    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."

    def aplicar_rendimento(self):
        return InvestimentoMixIn.aplicar_rendimento(self)