'''
Adicione três métodos à classe Student estudada em sala que compara dois objetos
Student. Um método deve testar a igualdade. Um segundo método deve testar para
menor que. O terceiro método deve testar para maior que ou igual a. Em cada caso, o
método retorna o resultado da comparação dos nomes dos dois alunos. Inclua uma
função main que testa todos os operadores de comparação. Em seguida, coloque
vários objetos Student em uma lista e embaralhe. Em seguida, execute o método sort
com esta lista e exiba todas as informações dos alunos.
'''

import random

# Classe que representa um estudante
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def print_info(self):
        print(f"Nome: {self.name}, Nota: {self.grade}")


# Classe para comparar dois objetos Student
class StudentComparator:
    def are_equal(self, student1, student2):
        return student1.name == student2.name

    def is_less_than(self, student1, student2):
        return student1.name < student2.name

    def is_greater_or_equal(self, student1, student2):
        return student1.name >= student2.name


# Classe responsável pela manipulação de listas de estudantes (embaralhar e ordenar)
class StudentListManager:
    def shuffle_students(self, students):
        random.shuffle(students)
        print("\nLista embaralhada:")
        for student in students:
            student.print_info()

    def sort_students(self, students):
        students.sort(key=lambda student: student.name)
        print("\nLista ordenada:")
        for student in students:
            student.print_info()


# Função para testar as comparações
def test_comparisons(student1, student2, comparator):
    print(f"Comparando {student1.name} com {student2.name}:")
    
    if comparator.are_equal(student1, student2):
        print("Os nomes são iguais.")
    else:
        print("Os nomes são diferentes.")
    
    if comparator.is_less_than(student1, student2):
        print(f"{student1.name} vem antes de {student2.name}.")
    else:
        print(f"{student1.name} não vem antes de {student2.name}.")
    
    if comparator.is_greater_or_equal(student1, student2):
        print(f"{student1.name} vem depois ou é igual a {student2.name}.")
    else:
        print(f"{student1.name} não vem depois de {student2.name}.")


# Função principal para testar
def main():
    # Criando alguns objetos Student
    student1 = Student("Ana", 85)
    student2 = Student("Bruno", 90)
    student3 = Student("Carlos", 75)

    # Criando o objeto de comparação
    comparator = StudentComparator()

    # Testando as comparações
    test_comparisons(student1, student2, comparator)
    test_comparisons(student2, student3, comparator)
    test_comparisons(student1, student3, comparator)

    # Criando uma lista de estudantes
    students = [student1, student2, student3]

    # Criando o gerenciador de lista de estudantes
    list_manager = StudentListManager()

    # Embaralhando e ordenando a lista de estudantes
    list_manager.shuffle_students(students)
    list_manager.sort_students(students)


main()
