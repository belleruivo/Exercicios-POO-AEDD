class Vehicle:
    def __init__(self, velocidade_kmh, direcao_graus, proprietario):
        self.velocidade_kmh = velocidade_kmh
        self.direcao_graus = direcao_graus
        self.proprietario = proprietario

    # Métodos de acesso
    def get_velocidade(self):
        return self.velocidade_kmh

    def get_direcao(self):
        return self.direcao_graus

    def get_proprietario(self):
        return self.proprietario

    # Métodos de modificação
    def set_velocidade(self, velocidade_kmh):
        self.velocidade_kmh = velocidade_kmh

    def set_direcao(self, direcao_graus):
        self.direcao_graus = direcao_graus

    def set_proprietario(self, proprietario):
        self.proprietario = proprietario

    # Método para imprimir as informações do veículo
    def imprimir_info(self):
        print(f"Proprietário: {self.proprietario}")
        print(f"Velocidade: {self.velocidade_kmh} km/h")
        print(f"Direção dos pneus: {self.direcao_graus} graus")

    # Método especial para exibir uma representação do veículo
    def __str__(self):
        return (f"Vehicle(proprietario={self.proprietario}, "
                f"velocidade_kmh={self.velocidade_kmh}, "
                f"direcao_graus={self.direcao_graus})")
        

meu_veiculo = Vehicle(100, 45, "Carlos Silva")

# Imprimir informações usando o método imprimir_info
meu_veiculo.imprimir_info()

# Modificar alguns atributos
meu_veiculo.set_velocidade(120)
meu_veiculo.set_direcao(90)
meu_veiculo.set_proprietario("Ana Costa")

# Imprimir informações novamente para verificar as alterações
print("\nInformações atualizadas:")
meu_veiculo.imprimir_info()

# Usar o método __str__ para imprimir a representação do objeto
print("\nRepresentação do veículo:")
print(meu_veiculo)