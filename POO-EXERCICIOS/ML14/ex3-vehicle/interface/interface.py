from abc import ABC, abstractmethod

class InterfaceVeiculos(ABC):
    @abstractmethod
    def registrar(self):
        pass

    @abstractmethod
    def consultar_veiculo(self):
        pass
