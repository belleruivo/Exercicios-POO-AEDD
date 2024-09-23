'''
8. implemente uma classe chamada guessinggame que represente um jogo de
adivinhação. essa classe deve gerar um número aleatório, permitir que o jogador faça
palpites e informar se o palpite está correto, informando se é maior ou menor que o
número gerado.

Em todos os exercícios abaixo, identifique a possibilidade de usar além dos métodos de
objetos, métodos de classe (@classmethod) e métodos fora de contexto (@staticmethod).
'''

import random  # importa o módulo random

class GuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)  # gera um número aleatório entre 1 e 100

    def guess(self, player_guess):
        if player_guess < self.number:
            return "o palpite é menor que o número gerado."
        elif player_guess > self.number:
            return "o palpite é maior que o número gerado."
        else:
            return "parabéns! você adivinhou o número."

if __name__ == "__main__":
    game = GuessingGame()  # cria uma instância do jogo
    while True:
        try:
            player_input = int(input("digite seu palpite (entre 0 e 100): "))  # solicita um palpite do jogador
            if player_input < 0 or player_input > 100:
                print("por favor, digite um número entre 0 e 100.")  # valida se o palpite está entre 0 e 100
                continue
            result = game.guess(player_input)  # verifica o palpite
            print(result)  # imprime o resultado
            if result == "parabéns! você adivinhou o número.":
                break  # termina o loop se o jogador adivinhar corretamente
        except ValueError:
            print("por favor, digite um número válido.")  # trata entradas inválidas