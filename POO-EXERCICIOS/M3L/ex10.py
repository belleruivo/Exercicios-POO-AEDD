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

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # Método para testar igualdade de nomes
    def __eq__(self, other):
        return self.name == other.name

    # Método para testar se um nome é menor que o outro
    def __lt__(self, other):
        return self.name < other.name

    # Método para testar se um nome é maior ou igual ao outro
    def __ge__(self, other):
        return self.name >= other.name

    # Método para exibir as informações do estudante
    def print_info(self):
        print(f"Nome: {self.name}, Nota: {self.grade}")


# Função para testar os operadores de comparação
def test_comparisons(student1, student2):
    print(f"Comparando {student1.name} com {student2.name}:")
    if student1 == student2:
        print("Os nomes são iguais.")
    else:
        print("Os nomes são diferentes.")
    
    if student1 < student2:
        print(f"{student1.name} vem antes de {student2.name}.")
    else:
        print(f"{student1.name} não vem antes de {student2.name}.")
    
    if student1 >= student2:
        print(f"{student1.name} vem depois ou é igual a {student2.name}.")
    else:
        print(f"{student1.name} não vem depois de {student2.name}.")


# Função para embaralhar e ordenar a lista de estudantes
def shuffle_and_sort_students(students):
    # Embaralhando a lista de estudantes
    random.shuffle(students)
    print("\nLista embaralhada:")
    for student in students:
        student.print_info()

    # Ordenando a lista de estudantes
    students.sort()
    print("\nLista ordenada:")
    for student in students:
        student.print_info()


def main():
    # Criando alguns objetos Student
    student1 = Student("Ana", 85)
    student2 = Student("Bruno", 90)
    student3 = Student("Carlos", 75)

    # Testando as comparações
    test_comparisons(student1, student2)
    test_comparisons(student2, student3)
    test_comparisons(student1, student3)

    # Criando uma lista de estudantes
    students = [student1, student2, student3]

    # Embaralhando e ordenando a lista de estudantes
    shuffle_and_sort_students(students)


main()
