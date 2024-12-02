from employee_repository import EmployeeRepository
from employee import Employee
from typing import List

# essa implementação concreta depende da abstração EmployeeRepository.
class InMemoryEmployeeRepository(EmployeeRepository): # !
    def __init__(self):
        self.employees = [] 

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def list_employees(self) -> List[Employee]:
        return self.employees