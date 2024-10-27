'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

from point import Point
from circle import Circle
from rectangle import Rectangle

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

# Análise do Código
# Classe Abstrata Shape:

# A classe Shape é uma classe abstrata que define os métodos area() e circumference(). Qualquer forma que herde de Shape deve implementar esses métodos.
# Isso permite que você adicione novas formas (por exemplo, triângulos, elipses, etc.) sem modificar o código existente. Você simplesmente cria uma nova classe que herda de Shape e implementa os métodos necessários.
# Classes Concretas (Circle e Rectangle):

# As classes Circle e Rectangle estendem a classe Shape e implementam os métodos area() e circumference().
# Se você quiser adicionar uma nova forma, como um triângulo, você pode simplesmente criar uma nova classe chamada Triangle que herda de Shape, sem ter que alterar as classes Circle, Rectangle ou Shape.
# Extensibilidade:

# O código permite a adição de novas formas ao sistema sem modificar as classes existentes. Isso é fundamental para o OCP, pois a lógica existente permanece intacta e não precisa ser testada novamente após a adição de novas formas.
# O uso de uma classe base (abstrata) e a herança garante que novos comportamentos possam ser adicionados de forma segura e sem impacto nas implementações existentes.