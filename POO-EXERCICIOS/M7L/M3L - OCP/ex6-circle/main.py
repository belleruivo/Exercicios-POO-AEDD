# main.py
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
