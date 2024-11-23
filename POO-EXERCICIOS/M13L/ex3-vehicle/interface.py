from abc import ABC, abstractmethod

class Vehicles(ABC):

    @abstractmethod
    def register(self):
        pass
    
    @abstractmethod
    def consult_vehicle(self):
       pass
    
    