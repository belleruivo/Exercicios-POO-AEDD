
from abc import ABC, abstractmethod
from habitat import Habitat

class Animal(ABC):
    
    def __init__(self, nome, idade, habitat: Habitat):
        self.nome = nome
        self.idade = idade
        self.habitat = habitat
    
    @abstractmethod
    def get_classificacao(self):
        pass
    
    @abstractmethod
    def emitir_som(self):
        pass
