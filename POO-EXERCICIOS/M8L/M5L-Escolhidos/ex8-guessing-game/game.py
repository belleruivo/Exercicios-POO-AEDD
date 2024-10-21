import random
from history import History

class GuessingGame:
    def __init__(self, player, score_tracker, dificuldade):
        self.number = random.randint(*dificuldade.intervalo)
        self.player = player
        self.score_tracker = score_tracker
        self.history = History()
        self.intervalo = dificuldade.intervalo  # Armazena o intervalo da dificuldade

    def guess(self, player_guess):
        """Verifica o palpite do jogador e retorna o resultado da adivinhação."""
        self.history.adicionar_palpite(player_guess)
        if player_guess < self.number:
            return "O palpite é menor que o número gerado."
        elif player_guess > self.number:
            return "O palpite é maior que o número gerado."
        else:
            self.score_tracker.aumentar_pontuacao()
            return "Parabéns! Você adivinhou o número."

    def validar_palpite(self, player_input):
        """Valida o palpite do jogador e mostra mensagem apropriada."""
        try:
            player_guess = int(player_input)
            if self.intervalo[0] <= player_guess <= self.intervalo[1]:
                return player_guess
            else:
                print(f"Por favor, digite um número entre {self.intervalo[0]} e {self.intervalo[1]}.")
                return None
        except ValueError:
            print("Por favor, digite um número válido.")
            return None
