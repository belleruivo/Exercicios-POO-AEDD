class ImprimirVehicle:
    # Classe para exibição, permitindo diferentes estilos de saída
    @staticmethod
    def imprimir_detalhes(vehicle):
        print("\nDETALHES DO VEÍCULO:")
        print(vehicle.exibir_detalhes())
        print("-="*40)
