from manager import Manager
from salesperson import Salesperson
from receptionist import Receptionist
from secretary import Secretary
from department import Department

# Agregação é um tipo de associação entre classes onde uma classe (o todo) contém referências a objetos de outra classe (as partes). Diferente da composição, na agregação, as partes podem existir independentemente do todo.

# Resumo das Alterações
# Para demonstrar a agregação de classes, foi criada a classe Department que agrega vários objetos Employee. A seguir, foram feitas as seguintes alterações:

# Criação da Classe Department:
# A classe Department gerencia uma lista de funcionários (Employee).
# Métodos foram adicionados para adicionar funcionários e obter a lista de funcionários.

# Essas alterações permitem a criação de departamentos e a adição de funcionários a esses departamentos, demonstrando a agregação de classes.

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
    departments = {}

    while True:
        print("\nMenu:")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Listar Departamentos")
        print("4. Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            employee = create_employee()
            if employee:
                dept_name = input("Nome do Departamento: ")
                if dept_name not in departments:
                    departments[dept_name] = Department(dept_name)
                departments[dept_name].add_employee(employee)
                print(f"{employee.name} foi adicionado ao departamento {dept_name} com sucesso!")
        elif option == "2":
            for dept_name, department in departments.items():
                print(f"\n{department}")
                for i, employee in enumerate(department.get_employees(), start=1):
                    print(f"  {i}. {employee}")
                    print(f"     Descrição do Trabalho: {employee.get_job_description()}")
        elif option == "3":
            if departments:
                print("\nLista de Departamentos:")
                for dept_name, department in departments.items():
                    print(f"{department}")
            else:
                print("\nNenhum departamento cadastrado.")
        elif option == "4":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()