from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, ano, marca, seguro):
        self.ano = ano
        self.marca = marca
        self.seguro = seguro

    @abstractmethod
    def registrar(self):
        pass

class Carro(Vehicle):
    def __init__(self, ano, marca, seguro, portas):
        super().__init__(ano, marca, seguro)
        self.portas = portas

    def registrar(self):
        return f"Carro {self.marca} de {self.ano} registrado com {self.portas} portas."

class Moto(Vehicle):
    def __init__(self, ano, marca, seguro, cilindradas):
        super().__init__(ano, marca, seguro)
        self.cilindradas = cilindradas

    def registrar(self):
        return f"Moto {self.marca} de {self.ano} registrada com {self.cilindradas} cilindradas."

class Caminhao(Vehicle):
    def __init__(self, ano, marca, seguro, capacidade_carga):
        super().__init__(ano, marca, seguro)
        self.capacidade_carga = capacidade_carga

    def registrar(self):
        return f"Caminhão {self.marca} de {self.ano} registrado com capacidade de {self.capacidade_carga} toneladas."