from coletar import VehicleColetarDados
from imprimirVehicle import ImprimirVehicle

def main():
    carro = VehicleColetarDados.coletar_dados()
    ImprimirVehicle.imprimir_detalhes(carro)

main()