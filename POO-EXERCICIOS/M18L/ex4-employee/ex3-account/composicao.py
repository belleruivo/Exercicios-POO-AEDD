from abc import ABC, abstractmethod

class Engine:
    def start(self):
        print("Motor ligado.")

class Vehicle(ABC):
    def __init__(self):
        self.engine = Engine()  # Composição: o veículo tem um motor

    def start_engine(self):
        self.engine.start()

    @abstractmethod
    def move(self):
        pass