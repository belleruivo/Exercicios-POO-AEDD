class Direção:
    def __init__(self, direção):
        self.direção = direção

    def get_direção(self):
        return self.direção

    def set_direção(self, direção):
        self.direção = direção

    def imprimir(self):
        print(f"Direção dos Pneus: {self.direção}°")