'''
Implemente um sistema de Concessionária com os tipos de veículos (automóvel,
moto, caminhão, etc.), evidenciando a classe Vehicle como uma classe abstrata.
'''
from vehicles import Car, Motorcycle, Truck

def main():
        car = Car()
        motorcycle = Motorcycle()
        truck = Truck()
        while True:
            try:
                print("\n--- Menu ---")
                print("1. Register Vehicle")
                print("2. Consult Vehicle")
                print("3. Exit")

                choice = int(input("Choose one option: "))

                if choice == 1:
                    print("VEHICLES:\n1. Car\n2. Motorcycle\n3. Truck")
                    vehicle = int(input("What vehicle do you want register? "))
                    
                    if vehicle == 1:
                        car.register()
                    if vehicle == 2:
                        motorcycle.register()
                    if vehicle == 3:
                        truck.register()

                elif choice == 2:
                    print("VEHICLES:\n1. Car\n2. Motorcycle\n3. Truck")
                    vehicle = int(input("What vehicle do you want consult? "))
                    
                    if vehicle == 1:
                        car.consult_vehicle()
                    if vehicle == 2:
                        motorcycle.consult_vehicle()
                    if vehicle == 3:
                        truck.consult_vehicle()
                
                elif choice == 3:
                    print("Exiting...")
                    break
                
                else:
                    print("Wrong value. Try again.")
            except ValueError:
                print("Please, enter a valid option.")

if __name__ == "__main__":
    main()
