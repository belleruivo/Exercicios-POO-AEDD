from abc import ABC, abstractmethod

class Student(ABC):
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @abstractmethod
    def get_student_type(self):
        pass
