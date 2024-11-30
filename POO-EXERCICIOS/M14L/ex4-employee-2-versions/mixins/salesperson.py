from employee import Employee
from mixins import CommunicationSkillsMixin

class Salesperson(Employee, CommunicationSkillsMixin):
    def __init__(self, name: str, salary: float, region: str):
        super().__init__(name, salary)
        self.region = region

    def get_job_description(self):
        return f"Vendedor responsável pela região {self.region}."

    def __str__(self):
        return f"{super().__str__()} (Vendedor - {self.region})"
