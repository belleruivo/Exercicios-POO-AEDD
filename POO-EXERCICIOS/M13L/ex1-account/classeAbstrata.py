from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def saque(self, valor):
        pass

    @abstractmethod
    def deposito(self, valor):
        pass

    def extrato(self):
        return f"Titular: {self.titular}, Saldo: R${self.saldo:.2f}"