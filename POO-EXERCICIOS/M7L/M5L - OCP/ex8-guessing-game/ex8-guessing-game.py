'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
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

class ExtendedGuessingGame(GuessingGame):
    def __init__(self):
        super().__init__()
        self.attempts = 0

    def guess(self, player_guess):
        self.attempts += 1
        result = super().guess(player_guess)
        if result == "parabéns! você adivinhou o número.":
            result += f" Você levou {self.attempts} tentativas."
        return result

def main():
    game = ExtendedGuessingGame.novo_jogo()  # cria uma nova instância do jogo
    while True:
        player_input = input("digite seu palpite (entre 0 e 100): ")  # solicita um palpite do jogador
        player_guess = GuessingGame.validar_palpite(player_input)
        if player_guess is None:
            continue
        result = game.guess(player_guess)  # verifica o palpite
        print(result)  # imprime o resultado
        if "parabéns! você adivinhou o número." in result:
            break  # termina o loop se o jogador adivinhar corretamente

if __name__ == "__main__":
    main()  # chama a função main para iniciar o programa