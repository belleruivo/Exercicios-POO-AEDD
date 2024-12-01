from animal import Animal

class Mamifero(Animal):
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def get_classificacao(self):
        return "Mamífero"
    
    def emitir_som(self):
        return "Som de Mamífero"
