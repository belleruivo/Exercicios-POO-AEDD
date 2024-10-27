class Jogador:
    def __init__(self, nome):
        self.nome = nome  
        self.historico_palpite = []  

    def adicionar_palpite(self, palpite):
        self.historico_palpite.append(palpite)  # adiciona o palpite ao histórico

    def exibir_historico(self):
        # exibe o histórico de palpites do jogador
        if self.historico_palpite:
            # se houver palpites no histórico, retorna uma string formatada com os palpites
            return f"histórico de palpites de {self.nome}: {', '.join(map(str, self.historico_palpite))}"
        else:
            return f"{self.nome} ainda não fez palpites."