class Proprietario:
    def __init__(self, nome):
        self.nome = nome
        self.veiculos = [] #lista de veículos associados ao proprietário

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo) #associa o veículo ao proprietário

    def imprimir_veiculos(self):
        print(f"\nVeículos de {self.nome}:")
        for i, veiculo in enumerate(self.veiculos, start=1): 
            print()
            print(f"{i}.Velocidade: {veiculo.get_velocidade()} km/h")
            print(f"    Direção: {veiculo.get_direcao()}°")