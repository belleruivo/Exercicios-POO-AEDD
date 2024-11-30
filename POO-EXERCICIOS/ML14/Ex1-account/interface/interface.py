from abc import ABC, abstractmethod

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