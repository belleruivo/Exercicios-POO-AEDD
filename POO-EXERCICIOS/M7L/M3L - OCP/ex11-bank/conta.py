class Conta:
    def __init__(self, nome, pin):
        self.nome = nome
        self.pin = pin

    def getNome(self):
        return self.nome

    def getPin(self):
        return self.pin

    def calcularJuros(self):
        return 0  # Implementação padrão

    def __str__(self):
        return f"Conta: {self.nome}, PIN: {self.pin}"

