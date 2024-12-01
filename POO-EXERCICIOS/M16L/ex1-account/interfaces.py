from abc import ABC, abstractmethod

# Interface de Conta (Abstração de alto nível)
class InterfaceConta(ABC):
    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def extrato(self):
        pass


# Interface de Gerenciamento de Contas (Abstração para alto nível)
class InterfaceContaManager(ABC):
    @abstractmethod
    def criar_conta(self):
        pass

    @abstractmethod
    def operar_conta(self, conta: InterfaceConta):
        pass

