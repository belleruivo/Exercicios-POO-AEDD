from student import Student

class Graduacao(Student):
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def get_student_type(self):
        return "Graduação"
