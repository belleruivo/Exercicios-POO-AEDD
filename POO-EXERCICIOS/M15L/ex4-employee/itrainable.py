from abc import ABC, abstractmethod

class ITrainable(ABC):
    @abstractmethod
    def conduct_training(self):
        """Realiza um treinamento."""
        pass
