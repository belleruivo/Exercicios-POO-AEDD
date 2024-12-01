from abc import ABC, abstractmethod


# Interface para funcionalidade de venda
class Vender(ABC):
    @abstractmethod
    def vender(self):
        pass


# Interface para funcionalidade de registro
class Registrar(ABC):
    @abstractmethod
    def registrar(self):
        pass


# Classe Carro implementando as interfaces Vender e Registrar
class Carro(Vender, Registrar):
    def __init__(self, ano, marca, seguro, portas):
        self.ano = ano
        self.marca = marca
        self.seguro = seguro
        self.portas = portas

    def vender(self):
        return f"Carro {self.marca} {self.ano} vendido!"

    def registrar(self):
        return f"Carro {self.marca} de {self.ano} registrado com {self.portas} portas."


# Classe Moto implementando as interfaces Vender e Registrar
class Moto(Vender, Registrar):
    def __init__(self, ano, marca, seguro, cilindradas):
        self.ano = ano
        self.marca = marca
        self.seguro = seguro
        self.cilindradas = cilindradas

    def vender(self):
        return f"Moto {self.marca} {self.ano} vendida!"

    def registrar(self):
        return f"Moto {self.marca} de {self.ano} registrada com {self.cilindradas} cilindradas."


# Classe Caminhao implementando as interfaces Vender e Registrar
class Caminhao(Vender, Registrar):
    def __init__(self, ano, marca, seguro, capacidade_carga):
        self.ano = ano
        self.marca = marca
        self.seguro = seguro
        self.capacidade_carga = capacidade_carga

    def vender(self):
        return f"Caminhão {self.marca} {self.ano} vendido!"

    def registrar(self):
        return f"Caminhão {self.marca} de {self.ano} registrado com capacidade de {self.capacidade_carga} toneladas."


def main():
    lista_veiculos = []  # Lista para armazenar os veículos registrados
    while True:
        print("\n=== Sistema de Concessionária ===")
        print("1. Registrar veículo")
        print("2. Vender veículo")
        print("3. Exibir veículos registrados")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            # Registrar veículo
            print("\nEscolha o tipo de veículo:")
            print("1. Automóvel")
            print("2. Moto")
            print("3. Caminhão")

            while True:
                tipo = input("Digite o número correspondente ao tipo de veículo: ").strip()
                if tipo not in {"1", "2", "3"}:
                    print("Tipo inválido! Tente novamente.")
                else:
                    break

            while True:
                try:
                    ano = int(input("Digite o ano do veículo: "))
                    break
                except ValueError:
                    print("Certifique-se de inserir um ano válido!")

            marca = input("Digite a marca do veículo: ")

            while True:
                seguro = input("O veículo possui seguro? (sim/não): ").strip().lower()
                if seguro in ("sim", "não"):
                    break
                print("Entrada inválida! Responda com 'sim' ou 'não'.")

            if tipo == "1":
                while True:
                    try:
                        portas = int(input("Digite o número de portas do automóvel: "))
                        veiculo = Carro(ano, marca, seguro, portas)
                        lista_veiculos.append(veiculo)
                        print("Veículo registrado com sucesso!")
                        break
                    except ValueError:
                        print("Certifique-se de inserir um número válido!")
            elif tipo == "2":
                while True:
                    try:
                        cilindradas = int(input("Digite a quantidade de cilindradas da moto: "))
                        veiculo = Moto(ano, marca, seguro, cilindradas)
                        lista_veiculos.append(veiculo)
                        print("Veículo registrado com sucesso!")
                        break
                    except ValueError:
                        print("Certifique-se de inserir um número válido!")
            elif tipo == "3":
                while True:
                    try:
                        capacidade_carga = float(input("Digite a capacidade de carga do caminhão (em toneladas): "))
                        veiculo = Caminhao(ano, marca, seguro, capacidade_carga)
                        lista_veiculos.append(veiculo)
                        print("Veículo registrado com sucesso!")
                        break
                    except ValueError:
                        print("Certifique-se de inserir um número válido!")

        elif opcao == "2":
            # Vender veículo
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
                            # Exibe a venda com as informações no formato desejado
                            print(f"\n{veiculo_vendido.vender()}")
                            break
                        else:
                            print("Opção inválida! Tente novamente.")
                    except ValueError:
                        print("Entrada inválida! Digite um número.")

        elif opcao == "3":
            # Exibir veículos registrados
            if not lista_veiculos:
                print("Nenhum veículo registrado.")
            else:
                print("\nVeículos registrados:")
                for veiculo in lista_veiculos:
                    print(veiculo.registrar())

        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
