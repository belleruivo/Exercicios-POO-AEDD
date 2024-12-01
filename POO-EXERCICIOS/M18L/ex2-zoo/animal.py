from abc import ABC, abstractmethod
from alimentacao import Alimentacao
from cuidados import Cuidados

class Animal(ABC):
    
    def __init__(self, nome, idade, alimentacao: Alimentacao, cuidados: Cuidados):
        self.nome = nome
        self.idade = idade
        self.alimentacao = alimentacao
        self.cuidados = cuidados
    
    @abstractmethod
    def get_classificacao(self):
        pass
    
    @abstractmethod
    def emitir_som(self):
        pass
