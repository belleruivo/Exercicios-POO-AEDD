'''
Escolha pelo menos 5 exercícios das listas M3L e M5L (5 de cada) para expandir o projeto do
exercício, incluindo novas classes relacionadas, conforme a sua criatividade, demonstrando
a injeção de dependência..

'''

import random

# Classe responsável por gerenciar a pontuação do jogador
class ScoreTracker:
    def __init__(self):
        self.score = 0  # Inicializa a pontuação

    def aumentar_pontuacao(self):
        """Incrementa a pontuação a cada palpite correto."""
        self.score += 1

    def exibir_pontuacao(self):
        """Exibe a pontuação atual do jogador."""
        return f"Sua pontuação atual é: {self.score}"

# Classe responsável por representar o jogador
class Player:
    def __init__(self, nome):
        self.nome = nome  # Nome do jogador

    def dar_palpite(self):
        """Solicita ao jogador um palpite."""
        return input(f"{self.nome}, digite seu palpite (entre 0 e 100): ")

# Classe responsável por definir o nível de dificuldade
class Dificuldade:
    def __init__(self, nivel):
        self.nivel = nivel
        self.intervalo = self.definir_intervalo()

    def definir_intervalo(self):
        """Define o intervalo de números com base no nível de dificuldade."""
        if self.nivel == 'fácil':
            return (1, 50)
        elif self.nivel == 'médio':
            return (1, 100)
        elif self.nivel == 'difícil':
            return (1, 200)
        else:
            raise ValueError("Nível de dificuldade inválido.")

# Classe principal do jogo de adivinhação
class GuessingGame:
    def __init__(self, player, score_tracker, dificuldade):
        # Injeção de dependência: as instâncias de Player, ScoreTracker e Dificuldade são passadas como parâmetros
        self.number = random.randint(*dificuldade.intervalo)  # Gera um número aleatório dentro do intervalo definido pela dificuldade
        self.player = player  # Jogador que está jogando
        self.score_tracker = score_tracker  # Instância de ScoreTracker para rastrear a pontuação

    def guess(self, player_guess):
        """Verifica o palpite do jogador e retorna o resultado da adivinhação."""
        if player_guess < self.number:
            return "O palpite é menor que o número gerado."
        elif player_guess > self.number:
            return "O palpite é maior que o número gerado."
        else:
            self.score_tracker.aumentar_pontuacao()  # Aumenta a pontuação se o palpite estiver correto
            return "Parabéns! Você adivinhou o número."

    @staticmethod
    def validar_palpite(player_input):
        """Valida o palpite do jogador."""
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
    def novo_jogo(cls, player, score_tracker, dificuldade):
        """Cria uma nova instância do jogo com as dependências injetadas."""
        return cls(player, score_tracker, dificuldade)

def main():
    nome_jogador = input("Digite o nome do jogador: ")  # Solicita o nome do jogador
    player = Player(nome_jogador)  # Cria uma instância de Player
    score_tracker = ScoreTracker()  # Cria uma instância de ScoreTracker

    # Solicita o nível de dificuldade
    nivel_dificuldade = input("Escolha o nível de dificuldade (fácil, médio, difícil): ").lower()
    dificuldade = Dificuldade(nivel_dificuldade)  # Cria uma instância de Dificuldade

    game = GuessingGame.novo_jogo(player, score_tracker, dificuldade)  # Cria uma nova instância do jogo com injeção de dependências
    
    while True:
        player_input = player.dar_palpite()  # O jogador faz um palpite
        player_guess = GuessingGame.validar_palpite(player_input)  # Valida o palpite
        if player_guess is None:
            continue

        result = game.guess(player_guess)  # Verifica o palpite
        print(result)  # Imprime o resultado

        if result == "Parabéns! Você adivinhou o número.":
            print(score_tracker.exibir_pontuacao())  # Exibe a pontuação atual
            break  # Termina o loop se o jogador adivinhar corretamente

if __name__ == "__main__":
    main()  # Chama a função main para iniciar o programa
