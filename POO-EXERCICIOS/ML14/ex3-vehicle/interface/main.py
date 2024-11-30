from veiculos import Carro, Caminhao

def main():
    carro = Carro()
    caminhao = Caminhao()

    while True:
        print("-" * 20, "Menu", "-" * 20)
        print("1. Registrar Veículo")
        print("2. Consultar Veículo")
        print("3. Agendar Manutenção")
        print("4. Consultar Manutenções")
        print("5. Sair")

        while True:
            escolha = input("\nEscolha uma opção: ")
            if escolha in ["1", "2", "3", "4", "5"]:
                break
            else:
                print("Por favor, insira uma opção válida!")

        if escolha == "1":
            print("\nVEÍCULOS:\n1. Carro\n2. Caminhão\n")
            veiculo = int(input("Qual veículo você deseja registrar? "))

            if veiculo == 1:
                carro.registrar()
            elif veiculo == 2:
                caminhao.registrar()
            else:
                print("Opção inválida.")

        elif escolha == "2":
            print("\nVEÍCULOS:\n1. Carro\n2. Caminhão\n")
            veiculo = int(input("Qual veículo você deseja consultar? "))

            if veiculo == 1:
                carro.consultar_veiculo()
            elif veiculo == 2:
                caminhao.consultar_veiculo()
            else:
                print("Opção inválida.")    

        elif escolha == "3":
            print("\nVEÍCULOS:\n1. Carro\n2. Caminhão\n")
            veiculo = int(input("Qual veículo você deseja agendar manutenção? "))

            if veiculo == 1:
                carro.agendar_manutencao()
            elif veiculo == 2:
                caminhao.agendar_manutencao()
            else:
                print("Opção inválida.")    

        elif escolha == "4":
            print("\nVEÍCULOS:\n1. Carro\n2. Caminhão\n")
            veiculo = int(input("Qual veículo você deseja consultar manutenções? "))

            if veiculo == 1:
                carro.consultar_manutencoes()
            elif veiculo == 2:
                caminhao.consultar_manutencoes()
            else:
                print("Opção inválida.")    

        else:
            print("Saindo...")
            break

main()
