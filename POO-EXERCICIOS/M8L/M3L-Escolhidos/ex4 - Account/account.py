# account.py

class Account:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

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
