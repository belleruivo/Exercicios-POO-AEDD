'''5. Escreva uma classe Point descrito por coordenadas reais x, y. Crie métodos get e set
e faça um programa de teste para a sua classe. A seguir, crie e teste os seguintes
métodos para a classe Ponto:
a. O método que recebe como parâmetros um deslocamento dx e outro dy para
movimentar o Ponto.
b. O método que retorna a distância entre este ponto e outro dado como
parâmetro.
Crie e teste um construtor para a classe Point, que inicialize x e y em 1, mas que
também possa receber valores dados.'''
import math

class Point:
    def __init__(self, x=1, y=1):
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

    def distancia(self, outro_ponto):
        dx = self.x - outro_ponto.getX()
        dy = self.y - outro_ponto.getY()
        return math.sqrt(dx**2 + dy**2)

def main():
    
    p1x = int(input("Insira o valor de X do primeiro ponto: "))
    p1y = int(input("Insira o valor de Y do primeiro ponto: "))
    
    p2x = int(input("Insira o valor de X do segundo ponto: "))
    p2y = int(input("Insira o valor de Y do segundo ponto: "))
    
    ponto1 = Point(p1x, p1y)
    ponto2 = Point(p2x, p2y)

    print(f"Ponto 1: {ponto1}")
    print(f"Ponto 2: {ponto2}")

    deslocamento_x = float(input("Digite o deslocamento em X para o ponto 1: "))
    deslocamento_y = float(input("Digite o deslocamento em Y para o ponto 1: "))
    ponto1.mover(deslocamento_x, deslocamento_y)
    
    print(f"Ponto 1 após movimentação: {ponto1}")

   
    distancia = ponto1.distancia(ponto2)
    print(f"Distância entre o ponto 1 e o ponto 2: {distancia:.2f}")


        
    
    
    p1 = Point()
    print(f"Ponto 1: {p1}")

    
    p2 = Point(3, 4)
    print(f"Ponto 2: {p2}")

    
    p1.mover(2, 3)
    print(f"Ponto 1 após movimentar: {p1}")

    
    distancia = p1.distancia(p2)
    print(f"Distância entre Ponto 1 e Ponto 2: {distancia:.2f}")

    
    p1.setX(5)
    p1.setY(6)
    print(f"Ponto 1 após SET: {p1}")
    print(f"Coordenada X de Ponto 1: {p1.getX()}")
    print(f"Coordenada Y de Ponto 1: {p1.getY()}")
