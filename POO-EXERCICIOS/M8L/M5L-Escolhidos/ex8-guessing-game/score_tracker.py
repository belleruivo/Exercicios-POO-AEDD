class ScoreTracker:
    def __init__(self):
        self.score = 0

    def aumentar_pontuacao(self):
        """Incrementa a pontuação a cada palpite correto."""
        self.score += 1

    def exibir_pontuacao(self):
        """Exibe a pontuação atual do jogador."""
        return f"Sua pontuação atual é: {self.score}"
