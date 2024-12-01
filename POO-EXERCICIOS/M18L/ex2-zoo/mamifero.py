from animal import Animal

class Mamifero(Animal):
    
    def __init__(self, nome, idade, alimentacao, cuidados):
        super().__init__(nome, idade, alimentacao, cuidados)

    def get_classificacao(self):
        return "Mamífero"
    
    def emitir_som(self):
        return "Som de Mamífero"
