from employee import Employee
from administrator import Administrator
from factory_worker import FactoryWorker
from seller import Seller

def adicionar_funcionario(tipo):
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
    
    if tipo == "Administrator":
        subsistence_allowance = float(input("Digite a ajuda de custo: "))
        return Administrator(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, subsistence_allowance)
    elif tipo == "FactoryWorker":
        value_production = float(input("Digite o valor da produção: "))
        commission = float(input("Digite a comissão (decimal): "))
        return FactoryWorker(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, value_production, commission)
    elif tipo == "Seller":
        value_sales = float(input("Digite o valor das vendas: "))
        commission = float(input("Digite a comissão (decimal): "))
        return Seller(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, value_sales, commission)
    else:
        return Employee(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)

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
            funcionario = adicionar_funcionario("Employee")
            funcionarios.append(funcionario)
            print("Empregado adicionado com sucesso!")
        elif opcao == 2:
            funcionario = adicionar_funcionario("Administrator")
            funcionarios.append(funcionario)
            print("Administrador adicionado com sucesso!")
        elif opcao == 3:
            funcionario = adicionar_funcionario("FactoryWorker")
            funcionarios.append(funcionario)
            print("Operário adicionado com sucesso!")
        elif opcao == 4:
            funcionario = adicionar_funcionario("Seller")
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

'''
Explicação das Diferenças Antes e Depois da Aplicação do LSP
Antes:
Cada tipo de funcionário (Employee, Administrator, FactoryWorker, Seller) tinha métodos específicos para adicionar e listar informações.

A interação com diferentes tipos de funcionários era feita de maneira individualizada, o que poderia levar a redundância no código e dificuldades de manutenção.

Depois:
Unificamos a adição de funcionários em uma função adicionar_funcionario(tipo) que aceita o tipo de funcionário como parâmetro.

Agora, a função listar_funcionarios trata os funcionários de maneira genérica, respeitando o princípio de Liskov, onde qualquer instância de Employee ou suas subclasses pode ser usada de maneira intercambiável.

O sistema ficou mais simples, mais fácil de manter e estende novas funcionalidades sem modificar o comportamento esperado das superclasses.
'''