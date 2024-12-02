from employee import Employee
from administrator import Administrator
from factory_worker import FactoryWorker
from seller import Seller

def adicionar_employee():
    nome = input("Digite o nome do funcionário: ")
    endereco = input("Digite o endereço do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")
    rg = input("Digite o RG do funcionário: ")
    telefone = input("Digite o telefone do funcionário: ")
    sector_code = int(input("Digite o código do setor: "))
    base_salary = float(input("Digite o salário base: "))
    
    while True:
        tax = float(input("Digite a porcentagem de imposto (decimal): "))
        if 0 <= tax <= 1:
            break
        else:
            print("Taxa inválida. Digite um valor entre 0 e 1.")
    
    return Employee(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)

def adicionar_administrator():
    nome = input("Digite o nome do administrador: ")
    endereco = input("Digite o endereço do administrador: ")
    cpf = input("Digite o CPF do administrador: ")
    rg = input("Digite o RG do administrador: ")
    telefone = input("Digite o telefone do administrador: ")
    sector_code = int(input("Digite o código do setor: "))
    base_salary = float(input("Digite o salário base: "))
    
    while True:
        tax = float(input("Digite a porcentagem de imposto (decimal): "))
        if 0 <= tax <= 1:
            break
        else:
            print("Taxa inválida. Digite um valor entre 0 e 1.")
    
    subsistence_allowance = float(input("Digite a ajuda de custo: "))
    return Administrator(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, subsistence_allowance)

def adicionar_factory_worker():
    nome = input("Digite o nome do operário: ")
    endereco = input("Digite o endereço do operário: ")
    cpf = input("Digite o CPF do operário: ")
    rg = input("Digite o RG do operário: ")
    telefone = input("Digite o telefone do operário: ")
    sector_code = int(input("Digite o código do setor: "))
    base_salary = float(input("Digite o salário base: "))
    
    while True:
        tax = float(input("Digite a porcentagem de imposto (decimal): "))
        if 0 <= tax <= 1:
            break
        else:
            print("Taxa inválida. Digite um valor entre 0 e 1.")
    
    value_production = float(input("Digite o valor da produção: "))
    commission = float(input("Digite a comissão (decimal): "))
    return FactoryWorker(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, value_production, commission)

def adicionar_seller():
    nome = input("Digite o nome do vendedor: ")
    endereco = input("Digite o endereço do vendedor: ")
    cpf = input("Digite o CPF do vendedor: ")
    rg = input("Digite o RG do vendedor: ")
    telefone = input("Digite o telefone do vendedor: ")
    sector_code = int(input("Digite o código do setor: "))
    base_salary = float(input("Digite o salário base: "))
    
    while True:
        tax = float(input("Digite a porcentagem de imposto (decimal): "))
        if 0 <= tax <= 1:
            break
        else:
            print("Taxa inválida. Digite um valor entre 0 e 1.")
    
    value_sales = float(input("Digite o valor das vendas: "))
    commission = float(input("Digite a comissão (decimal): "))
    return Seller(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, value_sales, commission)

def listar_funcionarios(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    
    for func in funcionarios:
        print(f'Nome: {func.get_nome()}, Salário: {func.calculate_salary()}')

def main():
    funcionarios = []
    
    while True:
        print("\nSistema de Gestão de Funcionários")
        print("1. Adicionar Empregado")
        print("2. Adicionar Administrador")
        print("3. Adicionar Operário")
        print("4. Adicionar Vendedor")
        print("5. Listar Funcionários")
        print("6. Sair")
        
        opcao = int(input("Selecione uma opção (1-6): "))
        
        if opcao == 1:
            funcionario = adicionar_employee()
            funcionarios.append(funcionario)
            print("Empregado adicionado com sucesso!")
        elif opcao == 2:
            funcionario = adicionar_administrator()
            funcionarios.append(funcionario)
            print("Administrador adicionado com sucesso!")
        elif opcao == 3:
            funcionario = adicionar_factory_worker()
            funcionarios.append(funcionario)
            print("Operário adicionado com sucesso!")
        elif opcao == 4:
            funcionario = adicionar_seller()
            funcionarios.append(funcionario)
            print("Vendedor adicionado com sucesso!")
        elif opcao == 5:
            listar_funcionarios(funcionarios)
        elif opcao == 6:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
