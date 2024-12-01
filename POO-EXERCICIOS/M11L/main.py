from employee import Employee
from seller import Seller
from supplier import Supplier
from factory_worker import FactoryWorker
from administrator import Administrator

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
    print("1. Administrador")
    print("2. Operário de Fábrica")
    print("3. Vendedor")
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

                if employee_type == "1":  # Administrador
                    subsistence_allowance = float(input("Subsídio de Subsistência: "))
                    return Administrator(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, subsistence_allowance)

                if employee_type == "2":  # Operário de Fábrica
                    value_production = float(input("Valor de Produção: "))
                    commission = float(input("Comissão (%): "))
                    return FactoryWorker(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, value_production, commission)

                if employee_type == "3":  # Vendedor
                    value_sales = float(input("Valor de Vendas: "))
                    commission = float(input("Comissão (%): "))
                    return Seller(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, value_sales, commission)

            except ValueError:
                print("Entrada inválida. Tente novamente.\n")


def main():
    people = []

    while True:
        option = display_menu()

        if option == "1":
            person = add_person()
            people.append(person)
            print(f"\nPessoa adicionada com sucesso!\n")

        elif option == "2":
            cpf = input("Digite o CPF do fornecedor: ")
            found = False
            for person in people:
                if isinstance(person, Supplier) and person.get_cpf() == cpf:
                    display_common_data(person)
                    found = True
                    break
            if not found:
                print("Fornecedor não encontrado.")

        elif option == "3":
            cpf = input("Digite o CPF do funcionário: ")
            found = False
            for person in people:
                if isinstance(person, Employee) and person.get_cpf() == cpf:
                    display_common_data(person)
                    found = True
                    break
            if not found:
                print("Funcionário não encontrado.")

        elif option == "4":
            cpf = input("Digite o CPF do funcionário para calcular o salário: ")
            found = False
            for person in people:
                if isinstance(person, Employee) and person.get_cpf() == cpf:
                    print(f"\nSalário Calculado: {person.calculate_salary():.2f}")
                    found = True
                    break
            if not found:
                print("Funcionário não encontrado.")

        elif option == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

'''Substituição sem Quebra de Comportamento:

O método display_salary() foi criado para aceitar qualquer objeto da classe Employee, 
e podemos passar um objeto de Administrator, FactoryWorker ou Seller sem problemas. 
O cálculo do salário será feito de forma apropriada para cada tipo de funcionário.
Isso demonstra que podemos substituir uma instância de Employee por qualquer uma de suas subclasses 
(semelhante a como substituímos um Employee genérico por um Administrator, FactoryWorker ou Seller) 
e o sistema continua funcionando corretamente, sem comportamentos inesperados.

Exemplo Prático:

No código, substituímos o Employee por suas subclasses e o método calculate_salary() 
se adapta automaticamente ao tipo de funcionário.
Ou seja, a função display_salary() aceita qualquer Employee ou suas subclasses e calcula 
o salário de maneira correta de acordo com a implementação de cada subclasse.

Conclusão: No meu código, a estrutura de herança e o uso do método polimórfico calculate_salary() 
em cada subclasse garantem que as instâncias das subclasses de Employee podem ser usadas 
de forma transparente no lugar da classe base, sem alterar o comportamento esperado. 
Isso é um exemplo claro do Princípio de Substituição de Liskov, onde a substituição de 
uma classe base por suas subclasses não altera a funcionalidade do sistema, mantendo 
a consistência e previsibilidade.

'''