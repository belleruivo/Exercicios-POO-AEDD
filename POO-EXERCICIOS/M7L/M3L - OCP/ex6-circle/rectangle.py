# rectangle.py
from shape import Shape

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
