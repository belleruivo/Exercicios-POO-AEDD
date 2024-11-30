from abc import ABC, abstractmethod

class Vehicle(ABC):
    def start_engine(self):
        print("Motor ligado.")

    @abstractmethod
    def move(self):
        pass
