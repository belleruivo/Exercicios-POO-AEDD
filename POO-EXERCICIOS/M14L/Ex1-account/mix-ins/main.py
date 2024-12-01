from contas import *

def criar_conta():
    print("Escolha o tipo de conta:")
    print("1-Corrente")
    print("2-Poupança")
    print("3-Investimento")
    
    while True:
        try:
            opcao = int(input("Digite sua opção: "))
            if opcao in [1, 2, 3]:
                break
            else:
                print("Escolha uma opção válida!\n")
        except ValueError:
            print("Por favor, insira um número válido.\n")

    titular = input("\nInforme o nome do titular: ")

    while True:
        try:
            saldo_inicial = float(input("Informe o saldo inicial: R$"))
            if saldo_inicial < 0:
                print("O saldo inicial não pode ser negativo!\n")
            else:
                break
        except ValueError:
            print("Por favor, insira um valor numérico válido para o saldo.\n")

    if opcao == 1:
        while True:
            try:
                limite = float(input("Informe o limite de crédito da conta corrente: R$"))
                if limite < 0:
                    print("O limite de crédito não pode ser negativo!\n")
                else:
                    break
            except ValueError:
                print("Por favor, insira um valor numérico válido para o limite de crédito.\n")
        return ContaCorrente(titular, saldo_inicial, limite)
    
    elif opcao == 2:
        return ContaPoupanca(titular, saldo_inicial)
    
    elif opcao == 3:
        while True:
            try:
                rendimento = float(input("Informe o rendimento da conta de investimento (exemplo: 0.05 para 5%): "))
                if rendimento < 0:
                    print("O rendimento não pode ser negativo!\n")
                else:
                    break
            except ValueError:
                print("Por favor, insira um valor numérico válido para o rendimento.\n")
        return ContaInvestimento(titular, saldo_inicial, rendimento)

def operar_conta(conta):
    while True:
        print("\nOpções de operações:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        
        if isinstance(conta, ContaInvestimento):
            print("4 - Aplicar rendimento")
        
        print("0 - Sair")

        opcao = input("Escolha uma operação: ")

        if opcao == "1":
            while True:
                try:
                    valor = float(input("Informe o valor do depósito: R$"))
                    if valor <= 0:
                        print("O valor do depósito deve ser positivo!\n")
                    else:
                        break
                except ValueError:
                    print("Por favor, insira um valor numérico válido para o depósito.\n")
            print(conta.depositar(valor))
        elif opcao == "2":
            while True:
                try:
                    valor = float(input("Informe o valor do saque: R$"))
                    if valor <= 0:
                        print("O valor do saque deve ser positivo!\n")
                    elif valor > conta.saldo:
                        print("Saldo insuficiente para saque!\n")
                    else:
                        break
                except ValueError:
                    print("Por favor, insira um valor numérico válido para o saque.\n")
            print(conta.sacar(valor))
        elif opcao == "3":
            print(conta.extrato())
        elif opcao == "4" and isinstance(conta, ContaInvestimento):
            print(conta.aplicar_rendimento())
        elif opcao == "0":
            break
        else:
            print("Opção inválida ou operação indisponível! Tente novamente.\n")

def main():
    conta = criar_conta()
    if conta:
        operar_conta(conta)

main()
