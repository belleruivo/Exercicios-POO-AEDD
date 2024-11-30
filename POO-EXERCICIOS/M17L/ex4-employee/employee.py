from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    @abstractmethod 
    def get_job_description(self):
        pass

    '''Essa implementação garante que Employee funcione como um contrato para todas as subclasses (como Manager, Salesperson, etc.), que são obrigadas a implementar o método abstrato.'''
    '''No nosso caso, a classe Employee tem o método abstrato get_job_description. Isso significa que qualquer classe filha (como Manager, Salesperson, etc.) deve implementar esse método. Se não o fizer, o Python levantará um erro.'''
    def __str__(self):
        return f"{self.name}, Salary: {self.salary}"
