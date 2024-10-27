class Bicycle:
    # Constantes simbólicas (limites válidos)
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

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        if speed >= Bicycle.MIN_SPEED:
            self._speed = speed
        else:
            raise ValueError("A velocidade não pode ser menor que zero.")

    def get_cadence(self):
        return self._cadence

    def set_cadence(self, cadence):
        if cadence >= Bicycle.MIN_CADENCE:
            self._cadence = cadence
        else:
            raise ValueError("A cadência não pode ser menor que zero.")

    def get_gear(self):
        return self._gear

    def set_gear(self, gear):
        if Bicycle.MIN_GEAR <= gear <= Bicycle.MAX_GEAR:
            self._gear = gear
        else:
            raise ValueError("A marcha deve estar entre 1 e 18.")

    def get_serial_number(self):
        return self._serial_number

    def set_serial_number(self, serial_number):
        if serial_number >= Bicycle.MIN_SERIAL_NUMBER:
            self._serial_number = serial_number
        else:
            raise ValueError("O número de série deve ser maior que 1000.")

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
