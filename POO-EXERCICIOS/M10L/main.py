# Crie um sistema chamado Sistema de Gestão de Pessoas (SGP). Nele, haverá um script
# principal chamado main.py com um menu para gerenciar dados de colaboradores
# relacionados com a empresa. Escreva todo o programa documentando e testando restrições
# de entradas de dados e exceções (pesquise como funciona o try-except no Python).
'''
from person import Person

def main():
    try:
        pessoa = Person()

        pessoa.set_nome("João Silva")
        pessoa.set_endereco("Rua das Flores, 123")
        pessoa.set_cpf("12345678901")
        pessoa.set_rg("MG1234567")
        pessoa.set_telefone("31987654321")

        print("Nome:", pessoa.get_nome())
        print("Endereço:", pessoa.get_endereco())
        print("CPF:", pessoa.get_cpf())
        print("RG:", pessoa.get_rg())
        print("Telefone:", pessoa.get_telefone())

    except ValueError as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
'''
from person import Person
from supplier import Supplier

def display_menu():
    print("\nSistema de Gestão de Pessoas (SGP)")
    print("1. Adicionar Pessoa")
    print("2. Adicionar Fornecedor")
    print("3. Consultar Fornecedor")
    print("4. Sair")
    return input("Escolha uma opção: ")

def add_person():
    while True:
        nome = input("Nome: ")
        if nome.isalpha():  
            break
        else:
            print("O nome deve conter apenas letras. Tente novamente.\n")

    endereco = input("Endereço: ")

    while True:
        try:
            cpf = input("CPF (Somente números): ")
            if len(cpf) == 11 and cpf.isdigit():
                break
            else:
                print("CPF deve ter 11 dígitos e conter apenas números.")
        except ValueError:
            print("Entrada inválida. Tente novamente.\n")

    while True:
        try:
            rg = input("RG (Somente números): ")
            if rg.isdigit():
                break
            else:
                print("RG deve conter apenas números.")
        except ValueError:
            print("Entrada inválida. Tente novamente.\n")
    
    while True:
        try:
            telefone = input("Telefone (Somente números): ")
            if telefone.isdigit():
                break
            else:
                print("Telefone deve conter apenas números.")
        except ValueError:
            print("Entrada inválida. Tente novamente.\n")

    pessoa = Person(nome, endereco, cpf, rg, telefone)
    return pessoa

def add_supplier():
    while True:
        nome = input("Nome: ")
        if nome.isalpha():  
            break
        else:
            print("O nome deve conter apenas letras. Tente novamente.\n")

    endereco = input("Endereço: ")

    while True:
        try:
            cpf = input("CPF (Somente números): ")
            if len(cpf) == 11 and cpf.isdigit():
                break
            else:
                print("CPF deve ter 11 dígitos e conter apenas números.")
        except ValueError:
            print("Entrada inválida. Tente novamente.\n")

    while True:
        try:
            rg = input("RG (Somente números): ")
            if rg.isdigit():
                break
            else:
                print("RG deve conter apenas números.")
        except ValueError:
            print("Entrada inválida. Tente novamente.\n")
    
    while True:
        try:
            telefone = input("Telefone (Somente números): ")
            if telefone.isdigit():
                break
            else:
                print("Telefone deve conter apenas números.")
        except ValueError:
            print("Entrada inválida. Tente novamente.\n")

    while True:
            try:
                value_credit = float(input("Crédito máximo: "))
                if value_credit < 0:
                    print("O crédito não pode ser negativo.")
                break
            except ValueError:
                print(f"Entrada inválida. Certifique-se de inserir um número válido\n")
    
    while True:
            try:
                value_debt = float(input("Dívida: "))
                if value_debt <0:
                    print("O crédito não pode ser negativo.")
                break
            except ValueError:
                print(f"Entrada inválida. Certifique-se de inserir um número válido\n")

    fornecedor = Supplier(nome, endereco, cpf, rg, telefone, value_credit, value_debt)
    return fornecedor

def consult_supplier(supplier):
    print(f"\nFornecedor: {supplier.get_nome()}")
    print(f"Endereço: {supplier.get_endereco()}")
    print(f"CPF: {supplier.get_cpf()}")
    print(f"RG: {supplier.get_rg()}")
    print(f"Telefone: {supplier.get_telefone()}")
    print(f"Crédito: {supplier.get_value_credit()}")
    print(f"Dívida: {supplier.get_value_debt()}")
    print(f"Saldo: {supplier.get_balance()}")

def main():
    print("-="*30)
    suppliers = []
    
    while True:
        option = display_menu()
        if option == "1":
            person = add_person()
            if person:
                print("Pessoa adicionada com sucesso.")
        elif option == "2":
            supplier = add_supplier()
            if supplier:
                suppliers.append(supplier)
                print("Fornecedor adicionado com sucesso.")
        elif option == "3":
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
        elif option == "4":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    print("-="*30)
main()