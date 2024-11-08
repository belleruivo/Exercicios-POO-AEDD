from pilha import Pilha
from fila import Fila

class SeparadorParImpar:
    def __init__(self, pilha):
        self.pilha = pilha
        self.fila_pares = Fila()
        self.fila_impares = Fila()

    def separar(self):
        # Separar os números da pilha em pares e ímpares
        while not self.pilha.is_empty():
            numero = self.pilha.pop()
            if numero % 2 == 0:
                self.fila_pares.enqueue(numero)
            else:
                self.fila_impares.enqueue(numero)

    def get_fila_pares(self):
        return self.fila_pares

    def get_fila_impares(self):
        return self.fila_impares
