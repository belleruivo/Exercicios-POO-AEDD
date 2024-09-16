'''5. Escreva uma classe Point descrito por coordenadas reais x, y. Crie métodos get e set
e faça um programa de teste para a sua classe. A seguir, crie e teste os seguintes
métodos para a classe Ponto:
a. O método que recebe como parâmetros um deslocamento dx e outro dy para
movimentar o Ponto.
b. O método que retorna a distância entre este ponto e outro dado como
parâmetro.
Crie e teste um construtor para a classe Point, que inicialize x e y em 1, mas que
também possa receber valores dados.'''

class Point:
    def __init__(self, x, y):
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
