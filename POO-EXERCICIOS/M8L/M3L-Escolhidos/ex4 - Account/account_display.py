class AccountDisplay:
    def __init__(self, account: any, display_formatter: callable = None):  # Injeção de dependência
        self.account = account
        self.display_formatter = display_formatter if display_formatter else self.default_display

    def default_display(self) -> str:
        """Formatador padrão para exibir as informações da conta."""
        return f"Nome: {self.account.name}, Saldo: {self.account.formatted_balance()}"

    def display_account(self):
        """Exibe as informações da conta usando o formatador injetado."""
        print(self.display_formatter() if self.display_formatter else self.default_display())
