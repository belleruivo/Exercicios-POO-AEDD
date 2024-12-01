from animal import Animal

class Reptil(Animal):
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def get_classificacao(self):
        return "Réptil"
    
    def emitir_som(self):
        return "Som de Réptil"
