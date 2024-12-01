from student import Student

class Mestrado(Student):
    
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade, curso)

    def get_student_type(self):
        return "Mestrado"
