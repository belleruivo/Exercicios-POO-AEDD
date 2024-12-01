from animal import Animal
from nadar_interface import NadarInterface

class Reptil(Animal, NadarInterface):
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def get_classificacao(self):
        return "Réptil"
    
    def emitir_som(self):
        return "Som de Réptil"
    
    def nadar(self):
        return "Este animal pode nadar."
