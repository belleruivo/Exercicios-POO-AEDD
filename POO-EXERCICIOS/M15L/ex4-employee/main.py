# O Princípio de Segregação de Interface diz que "nenhuma classe deve ser forçada a implementar interfaces que não usa".
# Ou seja, em vez de ter uma única interface genérica com muitos métodos, o ideal é criar várias interfaces menores e mais específicas, para que as classes implementem apenas o que realmente precisam.
# A interface ITrainable para aqueles que podem conduzir treinamentos.
# A interface IDepartmentAssignable para aqueles que podem ser atribuídos a um departamento.
# Isso é um exemplo de segregação de interfaces: dividimos as responsabilidades em interfaces mais específicas, para que, por exemplo, um gerente (que conduz treinamento e é responsável por um departamento) implemente as duas interfaces, enquanto um vendedor (que não conduz treinamento, mas pode ser atribuído a uma área) implementaria apenas a interface relacionada ao departamento.
from manager import Manager
from salesperson import Salesperson
from itrainable import ITrainable
from ilogistics_handler import ILogisticsHandler
from isalary_adjustable import ISalaryAdjustable
from idepartment_assignable import IDepartmentAssignable

def main():
    employees = []

    while True:
        print("\nMenu:")
        print("1. Adicionar Gerente")
        print("2. Adicionar Vendedor")
        print("3. Listar Funcionários")
        print("4. Executar Tarefas Adicionais")
        print("5. Atribuir Departamento")
        print("6. Ajustar Salário de um Gerente")
        print("7. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Nome do Gerente: ")
            salary = float(input("Salário: "))
            department = input("Departamento: ")
            manager = Manager(name, salary, department)
            employees.append(manager)
            print("Gerente adicionado com sucesso!")
        elif choice == "2":
            name = input("Nome do Vendedor: ")
            salary = float(input("Salário: "))
            region = input("Região: ")
            salesperson = Salesperson(name, salary, region)
            employees.append(salesperson)
            print("Vendedor adicionado com sucesso!")
        elif choice == "3":
            print("\nLista de Funcionários:")
            for i, employee in enumerate(employees, 1):
                print(f"{i}. {employee}")
        elif choice == "4":
            print("\nExecutando Tarefas Adicionais:")
            for employee in employees:
                if isinstance(employee, ITrainable):
                    print(employee.conduct_training())
                if isinstance(employee, ILogisticsHandler):
                    print(employee.handle_logistics())
        elif choice == "5":
            name = input("Nome do Gerente para Atribuição de Departamento: ")
            department = input("Nome do Departamento: ")
            for employee in employees:
                if isinstance(employee, IDepartmentAssignable) and employee.name == name:
                    print(employee.assign_department(department))
                    break
            else:
                print("Funcionário não encontrado ou não pode ser atribuído a um departamento.")
        elif choice == "6":
            name = input("Nome do Gerente para Ajuste de Salário: ")
            percentage = float(input("Percentual de aumento: "))
            for employee in employees:
                if isinstance(employee, ISalaryAdjustable) and employee.name == name:
                    print(employee.adjust_salary(percentage))
                    break
            else:
                print("Funcionário não encontrado ou não pode ter o salário ajustado.")
        elif choice == "7":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
