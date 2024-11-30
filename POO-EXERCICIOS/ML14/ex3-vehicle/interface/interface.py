from abc import ABC, abstractmethod

class InterfaceVeiculos(ABC):
    @abstractmethod
    def registrar(self):
        pass

    @abstractmethod
    def consultar_veiculo(self):
        pass

class InterfaceManutencao(ABC):
    @abstractmethod
    def agendar_manutencao(self):
        pass

    @abstractmethod
    def consultar_manutencoes(self):
        pass
