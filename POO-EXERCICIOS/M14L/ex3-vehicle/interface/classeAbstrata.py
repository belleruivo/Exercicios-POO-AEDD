from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, ano, marca, seguro):
        self.ano = ano
        self.marca = marca
        self.seguro = seguro

    def vender(self):
        return f"{self.__class__.__name__} {self.marca} de {self.ano} vendido!"

    @abstractmethod
    def registrar(self):
        pass