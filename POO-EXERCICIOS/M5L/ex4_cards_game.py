'''
Em todos os exercícios abaixo, identifique a possibilidade de usar além dos métodos de
objetos, métodos de classe (@classmethod) e métodos fora de contexto (@staticmethod).

4. Implemente uma classe chamada CardsGame que represente um jogo de cartas
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas,
distribuir as cartas aos jogadores e permitir jogadas.
'''

import random

class CardsGame:
    def __init__(self, jogadores):  # aqui inicializamos a classe CardsGame com os jogadores
        self.baralho = self.criar_baralho()  # aqui criamos o baralho
        self.jogadores = {jogador: [] for jogador in jogadores}  # aqui inicializamos as mãos dos jogadores
        self.pilha_de_descarte = []  # aqui inicializamos a pilha de descarte
        self.jogador_atual = jogadores[0]  # aqui inicializamos com o primeiro jogador

    def criar_baralho(self):  # aqui criamos o baralho com as cartas do jogo
        cores = ['Vermelho', 'Amarelo', 'Verde', 'Azul']
        valores = list(range(1, 10)) + ['Pular', 'Reverter', 'Comprar Dois']
        baralho = [(cor, str(valor)) for cor in cores for valor in valores]
        baralho += [('Curinga', 'Troca de Cor'), ('Curinga', 'Comprar Quatro')] * 4
        return baralho

    def embaralhar_baralho(self):  # aqui embaralhamos o baralho
        random.shuffle(self.baralho)

    def distribuir_cartas(self, num_cartas=7):  # aqui distribuímos as cartas para os jogadores
        for _ in range(num_cartas):
            for jogador in self.jogadores:
                self.jogadores[jogador].append(self.baralho.pop())  # aqui removemos uma carta do baralho e adicionamos à mão do jogador

    def jogar_carta(self, jogador, carta):  # aqui implementamos a lógica para jogar uma carta
        if jogador != self.jogador_atual:  # verifica se é a vez do jogador
            print(f"Não é a vez de {jogador}.")
            return False
        if carta not in self.jogadores[jogador]:  # verifica se a carta está na mão do jogador
            print("Carta não está na mão do jogador.")
            return False
        if not self.validar_jogada(carta):  # verifica se a jogada é válida
            print("Jogada inválida. Tente novamente.")
            return False
        self.jogadores[jogador].remove(carta)  # remove a carta da mão do jogador
        self.pilha_de_descarte.append(carta)  # adiciona a carta à pilha de descarte
        self.proximo_turno()  # passa a vez para o próximo jogador
        return True

    def validar_jogada(self, carta):  # aqui validamos se a jogada é válida
        if not self.pilha_de_descarte:  # se a pilha de descarte estiver vazia, a jogada é válida
            return True
        carta_topo = self.pilha_de_descarte[-1]  # pega a carta do topo da pilha de descarte
        return (carta[0] == carta_topo[0] or  # verifica se a cor é a mesma
                carta[1] == carta_topo[1] or  # verifica se o valor é o mesmo
                carta[0] == 'Curinga')        # verifica se a carta é um curinga

    def proximo_turno(self):  # aqui passamos a vez para o próximo jogador
        lista_de_jogadores = list(self.jogadores.keys())
        indice_atual = lista_de_jogadores.index(self.jogador_atual)
        self.jogador_atual = lista_de_jogadores[(indice_atual + 1) % len(lista_de_jogadores)]  # calcula o próximo jogador

def main():
    while True:
        num_jogadores = input("Digite o número de jogadores (2-3): ")
        if not num_jogadores.isdigit():  # verifica se a entrada é um número
            print("Entrada inválida. Por favor, digite um número entre 2 e 3.")
            continue
        num_jogadores = int(num_jogadores)
        if num_jogadores < 2 or num_jogadores > 3:  # verifica se o número de jogadores está entre 2 e 3
            print("O número de jogadores deve ser entre 2 e 3.")
            continue
        break

    jogadores = []
    for i in range(num_jogadores):
        while True:
            nome = input(f"Digite o nome do jogador {i+1}: ")
            if nome.isdigit() or not nome.strip():  # verifica se o nome é válido
                print("Nome inválido. O nome não pode ser um número ou vazio.")
            else:
                jogadores.append(nome)
                break
    
    jogo = CardsGame(jogadores)  # aqui criamos o objeto CardsGame
    jogo.embaralhar_baralho()  # aqui embaralhamos o baralho
    jogo.distribuir_cartas()  # aqui distribuímos as cartas
    
    print("\n====================================")
    print("           Mãos iniciais            ")
    print("====================================")
    for jogador, mao in jogo.jogadores.items():  # aqui exibimos as mãos iniciais dos jogadores
        print(f"{jogador}: {mao}")
    
    while True:
        jogador = jogo.jogador_atual
        print("\n====================================")
        print(f"           É a vez de {jogador}           ")
        print("====================================")
        print(f"Sua mão: {jogo.jogadores[jogador]}")
        carta_para_jogar = input("Digite a carta para jogar (ex: 'Vermelho 5' ou 'Curinga Comprar Quatro'): ")
        
        try:
            partes = carta_para_jogar.split()  # divide a entrada em partes
            cor = partes[0]
            valor = ' '.join(partes[1:])
            carta = (cor, valor)
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar no formato 'Cor Valor'.")
            continue
        
        if not jogo.jogar_carta(jogador, carta):  # tenta jogar a carta
            continue
        
        if not jogo.jogadores[jogador]:  # verifica se o jogador venceu
            print(f"{jogador} venceu o jogo!")
            break
        
        print("\n====================================")
        print(f"Pilha de descarte: {jogo.pilha_de_descarte}")
        print(f"Jogador atual: {jogo.jogador_atual}")
        print("====================================")

if __name__ == "__main__":
    main()  # aqui chamamos a função main para executar o código