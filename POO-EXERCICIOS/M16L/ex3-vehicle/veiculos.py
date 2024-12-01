from abc import ABC, abstractmethod

class VehicleAction(ABC):
    @abstractmethod
    def registrar(self):
        pass
    
    @abstractmethod
    def vender(self):
        pass


class Vehicle(ABC):
    def __init__(self, ano, marca, seguro):
        self.ano = ano
        self.marca = marca
        self.seguro = seguro

    @abstractmethod
    def obter_informacoes(self):
        pass

class Carro(Vehicle, VehicleAction):
    def __init__(self, ano, marca, seguro, portas):
        super().__init__(ano, marca, seguro)
        self.portas = portas

    def registrar(self):
        return f"Carro {self.marca} de {self.ano} registrado com {self.portas} portas."

    def vender(self):
        return f"Carro {self.marca} de {self.ano} vendido!"

    def obter_informacoes(self):
        return f"Carro {self.marca}, {self.ano}, {self.portas} portas"

class Moto(Vehicle, VehicleAction):
    def __init__(self, ano, marca, seguro, cilindradas):
        super().__init__(ano, marca, seguro)
        self.cilindradas = cilindradas

    def registrar(self):
        return f"Moto {self.marca} de {self.ano} registrada com {self.cilindradas} cilindradas."

    def vender(self):
        return f"Moto {self.marca} de {self.ano} vendida!"

    def obter_informacoes(self):
        return f"Moto {self.marca}, {self.ano}, {self.cilindradas} cilindradas"

class Caminhao(Vehicle, VehicleAction):
    def __init__(self, ano, marca, seguro, capacidade_carga):
        super().__init__(ano, marca, seguro)
        self.capacidade_carga = capacidade_carga

    def registrar(self):
        return f"Caminhão {self.marca} de {self.ano} registrado com capacidade de {self.capacidade_carga} toneladas."

    def vender(self):
        return f"Caminhão {self.marca} de {self.ano} vendido!"

    def obter_informacoes(self):
        return f"Caminhão {self.marca}, {self.ano}, {self.capacidade_carga} toneladas de carga"