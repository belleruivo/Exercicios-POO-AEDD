'''Refazer a Lista M3L, aplicando o Princípio da Responsabilidade Única e mostrar as
diferenças de seu código, antes e depois.'''

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Circle:
    def __init__(self, center=None, radius=0):
        self.center = center if center is not None else Point()
        self._radius = max(radius, 0)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Ops... O raio não pode ser negativo!")

    def area(self):
        return math.pi * (self._radius ** 2)

    def move(self, dx, dy):
        self.center.move(dx, dy)

class CircleDisplay:
    def display(self, circle):
        print(f"Centro: ({circle.center.x}, {circle.center.y}), Raio: {circle.radius}, Área: {circle.area()}")

def main():
    # círculo com valores padrão
    circle1 = Circle()
    display = CircleDisplay()
    display.display(circle1)

    # círculo com valores fornecidos
    center_point = Point(5, 5)
    circle2 = Circle(center_point, 10)
    display.display(circle2)

    # movendo o círculo
    circle2.move(3, 4)
    display.display(circle2)

if __name__ == "__main__":
    main()