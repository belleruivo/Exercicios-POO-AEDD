from manager import Manager
from salesperson import Salesperson
from receptionist import Receptionist
from secretary import Secretary
from address import Address

# A composição de classes foi demonstrada ao introduzir a classe Address e usá-la como um atributo na classe Employee. A composição é uma forma de construir classes complexas a partir de outras classes, estabelecendo uma relação "tem um" (has-a) entre elas.

# Definição de Composição de Classes
# Composição é um conceito de design de software onde uma classe é composta de uma ou mais instâncias de outras classes. Isso permite criar objetos complexos que são compostos de objetos mais simples.

# Implementação
# Classe Address:

# Criada para armazenar informações de endereço.
# Inclui atributos como street, city, state, e zip_code.
# Classe Employee:

# Modificada para incluir um atributo address do tipo Address.
# O construtor da classe Employee agora aceita um objeto Address como parâmetro.

def create_employee():
    print("\nSelecione o tipo de funcionário:")
    print("1. Gerente")
    print("2. Vendedor")
    print("3. Recepcionista")
    print("4. Secretário")

    choice = input("Escolha (1-4): ")
    name = input("Nome: ")
    salary = float(input("Salário: "))
    street = input("Rua: ")
    city = input("Cidade: ")
    state = input("Estado: ")
    zip_code = input("CEP: ")
    address = Address(street, city, state, zip_code)

    if choice == "1":
        department = input("Departamento: ")
        return Manager(name, salary, address, department)
    elif choice == "2":
        region = input("Região: ")
        return Salesperson(name, salary, address, region)
    elif choice == "3":
        return Receptionist(name, salary, address)
    elif choice == "4":
        return Secretary(name, salary, address)
    else:
        print("Escolha inválida!")
        return None

def main():
    employees = []

    while True:
        print("\nMenu:")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            employee = create_employee()
            if employee:
                employees.append(employee)
                print(f"{employee.name} foi adicionado com sucesso!")
        elif option == "2":
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