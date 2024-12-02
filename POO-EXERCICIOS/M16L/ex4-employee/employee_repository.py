from abc import ABC, abstractmethod
from employee import Employee
from typing import List

# tanto baixo e alto nível dependem da abstração
class EmployeeRepository(ABC):
    @abstractmethod
    def add_employee(self, employee: Employee): # devem ser implementados por uma classe concreta
        pass

    @abstractmethod
    def list_employees(self) -> List[Employee]:
        pass