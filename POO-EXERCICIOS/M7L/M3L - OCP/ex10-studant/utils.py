import random

class StudentManager:
    def __init__(self, students):
        self.students = students

    def shuffle_students(self):
        """Embaralha a lista de estudantes."""
        random.shuffle(self.students)
        print("\nLista embaralhada:")
        self.print_students()

    def sort_students(self):
        """Ordena a lista de estudantes."""
        self.students.sort()
        print("\nLista ordenada:")
        self.print_students()

    def print_students(self):
        """Imprime as informações dos estudantes."""
        for student in self.students:
            student.print_info()

    def shuffle_and_sort_students(self):
        """Função que embaralha e ordena a lista de estudantes, imprimindo os resultados."""
        self.shuffle_students()
        self.sort_students()

# Exemplo de uso:
# students = [Student("Ana", 85), Student("Bruno", 90), Student("Carlos", 75)]
# manager = StudentManager(students)
# manager.shuffle_and_sort_students()
