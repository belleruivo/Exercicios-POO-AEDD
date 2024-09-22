'''
Escreva um programa completo para jogar o jogo da velha. Para tanto crie uma
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

class CellState(Enum):
    EMPTY = 0
    PLAYER_1 = 1
    PLAYER_2 = 2

class NoughtsAndCrosses:
    def __init__(self):
        self.grid = [[CellState.EMPTY for _ in range(3)] for _ in range(3)]
        self.current_player = CellState.PLAYER_1
    
    def display_grid(self):
        for row in self.grid:
            print(' | '.join(self.cell_to_string(cell) for cell in row))
            print("-" * 9)

    @staticmethod
    def cell_to_string(cell):
        if cell == CellState.EMPTY:
            return " "
        elif cell == CellState.PLAYER_1:
            return "X"
        elif cell == CellState.PLAYER_2:
            return "O"

    def play_game(self):
        while True:
            self.display_grid()
            row, col = self.get_move()
            if self.grid[row][col] != CellState.EMPTY:
                print("Movimento inválido! Casa ocupada, tente novamente.")
                continue
            self.grid[row][col] = self.current_player
            
            if self.check_winner():
                self.display_grid()
                print(f"Jogador {self.current_player.value} venceu!")
                break
            elif self.check_draw():
                self.display_grid()
                print("Empate!")
                break
            
            self.current_player = self.toggle_player()

    def get_move(self):
        while True:
            try:
                row = int(input(f"Jogador {self.current_player.value}, insira a linha (1-3): ")) - 1
                col = int(input(f"Jogador {self.current_player.value}, insira a coluna (1-3): ")) - 1
                if 0 <= row <= 2 and 0 <= col <= 2:
                    return row, col
                else:
                    print("Posição inválida. Insira valores entre 1 e 3.")
            except ValueError:
                print("Entrada inválida. Tente novamente.")

    def toggle_player(self):
        return CellState.PLAYER_2 if self.current_player == CellState.PLAYER_1 else CellState.PLAYER_1

    def check_winner(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != CellState.EMPTY:
                return True
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != CellState.EMPTY:
                return True
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != CellState.EMPTY:
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != CellState.EMPTY:
            return True
        return False

    def check_draw(self):
        return all(cell != CellState.EMPTY for row in self.grid for cell in row)

    @classmethod
    def create_full_grid(cls, player):
        instance = cls()
        instance.grid = [[player for _ in range(3)] for _ in range(3)]
        return instance

def main():
    game = NoughtsAndCrosses()
    game.play_game()

main()
