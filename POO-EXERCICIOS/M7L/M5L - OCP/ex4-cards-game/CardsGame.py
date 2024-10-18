from Deck import Deck
from abc import ABC, abstractmethod

class CardsGame(ABC):
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.maos = {jogador: [] for jogador in jogadores}
        self.baralho = Deck()

    @staticmethod
    def valor_carta(carta):
        ordem_valores = {'As': 14, 'Rei': 13, 'Dama': 12, 'Valete': 11,
                         '10': 10, '9': 9, '8': 8, '7': 7, '6': 6,
                         '5': 5, '4': 4, '3': 3, '2': 2}
        return ordem_valores[carta.valor]

    def distribuir_cartas(self, num_cartas=5):
        for jogador in self.jogadores:
            self.maos[jogador] = self.baralho.distribuir(num_cartas)

    @abstractmethod
    def jogar_rodada(self):
        pass
