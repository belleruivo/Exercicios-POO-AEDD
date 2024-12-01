from animal import Animal

class Ave(Animal):
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def get_classificacao(self):
        return "Ave"
    
    def emitir_som(self):
        return "Som de Ave"
