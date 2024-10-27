from bicycle import Bicycle
from electric_bicycle import ElectricBicycle

def exibir_menu():
    print("\n--- Sistema de Gerenciamento de Bicicletas ---")
    print("1. Adicionar Bicicleta")
    print("2. Adicionar Bicicleta Elétrica")
    print("3. Exibir Todas as Bicicletas")
    print("4. Calcular Velocidade Relativa")
    print("5. Sair")

def main():
    bicicletas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            speed = int(input("Digite a velocidade da bicicleta (km/h): "))
            cadence = int(input("Digite a cadência (rpm): "))
            gear = int(input("Digite a marcha (1 a 18): "))
            serial_number = int(input("Digite o número de série (maior que 1000): "))
            try:
                bike = Bicycle(speed=speed, cadence=cadence, gear=gear, serial_number=serial_number)
                bicicletas.append(bike)
                print("Bicicleta adicionada com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == '2':
            speed = int(input("Digite a velocidade da bicicleta elétrica (km/h): "))
            cadence = int(input("Digite a cadência (rpm): "))
            gear = int(input("Digite a marcha (1 a 18): "))
            serial_number = int(input("Digite o número de série (maior que 1000): "))
            battery_level = int(input("Digite o nível da bateria (0 a 100): "))
            try:
                e_bike = ElectricBicycle(speed=speed, cadence=cadence, gear=gear, serial_number=serial_number, battery_level=battery_level)
                bicicletas.append(e_bike)
                print("Bicicleta elétrica adicionada com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == '3':
            if not bicicletas:
                print("Nenhuma bicicleta cadastrada.")
            else:
                for i, bike in enumerate(bicicletas, start=1):
                    print(f"\nBicicleta {i}:")
                    bike.print_status()

        elif opcao == '4':
            if len(bicicletas) < 2:
                print("Adicione pelo menos duas bicicletas para calcular a velocidade relativa.")
            else:
                print("Escolha as bicicletas para calcular a velocidade relativa:")
                for i, bike in enumerate(bicicletas, start=1):
                    print(f"{i}. Bicicleta {i}")
                index1 = int(input("Selecione a primeira bicicleta (número): ")) - 1
                index2 = int(input("Selecione a segunda bicicleta (número): ")) - 1

                try:
                    relative_speed = bicicletas[index1].relative_speed(bicicletas[index2])
                    print(f"Velocidade relativa entre a Bicicleta {index1 + 1} e a Bicicleta {index2 + 1}: {relative_speed} km/h")
                except TypeError as e:
                    print(f"Erro: {e}")

        elif opcao == '5':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
