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

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def distancia(self, outro_ponto):
         return math.sqrt((self.x - outro_ponto.x) ** 2 + (self.y - outro_ponto.y) ** 2)
    
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"


if __name__ == "__main__":
    
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
