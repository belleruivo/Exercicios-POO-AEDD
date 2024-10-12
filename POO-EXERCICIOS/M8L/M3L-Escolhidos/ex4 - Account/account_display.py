# account_display.py

class AccountDisplay:
    def __init__(self, account: any):  # Injeção de dependência
        self.account = account

    def display_account(self):
        """Exibe as informações da conta."""
        print(f"Nome: {self.account.name}, Saldo: {self.account.balance:.2f}")
