'''
Escolha pelo menos 5 exercícios das listas M3L e M5L (5 de cada) para expandir o projeto do
exercício, incluindo novas classes relacionadas, conforme a sua criatividade, demonstrando
a injeção de dependência..

'''

import random

# Classe responsável por gerenciar a pontuação do jogador
class ScoreTracker:
    def __init__(self):
        self.score = 0  # inicializa a pontuação

    def aumentar_pontuacao(self):
        self.score += 1  # incrementa a pontuação a cada palpite correto

    def exibir_pontuacao(self):
        return f"Sua pontuação atual é: {self.score}"

# Classe responsável por representar o jogador
class Player:
    def __init__(self, nome):
        self.nome = nome  # nome do jogador

    def dar_palpite(self):
        # Solicita ao jogador um palpite
        return input(f"{self.nome}, digite seu palpite (entre 0 e 100): ")

# Classe principal do jogo de adivinhação
class GuessingGame:
    def __init__(self, player, score_tracker):
        # Injeção de dependência: as instâncias de Player e ScoreTracker são passadas como parâmetros
        self.number = random.randint(1, 100)  # gera um número aleatório
        self.player = player  # jogador que está jogando
        self.score_tracker = score_tracker  # instância de ScoreTracker para rastrear a pontuação

    def guess(self, player_guess):
        if player_guess < self.number:
            return "O palpite é menor que o número gerado."
        elif player_guess > self.number:
            return "O palpite é maior que o número gerado."
        else:
            self.score_tracker.aumentar_pontuacao()  # aumenta a pontuação se o palpite estiver correto
            return "Parabéns! Você adivinhou o número."

    @staticmethod
    def validar_palpite(player_input):
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
    def novo_jogo(cls, player, score_tracker):
        return cls(player, score_tracker)  # cria uma nova instância do jogo com as dependências injetadas

def main():
    nome_jogador = input("Digite o nome do jogador: ")  # solicita o nome do jogador
    player = Player(nome_jogador)  # cria uma instância de Player
    score_tracker = ScoreTracker()  # cria uma instância de ScoreTracker

    game = GuessingGame.novo_jogo(player, score_tracker)  # cria uma nova instância do jogo com injeção de dependências
    
    while True:
        player_input = player.dar_palpite()  # o jogador faz um palpite
        player_guess = GuessingGame.validar_palpite(player_input)  # valida o palpite
        if player_guess is None:
            continue

        result = game.guess(player_guess)  # verifica o palpite
        print(result)  # imprime o resultado

        if result == "Parabéns! Você adivinhou o número.":
            print(score_tracker.exibir_pontuacao())  # exibe a pontuação atual
            break  # termina o loop se o jogador adivinhar corretamente

if __name__ == "__main__":
    main()  # chama a função main para iniciar o programa
