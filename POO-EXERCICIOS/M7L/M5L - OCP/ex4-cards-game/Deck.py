import random
from Card import Card

class Deck:
    naipes = ['Copas', 'Paus', 'Ouros', 'Espadas']
    valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

    def __init__(self):
        self.cartas = [Card(naipe, valor) for naipe in self.naipes for valor in self.valores]
        self.embaralhar()

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self, quantidade: int):
        return [self.cartas.pop() for _ in range(quantidade)]
