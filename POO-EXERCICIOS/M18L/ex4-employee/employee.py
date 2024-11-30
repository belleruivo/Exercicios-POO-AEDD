from abc import ABC, abstractmethod
from address import Address

class Employee(ABC):
    def __init__(self, name: str, salary: float, address: Address):
        self.name = name
        self.salary = salary
        self.address = address

    @abstractmethod 
    def get_job_description(self):
        pass

    def __str__(self):
        return f"{self.name}, Salary: {self.salary}, Address: {self.address}"