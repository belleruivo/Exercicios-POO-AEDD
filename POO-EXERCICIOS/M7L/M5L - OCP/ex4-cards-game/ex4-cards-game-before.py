'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

import random
from abc import ABC, abstractmethod

class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Remove e retorna uma carta do baralho."""
        return self.cards.pop()

class CardGame(ABC):
    def __init__(self):
        self.deck = Deck()

    @abstractmethod
    def play(self):
        """Método abstrato para jogar uma partida, a ser implementado pelas subclasses."""
        pass

class SimpleCardGame(CardGame):
    """Jogo simples de uma rodada."""
    def play(self):
        player1_card = self.deck.draw_card()
        player2_card = self.deck.draw_card()
        print(f"Player 1 drew {player1_card}")
        print(f"Player 2 drew {player2_card}")

        # Comparação do valor das cartas
        if self.deck.ranks.index(player1_card.rank) > self.deck.ranks.index(player2_card.rank):
            print("Player 1 wins!")
        elif self.deck.ranks.index(player1_card.rank) < self.deck.ranks.index(player2_card.rank):
            print("Player 2 wins!")
        else:
            print("It's a tie!")

class ScoreCardGame(CardGame):
    """Jogo de múltiplas rodadas com pontuação."""
    def __init__(self, rounds: int = 5):
        super().__init__()
        self.rounds = rounds

    def play(self):
        player1_score = 0
        player2_score = 0

        # Joga as rodadas especificadas
        for round_num in range(1, self.rounds + 1):
            input(f"Press Enter to draw cards for Round {round_num}")
            player1_card = self.deck.draw_card()
            player2_card = self.deck.draw_card()
            print(f"Player 1 drew {player1_card}")
            print(f"Player 2 drew {player2_card}")

            if self.deck.ranks.index(player1_card.rank) > self.deck.ranks.index(player2_card.rank):
                player1_score += 1
                print("Player 1 wins this round!")
            elif self.deck.ranks.index(player1_card.rank) < self.deck.ranks.index(player2_card.rank):
                player2_score += 1
                print("Player 2 wins this round!")
            else:
                print("This round is a tie!")

            print(f"Current Score - Player 1: {player1_score}, Player 2: {player2_score}\n")

        # Resultado final
        print(f"Final Score - Player 1: {player1_score}, Player 2: {player2_score}")
        if player1_score > player2_score:
            print("Player 1 wins the game!")
        elif player1_score < player2_score:
            print("Player 2 wins the game!")
        else:
            print("The game is a tie!")

def main():
    # Escolha do tipo de jogo a ser jogado
    game_type = input("Choose game type (simple/score): ").strip().lower()

    if game_type == "simple":
        game = SimpleCardGame()
    elif game_type == "score":
        # Perguntar o número de rodadas para o jogo de pontuação
        try:
            rounds = int(input("Enter the number of rounds: "))
        except ValueError:
            print("Invalid number of rounds. Defaulting to 5 rounds.")
            rounds = 5
        game = ScoreCardGame(rounds)
    else:
        print("Invalid game type. Defaulting to simple game.")
        game = SimpleCardGame()

    game.play()

if __name__ == "__main__":
    main()
