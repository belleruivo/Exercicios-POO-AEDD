from abc import ABC, abstractmethod
from employee import Employee
from typing import List

class EmployeeRepository(ABC):
    @abstractmethod
    def add_employee(self, employee: Employee):
        pass

    @abstractmethod
    def list_employees(self) -> List[Employee]:
        pass