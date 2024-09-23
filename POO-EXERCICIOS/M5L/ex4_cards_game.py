'''
Em todos os exercícios abaixo, identifique a possibilidade de usar além dos métodos de
objetos, métodos de classe (@classmethod) e métodos fora de contexto (@staticmethod).

4. Implemente uma classe chamada CardsGame que represente um jogo de cartas
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas,
distribuir as cartas aos jogadores e permitir jogadas.
'''

import random

class CardsGame:
    # Atributo de classe que define as cartas do jogo
    deck = [f'{rank} de {suit}' for suit in ['Copas', 'Paus', 'Ouros', 'Espadas']
            for rank in ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']]

    def __init__(self, players):
        self.players = players
        self.hands = {player: [] for player in players}
        self.current_card = None

    @classmethod
    def shuffle_deck(cls):
        """Método de classe para embaralhar o baralho."""
        random.shuffle(cls.deck)

    def deal_cards(self, num_cards=5):
        """Distribui cartas para os jogadores."""
        self.shuffle_deck()
        for player in self.players:
            self.hands[player] = [self.deck.pop() for _ in range(num_cards)]

    @staticmethod
    def card_value(card):
        """Método estático que retorna o valor de uma carta."""
        rank_order = {'As': 14, 'Rei': 13, 'Dama': 12, 'Valete': 11, 
                      '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, 
                      '5': 5, '4': 4, '3': 3, '2': 2}
        rank = card.split(' de ')[0].capitalize()
        return rank_order[rank]

    def play_round(self):
        """Joga uma rodada e determina o vencedor."""
        played_cards = {}
        for player in self.players:
            print(f"\n{player}, suas cartas: {self.hands[player]}")
            card = input(f"Escolha uma carta para jogar: ").lower()
            while card not in [c.lower() for c in self.hands[player]]:
                print("Você não tem essa carta. Escolha uma carta válida.\n")
                card = input(f"Escolha uma carta para jogar: ").lower()
            self.hands[player] = [c for c in self.hands[player] if c.lower() != card]
            played_cards[player] = card
            print(f"{player} jogou {card}.")

        # Determinar o vencedor
        winner = max(played_cards, key=lambda player: self.card_value(played_cards[player]))
        print(f"\nO vencedor da rodada é {winner} com {played_cards[winner]}!")

def main():
    players = []
    for i in range(2):
        while True:
            player_name = input(f"Nome do jogador {i + 1}: ").strip()
            if player_name:
                players.append(player_name)
                break
            else:
                print("O nome do jogador não pode estar em branco. Por favor, insira um nome válido.")
    
    jogo = CardsGame(players)
    jogo.deal_cards()
    
    while True:
        jogo.play_round()
        if input("Deseja jogar outra rodada? (s/n) ").lower() != 's':
            break

if __name__ == "__main__":
    main()