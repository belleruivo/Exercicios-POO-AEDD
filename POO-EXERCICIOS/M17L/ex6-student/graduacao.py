from student import Student
from lider_interface import LiderInterface
from clube_interface import ClubeInterface

class Graduacao(Student):
    
    def __init__(self, nome, idade, curso, clube):
        super().__init__(nome, idade, curso)
        self.clube = clube
        self.lider = True

    def get_student_type(self):
        return "Graduação"
    
    def is_lider(self):
        return self.lider
    
    def get_clube(self):
        return self.clube

# Registro da subclasse virtual
LiderInterface.register(Graduacao)
ClubeInterface.register(Graduacao)
