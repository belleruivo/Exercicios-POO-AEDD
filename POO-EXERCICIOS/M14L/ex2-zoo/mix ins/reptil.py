from animal import Animal
from nadar_mixin import NadarMixin

class Reptil(Animal, NadarMixin):
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def get_classificacao(self):
        return "Réptil"
    
    def emitir_som(self):
        return "Som de Réptil"
