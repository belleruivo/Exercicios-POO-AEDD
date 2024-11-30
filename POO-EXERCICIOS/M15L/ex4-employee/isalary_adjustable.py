from abc import ABC, abstractmethod

class ISalaryAdjustable(ABC):
    @abstractmethod
    def adjust_salary(self, amount: float):
        """Ajusta o salário do funcionário."""
        pass
