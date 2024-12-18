'''Implemente um sistema de Banco com seus 3 tipos de contas (corrente, poupança e
investimento), evidenciando a classe Account como uma classe abstrata.'''

from abc import ABC, abstractmethod
from interface import *

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

class ContaCorrente(Conta, LimiteCreditoInterface):
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

    def set_limite(self, limite):
        self.limite = limite

    def get_limite(self):
        return self.limite

class ContaPoupanca(Conta, JurosInterface):
    def __init__(self, titular, saldo=0, taxa_juros=0.01):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."

    def aplicar_juros(self):
        self.saldo += self.saldo * self.taxa_juros
        return f"Juros aplicados. Novo saldo: R${self.saldo:.2f}"

class ContaInvestimento(Conta, RendimentoInterface):
    def __init__(self, titular, saldo=0, rendimento=0.05):
        super().__init__(titular, saldo)
        self.rendimento = rendimento
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."
    
    def aplicar_rendimento(self):
        self.saldo += self.saldo * self.rendimento
        return f"Rendimento aplicado. Novo saldo: R${self.saldo:.2f}"


