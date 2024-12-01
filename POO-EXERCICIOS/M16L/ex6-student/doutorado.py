from student import Student

class Doutorado(Student):
    
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def get_student_type(self):
        return "Doutorado"
