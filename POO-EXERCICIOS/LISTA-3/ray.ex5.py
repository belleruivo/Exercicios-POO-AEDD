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

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def distancia(self, outro_ponto):
        dx = outro_ponto.x - self.getX()
        dy = outro_ponto.y - self.getY()
        return math.sqrt(dx**2 + dy**2)

        
def main():
    x1 = float(input("Insira a coordenada x do Ponto 1: "))
    y1 = float(input("Insira a coordenada y do Ponto 1: "))
    p1 = Point(x1, y1)

    x2 = float(input("Insira a coordenada x do Ponto 2: "))
    y2 = float(input("Insira a coordenada y do Ponto 2: "))
    p2 = Point(x2, y2)
   
    print(f"Ponto 1: ({p1.getX()}, {p1.gety()})")
    print(f"Ponto 2: ({p2.getx()}, {p2.gety()})")

    distancia = p1.distance(p2)
    print(f"Distância entre Ponto 1 e Ponto 2: {distancia}")
