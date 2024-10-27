import random
from Card import Card

class Deck:
    # define os naipes e valores das cartas como atributos de classe
    naipes = ['Copas', 'Paus', 'Ouros', 'Espadas']
    valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

    def __init__(self):
        # inicializa a classe Deck criando uma lista de cartas
        # usa uma compreensão de lista para criar uma lista de objetos Card, combinando cada naipe com cada valor
        self.cartas = [Card(naipe, valor) for naipe in self.naipes for valor in self.valores]
        self.embaralhar()  # chama o método embaralhar para embaralhar as cartas ao inicializar o baralho

    def embaralhar(self):
        # embaralha as cartas do baralho usando a função shuffle do módulo random
        random.shuffle(self.cartas)

    def distribuir(self, quantidade: int):
        # distribui uma quantidade especificada de cartas do baralho
        # usa uma compreensão de lista para remover e retornar a quantidade especificada de cartas do topo do baralho
        # o método pop remove e retorna o último item da lista (o topo do baralho)
        return [self.cartas.pop() for _ in range(quantidade)]