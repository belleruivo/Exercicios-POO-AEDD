class History:
    def __init__(self):
        self.palpites = []

    def adicionar_palpite(self, palpite):
        """Adiciona um palpite ao histórico."""
        self.palpites.append(palpite)

    def exibir_historico(self):
        """Exibe o histórico de palpites."""
        return self.palpites
