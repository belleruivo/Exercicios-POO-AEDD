from person import Person
from supplier import Supplier
from employee import Employee

def display_menu():
    print("\nSistema de Gestão de Pessoas (SGP)")
    print("1. Adicionar Pessoa")
    print("2. Consultar Fornecedor")
    print("3. Consultar Funcionário")
    print("4. Calcular Salário de Funcionário")
    print("5. Sair")
    return input("Escolha uma opção: ")

def display_person_type_menu():
    print("\nEscolha o tipo de pessoa:")
    print("1. Fornecedor")
    print("2. Funcionário")
    return input("Digite o número correspondente ao tipo: ")

def collect_common_data():
    while True:
        nome = input("Nome: ")
        if all(char.isalpha() or char.isspace() for char in nome):
            break
        else:
            print("O nome deve conter apenas letras e espaços. Tente novamente.\n")

    endereco = input("Endereço: ")

    while True:
        cpf = input("CPF (Somente números): ")
        if len(cpf) == 11 and cpf.isdigit():
            break
        else:
            print("CPF deve ter 11 dígitos e conter apenas números.")

    while True:
        rg = input("RG (Somente números): ")
        if rg.isdigit():
            break
        else:
            print("RG deve conter apenas números.")

    while True:
        telefone = input("Telefone (Somente números): ")
        if telefone.isdigit():
            break
        else:
            print("Telefone deve conter apenas números.")
    
    return nome, endereco, cpf, rg, telefone

def display_common_data(person):
    print(f"\nNome: {person.get_nome()}")
    print(f"Endereço: {person.get_endereco()}")
    print(f"CPF: {person.get_cpf()}")
    print(f"RG: {person.get_rg()}")
    print(f"Telefone: {person.get_telefone()}")

def add_person():
    nome, endereco, cpf, rg, telefone = collect_common_data()
    person_type = display_person_type_menu()

    if person_type == "1":  # Fornecedor
        while True:
            try:
                value_credit = float(input("Crédito máximo: "))
                if value_credit < 0:
                    print("O crédito não pode ser negativo.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir um número válido\n")

        while True:
            try:
                value_debt = float(input("Dívida: "))
                if value_debt < 0:
                    print("A dívida não pode ser negativa.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir um número válido\n")

        return Supplier(nome, endereco, cpf, rg, telefone, value_credit, value_debt)

    elif person_type == "2":  # Funcionário
        while True:
            try:
                sector_code = int(input("Código do Setor: "))
                base_salary = float(input("Salário Base: "))
                tax = float(input("Imposto (%): "))
                break
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir valores numéricos válidos.\n")

        return Employee(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)
    
    else:
        print("Tipo inválido. Pessoa não adicionada.")
        return None

def consult_supplier(supplier):
    display_common_data(supplier)
    print(f"Crédito: {supplier.get_value_credit()}")
    print(f"Dívida: {supplier.get_value_debt()}")
    print(f"Saldo: {supplier.get_balance()}")

def consult_employee(employee):
    display_common_data(employee)
    print(f"Código do Setor: {employee.get_sector_code()}")
    print(f"Salário Base: {employee.get_base_salary()}")
    print(f"Imposto: {employee.get_tax()}%")

def calculate_employee_salary(employee):
    print(f"\nSalário final de {employee.get_nome()}: {employee.calculate_salary()}")

def main():
    print("-="*30)
    suppliers = []
    employees = []

    while True:
        option = display_menu()
        if option == "1":
            person = add_person()
            if person:
                if isinstance(person, Supplier):
                    suppliers.append(person)
                    print("Fornecedor adicionado com sucesso.")
                elif isinstance(person, Employee):
                    employees.append(person)
                    print("Funcionário adicionado com sucesso.")
        elif option == "2":
            if suppliers:
                for idx, supplier in enumerate(suppliers):
                    print(f"\n{idx + 1}. {supplier.get_nome()}")
                try:
                    choice = int(input("Escolha o fornecedor para consultar: ")) - 1
                    if 0 <= choice < len(suppliers):
                        consult_supplier(suppliers[choice])
                    else:
                        print("Fornecedor inválido.")
                except ValueError:
                    print("Entrada inválida. Tente novamente.")
            else:
                print("Nenhum fornecedor cadastrado.")
        elif option == "3":
            if employees:
                for idx, employee in enumerate(employees):
                    print(f"\n{idx + 1}. {employee.get_nome()}")
                try:
                    choice = int(input("Escolha o funcionário para consultar: ")) - 1
                    if 0 <= choice < len(employees):
                        consult_employee(employees[choice])
                    else:
                        print("Funcionário inválido.")
                except ValueError:
                    print("Entrada inválida. Tente novamente.")
            else:
                print("Nenhum funcionário cadastrado.")
        elif option == "4":
            if employees:
                for idx, employee in enumerate(employees):
                    print(f"\n{idx + 1}. {employee.get_nome()}")
                try:
                    choice = int(input("Escolha o funcionário para calcular o salário: ")) - 1
                    if 0 <= choice < len(employees):
                        calculate_employee_salary(employees[choice])
                    else:
                        print("Funcionário inválido.")
                except ValueError:
                    print("Entrada inválida. Tente novamente.")
            else:
                print("Nenhum funcionário cadastrado.")
        elif option == "5":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    print("-="*30)

if __name__ == "__main__":
    main()
