from animal import Animal

class Ave(Animal):
    
    def __init__(self, nome, idade, habitat):
        super().__init__(nome, idade, habitat)

    def get_classificacao(self):
        return "Ave"
    
    def emitir_som(self):
        return "Som de Ave"
