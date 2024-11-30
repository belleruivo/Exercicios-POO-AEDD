from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    @abstractmethod
    def get_job_description(self):
        """Descreve o trabalho do funcionário."""
        pass

    def __str__(self):
        return f"{self.name}, Salário: R${self.salary:.2f}"
