from abc import ABC, abstractmethod

class IDepartmentAssignable(ABC):
    @abstractmethod
    def assign_department(self, department: str):
        """Atribui o funcionário a um departamento."""
        pass
