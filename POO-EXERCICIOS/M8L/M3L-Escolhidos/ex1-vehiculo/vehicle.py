''' 1. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em
km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de
acesso e impressão para esta classe e faça um programa de teste.
'''
from gps import GPS
from consumo import Consumo

class Vehicle:
    def __init__(self, velocidade, direção, nome, gps: GPS, consumo: Consumo): # Passa os parametros definidos na Class GPS para gerenciar a localização
        self.velocidade = velocidade
        self.direção = direção
        self.nome = nome
        self.gps = gps # Class Vehicle não cria os objetos de GPS e Consumo internamente 
        self.consumo = consumo

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
        print("-"*50)
        print("         DETALHES DO VEÍCULO:")
        print("-"*50)
        print(f"Velocidade Atual: {self.velocidade}km/h")
        print(f"Direção dos Pneus: {self.direção}°")
        print(f"Nome do Proprietário: {self.nome}")
        self.gps.imprimir()
        self.consumo.imprimir()
        print("-"*50)
        
# Exemplo de Injeção de Dependencia 
# Imagine que voce esta montando um carro. Para isso, você precisa de varias peças. Ao invés de construir essas peças dentro do carro, você vai comprá-las
# separadamente e depois injeta-las no carro. Assim, se um dia você quiser trocar as rodas por rodas melhores, pode fazer isso sem precisar construir um novo carro 