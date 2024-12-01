from student import Student
from lider_interface import LiderInterface
from clube_interface import ClubeInterface

class Graduacao(Student, LiderInterface, ClubeInterface):
    
    def __init__(self, nome, idade, clube):
        super().__init__(nome, idade)
        self.clube = clube
        self.lider = True

    def get_student_type(self):
        return "Graduação"
    
    def is_lider(self):
        return self.lider
    
    def get_clube(self):
        return self.clube
