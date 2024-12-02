from abc import ABC, abstractmethod

class Borrowable(ABC):
    @abstractmethod
    def emprestar(self):
        pass

    @abstractmethod
    def devolver(self):
        pass