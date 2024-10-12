class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display_account(self):
        print(f"Nome: {self.name}, Saldo: R${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Depósito de R${amount:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Saque de R${amount:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")
