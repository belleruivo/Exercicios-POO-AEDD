from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

class GPS(ABC):
    @abstractmethod
    def get_location(self):
        pass

class Altitude(ABC):
    @abstractmethod
    def get_altitude(self):
        pass