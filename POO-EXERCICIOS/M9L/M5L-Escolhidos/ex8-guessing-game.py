'''
Escolha pelo menos 5 exercícios das listas M3L e M5L (5 de cada) para expandir o projeto do
exercício, incluindo novas classes relacionadas, conforme a sua criatividade, demonstrando
a associação bilateral.

'''

import random

class Player:
    def __init__(self, name):
        self.name = name  # nome do jogador
        self.attempts = 0  # contador de tentativas
        self.guesses = []  # lista para armazenar os palpites do jogador

    def add_guess(self, guess):
        """Adiciona o palpite à lista de palpites e incrementa as tentativas"""
        self.guesses.append(guess)
        self.attempts += 1

    def show_stats(self):
        """Exibe as estatísticas do jogador"""
        print(f"\n{self.name}, você fez {self.attempts} tentativas.")
        print("Seus palpites: ", self.guesses)

class GuessingGame:
    def __init__(self, player):
        self.player = player  # associa o jogador ao jogo (associação bilateral)
        self.number = random.randint(1, 100)  # gera um número aleatório entre 1 e 100

    def guess(self, player_guess):
        """Compara o palpite do jogador com o número gerado"""
        self.player.add_guess(player_guess)  # registra o palpite no jogador
        if player_guess < self.number:
            return "O palpite é menor que o número gerado."
        elif player_guess > self.number:
            return "O palpite é maior que o número gerado."
        else:
            return "Parabéns! Você adivinhou o número."

    @staticmethod
    def validar_palpite(player_input):
        """Valida se o palpite está entre 0 e 100"""
        try:
            player_guess = int(player_input)
            if 0 <= player_guess <= 100:
                return player_guess
            else:
                print("Por favor, digite um número entre 0 e 100.")
                return None
        except ValueError:
            print("Por favor, digite um número válido.")
            return None

    @classmethod
    def novo_jogo(cls, player):
        """Cria uma nova instância do jogo"""
        return cls(player)

def iniciar_jogo():
    """Função principal para iniciar o jogo"""
    nome = input("Digite seu nome: ")  # solicita o nome do jogador
    player = Player(nome)  # cria um jogador
    game = GuessingGame.novo_jogo(player)  # cria um novo jogo associando o jogador

    while True:
        player_input = input(f"\n{player.name}, digite seu palpite (entre 0 e 100): ")  # solicita um palpite
        player_guess = GuessingGame.validar_palpite(player_input)
        if player_guess is None:
            continue
        result = game.guess(player_guess)  # verifica o palpite
        print(result)  # imprime o resultado
        if result == "Parabéns! Você adivinhou o número.":
            player.show_stats()  # exibe as estatísticas do jogador ao final do jogo
            break  # termina o loop se o jogador adivinhar corretamente

if __name__ == "__main__":
    iniciar_jogo()  # chama a função para iniciar o jogo
