class Player:
    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade  # Recebe a dificuldade para ajustar a mensagem

    def dar_palpite(self):
        """Solicita ao jogador um palpite baseado no nível de dificuldade."""
        intervalo = self.dificuldade.intervalo
        return input(f"{self.nome}, digite seu palpite entre {intervalo[0]} e {intervalo[1]}: ")
