from bank import Bank

def main():
    bank = Bank()

    while True:
        print("\n--- Menu do Banco ---")
        print("1. Adicionar nova conta")
        print("2. Exibir todas as contas")
        print("3. Gerenciar uma conta")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Digite o nome do titular: ")
            balance = float(input("Digite o saldo inicial: "))
            bank.add_account(name, balance)
        elif choice == '2':
            bank.display_all_accounts()
        elif choice == '3':
            name = input("Digite o nome da conta para gerenciar: ")
            bank.manage_account(name)
        elif choice == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
