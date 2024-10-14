from proprietario import Proprietario

class Vehicle:
    def __init__(self, velocidade, direção, owner):
        self.velocidade = velocidade
        self.direção = direção
        self.owner = owner
        owner.adicionar_veiculo(self)  # Associa o veículo ao proprietário

    def getVelocidade(self):
        return self.velocidade

    def getDireção(self):
        return self.direção

    def getNome(self):
        return self.owner.nome  # Obtém o nome do proprietário

    def setVelocidade(self, velocidade):
        self.velocidade = velocidade

    def setDireção(self, direção):
        self.direção = direção