'''
8. implemente uma classe chamada guessinggame que represente um jogo de
adivinhação. essa classe deve gerar um número aleatório, permitir que o jogador faça
palpites e informar se o palpite está correto, informando se é maior ou menor que o
número gerado.

Em todos os exercícios abaixo, identifique a possibilidade de usar além dos métodos de
objetos, métodos de classe (@classmethod) e métodos fora de contexto (@staticmethod).
'''

import random  

class GuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)  

    def guess(self, player_guess):
        if player_guess < self.number:
            return "o palpite é menor que o número gerado."
        elif player_guess > self.number:
            return "o palpite é maior que o número gerado."
        else:
            return "parabéns! você adivinhou o número."

    @staticmethod
    def validar_palpite(player_input):
        try:
            player_guess = int(player_input)
            if 0 <= player_guess <= 100:
                return player_guess
            else:
                print("por favor, digite um número entre 0 e 100.")
                return None
        except ValueError:
            print("por favor, digite um número válido.")
            return None

    @classmethod
    def novo_jogo(cls):
        return cls()

def main():
    game = GuessingGame.novo_jogo()  
    while True:
        player_input = input("digite seu palpite (entre 0 e 100): ")  
        player_guess = GuessingGame.validar_palpite(player_input)
        if player_guess is None:
            continue
        result = game.guess(player_guess)  
        print(result)  
        if result == "parabéns! você adivinhou o número.":
            break

if __name__ == "__main__":
    main()  