from interface import Vehicle, GPS

class Car(Vehicle, GPS):
    def start_engine(self):
        print("Motor do carro ligado.")

    def move(self):
        print("O carro está se movendo sobre rodas.")
    
    def get_location(self):
        print("O carro está localizado na Rua Faria Lima em São Paulo")

    def get_altitude(self):
        print("O carro está a uma altitude de 1.200 metros acima do nível do mar")

class Airplane(Vehicle, GPS):
    def start_engine(self):
        print("Motores do avião ligados.")

    def move(self):
        print("O avião está voando pelo céu.")

    def get_location(self):
        print("O avião está localizado nas coordenadas 40° N, 74° W.")

    def get_altitude(self):
        print("Altitude atual do avião: 10.000 metros acima do nível do mar")