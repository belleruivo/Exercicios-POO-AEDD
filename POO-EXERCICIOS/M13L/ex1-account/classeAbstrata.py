from abc import ABC, abstractmethod

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

