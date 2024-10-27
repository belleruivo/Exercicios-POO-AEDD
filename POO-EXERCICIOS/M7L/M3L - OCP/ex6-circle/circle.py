# circle.py
import math
from point import Point
from shape import Shape

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
