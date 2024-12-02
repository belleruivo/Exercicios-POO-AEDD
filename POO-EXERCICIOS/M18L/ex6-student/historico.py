class Historico:
    
    def __init__(self, notas=[]):
        self.notas = notas

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0.0
