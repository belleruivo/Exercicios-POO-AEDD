from account import Account
from account_display import AccountDisplay
from account_manager import AccountManager

def main():
    manager = AccountManager()  # Gerenciador de contas

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Conta")
        print("2. Listar Contas")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Digite o nome do titular da conta: ")
            balance = float(input("Digite o saldo inicial: "))
            manager.add_account(name, balance)
            print(f"Conta de {name} adicionada com sucesso!")
        
        elif choice == '2':
            print("\nLista de Contas:")
            for account in manager.list_accounts():
                account_display = AccountDisplay(account)  # Utilizando o display padrão
                account_display.display_account()
        
        elif choice == '3':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
