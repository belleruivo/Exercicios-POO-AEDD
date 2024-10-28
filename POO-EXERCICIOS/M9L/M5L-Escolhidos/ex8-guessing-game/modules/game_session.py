from .guessing_game import GuessingGame
from .player import Player

class GameSession:
    def __init__(self, player):
        self.player = player  # Associa um jogador à sessão
        self.game = GuessingGame()  # Cria uma nova instância do jogo

    def play(self):
        while True:
            player_input = input(f"{self.player.get_name()}, digite seu palpite (entre 1 e 100): ")  # Solicita um palpite
            player_guess = GuessingGame.validar_palpite(player_input)
            if player_guess is None:
                continue
            self.player.increment_guesses()  # Incrementa o contador de palpites do jogador
            result = self.game.guess(player_guess)  # Verifica o palpite
            print(result)  # Imprime o resultado
            if result == "Parabéns! Você adivinhou o número.":
                print(f"{self.player.get_name()} fez {self.player.guesses} palpites.")
                break  # Termina o loop se o jogador adivinhar corretamente
