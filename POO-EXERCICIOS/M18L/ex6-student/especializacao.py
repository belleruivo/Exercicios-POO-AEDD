from student import Student
from perfil_academico import PerfilAcademico

class Especializacao(Student):
    
    def __init__(self, nome, idade, curso):
        perfil = PerfilAcademico("Especialização")
        super().__init__(nome, idade, curso, perfil)

    def obter_papeis(self):
        return {}
