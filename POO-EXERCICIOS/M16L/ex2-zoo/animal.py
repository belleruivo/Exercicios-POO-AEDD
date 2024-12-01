from abc import ABC, abstractmethod

class Animal(ABC):
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @abstractmethod
    def get_classificacao(self):
        pass
    
    @abstractmethod
    def emitir_som(self):
        pass
