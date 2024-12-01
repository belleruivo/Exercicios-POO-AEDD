from classeAbstrata import Vehicle

class Carro(Vehicle):
    def move(self):
        print("O carro está se movendo sobre rodas.")

class Barco(Vehicle):
    def move(self):
        print("O barco está navegando na água.")

class Driver:
    def __init__(self, name):
        self.name = name 
        self.vehicles = []  

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def list_vehicles(self):
        print(f"\nVeículos associados ao motorista {self.name}:")
        for i, vehicle in enumerate(self.vehicles, 1):
            print(f"{i}. {type(vehicle).__name__}")

    def drive_vehicle(self, vehicle_index):
        vehicle = self.vehicles[vehicle_index]
        print(f"\nMotorista {self.name} está dirigindo o {type(vehicle).__name__}")
        vehicle.start_engine()
        vehicle.move()
