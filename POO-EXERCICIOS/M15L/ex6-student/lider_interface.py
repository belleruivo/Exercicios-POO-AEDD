from abc import ABC, abstractmethod

class LiderInterface(ABC):
    
    @abstractmethod
    def is_lider(self):
        pass
