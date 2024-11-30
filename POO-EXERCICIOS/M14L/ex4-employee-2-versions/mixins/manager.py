from employee import Employee
from mixins import PerformanceEvaluatorMixin

class Manager(Employee, PerformanceEvaluatorMixin): #heranca
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department

    def get_job_description(self):
        return f"Gerente do departamento {self.department}."

    def __str__(self):
        return f"{super().__str__()} (Gerente - {self.department})"
