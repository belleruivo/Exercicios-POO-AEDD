from person import Person
from supplier import Supplier
from employee import Employee
from administrator import Administrator
from factory_worker import FactoryWorker
from seller import Seller

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

def display_employee_type_menu():
    print("\nEscolha o tipo de funcionário:")
    print("1. Funcionário Comum")
    print("2. Administrador")
    print("3. Operário de Fábrica")
    print("4. Vendedor")
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
        employee_type = display_employee_type_menu()
        while True:
            try:
                sector_code = int(input("Código do Setor: "))
                base_salary = float(input("Salário Base: "))
                tax = float(input("Imposto (%): "))
                
                if employee_type == "1":  # Funcionário Comum
                    return Employee(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)
                elif employee_type == "2":  # Administrador
                    subsistence_allowance = float(input("Ajuda de custo: "))
                    return Administrator(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, subsistence_allowance)
                elif employee_type == "3":  # Operário de Fábrica
                    value_production = float(input("Valor da Produção: "))
                    commission = float(input("Comissão (%): "))
                    return FactoryWorker(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, value_production, commission)
                elif employee_type == "4":  # Vendedor
                    value_sales = float(input("Valor das Vendas: "))
                    commission = float(input("Comissão (%): "))
                    return Seller(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, value_sales, commission)
                else:
                    print("Tipo de funcionário inválido. Tente novamente.")
                    return None
                
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir valores numéricos válidos.\n")
    
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

    # Verifica se o funcionário é um administrador
    if isinstance(employee, Administrator):
        print(f"Ajuda de Custo: {employee.get_subsistence_allowance()}")
        print("Tipo: Administrador")
    elif isinstance(employee, FactoryWorker):
        print(f"Valor da Produção: {employee.get_value_production()}")
        print(f"Comissão: {employee.get_commission()}%")
        print("Tipo: Operário de Fábrica")
    elif isinstance(employee, Seller):
        print(f"Valor das Vendas: {employee.get_value_sales()}")
        print(f"Comissão: {employee.get_commission()}%")
        print("Tipo: Vendedor")
    else:
        print("Tipo: Funcionário Comum")

def calculate_employee_salary(employee):
    print(f"\nSalário final de {employee.get_nome()}: {employee.calculate_salary()}")

def consult_all_employees(employees):
    print("\nFuncionários cadastrados:")
    for i, employee in enumerate(employees, start=1):
        if isinstance(employee, Administrator):
            type_employee = "Administrador"
        elif isinstance(employee, FactoryWorker):
            type_employee = "Operário de Fábrica"
        elif isinstance(employee, Seller):
            type_employee = "Vendedor"
        else:
            type_employee = "Funcionário Comum"
        
        print(f"{i}. {employee.get_nome()} ({type_employee})")
    
    while True:
        try:
            choice = int(input("Digite o número do funcionário que deseja consultar: "))
            if 1 <= choice <= len(employees):
                consult_employee(employees[choice - 1])
                break
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

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
                for supplier in suppliers:
                    consult_supplier(supplier)
            else:
                print("Nenhum fornecedor cadastrado.")
        elif option == "3":
            if employees:
                consult_all_employees(employees)
            else:
                print("Nenhum funcionário cadastrado.")
        elif option == "4":
            if employees:
                for employee in employees:
                    calculate_employee_salary(employee)
            else:
                print("Nenhum funcionário cadastrado.")
        elif option == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
