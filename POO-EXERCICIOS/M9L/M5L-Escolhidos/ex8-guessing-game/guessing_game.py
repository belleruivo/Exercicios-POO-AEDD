import random

class GuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)

    def guess(self, player_guess):
        if player_guess < self.number:
            return "O palpite é menor que o número gerado."
        elif player_guess > self.number:
            return "O palpite é maior que o número gerado."
        else:
            return "Parabéns! Você adivinhou o número."

    @staticmethod
    def validar_palpite(player_input):
        try:
            player_guess = int(player_input)
            if 1 <= player_guess <= 100:
                return player_guess
            else:
                print("Por favor, digite um número entre 1 e 100.")
                return None
        except ValueError:
            print("Por favor, digite um número válido.")
            return None
