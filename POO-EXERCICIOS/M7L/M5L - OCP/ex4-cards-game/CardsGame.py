from Deck import Deck
from abc import ABC, abstractmethod

class CardsGame(ABC):
    def __init__(self, jogadores):
        # inicializa a classe CardsGame com uma lista de jogadores
        self.jogadores = jogadores  # armazena a lista de jogadores
        # cria um dicionário para armazenar as mãos dos jogadores, inicializando cada jogador com uma lista vazia
        self.maos = {jogador: [] for jogador in jogadores}
        self.baralho = Deck()  # cria uma instância de Deck para o baralho do jogo

    @staticmethod
    def valor_carta(carta):
        # método estático para obter o valor de uma carta
        # um método estático não depende da instância da classe, pode ser chamado diretamente pela classe
        ordem_valores = {'As': 14, 'Rei': 13, 'Dama': 12, 'Valete': 11,
                         '10': 10, '9': 9, '8': 8, '7': 7, '6': 6,
                         '5': 5, '4': 4, '3': 3, '2': 2}
        # retorna o valor da carta baseado no dicionário ordem_valores
        return ordem_valores[carta.valor]

    def distribuir_cartas(self, num_cartas=5):
        # distribui um número especificado de cartas para cada jogador
        for jogador in self.jogadores:
            # para cada jogador, distribui num_cartas cartas do baralho e armazena na mão do jogador
            self.maos[jogador] = self.baralho.distribuir(num_cartas)

    @abstractmethod
    def jogar_rodada(self):
        # método abstrato que deve ser implementado pelas subclasses
        # um método abstrato é declarado, mas não implementado na classe base
        # força as subclasses a fornecerem uma implementação específica para este método
        pass