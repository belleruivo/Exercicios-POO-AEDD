from composicao import Vehicle

class Car(Vehicle):
    def move(self):
        print("O carro está se movendo sobre rodas.")

class Boat(Vehicle):
    def move(self):
        print("O barco está navegando na água.")