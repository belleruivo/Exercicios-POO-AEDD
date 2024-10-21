class Vehicle:
    def __init__(self, velocidade, direção, nome):
        self.velocidade = velocidade
        self.direção = direção
        self.nome = nome
                                                                                                                                               
    def get_velocidade(self):
        return self.velocidade
    
    def get_direção(self):
        return self.direção
    
    def get_nome(self):
        return self.nome

    def set_velocidade(self, velocidade):
        self.velocidade = velocidade
        
    def set_direção(self, direção):
        self.direção = direção
        
    def set_nome(self, nome):
        self.nome = nome
        