from vehicle import Vehicle

class Carro(Vehicle):
    def __init__(self, velocidade, direcao, owner):
        super().__init__(velocidade, direcao, owner)