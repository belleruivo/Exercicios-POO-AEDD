import random

class NumeroGerado:
    def __init__(self):
        self.numero = random.randint(1, 100)  # Gera número entre 1 e 100

    def verificar_palpite(self, palpite):
        if palpite < self.numero:
            return "o palpite é menor que o número gerado."
        elif palpite > self.numero:
            return "o palpite é maior que o número gerado."
        else:
            return "Parabéns! Você adivinhou o número."
