# Crie um sistema chamado Sistema de Gestão de Pessoas (SGP). Nele, haverá um script
# principal chamado main.py com um menu para gerenciar dados de colaboradores
# relacionados com a empresa. Escreva todo o programa documentando e testando restrições
# de entradas de dados e exceções (pesquise como funciona o try-except no Python).

'''Para ajudar a gente a entender, dps a gente apaga -> Sim, o código atende ao Princípio da Substituição de 
Liskov (Liskov Substitution Principle - LSP) do SOLID. O LSP afirma que uma subclasse deve ser substituível
por sua superclasse sem alterar o comportamento esperado do sistema. Em outras palavras, 
qualquer instância da subclasse Supplier pode ser usada em um contexto onde 
uma instância de Person é esperada, sem causar problemas no programa.'''

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
    pessoa = add_person() # Cria uma pessoa para ser usada como base para Supplier
    
    # Dados adicionais exclusivos de Supplier
    while True:
        try:
            value_credit = float(input("Crédito máximo: "))
            if value_credit >= 0:
                break
            else:
                print("Crédito não pode ser negativo.")
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir um valor numérico.")

    while True:
        try:
            value_debt = float(input("Dívida: "))
            if value_debt >= 0:
                break
            else:
                print("Dívida não pode ser negativa.")
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir um valor numérico.")

    fornecedor = Supplier(
        pessoa.get_nome(),
        pessoa.get_endereco(),
        pessoa.get_cpf(),
        pessoa.get_rg(),
        pessoa.get_telefone(),
        value_credit,
        value_debt
    )
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