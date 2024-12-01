from abc import ABC, abstractmethod

class Student(ABC):
    
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    @abstractmethod
    def get_student_type(self):
        pass
