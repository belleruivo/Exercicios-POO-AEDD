'''
Em todos os exercícios abaixo, identifique a possibilidade de usar além dos métodos de
objetos, métodos de classe (@classmethod) e métodos fora de contexto (@staticmethod).

4. Implemente uma classe chamada CardsGame que represente um jogo de cartas
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas,
distribuir as cartas aos jogadores e permitir jogadas.
'''

import random  # importa o módulo random para embaralhar o baralho

class CardsGame:
    def __init__(self, jogadores):  # inicializa a classe CardsGame com os jogadores
        self.baralho = self.criar_baralho()  # cria o baralho
        self.jogadores = {jogador: [] for jogador in jogadores}  # inicializa as mãos dos jogadores
        self.pilha_de_descarte = []  # inicializa a pilha de descarte
        self.jogador_atual = jogadores[0]  # define o primeiro jogador como o jogador atual

    @staticmethod
    def criar_baralho():  # cria o baralho com as cartas do jogo
        cores = ['Vermelho', 'Amarelo', 'Verde', 'Azul']  # define as cores das cartas
        valores = list(range(1, 10)) + ['Pular', 'Reverter', 'Comprar Dois']  # define os valores das cartas
        baralho = [(cor, str(valor)) for cor in cores for valor in valores]  # cria as cartas combinando cores e valores
        baralho += [('Curinga', 'Troca de Cor'), ('Curinga', 'Comprar Quatro')] * 4  # adiciona cartas curingas ao baralho
        return baralho  # retorna o baralho criado

    def embaralhar_baralho(self):  # embaralha o baralho
        random.shuffle(self.baralho)  # usa o método shuffle do módulo random para embaralhar

    def distribuir_cartas(self, num_cartas=7):  # distribui as cartas para os jogadores
        for _ in range(num_cartas):  # repete o processo para o número de cartas especificado
            for jogador in self.jogadores:  # para cada jogador
                self.jogadores[jogador].append(self.baralho.pop())  # remove uma carta do baralho e adiciona à mão do jogador

    def jogar_carta(self, jogador, carta):  # implementa a lógica para jogar uma carta
        if jogador != self.jogador_atual:  # verifica se é a vez do jogador
            print(f"Não é a vez de {jogador}.")  # imprime mensagem de erro
            return False  # retorna False indicando jogada inválida
        if carta not in self.jogadores[jogador]:  # verifica se a carta está na mão do jogador
            print("Carta não está na mão do jogador.")  # imprime mensagem de erro
            return False  # retorna False indicando jogada inválida
        if not self.validar_jogada(carta):  # verifica se a jogada é válida
            print("Jogada inválida. Tente novamente.")  # imprime mensagem de erro
            return False  # retorna False indicando jogada inválida
        self.jogadores[jogador].remove(carta)  # remove a carta da mão do jogador
        self.pilha_de_descarte.append(carta)  # adiciona a carta à pilha de descarte
        self.proximo_turno()  # passa a vez para o próximo jogador
        return True  # retorna True indicando jogada válida

    def validar_jogada(self, carta):  # valida se a jogada é válida
        if not self.pilha_de_descarte:  # se a pilha de descarte estiver vazia, a jogada é válida
            return True  # retorna True indicando jogada válida
        carta_topo = self.pilha_de_descarte[-1]  # pega a carta do topo da pilha de descarte
        return (carta[0] == carta_topo[0] or  # verifica se a cor é a mesma
                carta[1] == carta_topo[1] or  # verifica se o valor é o mesmo
                carta[0] == 'Curinga')        # verifica se a carta é um curinga

    def proximo_turno(self):  # passa a vez para o próximo jogador
        lista_de_jogadores = list(self.jogadores.keys())  # cria uma lista com os jogadores
        indice_atual = lista_de_jogadores.index(self.jogador_atual)  # encontra o índice do jogador atual
        self.jogador_atual = lista_de_jogadores[(indice_atual + 1) % len(lista_de_jogadores)]  # calcula o próximo jogador

    def inicializar_jogo(self):  # inicializa o jogo
        self.embaralhar_baralho()  # embaralha o baralho
        self.distribuir_cartas()  # distribui as cartas para os jogadores
        print("\n====================================")
        print("           Mãos iniciais            ")
        print("====================================")
        for jogador, mao in self.jogadores.items():  # para cada jogador e sua mão
            print(f"{jogador}: {mao}")  # imprime a mão inicial do jogador

    def jogar(self):  # método principal para jogar o jogo
        while True:  # loop infinito até que o jogo termine
            jogador = self.jogador_atual  # define o jogador atual
            print("\n====================================")
            print(f"           É a vez de {jogador}           ")
            print("====================================")
            print(f"Sua mão: {self.jogadores[jogador]}")  # imprime a mão do jogador atual
            carta_para_jogar = input("Digite a carta para jogar (ex: 'Vermelho 5' ou 'Curinga Comprar Quatro'): ")  # solicita a carta para jogar

            try:
                partes = carta_para_jogar.split()  # divide a entrada em partes
                cor = partes[0]  # define a cor da carta
                valor = ' '.join(partes[1:])  # define o valor da carta
                carta = (cor, valor)  # cria a carta como uma tupla
            except ValueError:  # captura erro de valor
                print("Entrada inválida. Certifique-se de digitar no formato 'Cor Valor'.")  # imprime mensagem de erro
                continue  # continua o loop

            if not self.jogar_carta(jogador, carta):  # tenta jogar a carta
                continue  # se a jogada for inválida, continua o loop

            if not self.jogadores[jogador]:  # verifica se o jogador venceu
                print(f"{jogador} venceu o jogo!")  # imprime mensagem de vitória
                break  # termina o loop

            print("\n====================================")
            print(f"Pilha de descarte: {self.pilha_de_descarte}")  # imprime a pilha de descarte
            print(f"Jogador atual: {self.jogador_atual}")  # imprime o jogador atual
            print("====================================")

def obter_jogadores():  # função para obter os jogadores
    while True:  # loop infinito até que a entrada seja válida
        num_jogadores = input("Digite o número de jogadores (2-3): ")  # solicita o número de jogadores
        if not num_jogadores.isdigit():  # verifica se a entrada é um número
            print("Entrada inválida. Por favor, digite um número entre 2 e 3.")  # imprime mensagem de erro
            continue  # continua o loop
        num_jogadores = int(num_jogadores)  # converte a entrada para inteiro
        if num_jogadores < 2 or num_jogadores > 3:  # verifica se o número de jogadores está entre 2 e 3
            print("O número de jogadores deve ser entre 2 e 3.")  # imprime mensagem de erro
            continue  # continua o loop
        break  # termina o loop

    jogadores = []  # inicializa a lista de jogadores
    for i in range(num_jogadores):  # para cada jogador
        while True:  # loop infinito até que a entrada seja válida
            nome = input(f"Digite o nome do jogador {i+1}: ")  # solicita o nome do jogador
            if nome.isdigit() or not nome.strip():  # verifica se o nome é válido
                print("Nome inválido. O nome não pode ser um número ou vazio.")  # imprime mensagem de erro
            else:
                jogadores.append(nome)  # adiciona o nome à lista de jogadores
                break  # termina o loop
    return jogadores  # retorna a lista de jogadores

def main():  # função principal
    jogadores = obter_jogadores()  # obtém os jogadores
    jogo = CardsGame(jogadores)  # cria uma instância da classe CardsGame
    jogo.inicializar_jogo()  # inicializa o jogo
    jogo.jogar()  # começa a jogar

if __name__ == "__main__":  # verifica se o script está sendo executado diretamente
    main()  # chama a função main para executar o código