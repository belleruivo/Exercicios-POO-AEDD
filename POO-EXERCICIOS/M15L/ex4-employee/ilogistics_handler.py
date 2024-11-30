from abc import ABC, abstractmethod

class ILogisticsHandler(ABC):
    @abstractmethod
    def handle_logistics(self):
        """Gerencia a logística."""
        pass
