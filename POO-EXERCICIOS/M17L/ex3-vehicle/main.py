from vehicle import *

def main():
    name = input("Digite o nome do motorista: ")
    driver = Driver(name)

    carro = Carro()
    barco = Barco()

    driver.add_vehicle(carro)
    driver.add_vehicle(barco)

    driver.list_vehicles()

    while True:
        try:
            vehicle_index = int(input("\nDigite o número do veículo que o motorista irá dirigir: ")) - 1
            if 0 <= vehicle_index < len(driver.vehicles):
                driver.drive_vehicle(vehicle_index)
                break  
            else:
                print("Índice de veículo inválido. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")
    print()

main()





