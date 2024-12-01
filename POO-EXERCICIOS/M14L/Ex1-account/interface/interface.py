from abc import ABC, abstractmethod

class LimiteCreditoInterface(ABC):
    @abstractmethod
    def set_limite(self, limite):
        pass
    
    @abstractmethod
    def get_limite(self):
        pass

class JurosInterface(ABC):
    @abstractmethod
    def aplicar_juros(self):
        pass

class RendimentoInterface(ABC):
    @abstractmethod
    def aplicar_rendimento(self):
        pass



