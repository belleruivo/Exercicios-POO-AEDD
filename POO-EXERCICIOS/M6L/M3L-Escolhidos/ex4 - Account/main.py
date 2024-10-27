from bank import Bank

def main():
    bank = Bank()

    while True:
        print("\n--- Menu do Banco ---")
        print("1. Adicionar nova conta")
        print("2. Exibir todas as contas")
        print("3. Gerenciar uma conta")
        print("4. Sair")
        
        choice = input("Escolha uma opção (1-4): ")

        if choice == '1':
            try:
                name = input("Digite o nome do titular: ").strip().lower()
                balance = float(input("Digite o saldo inicial: "))
                bank.add_account(name, balance)
                print("Conta adicionada com sucesso.")
            except ValueError:
                print("Erro: Digite um valor numérico válido para o saldo inicial.")
                
        elif choice == '2':
            bank.display_all_accounts()
            
        elif choice == '3':
            name = input("Digite o nome da conta para gerenciar: ").strip().lower()
            bank.manage_account(name)
            
        elif choice == '4':
            print("Saindo do sistema...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
