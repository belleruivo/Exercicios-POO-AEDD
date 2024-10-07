class Velocidade:
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def get_velocidade(self):
        return self.velocidade

    def set_velocidade(self, velocidade):
        self.velocidade = velocidade

    def imprimir(self):
        print(f"Velocidade Atual: {self.velocidade} km/h")