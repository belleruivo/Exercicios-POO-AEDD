from employee import Employee
from address import Address

class Salesperson(Employee):
    def __init__(self, name: str, salary: float, address: Address, region: str):
        super().__init__(name, salary, address)
        self.region = region

    def get_job_description(self):
        return f"Salesperson responsible for the {self.region} region."

    def __str__(self):
        return f"{super().__str__()} (Salesperson - {self.region})"