from student import Student
from lider_mixin import LiderMixin
from clube_mixin import ClubeMixin

class Graduacao(Student, LiderMixin, ClubeMixin):
    
    def __init__(self, nome, idade, clube):
        Student.__init__(self, nome, idade)
        ClubeMixin.__init__(self, clube)
        LiderMixin.__init__(self)

    def get_student_type(self):
        return "Graduação"
