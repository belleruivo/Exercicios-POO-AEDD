'''Implemente um sistema de Banco com seus 3 tipos de contas (corrente, poupança e
investimento), evidenciando a classe Account como uma classe abstrata.'''

from account import *

def criar_conta():
    print("Escolha o tipo de conta:")
    print("1-Corrente")
    print("2-Poupança")
    print("3-Investimento")
    
    while True:
        try:
            opcao = int(input("Digite sua Opção: "))
            if opcao in [1, 2, 3]:
                break
            else:
                ("Certifique-se de esolher uma opção válida!\n")
        except ValueError:
            print("Certifique-se de esolher uma opção válida!\n")

    titular = input("Informe o nome do titular: ")

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
        while True:
            try:
                taxa_juros = float(input("Informe a taxa de juros anual da conta poupança (%): "))
                if taxa_juros < 0:
                    print("A taxa de juros não pode ser negativa!\n")
                else:
                    break
            except ValueError:
                print("Por favor, insira um valor numérico válido para a taxa de juros.\n")
        return ContaPoupança(titular, saldo_inicial, taxa_juros)
    elif opcao == 3:
        while True:
            tipo_investimento = input("Informe o tipo de investimento (alto_rendimento ou baixo_rendimento): ").lower()
            if tipo_investimento in ["alto_rendimento", "baixo_rendimento"]:
                break
            else:
                print("Opção inválida! Informe 'alto_rendimento' ou 'baixo_rendimento'.\n")
        return ContaInvestimento(titular, saldo_inicial, tipo_investimento)

def operar_conta(conta):
    while True:
        print("\nOpções de operações:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        if isinstance(conta, ContaPoupança):
            print("4 - Aplicar Juros")
        if isinstance(conta, ContaInvestimento):
            print("4 - Aplicar Investimento")
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
            print(conta.deposito(valor))
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
            print(conta.saque(valor))
        elif opcao == "3":
            print(conta.extrato())
        elif opcao == "4":
            if isinstance(conta, ContaPoupança):
                print(conta.aplicar_juros())
            elif isinstance(conta, ContaInvestimento):
                print(conta.aplicar_investimento())
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.\n")

def main():
    conta = criar_conta()
    if conta:
        operar_conta(conta)

main()