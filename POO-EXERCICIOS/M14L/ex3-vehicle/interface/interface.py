from abc import ABC, abstractmethod

<<<<<<< HEAD
class InterfaceVeiculos(ABC):
    @abstractmethod
    def registrar(self):
        pass

    @abstractmethod
    def consultar_veiculo(self):
        pass
=======
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

    @abstractmethod
    def get_altitude(self):
        pass


>>>>>>> 8d4c7a5a5e476c0d2f16b37e02f1281d78c4562b