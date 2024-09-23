'''
Em todos os exercícios abaixo, identifique a possibilidade de usar além dos métodos de
objetos, métodos de classe (@classmethod) e métodos fora de contexto (@staticmethod).

10. Escreva um programa completo para jogar o jogo da velha. Para tanto crie uma
classe NoughtsAndCrosses (jogo da velha):
• a classe deve conter como dados privados um array bidimensional 3x3 para
representar a grade do jogo
• crie uma enumeração para representar as possibilidades de ocupação de uma
casa na grade (vazia, jogador 1 ou jogador 2)
• o construtor deve inicializar a grade como vazia
• forneça um método para exibir a grade
• permita dois jogadores humanos
• forneça um método para jogar o jogo; todo movimento deve ocorrer em uma
casa vazia; depois de cada movimento, determine se houve uma derrota ou um
empate.
'''

from enum import Enum

# Enumeração para representar as possibilidades de ocupação de uma casa na grade (vazia, jogador 1 ou jogador 2)
class EstadoCasa(Enum):
    VAZIA = " "
    JOGADOR1 = "X"
    JOGADOR2 = "O"

class NoughtsAndCrosses:
    def __init__(self):
        # Construtor que inicializa a grade como vazia
        self.__tabuleiro = [[EstadoCasa.VAZIA for _ in range(3)] for _ in range(3)]
    
    # Método para exibir a grade
    def exibir_grade(self):
        for linha in self.__tabuleiro:
            print("|".join(casa.value for casa in linha))
            print("-" * 5)
    
    # Método para jogar o jogo; todo movimento deve ocorrer em uma casa vazia; depois de cada movimento, determine se houve uma derrota ou um empate
    def jogar(self):
        jogador_atual = EstadoCasa.JOGADOR1
        while True:
            self.exibir_grade()
            try:
                # Entrada do jogador para linha e coluna
                linha = int(input(f"Jogador {1 if jogador_atual == EstadoCasa.JOGADOR1 else 2}, insira a linha (0-2): "))
                coluna = int(input(f"Jogador {1 if jogador_atual == EstadoCasa.JOGADOR1 else 2}, insira a coluna (0-2): "))
                if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                    print("Movimento inválido! As coordenadas devem estar entre 0 e 2.")
                    continue
            except ValueError:
                print("Entrada inválida! As coordenadas devem estar entre 0 e 2.")
                continue

            # Verifica se a casa está vazia antes de fazer o movimento
            if self.__tabuleiro[linha][coluna] == EstadoCasa.VAZIA:
                self.__tabuleiro[linha][coluna] = jogador_atual
                # Verifica se houve uma vitória
                if self.verificar_vencedor(jogador_atual):
                    self.exibir_grade()
                    print(f"Jogador {1 if jogador_atual == EstadoCasa.JOGADOR1 else 2} venceu!")
                    break
                # Verifica se houve um empate
                if self.verificar_empate():
                    self.exibir_grade()
                    print("Empate!")
                    break
                # Alterna o jogador atual
                jogador_atual = EstadoCasa.JOGADOR2 if jogador_atual == EstadoCasa.JOGADOR1 else EstadoCasa.JOGADOR1
            else:
                print("Casa já ocupada, escolha outra!")
    
    # Método para verificar se houve uma vitória
    def verificar_vencedor(self, jogador):
        for linha in self.__tabuleiro:
            if all(casa == jogador for casa in linha):
                return True
        for coluna in range(3):
            if all(self.__tabuleiro[linha][coluna] == jogador for linha in range(3)):
                return True
        if all(self.__tabuleiro[i][i] == jogador for i in range(3)) or all(self.__tabuleiro[i][2-i] == jogador for i in range(3)):
            return True
        return False
    
    # Método para verificar se houve um empate
    def verificar_empate(self):
        return all(casa != EstadoCasa.VAZIA for linha in self.__tabuleiro for casa in linha)

# Função principal para iniciar o jogo
def main():
    jogo = NoughtsAndCrosses()
    jogo.jogar()

if __name__ == "__main__":
    main()