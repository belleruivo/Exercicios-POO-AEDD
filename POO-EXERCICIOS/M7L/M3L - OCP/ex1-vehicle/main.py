''' 1. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em
km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de
acesso e impressão para esta classe e faça um programa de teste.
'''

from coletar import VehicleColetarDados
from vehicleDetalhado import VehicleDetalhado

def main():
    carro = VehicleColetarDados.coletar_dados()
    print("\nDETALHES DO VEÍCULO:")
    print(carro.exibir_detalhes())
    print("-="*40)

main()