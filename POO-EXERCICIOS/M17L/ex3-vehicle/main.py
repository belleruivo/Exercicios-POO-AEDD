from abc import ABC, abstractmethod

class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def ligar(self):
        print(f"O motor de {self.potencia} cavalos de potência e tipo {self.tipo} está ligado.")

class Vehicle(ABC):
    def __init__(self, motor):
        self.motor = motor  # A classe Vehicle tem uma referência ao motor

    def start_engine(self):
        self.motor.ligar()  # O veículo usa o motor para ligar

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def __init__(self, motor, modelo):
        super().__init__(motor)
        self.modelo = modelo

    def move(self):
        print(f"O carro {self.modelo} está em movimento.")

# Criando um motor
motor_v8 = Motor("V8", 400)

# Criando um veículo (carro) com o motor V8
carro = Car(motor_v8, "Civic")
carro.start_engine()  # Ligando o motor
carro.move()  # O carro em movimento

# Criando outro veículo com o mesmo motor
outro_carro = Car(motor_v8, "Corolla")
outro_carro.start_engine()
outro_carro.move()

