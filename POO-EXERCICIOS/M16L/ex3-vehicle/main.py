from vehicle import Car, Boat, VehicleController

def main():
    # Podemos passar qualquer implementação de Vehicle para VehicleController
    car = Car()
    boat = Boat()

    car_controller = VehicleController(car)
    boat_controller = VehicleController(boat)

    print("Controlando o Carro:")
    car_controller.start_and_move()
    
    print("\nControlando o Barco:")
    boat_controller.start_and_move()

main()
