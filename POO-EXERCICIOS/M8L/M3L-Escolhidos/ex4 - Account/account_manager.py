from account import Account

class AccountManager:
    def __init__(self, account_generator: callable = Account):  # Injeção de dependência
        self.accounts = []
        self.account_generator = account_generator  # O gerador de contas

    def add_account(self, name: str, balance: float):
        """Adiciona uma nova conta ao gerenciador."""
        new_account = self.account_generator(name, balance)  # Usando o gerador injetado
        self.accounts.append(new_account)

    def list_accounts(self):
        """Lista todas as contas gerenciadas."""
        return self.accounts
