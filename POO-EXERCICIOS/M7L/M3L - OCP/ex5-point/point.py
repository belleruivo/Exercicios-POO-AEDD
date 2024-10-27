
class Point:
    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def exibir(self):
        print(f"Ponto(x: {self.x}, y: {self.y})")