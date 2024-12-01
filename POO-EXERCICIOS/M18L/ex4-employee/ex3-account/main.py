from veiculos import Car, Boat

def main():
    car = Car()
    boat = Boat()

    car.start_engine()
    car.move()
    
    print()
    boat.start_engine()
    boat.move()

main()

