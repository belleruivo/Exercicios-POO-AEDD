'''
Em todos os exercícios abaixo, identifique a possibilidade de usar além dos métodos de
objetos, métodos de classe (@classmethod) e métodos fora de contexto (@staticmethod).

4. Implemente uma classe chamada CardsGame que represente um jogo de cartas
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas,
distribuir as cartas aos jogadores e permitir jogadas.
'''

import random

class CardsGame:
    # Atributo de classe que define as cartas do jogo
    baralho = [f'{valor} de {naipe}' for naipe in ['Copas', 'Paus', 'Ouros', 'Espadas']
               for valor in ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']]
    # 'baralho' é uma lista que contém todas as combinações de valores e naipes de cartas

    def __init__(self, jogadores):
        self.jogadores = jogadores  # Lista de jogadores
        self.maos = {jogador: [] for jogador in jogadores}  # Dicionário que mapeia cada jogador para suas cartas
        self.carta_atual = None  

    @classmethod
    def embaralhar_baralho(cls):
        """Método de classe para embaralhar o baralho."""
        random.shuffle(cls.baralho)  # embaralha a lista 'baralho' da classe
        # Usamos @classmethod para acessar e modificar o atributo de classe 'baralho'

    def distribuir_cartas(self, num_cartas=5):
        """Distribui cartas para os jogadores."""
        self.embaralhar_baralho()  # embaralha antes de distribuir
        for jogador in self.jogadores:
            self.maos[jogador] = [self.baralho.pop() for _ in range(num_cartas)]
            # pra cada jogador, distribui 'num_cartas' cartas removidas do baralho

    @staticmethod
    def valor_carta(carta):
        # retorna o valor de uma carta.
        ordem_valores = {'As': 14, 'Rei': 13, 'Dama': 12, 'Valete': 11, 
                         '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, 
                         '5': 5, '4': 4, '3': 3, '2': 2}
        valor = carta.split(' de ')[0].capitalize()  # pega o valor da carta e capitaliza
        return ordem_valores[valor]  # valor numérico da carta
        # esse método não depende de nenhum atributo da instância ou da classe

    def jogar_rodada(self):
        # joga uma rodada e determina o vencedor.
        cartas_jogadas = {}
        for jogador in self.jogadores:
            print(f"\n{jogador}, suas cartas: {self.maos[jogador]}")
            carta = input(f"Escolha uma carta para jogar: ").lower()
            while carta not in [c.lower() for c in self.maos[jogador]]:
                print("Você não tem essa carta. Escolha uma carta válida.\n")
                carta = input(f"Escolha uma carta para jogar: ").lower()
            self.maos[jogador] = [c for c in self.maos[jogador] if c.lower() != carta]
            # remove a carta jogada da mão do jogador
            cartas_jogadas[jogador] = carta
            print(f"{jogador} jogou {carta}.")

        vencedor = max(cartas_jogadas, key=lambda jogador: self.valor_carta(cartas_jogadas[jogador]))
        # acha jogador com a carta de maior valor
        print(f"\nO vencedor da rodada é {vencedor} com {cartas_jogadas[vencedor]}!")

def main():
    jogadores = []
    for i in range(2):
        while True:
            nome_jogador = input(f"Nome do jogador {i + 1}: ").strip()
            # 'i + 1' é usado para exibir o número do jogador começando de 1
            if nome_jogador:
                jogadores.append(nome_jogador)  # adc o nome do jogador à lista 'jogadores'
                break
            else:
                print("O nome do jogador não pode estar em branco. Por favor, insira um nome válido.")
    
    jogo = CardsGame(jogadores)  # instância de CardsGame com os jogadores
    jogo.distribuir_cartas()  
    
    while True:
        jogo.jogar_rodada()  
        if input("Deseja jogar outra rodada? (s/n) ").lower() != 's':
            break 

if __name__ == "__main__":
    main()  