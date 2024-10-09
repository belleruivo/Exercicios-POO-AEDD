'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class CardGame:
    def __init__(self):
        self.deck = Deck()

    def play(self):
        player1_card = self.deck.draw_card()
        player2_card = self.deck.draw_card()
        print(f"Player 1 drew {player1_card}")
        print(f"Player 2 drew {player2_card}")

        if self.deck.ranks.index(player1_card.rank) > self.deck.ranks.index(player2_card.rank):
            print("Player 1 wins!")
        elif self.deck.ranks.index(player1_card.rank) < self.deck.ranks.index(player2_card.rank):
            print("Player 2 wins!")
        else:
            print("It's a tie!")

class ExtendedCardGame(CardGame):
    def play_with_score(self):
        player1_score = 0
        player2_score = 0

        for _ in range(5):  # Play 5 rounds
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

        print(f"Final Score - Player 1: {player1_score}, Player 2: {player2_score}")
        if player1_score > player2_score:
            print("Player 1 wins the game!")
        elif player1_score < player2_score:
            print("Player 2 wins the game!")
        else:
            print("The game is a tie!")

def main():
    game = ExtendedCardGame()
    game.play_with_score()

if __name__ == "__main__":
    main()