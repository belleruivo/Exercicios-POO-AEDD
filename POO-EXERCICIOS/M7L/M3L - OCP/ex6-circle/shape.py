# shape.py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calcula a área da forma."""
        pass

    @abstractmethod
    def circumference(self):
        """Calcula a circunferência da forma."""
        pass
