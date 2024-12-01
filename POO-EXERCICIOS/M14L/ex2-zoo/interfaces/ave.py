from animal import Animal
from voar_interface import VoarInterface

class Ave(Animal, VoarInterface):
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def get_classificacao(self):
        return "Ave"
    
    def emitir_som(self):
        return "Som de Ave"
    
    def voar(self):
        return "Este animal pode voar."
