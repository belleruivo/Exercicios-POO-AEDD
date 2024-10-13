class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def displayAccount(self):
        print(f"Nome: {self.name}, Saldo: {self.balance}")
