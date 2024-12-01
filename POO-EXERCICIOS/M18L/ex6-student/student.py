from abc import ABC, abstractmethod
from curso import Curso
from perfil_academico import PerfilAcademico

class Student(ABC):
    
    def __init__(self, nome, idade, curso: Curso, perfil: PerfilAcademico):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.perfil = perfil
    
    def get_student_type(self):
        return self.perfil.get_tipo()
    
    @abstractmethod
    def obter_papeis(self):
        pass
