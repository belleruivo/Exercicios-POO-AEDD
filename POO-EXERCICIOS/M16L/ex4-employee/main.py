from manager import Manager
from salesperson import Salesperson
from receptionist import Receptionist
from secretary import Secretary
from in_memory_employee_repository import InMemoryEmployeeRepository

# "Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações. Abstrações não devem depender de detalhes. Detalhes devem depender de abstrações."

def create_employee():
    print("\nSelecione o tipo de funcionário:")
    print("1. Gerente")
    print("2. Vendedor")
    print("3. Recepcionista")
    print("4. Secretário")

    choice = input("Escolha (1-4): ")
    name = input("Nome: ")
    salary = float(input("Salário: "))

    if choice == "1":
        department = input("Departamento: ")
        return Manager(name, salary, department)
    elif choice == "2":
        region = input("Região: ")
        return Salesperson(name, salary, region)
    elif choice == "3":
        return Receptionist(name, salary)
    elif choice == "4":
        return Secretary(name, salary)
    else:
        print("Escolha inválida!")
        return None

def main():
    repository = InMemoryEmployeeRepository() # poderia trocar por outro, alterando a concreta
 
    while True:
        print("\nMenu:")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Sair")

        option = input("Escolha uma opção: ")
    
        if option == "1":
            employee = create_employee()
            if employee:
                # usando add_employee da abstração EmployeeRepository
                repository.add_employee(employee) # !
                print(f"{employee.name} foi adicionado com sucesso!")
        elif option == "2":
            employees = repository.list_employees() # !
            if employees:
                print("\nLista de Funcionários:")
                for i, employee in enumerate(employees, start=1):
                    print(f"{i}. {employee}")
                    print(f"   Descrição do Trabalho: {employee.get_job_description()}")
            else:
                print("\nNenhum funcionário cadastrado.")
        elif option == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()