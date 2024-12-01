from abc import ABC, abstractmethod


class Registravel(ABC):
    @abstractmethod
    def registrar(self):
        pass


class Financiavel(ABC):
    @abstractmethod
    def calcular_financiamento(self, meses):
        pass


class AvaliacaoSeguro(ABC):
    @abstractmethod
    def avaliar_seguro(self):
        pass


class Vehicle(Registravel, ABC):
    def __init__(self, ano, marca, seguro):
        self.ano = ano
        self.marca = marca
        self.seguro = seguro

    def vender(self):
        return f"{self.__class__.__name__} {self.marca} de {self.ano} vendido!"


# Registrando as classes em suas respectivas interfaces (Financiavel e AvaliacaoSeguro)
Financiavel.register(Vehicle)
AvaliacaoSeguro.register(Vehicle)


class Carro(Vehicle):
    def __init__(self, ano, marca, seguro, portas):
        super().__init__(ano, marca, seguro)
        self.portas = portas

    def registrar(self):
        return f"Carro {self.marca} de {self.ano} registrado com {self.portas} portas."

    def calcular_financiamento(self, meses):
        return f"Financiamento do carro por {meses} meses."

    def avaliar_seguro(self):
        return "Seguro do carro avaliado."


# Registrando a classe Carro em Financiavel e AvaliacaoSeguro
Financiavel.register(Carro)
AvaliacaoSeguro.register(Carro)


class Moto(Vehicle):
    def __init__(self, ano, marca, seguro, cilindradas):
        super().__init__(ano, marca, seguro)
        self.cilindradas = cilindradas

    def registrar(self):
        return f"Moto {self.marca} de {self.ano} registrada com {self.cilindradas} cilindradas."

    def calcular_financiamento(self, meses):
        return f"Financiamento da moto por {meses} meses."

    def avaliar_seguro(self):
        return "Seguro da moto avaliado."


# Registrando a classe Moto em Financiavel e AvaliacaoSeguro
Financiavel.register(Moto)
AvaliacaoSeguro.register(Moto)


class Caminhao(Vehicle):
    def __init__(self, ano, marca, seguro, capacidade_carga):
        super().__init__(ano, marca, seguro)
        self.capacidade_carga = capacidade_carga

    def registrar(self):
        return f"Caminhão {self.marca} de {self.ano} registrado com capacidade de {self.capacidade_carga} toneladas."

    def calcular_financiamento(self, meses):
        return f"Financiamento do caminhão por {meses} meses."

    def avaliar_seguro(self):
        return "Seguro do caminhão avaliado."


# Registrando a classe Caminhao em Financiavel e AvaliacaoSeguro
Financiavel.register(Caminhao)
AvaliacaoSeguro.register(Caminhao)


# Sistema principal
def main():
    lista_veiculos = []

    while True:
        print("\n=== Sistema de Concessionária ===")
        print("1. Registrar veículo")
        print("2. Vender veículo")
        print("3. Calcular financiamento")
        print("4. Avaliar seguro")
        print("5. Sair")

        while True:
            opcao = input("Escolha uma opção: ").strip()
            if opcao not in {"1", "2", "3", "4", "5"}:
                print("Opção inválida! Tente novamente.\n")
            else:
                break

        if opcao == "1":  # Registrar veículo
            print("\nEscolha o tipo de veículo:")
            print("1. Carro")
            print("2. Moto")
            print("3. Caminhão\n")

            while True:
                tipo = input("Digite o número correspondente ao tipo de veículo: ").strip()
                if tipo not in {"1", "2", "3"}:
                    print("Tipo inválido! Tente novamente.\n")
                else:
                    break

            while True:
                try:
                    ano = int(input("Digite o ano do veículo: "))
                    break
                except ValueError:
                    print("Certifique-se de inserir um ano válido!\n")

            marca = input("Digite a marca do veículo: ")

            while True:
                seguro = input("O veículo possui seguro? (sim/não): ").strip().lower()
                if seguro in ("sim", "não"):
                    break
                print("Entrada inválida! Responda com 'sim' ou 'não'.\n")

            if tipo == "1":
                while True:
                    try:
                        portas = int(input("Digite o número de portas do automóvel: "))
                        veiculo = Carro(ano, marca, seguro, portas)
                        lista_veiculos.append(veiculo)
                        print("Carro registrado com sucesso!")
                        break
                    except ValueError:
                        print("Certifique-se de inserir um número válido!\n")
            elif tipo == "2":
                while True:
                    try:
                        cilindradas = int(input("Digite a quantidade de cilindradas da moto: "))
                        veiculo = Moto(ano, marca, seguro, cilindradas)
                        lista_veiculos.append(veiculo)
                        print("Moto registrada com sucesso!")
                        break
                    except ValueError:
                        print("Certifique-se de inserir um número válido!\n")
            elif tipo == "3":
                while True:
                    try:
                        capacidade_carga = float(input("Digite a capacidade de carga do caminhão (em toneladas): "))
                        veiculo = Caminhao(ano, marca, seguro, capacidade_carga)
                        lista_veiculos.append(veiculo)
                        print("Caminhão registrado com sucesso!")
                        break
                    except ValueError:
                        print("Certifique-se de inserir um número válido!\n")

        elif opcao == "2":  # Vender veículo
            if not lista_veiculos:
                print("Nenhum veículo registrado para venda!")
            else:
                print("\nVeículos registrados:")
                for i, veiculo in enumerate(lista_veiculos, 1):
                    print(f"{i}. {veiculo.registrar()}")

                while True:
                    try:
                        venda_id = int(input("\nDigite o número do veículo a ser vendido: ")) - 1
                        if 0 <= venda_id < len(lista_veiculos):
                            veiculo_vendido = lista_veiculos.pop(venda_id)
                            print(f"\n{veiculo_vendido.vender()}")
                            break
                        else:
                            print("Opção inválida! Tente novamente.\n")
                    except ValueError:
                        print("Entrada inválida! Digite um número.\n")

        elif opcao == "3":  # Calcular financiamento
            if not lista_veiculos:
                print("Nenhum veículo registrado para calcular financiamento!")
            else:
                print("\nVeículos disponíveis para financiamento:")
                for i, veiculo in enumerate(lista_veiculos, 1):
                    print(f"{i}. {veiculo.registrar()}")

                while True:
                    try:
                        financiamento_id = int(input("\nDigite o número do veículo para calcular o financiamento: ")) - 1
                        if 0 <= financiamento_id < len(lista_veiculos):
                            veiculo = lista_veiculos[financiamento_id]
                            if isinstance(veiculo, Financiavel):
                                meses = int(input("Digite o número de meses para o financiamento: "))
                                print(veiculo.calcular_financiamento(meses))
                            else:
                                print("Este veículo não é financiável!")
                            break
                        else:
                            print("Opção inválida! Tente novamente.\n")
                    except ValueError:
                        print("Entrada inválida! Digite um número.\n")

        elif opcao == "4":  # Avaliar seguro
            if not lista_veiculos:
                print("Nenhum veículo registrado para avaliar seguro!")
            else:
                print("\nVeículos disponíveis para avaliação de seguro:")
                for i, veiculo in enumerate(lista_veiculos, 1):
                    print(f"{i}. {veiculo.registrar()}")

                while True:
                    try:
                        seguro_id = int(input("\nDigite o número do veículo para avaliar o seguro: ")) - 1
                        if 0 <= seguro_id < len(lista_veiculos):
                            veiculo = lista_veiculos[seguro_id]
                            if isinstance(veiculo, AvaliacaoSeguro):
                                print(veiculo.avaliar_seguro())
                            else:
                                print("Este veículo não pode ser avaliado para seguro!")
                            break
                        else:
                            print("Opção inválida! Tente novamente.\n")
                    except ValueError:
                        print("Entrada inválida! Digite um número.\n")

        elif opcao == "5":  # Sair
            print("\nSaindo do sistema...")
            break


main()
