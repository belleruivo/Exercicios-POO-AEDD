from numero_gerado import NumeroGerado
from jogador import Jogador

class JogoAdivinhacao:
    def __init__(self, jogador_nome):
        self.jogador = Jogador(jogador_nome)  # Cria o jogador
        self.numero_gerado = NumeroGerado()  # Gera o número aleatório

    def jogar(self, palpite):
        if not (1 <= palpite <= 100):  # Verifica se o palpite está entre 1 e 100
            return "Por favor, insira um número entre 1 e 100."

        self.jogador.adicionar_palpite(palpite)  # Armazena o palpite no histórico do jogador

        resultado = self.numero_gerado.verificar_palpite(palpite)

        if resultado == "Parabéns! Você adivinhou o número.":
            return f"{self.jogador.nome}, {resultado} O número era {self.numero_gerado.numero}."

        return f"{self.jogador.nome}, {resultado}"

    def exibir_historico(self):
        return self.jogador.exibir_historico()  # Exibe o histórico de palpites do jogador
