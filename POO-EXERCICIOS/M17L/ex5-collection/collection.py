from abc import ABC, abstractmethod

class Collection(ABC):
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    @abstractmethod # precisa ser implementado pelas subclasses
    def descricao(self):
        pass
