from interface import *
from classeAbstrata import *

class Carro(Vehicle, Financiavel, AvaliacaoSeguro):
    def __init__(self, ano, marca, seguro, portas):
        super().__init__(ano, marca, seguro)
        self.portas = portas

    def registrar(self):
        return f"Carro {self.marca} de {self.ano} registrado com {self.portas} portas."

    def calcular_financiamento(self, meses):
        valor_base = 50000
        juros = 0.02
        total = valor_base * (1 + juros) ** meses
        valor_mensal = total / meses
        return f"Valor do financiamento por mês: R$ {valor_mensal:.2f}"

    def avaliar_seguro(self):
        return f"Avaliando seguro para Carro {self.marca} de {self.ano}."

class Moto(Vehicle, Financiavel):
    def __init__(self, ano, marca, seguro, cilindradas):
        super().__init__(ano, marca, seguro)
        self.cilindradas = cilindradas

    def registrar(self):
        return f"Moto {self.marca} de {self.ano} registrada com {self.cilindradas} cilindradas."
    
    def calcular_financiamento(self, meses):
        valor_base = 100000
        juros = 0.03
        total = valor_base * (1 + juros) ** meses
        valor_mensal = total / meses
        return f"Valor do financiamento por mês: R$ {valor_mensal:.2f}"

class Caminhao(Vehicle, AvaliacaoSeguro):
    def __init__(self, ano, marca, seguro, capacidade_carga):
        super().__init__(ano, marca, seguro)
        self.capacidade_carga = capacidade_carga

    def registrar(self):
        return f"Caminhão {self.marca} de {self.ano} registrado com capacidade de {self.capacidade_carga} toneladas."
    
    def avaliar_seguro(self):
        return f"Avaliando seguro para Caminhão {self.marca} de {self.ano}."