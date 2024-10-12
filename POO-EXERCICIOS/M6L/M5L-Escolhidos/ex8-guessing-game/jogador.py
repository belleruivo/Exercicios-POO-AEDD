class Jogador:
    def __init__(self, nome):
        self.nome = nome  # Armazena o nome do jogador
        self.historico_palpite = []  # Inicializa uma lista para armazenar o histórico de palpites

    def adicionar_palpite(self, palpite):
        self.historico_palpite.append(palpite)  # Adiciona o palpite ao histórico

    def exibir_historico(self):
        if self.historico_palpite:
            return f"Histórico de palpites de {self.nome}: {', '.join(map(str, self.historico_palpite))}"
        else:
            return f"{self.nome} ainda não fez palpites."
