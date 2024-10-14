class Proprietario:
    def __init__(self, nome):
        self.nome = nome
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def imprimir_veiculos(self):
        print(f"\nVeículos de {self.nome}:")
        for i, veiculo in enumerate(self.veiculos, start=1):  # Enumerate com contagem iniciando em 1
            print(f"{i}-")
            print(f"   Velocidade: {veiculo.getVelocidade()} km/h")
            print(f"   Direção: {veiculo.getDireção()}°")