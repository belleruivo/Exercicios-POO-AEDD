class Account:
    def __init__(self, name: str, balance: float, formatter: callable = None):
        self.name = name
        self.balance = balance
        self.formatter = formatter if formatter else self.default_formatter  # Injeção de dependência

    def default_formatter(self, value: float) -> str:
        """Formatador padrão para o saldo."""
        return f"{value:.2f}"

    def formatted_balance(self) -> str:
        """Retorna o saldo formatado usando o formatador injetado."""
        return self.formatter(self.balance)

    def deposit(self, amount: float):
        """Adiciona um valor ao saldo da conta."""
        if amount > 0:
            self.balance += amount
        else:
            print("Valor do depósito deve ser positivo.")

    def withdraw(self, amount: float):
        """Retira um valor do saldo da conta."""
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Valor de retirada inválido.")
