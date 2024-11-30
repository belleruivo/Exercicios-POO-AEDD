from manager import Manager
from salesperson import Salesperson
from receptionist import Receptionist
from secretary import Secretary

'''Definição dos Mixins:

PerformanceEvaluatorMixin e CommunicationSkillsMixin foram definidos no arquivo mixins.py.
Herança dos Mixins:

A classe Manager herda de PerformanceEvaluatorMixin, adicionando o método evaluate_performance.
A classe Salesperson herda de CommunicationSkillsMixin, adicionando o método communicate_effectively.
Utilização dos Mixins:

No arquivo main.py, ao exibir os detalhes de um funcionário, o código verifica se o objeto possui os métodos dos mixins (evaluate_performance e communicate_effectively) e os chama se existirem.'''

def create_manager():
    name = input("Nome do gerente: ")
    salary = float(input("Salário do gerente: R$"))
    department = input("Departamento do gerente: ")
    return Manager(name, salary, department)

def create_salesperson():
    name = input("Nome do vendedor: ")
    salary = float(input("Salário do vendedor: R$"))
    region = input("Região do vendedor: ")
    return Salesperson(name, salary, region)

def create_receptionist():
    name = input("Nome do recepcionista: ")
    salary = float(input("Salário do recepcionista: R$"))
    return Receptionist(name, salary)

def create_secretary():
    name = input("Nome do secretário: ")
    salary = float(input("Salário do secretário: R$"))
    return Secretary(name, salary)

def main():
    employees = []

    while True:
        print("\nO que você deseja fazer?")
        print("1. Adicionar um Gerente")
        print("2. Adicionar um Vendedor")
        print("3. Adicionar um Recepcionista")
        print("4. Adicionar um Secretário")
        print("5. Listar Funcionários")
        print("6. Ver detalhes de um funcionário")
        print("7. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            manager = create_manager()
            employees.append(manager)
            print("Gerente adicionado com sucesso!")
        elif choice == "2":
            salesperson = create_salesperson()
            employees.append(salesperson)
            print("Vendedor adicionado com sucesso!")
        elif choice == "3":
            receptionist = create_receptionist()
            employees.append(receptionist)
            print("Recepcionista adicionado com sucesso!")
        elif choice == "4":
            secretary = create_secretary()
            employees.append(secretary)
            print("Secretário adicionado com sucesso!")
        elif choice == "5":
            print("\nLista de Funcionários:")
            for i, employee in enumerate(employees, start=1):
                print(f"{i}. {employee}")
        elif choice == "6":
            emp_index = int(input("Digite o número do funcionário para ver detalhes: ")) - 1
            employee = employees[emp_index]
            print(f"\nDetalhes do Funcionário:\n{employee}")
            print("Descrição do Cargo:", employee.get_job_description())

            if hasattr(employee, 'evaluate_performance'):
                print("Avaliação de Desempenho:", employee.evaluate_performance())

            if hasattr(employee, 'communicate_effectively'):
                print("Habilidade de Comunicação:", employee.communicate_effectively())

        elif choice == "7":
            print("Saindo... Até logo!")
            break

if __name__ == "__main__":
    main()
