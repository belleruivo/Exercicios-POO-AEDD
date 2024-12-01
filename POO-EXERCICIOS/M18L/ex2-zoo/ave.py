from animal import Animal

class Ave(Animal):
    
    def __init__(self, nome, idade, alimentacao, cuidados):
        super().__init__(nome, idade, alimentacao, cuidados)

    def get_classificacao(self):
        return "Ave"
    
    def emitir_som(self):
        return "Som de Ave"
