from velocidade import Velocidade
from direcao import Direção
from proprietario import Proprietario
from gps import GPS

class Vehicle:
    def __init__(self, velocidade, direção, proprietario, gps):
        self.velocidade = Velocidade(velocidade)  
        self.direção = Direção(direção)  
        self.proprietario = Proprietario(proprietario)  
        self.gps = gps

    def imprimir(self):
        print("\nDETALHES DO VEÍCULO:")
        self.velocidade.imprimir()
        self.direção.imprimir()
        self.proprietario.imprimir()
        self.gps.imprimir()
        print("-=" * 40)

