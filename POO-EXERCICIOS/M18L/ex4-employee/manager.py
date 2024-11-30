from employee import Employee
from address import Address

class Manager(Employee):
    def __init__(self, name: str, salary: float, address: Address, department: str):
        super().__init__(name, salary, address)
        self.department = department

    def get_job_description(self):
        return f"Manager of {self.department} department."

    def __str__(self):
        return f"{super().__str__()} (Manager - {self.department})"