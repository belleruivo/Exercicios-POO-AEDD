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

class Bicycle:
    # Constantes simbólicas
    MIN_SPEED = 0
    MIN_CADENCE = 0
    MIN_GEAR = 1
    MAX_GEAR = 18
    MIN_SERIAL_NUMBER = 1001

    def __init__(self, speed=0, cadence=0, gear=1, serial_number=1001):
        self.set_speed(speed)
        self.set_cadence(cadence)
        self.set_gear(gear)
        self.set_serial_number(serial_number)

    # Métodos de acesso (getters e setters) para a velocidade
    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        if speed >= Bicycle.MIN_SPEED:
            self._speed = speed
        else:
            raise ValueError("A velocidade não pode ser menor que zero.")

    # Métodos de acesso (getters e setters) para a cadência
    def get_cadence(self):
        return self._cadence

    def set_cadence(self, cadence):
        if cadence >= Bicycle.MIN_CADENCE:
            self._cadence = cadence
        else:
            raise ValueError("A cadência não pode ser menor que zero.")

    # Métodos de acesso (getters e setters) para a marcha
    def get_gear(self):
        return self._gear

    def set_gear(self, gear):
        if Bicycle.MIN_GEAR <= gear <= Bicycle.MAX_GEAR:
            self._gear = gear
        else:
            raise ValueError("A marcha deve estar entre 1 e 18.")

    # Métodos de acesso (getters e setters) para o número de série
    def get_serial_number(self):
        return self._serial_number

    def set_serial_number(self, serial_number):
        if serial_number >= Bicycle.MIN_SERIAL_NUMBER:
            self._serial_number = serial_number
        else:
            raise ValueError("O número de série deve ser maior que 1000.")

    # Método de impressão para exibir o estado atual da bicicleta
    def print_status(self):
        print(f"Velocidade: {self.get_speed()} km/h")
        print(f"Cadência: {self.get_cadence()} rpm")
        print(f"Marcha atual: {self.get_gear()}")
        print(f"Número de série: {self.get_serial_number()}")

    # Método para calcular a velocidade relativa entre duas bicicletas
    def relative_speed(self, other_bike):
        if isinstance(other_bike, Bicycle):
            return abs(self.get_speed() - other_bike.get_speed())
        else:
            raise TypeError("O parâmetro deve ser uma instância de Bicycle.")

# Testando a classe Bicycle e seus métodos
if __name__ == "__main__":
    bike1 = Bicycle(speed=15, cadence=80, gear=5, serial_number=1200)
    bike2 = Bicycle(speed=20, cadence=90, gear=6, serial_number=1500)

    # Imprimindo o status das bicicletas
    print("Bike 1")
    bike1.print_status()
    print("Bike 2")
    bike2.print_status()

    # Calculando e exibindo a velocidade relativa entre as duas bicicletas
    print(f"Velocidade relativa entre bike1 e bike2: {bike1.relative_speed(bike2)} km/h")
