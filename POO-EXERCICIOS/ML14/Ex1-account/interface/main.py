def criar_conta():
    print("Escolha o tipo de conta:")
    print("1 - Corrente")
    print("2 - Poupança")
    print("3 - Investimento")

    while True:
        try:
            tipo = int(input("Digite sua opção: "))
            if tipo in [1, 2, 3]:
                break
            print("Escolha uma opção válida!")
        except ValueError:
            print("Entrada inválida! Escolha uma opção numérica válida.")

    titular = input("Informe o nome do titular: ")
    
    while True:
        try:
            saldo = float(input("Informe o saldo inicial (deve ser positivo): R$"))
            if saldo >= 0:
                break
            print("O saldo inicial deve ser positivo!")
        except ValueError:
            print("Por favor, insira um valor válido para o saldo.")

    if tipo == 1:
        while True:
            try:
                limite = float(input("Informe o limite de crédito (deve ser positivo): R$"))
                if limite >= 0:
                    break
                print("O limite deve ser positivo!")
            except ValueError:
                print("Por favor, insira um valor válido para o limite.")
        return ContaCorrente(titular, saldo, limite)

    elif tipo == 2:
        while True:
            try:
                taxa_juros = float(input("Informe a taxa de juros anual (%): "))
                if taxa_juros >= 0:
                    break
                print("A taxa de juros deve ser positiva!")
            except ValueError:
                print("Por favor, insira um valor válido para a taxa de juros.")
        return ContaPoupança(titular, saldo, taxa_juros)

    elif tipo == 3:
        while True:
            tipo_investimento = input("Informe o tipo de investimento (1-Alto Rendimento, 2-Baixo Rendimento): ")
            if tipo_investimento in ["1", "2"]:
                break
            print("O tipo de investimento deve ser '1' ou '2'.")
        return ContaInvestimento(titular, saldo, tipo_investimento)


# Operações com a conta
def operar_conta(conta):
    while True:
        print("\nOpções de Operação:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        if isinstance(conta, Rendimento):
            print("4 - Aplicar Rendimento")
        print("0 - Sair")

        opcao = input("Escolha uma operação: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$"))
            print(conta.deposito(valor))
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$"))
            print(conta.saque(valor))
        elif opcao == "3":
            print(conta.extrato())
        elif opcao == "4" and isinstance(conta, Rendimento):
            print(conta.aplicar_rendimento())
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# Função principal
def main():
    conta = criar_conta()
    operar_conta(conta)

main()
