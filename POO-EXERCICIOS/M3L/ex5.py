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
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y
    
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def distancia(self, outro_ponto):
        dx = outro_ponto.getX() - self.x
        dy = outro_ponto.getY() - self.y
        return math.sqrt(dx**2 + dy**2)
    
    def exibir(self):
        print(f"Point(x: {self.x}, y: {self.y})")

def obter_coordenada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um caractere numérico.\n")

def main():
    print("-="*30)
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
    ponto1.mover(dx, dy)

    print("\nPonto 1 após o movimento:")
    ponto1.exibir()

    distancia = ponto1.distancia(ponto2)
    print(f"\nA distância entre o ponto 1 e o ponto 2 é: {distancia:.2f}")
    print("-="*30)

main()