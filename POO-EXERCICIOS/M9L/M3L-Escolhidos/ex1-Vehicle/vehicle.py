from abc import ABC, abstractmethod

class VeiculoInterface(ABC):
    @abstractmethod
    def get_velocidade(self):
        pass

    @abstractmethod
    def get_direcao(self):
        pass

class Vehicle(VeiculoInterface):
    def __init__(self, velocidade, direcao, owner):
        self.velocidade = velocidade
        self.direcao = direcao
        self.owner = owner   #referência ao proprietário do veículo
        owner.adicionar_veiculo(self)  #associa o veículo ao proprietário

    def get_velocidade(self):
        return self.velocidade

    def get_direcao(self):
        return self.direcao