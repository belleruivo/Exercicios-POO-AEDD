# account_manager.py

from account import Account

class AccountManager:
    def __init__(self):
        self.accounts = []

    def add_account(self, name: str, balance: float):
        """Adiciona uma nova conta ao gerenciador."""
        new_account = Account(name, balance)
        self.accounts.append(new_account)

    def list_accounts(self):
        """Lista todas as contas gerenciadas."""
        return self.accounts
