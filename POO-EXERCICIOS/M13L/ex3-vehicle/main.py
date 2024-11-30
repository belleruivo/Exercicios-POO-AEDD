'''
Implemente um sistema de Concessionária com os tipos de veículos (automóvel,
moto, caminhão, etc.), evidenciando a classe Vehicle como uma classe abstrata.
'''
from vehicles import Car, Boat

def main():
    car = Car()
    boat = Boat()

    car.start_engine()
    car.move()
    
    print()
    boat.start_engine()
    boat.move()

main()