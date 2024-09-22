'''
6. Escreva uma classe Circle composta de um ponto para indicar o centro e o tamanho
do raio, que não deve ser menor que zero. 

Utilize a classe Point criada anteriormente.

Crie métodos get e set para testar sua classe. A seguir crie:
a. Um método que retorne a área do círculo.
b. Um método move que movimente o centro do círculo (utilize o método move
da classe ponto).

Crie e teste um construtor para a classe Circle com todos os valores zerados, mas
que também possa receber valores dados.
'''

import math 

class Point:
    def __init__(self, x=0, y=0):  # a class point com atributos x e y, o self é a referência ao objeto que está sendo criado
        self.x = x
        self.y = y

    def move(self, dx, dy):  # método que muda a posição do ponto
        self.x += dx
        self.y += dy

class Circle:
    def __init__(self, center = None, radius = 0):  
        self.center = center if center is not None else Point() # se o centro não for fornecido, ele será o ponto (0, 0)
        self._radius = max(radius, 0)  # pelo menos 0, para que seja positivo

    @property
    def radius(self):  # getter para o raio
        return self._radius

    @radius.setter
    def radius(self, value):  # setter para o raio
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Ops... O raio não pode ser negativo!") 

    def area(self):  # método para calcular a área do círculo -> A = π * r²
        return math.pi * (self._radius ** 2)

    def move(self, dx, dy):  # mover o centro do círculo
        self.center.move(dx, dy)

def main():
    # círculo com valores padrão
    circle1 = Circle()
    print(f"Centro: ({circle1.center.x}, {circle1.center.y}), Raio: {circle1.radius}, Área: {circle1.area()}")

    # círculo com valores fornecido, criando a instancia de point, atribuindo x e y
    center_point = Point(5, 5)
    circle2 = Circle(center_point, 10)
    print(f"Centro: ({circle2.center.x}, {circle2.center.y}), Raio: {circle2.radius}, Área: {circle2.area()}")

    # aqui movemos o círculo
    circle2.move(3, 4)
    print(f"Novo Centro: ({circle2.center.x}, {circle2.center.y}), Raio: {circle2.radius}, Área: {circle2.area()}")

if __name__ == "__main__":
    main()  