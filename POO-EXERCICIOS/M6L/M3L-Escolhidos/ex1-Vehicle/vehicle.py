from consumo import Consumo
from gps import GPS

class Vehicle:
    def __init__(self, velocidade, direção, nome, localização, destino, distancia, valor_combustivel, consumo_por_km): 
        self.velocidade = velocidade
        self.direção = direção
        self.nome = nome
        self.gps = GPS(localização, destino, distancia) #atributo que contém uma instância da classe GPS
        self.consumo = Consumo(valor_combustivel, consumo_por_km, self.gps)  #atributo que contém uma instância da classe Consumo
                                                                                                                                               
    def getVelocidade(self):
        return self.velocidade
    
    def getDireção(self):
        return self.direção
    
    def getNome(self):
        return self.nome

    def setVelocidade(self, velocidade):
        self.velocidade = velocidade
        
    def setDireção(self, direção):
        self.direção = direção
        
    def setNome(self, nome):
        self.nome = nome
        
    def imprimir(self):
        print("\nDETALHES DO VEÍCULO:")
        print(f"\nVelocidade Atual: {self.velocidade}km/h")
        print(f"Direção dos Pneus: {self.direção}°")
        print(f"Nome do Proprietário: {self.nome}")
        self.gps.imprimir()
        self.consumo.imprimir()
        print("-="*40)


