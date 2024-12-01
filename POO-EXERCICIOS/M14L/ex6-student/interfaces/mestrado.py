from student import Student

class Mestrado(Student):
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def get_student_type(self):
        return "Mestrado"
