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

# Classe para controlar a velocidade
class SpeedController:
    MIN_SPEED = 0

    def __init__(self, speed=0):
        self.set_speed(speed)

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        if speed >= SpeedController.MIN_SPEED:
            self._speed = speed
        else:
            raise ValueError("A velocidade não pode ser menor que zero.")

# Classe para controlar a cadência
class CadenceController:
    MIN_CADENCE = 0

    def __init__(self, cadence=0):
        self.set_cadence(cadence)

    def get_cadence(self):
        return self._cadence

    def set_cadence(self, cadence):
        if cadence >= CadenceController.MIN_CADENCE:
            self._cadence = cadence
        else:
            raise ValueError("A cadência não pode ser menor que zero.")

# Classe para controlar as marchas
class GearController:
    MIN_GEAR = 1
    MAX_GEAR = 18

    def __init__(self, gear=1):
        self.set_gear(gear)

    def get_gear(self):
        return self._gear

    def set_gear(self, gear):
        if GearController.MIN_GEAR <= gear <= GearController.MAX_GEAR:
            self._gear = gear
        else:
            raise ValueError("A marcha deve estar entre 1 e 18.")

# Classe para controlar o número de série
class SerialNumberController:
    MIN_SERIAL_NUMBER = 1001

    def __init__(self, serial_number=1001):
        self.set_serial_number(serial_number)

    def get_serial_number(self):
        return self._serial_number

    def set_serial_number(self, serial_number):
        if serial_number >= SerialNumberController.MIN_SERIAL_NUMBER:
            self._serial_number = serial_number
        else:
            raise ValueError("O número de série deve ser maior que 1000.")

# Classe Bicycle que usa as outras classes para manter a responsabilidade única
class Bicycle:
    def __init__(self, speed=0, cadence=0, gear=1, serial_number=1001):
        self.speed_controller = SpeedController(speed)
        self.cadence_controller = CadenceController(cadence)
        self.gear_controller = GearController(gear)
        self.serial_number_controller = SerialNumberController(serial_number)

    def print_status(self):
        print(f"Velocidade: {self.speed_controller.get_speed()} km/h")
        print(f"Cadência: {self.cadence_controller.get_cadence()} rpm")
        print(f"Marcha atual: {self.gear_controller.get_gear()}")
        print(f"Número de série: {self.serial_number_controller.get_serial_number()}")

    # Método para calcular a velocidade relativa entre duas bicicletas
    def relative_speed(self, other_bike):
        return self.speed_controller.get_speed() - other_bike.speed_controller.get_speed()

# Testando a classe Bicycle e suas classes relacionadas
if __name__ == "__main__":
    bike1 = Bicycle(speed=15, cadence=80, gear=5, serial_number=1200)
    bike2 = Bicycle(speed=20, cadence=90, gear=6, serial_number=1500)

    bike1.print_status()
    bike2.print_status()

    # Calculando e exibindo a velocidade relativa entre as duas bicicletas
    print(f"Velocidade relativa entre bike1 e bike2: {bike1.relative_speed(bike2)} km/h")
