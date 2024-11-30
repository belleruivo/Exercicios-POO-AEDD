from employee import Employee
from itrainable import ITrainable

class Manager(Employee, ITrainable):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department

    def get_job_description(self):
        return f"Gerente do departamento {self.department}."

    # Implementação do método abstrato da interface ITrainable
    def conduct_training(self):
        return f"{self.name} está conduzindo um treinamento no departamento {self.department}."

    def __str__(self):
        return f"{super().__str__()} (Gerente - {self.department})"
