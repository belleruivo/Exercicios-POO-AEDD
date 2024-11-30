from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        self.veiculos = []

    @abstractmethod
    def registrar(self):
        pass

    def consultar_veiculo(self):
        if not self.veiculos:
            print("Nenhum veículo registrado ainda.")
            return

        print("\nVeículos Registrados:")
        for i, veiculo in enumerate(self.veiculos, start=1):
            print(f"\nVeículo {i}:")
            for chave, valor in veiculo.items():
                print(f"  {chave}: {valor}")