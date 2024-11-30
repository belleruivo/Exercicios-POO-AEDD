from manager import Manager
from salesperson import Salesperson
from receptionist import Receptionist
from secretary import Secretary
from in_memory_employee_repository import InMemoryEmployeeRepository

# O Princípio da Inversão da Dependência (DIP) é o "D" nos princípios SOLID. Ele afirma que:

# Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.
# Abstrações não devem depender de detalhes. Detalhes devem depender de abstrações.
# Aplicação do DIP no Código
# Criação da Interface EmployeeRepository:

# Arquivo: employee_repository.py
# Descrição: Definimos uma interface abstrata EmployeeRepository com métodos add_employee e list_employees. Isso cria uma abstração para a persistência de dados.
# Implementação Concreta InMemoryEmployeeRepository:

# Arquivo: in_memory_employee_repository.py
# Descrição: Implementamos a interface EmployeeRepository em InMemoryEmployeeRepository, que usa uma lista para armazenar os funcionários. Esta implementação concreta depende da abstração EmployeeRepository.
# Modificação do main.py:

# Arquivo: main.py
# Descrição:
# Importamos a implementação concreta InMemoryEmployeeRepository.
# Substituímos a lista de funcionários por uma instância de InMemoryEmployeeRepository.
# Usamos os métodos add_employee e list_employees da interface para adicionar e listar funcionários.
# Como o DIP é Atendido
# Módulo de Alto Nível (main.py):

# Depende da abstração EmployeeRepository em vez de uma implementação concreta.
# Isso permite que main.py funcione com qualquer implementação de EmployeeRepository, promovendo flexibilidade e desacoplamento.
# Módulo de Baixo Nível (InMemoryEmployeeRepository):

# Implementa a abstração EmployeeRepository.
# Detalhes da implementação concreta dependem da abstração, não o contrário.
# Ao seguir o DIP, o código se torna mais modular, flexível e fácil de manter, pois as dependências são invertidas para depender de abstrações em vez de implementações concretas.

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
    repository = InMemoryEmployeeRepository()

    while True:
        print("\nMenu:")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            employee = create_employee()
            if employee:
                repository.add_employee(employee)
                print(f"{employee.name} foi adicionado com sucesso!")
        elif option == "2":
            employees = repository.list_employees()
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