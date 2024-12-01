from animal import Animal
from voar_mixin import VoarMixin

class Ave(Animal, VoarMixin):
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def get_classificacao(self):
        return "Ave"
    
    def emitir_som(self):
        return "Som de Ave"
