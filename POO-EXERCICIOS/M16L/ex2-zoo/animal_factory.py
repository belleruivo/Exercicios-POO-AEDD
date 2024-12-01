from mamifero import Mamifero
from ave import Ave
from reptil import Reptil

class AnimalFactory:
    
    @staticmethod
    def create_animal(tipo, nome, idade):
        if tipo == 1:
            return Mamifero(nome, idade)
        elif tipo == 2:
            return Ave(nome, idade)
        elif tipo == 3:
            return Reptil(nome, idade)
        else:
            raise ValueError("Tipo inválido.")
