class Jogador:
    def __init__(self, nome):
        # inicializa a classe jogador com nome e uma lista vazia para o histórico de palpites
        self.nome = nome  # armazena o nome do jogador
        self.historico_palpite = []  # inicializa uma lista para armazenar o histórico de palpites

    def adicionar_palpite(self, palpite):
        # adiciona um palpite ao histórico de palpites do jogador
        self.historico_palpite.append(palpite)  # adiciona o palpite ao histórico

    def exibir_historico(self):
        # exibe o histórico de palpites do jogador
        if self.historico_palpite:
            # se houver palpites no histórico, retorna uma string formatada com os palpites
            return f"histórico de palpites de {self.nome}: {', '.join(map(str, self.historico_palpite))}"
        else:
            # se não houver palpites no histórico, retorna uma mensagem indicando isso
            return f"{self.nome} ainda não fez palpites."