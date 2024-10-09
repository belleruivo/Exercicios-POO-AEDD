'''
Escreva uma classe chamada Bicycle que possua campos para a velocidade,
cadência dos pedais (número de rotações dos pedais por minuto), marcha atual e
número de série. A velocidade e a cadência dos pedais não podem ser menores que
zero, a marcha atual deve estar entre 1 e 18 e o número de série deve ser maior que
1000. Crie constantes simbólicas e métodos de acesso e impressão que reflitam
esses limites. Teste a classe implementada e seus métodos. A seguir, crie um método
que calcule a velocidade relativa entre a bicicleta e outra dada como parâmetro. Teste
o seu novo método.
'''

from abc import ABC, abstractmethod

# Classe base para validação de bicicletas
class BicycleValidator(ABC):
    @abstractmethod
    def validate_speed(self, speed):
        pass

    @abstractmethod
    def validate_cadence(self, cadence):
        pass

    @abstractmethod
    def validate_gear(self, gear):
        pass

    @abstractmethod
    def validate_serial_number(self, serial_number):
        pass

# Validação padrão para bicicletas
class DefaultBicycleValidator(BicycleValidator):
    MIN_SPEED = 0
    MIN_CADENCE = 0
    MIN_GEAR = 1
    MAX_GEAR = 18
    MIN_SERIAL_NUMBER = 1001

    def validate_speed(self, speed):
        if speed < DefaultBicycleValidator.MIN_SPEED:
            raise ValueError("A velocidade não pode ser menor que zero.")
    
    def validate_cadence(self, cadence):
        if cadence < DefaultBicycleValidator.MIN_CADENCE:
            raise ValueError("A cadência não pode ser menor que zero.")

    def validate_gear(self, gear):
        if gear < DefaultBicycleValidator.MIN_GEAR or gear > DefaultBicycleValidator.MAX_GEAR:
            raise ValueError("A marcha deve estar entre 1 e 18.")
    
    def validate_serial_number(self, serial_number):
        if serial_number < DefaultBicycleValidator.MIN_SERIAL_NUMBER:
            raise ValueError("O número de série deve ser maior que 1000.")

# Classe Bicycle agora está aberta para validação extensível
class Bicycle:
    def __init__(self, speed=0, cadence=0, gear=1, serial_number=1001, validator=None):
        self.validator = validator if validator else DefaultBicycleValidator()
        self.set_speed(speed)
        self.set_cadence(cadence)
        self.set_gear(gear)
        self.set_serial_number(serial_number)

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self.validator.validate_speed(speed)
        self._speed = speed

    def get_cadence(self):
        return self._cadence

    def set_cadence(self, cadence):
        self.validator.validate_cadence(cadence)
        self._cadence = cadence

    def get_gear(self):
        return self._gear

    def set_gear(self, gear):
        self.validator.validate_gear(gear)
        self._gear = gear

    def get_serial_number(self):
        return self._serial_number

    def set_serial_number(self, serial_number):
        self.validator.validate_serial_number(serial_number)
        self._serial_number = serial_number

    def print_status(self):
        print(f"Velocidade: {self.get_speed()} km/h")
        print(f"Cadência: {self.get_cadence()} rpm")
        print(f"Marcha atual: {self.get_gear()}")
        print(f"Número de série: {self.get_serial_number()}")

    def relative_speed(self, other_bike):
        if isinstance(other_bike, Bicycle):
            return abs(self.get_speed() - other_bike.get_speed())
        else:
            raise TypeError("O parâmetro deve ser uma instância de Bicycle.")

# Exemplo de uma nova validação que estende as regras
class MountainBikeValidator(DefaultBicycleValidator):
    MIN_GEAR = 1
    MAX_GEAR = 21  

def main():
    bikes = []

    while True:
        print("\nMenu:")
        print("1. Adicionar nova bicicleta")
        print("2. Mostrar informações de bicicletas")
        print("3. Calcular velocidade relativa entre duas bicicletas")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            try:
                speed = float(input("Insira a velocidade (km/h): "))
                cadence = float(input("Insira a cadência (rpm): "))
                gear = int(input("Insira a marcha (1-18): "))
                serial_number = int(input("Insira o número de série (maior que 1000): "))
                
                bike = Bicycle(speed, cadence, gear, serial_number)
                bikes.append(bike)
                print("Bicicleta adicionada com sucesso!")

            except ValueError as ve:
                print(f"Erro: {ve}")
            except Exception as e:
                print(f"Erro: {e}")

        elif choice == "2":
            if not bikes:
                print("Nenhuma bicicleta cadastrada.")
            else:
                for i, bike in enumerate(bikes):
                    print(f"\nBicicleta {i+1}:")
                    bike.print_status()

        elif choice == "3":
            if len(bikes) < 2:
                print("É necessário ter pelo menos duas bicicletas cadastradas para calcular a velocidade relativa.")
            else:
                for i, bike in enumerate(bikes):
                    print(f"Bicicleta {i+1}:")
                    bike.print_status()
                
                bike1_index = int(input("Escolha a primeira bicicleta (1 ou 2): ")) - 1
                bike2_index = int(input("Escolha a segunda bicicleta (1 ou 2): ")) - 1
                
                if bike1_index < 0 or bike1_index >= len(bikes) or bike2_index < 0 or bike2_index >= len(bikes):
                    print("Índice inválido.")
                else:
                    relative_speed = bikes[bike1_index].relative_speed(bikes[bike2_index])
                    print(f"Velocidade relativa entre bicicleta {bike1_index+1} e bicicleta {bike2_index+1}: {relative_speed} km/h")

        elif choice == "4":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()