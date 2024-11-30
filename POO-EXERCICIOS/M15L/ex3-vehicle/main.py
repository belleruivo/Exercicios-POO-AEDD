from veiculos import Car, Airplane

def main():
    car = Car()
    airplane = Airplane()

    car.start_engine()
    car.move()
    car.get_location()

    print()
    airplane.start_engine()
    airplane.move()
    airplane.get_location()
    airplane.get_altitude()

main()