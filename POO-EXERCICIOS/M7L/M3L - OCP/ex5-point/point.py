'''5. Escreva uma classe Point descrito por coordenadas reais x, y. Crie métodos get e set
e faça um programa de teste para a sua classe. A seguir, crie e teste os seguintes
métodos para a classe Ponto:
a. O método que recebe como parâmetros um deslocamento dx e outro dy para
movimentar o Ponto.
b. O método que retorna a distância entre este ponto e outro dado como
parâmetro. 
Crie e teste um construtor para a classe Point, que inicialize x e y em 1, mas que
também possa receber valores dados.
dAB² = (xB - xA)² + (yB - yA)².
'''
import math

class Point:
    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def exibir(self):
        print(f"Ponto(x: {self.x}, y: {self.y})")

class ManipuladorDePonto:
    @staticmethod
    def mover(ponto, dx, dy):
        ponto.set_x(ponto.get_x() + dx)
        ponto.set_y(ponto.get_y() + dy)

    @staticmethod
    def calcular_distancia(ponto1, ponto2):
        dx = ponto2.get_x() - ponto1.get_x()
        dy = ponto2.get_y() - ponto1.get_y()
        return math.sqrt(dx**2 + dy**2)
    
    #exemplo: poderia adicionar um metodo rotacionar sem alterar a classe Point

def obter_coordenada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um caractere numérico.\n")

def main():
    print("-=" * 30)
    print("Insira as coordenadas do primeiro ponto:")
    x1 = obter_coordenada("Digite o valor de x1: ")
    y1 = obter_coordenada("Digite o valor de y1: ")
    ponto1 = Point(x1, y1)

    print("\nInsira as coordenadas do segundo ponto:")
    x2 = obter_coordenada("Digite o valor de x2: ")
    y2 = obter_coordenada("Digite o valor de y2: ")
    ponto2 = Point(x2, y2)

    print("\nPonto 1:")
    ponto1.exibir()

    print("\nPonto 2:")
    ponto2.exibir()

    print("\nAgora, vamos mover o primeiro ponto.")
    dx = obter_coordenada("Digite o deslocamento em x (dx): ")
    dy = obter_coordenada("Digite o deslocamento em y (dy): ")
    ManipuladorDePonto.mover(ponto1, dx, dy)

    print("\nPonto 1 após o movimento:")
    ponto1.exibir()

    distancia = ManipuladorDePonto.calcular_distancia(ponto1, ponto2)
    print(f"\nA distância entre o ponto 1 e o ponto 2 é: {distancia:.2f}")
    print("-=" * 30)

main()