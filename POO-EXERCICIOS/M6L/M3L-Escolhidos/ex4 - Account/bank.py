from account import Account

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, name, balance):
        account = Account(name, balance)
        self.accounts.append(account)
        print(f"Conta de {name} adicionada com sucesso!")

    def display_all_accounts(self):
        if not self.accounts:
            print("Nenhuma conta cadastrada.")
        else:
            print("\n--- Lista de Contas ---")
            for account in self.accounts:
                account.display_account()

    def find_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None

    def manage_account(self, name):
        account = self.find_account(name)
        if account:
            while True:
                print(f"\n--- Gerenciando a Conta de {name} ---")
                print("1. Exibir saldo")
                print("2. Depositar")
                print("3. Sacar")
                print("4. Voltar ao menu principal")
                choice = input("Escolha uma opção: ")

                if choice == '1':
                    account.display_account()
                elif choice == '2':
                    amount = float(input("Digite o valor do depósito: "))
                    account.deposit(amount)
                elif choice == '3':
                    amount = float(input("Digite o valor do saque: "))
                    account.withdraw(amount)
                elif choice == '4':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        else:
            print(f"Conta de {name} não encontrada.")
