from animal import Animal

class Mamifero(Animal):
    
    def __init__(self, nome, idade, habitat):
        super().__init__(nome, idade, habitat)

    def get_classificacao(self):
        return "Mamífero"
    
    def emitir_som(self):
        return "Som de Mamífero"
