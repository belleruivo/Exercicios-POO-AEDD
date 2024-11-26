'''
Implemente um sistema de Concessionária com os tipos de veículos (automóvel,
moto, caminhão, etc.), evidenciando a classe Vehicle como uma classe abstrata.
'''
from vehicles import * 

def main():
    carro = Carro()
    caminhao = Caminhao()

    while True:
        try:
            print("-"*20,"Menu", "-"*20)
            print("1. Registrar Veículo")
            print("2. Consultar Veículo")
            print("3. Sair")

            escolha = int(input("Escolha uma opção: "))

            if escolha == 1:
                print("\nVEÍCULOS:\n1. Carro\n2. Caminhão\n")
                veiculo = int(input("Qual veículo você deseja registrar? "))

                if veiculo == 1:
                    carro.registrar()
                elif veiculo == 2:
                    caminhao.registrar()
                else:
                    print("Opção inválida.")

            elif escolha == 2:
                print("\nVEÍCULOS:\n1. Carro\n2. Moto\n3. Caminhão\n")
                veiculo = int(input("Qual veículo você deseja consultar? "))

                if veiculo == 1:
                    carro.consultar_veiculo()
                elif veiculo == 2:
                    caminhao.consultar_veiculo()
                else:
                    print("Opção inválida.")

            elif escolha == 3:
                print("Saindo...")
                break

            else:
                print("Valor inválido. Tente novamente.")
        except ValueError:
            print("Por favor, insira uma opção válida.")


main()