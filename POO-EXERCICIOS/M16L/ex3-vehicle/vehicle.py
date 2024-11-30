from abc import ABC, abstractmethod

# A abstração (interface) que define o comportamento de veículos
class Vehicle(ABC):
    def start_engine(self):
        print("Motor ligado.")

    @abstractmethod
    def move(self):
        pass

# Implementações concretas de diferentes tipos de veículos
class Car(Vehicle):
    def move(self):
        print("O carro está se movendo sobre rodas.")

class Boat(Vehicle):
    def move(self):
        print("O barco está navegando na água.")

# Agora, o controlador (classe de alto nível) depende da abstração (Vehicle) 
# e não das implementações concretas (Car ou Boat)

class VehicleController:
    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def start_and_move(self):
        self.vehicle.start_engine()
        self.vehicle.move()