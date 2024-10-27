from bicycle import Bicycle

class ElectricBicycle(Bicycle):
    def __init__(self, speed=0, cadence=0, gear=1, serial_number=1001, battery_level=100):
        super().__init__(speed, cadence, gear, serial_number)
        self.set_battery_level(battery_level)

    def get_battery_level(self):
        return self._battery_level

    def set_battery_level(self, battery_level):
        if 0 <= battery_level <= 100:
            self._battery_level = battery_level
        else:
            raise ValueError("O nível da bateria deve estar entre 0 e 100.")

    def print_status(self):
        super().print_status()
        print(f"Nível da bateria: {self.get_battery_level()}%")
