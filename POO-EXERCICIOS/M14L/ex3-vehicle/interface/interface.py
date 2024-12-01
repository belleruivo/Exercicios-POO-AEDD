from abc import ABC, abstractmethod

class Financiavel(ABC):
    @abstractmethod
    def calcular_financiamento(self, meses):
        pass

class AvaliacaoSeguro(ABC):
    @abstractmethod
    def avaliar_seguro(self):
        pass

