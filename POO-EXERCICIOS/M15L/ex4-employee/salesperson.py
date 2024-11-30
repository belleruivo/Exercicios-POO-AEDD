from employee import Employee
from ilogistics_handler import ILogisticsHandler

class Salesperson(Employee):
    def __init__(self, name: str, salary: float, region: str):
        super().__init__(name, salary)
        self.region = region

    def get_job_description(self):
        return f"Vendedor responsável pela região {self.region}."

    def handle_logistics(self):
        return f"{self.name} está gerenciando a logística da região {self.region}."

    def __str__(self):
        return f"{super().__str__()} (Vendedor - Região: {self.region})"

# Registro como subclasse virtual
ILogisticsHandler.register(Salesperson)
