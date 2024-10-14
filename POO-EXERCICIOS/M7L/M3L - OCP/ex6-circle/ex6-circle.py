'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

import math
from abc import ABC, abstractmethod

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """Move o ponto para uma nova posição."""
        self.x += dx
        self.y += dy

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calcula a área da forma."""
        pass

    @abstractmethod
    def circumference(self):
        """Calcula a circunferência da forma."""
        pass

class Circle(Shape):
    def __init__(self, center=None, radius=0):
        """Inicializa o círculo com um ponto central e um raio."""
        self.center = center if center is not None else Point()
        self._radius = max(radius, 0)

    @property
    def radius(self):
        """Obtém o raio do círculo."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Define o raio do círculo, garantindo que seja não negativo."""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Ops... O raio não pode ser negativo!") 

    def area(self):
        """Calcula a área do círculo."""
        return math.pi * (self._radius ** 2)

    def circumference(self):
        """Calcula a circunferência do círculo."""
        return 2 * math.pi * self._radius

    def move(self, dx, dy):
        """Move o círculo para uma nova posição."""
        self.center.move(dx, dy)

class Rectangle(Shape):
    def __init__(self, width, height):
        """Inicializa o retângulo com uma largura e altura."""
        self.width = width
        self.height = height

    def area(self):
        """Calcula a área do retângulo."""
        return self.width * self.height

    def circumference(self):
        """Calcula o perímetro do retângulo."""
        return 2 * (self.width + self.height)

def main():
    # Testando o círculo
    circle1 = Circle()
    print(f"Centro: ({circle1.center.x}, {circle1.center.y}), Raio: {circle1.radius}, Área: {circle1.area()}, Circunferência: {circle1.circumference()}")

    center_point = Point(5, 5)
    circle2 = Circle(center_point, 10)
    print(f"Centro: ({circle2.center.x}, {circle2.center.y}), Raio: {circle2.radius}, Área: {circle2.area()}, Circunferência: {circle2.circumference()}")

    circle2.move(3, 4)
    print(f"Novo Centro: ({circle2.center.x}, {circle2.center.y}), Raio: {circle2.radius}, Área: {circle2.area()}, Circunferência: {circle2.circumference()}")

    # Testando o retângulo
    rectangle = Rectangle(4, 6)
    print(f"Retângulo - Largura: {rectangle.width}, Altura: {rectangle.height}, Área: {rectangle.area()}, Perímetro: {rectangle.circumference()}")

if __name__ == "__main__":
    main()
