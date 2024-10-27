from student import Student
from utils import StudentManager  # Importando a nova classe

def get_grade():
    while True:
        try:
            grade = float(input("Digite a nota do estudante (1 a 10): "))
            if 1 <= grade <= 10:
                return grade
            print("A nota deve estar entre 1 e 10. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def main():
    students = []
    number_of_students = int(input("Quantos estudantes você deseja adicionar? "))

    # Adicionando estudantes
    for _ in range(number_of_students):
        name = input("Digite o nome do estudante: ")
        grade = get_grade()
        students.append(Student(name, grade))

    # Testando comparações
    print("\nResultados das comparações:")
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            print(f"\nComparando {students[i].name} com {students[j].name}:")
            comparison_result = students[i].compare(students[j])
            print(comparison_result)

    # Criando uma instância de StudentManager e usando seus métodos
    manager = StudentManager(students)
    manager.shuffle_and_sort_students()

if __name__ == "__main__":
    main()
