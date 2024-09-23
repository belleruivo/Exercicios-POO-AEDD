'''Refazer a Lista M3L, aplicando o Princípio da Responsabilidade Única e mostrar as
diferenças de seu código, antes e depois.'''

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class AccountDisplay:
    def displayAccount(self, account):
        print(f"Nome: {account.name}, Saldo: {account.balance}")

def main():
    conta = Account("João Silva", 1000.0)
    display = AccountDisplay()
    display.displayAccount(conta)

if __name__ == "__main__":
    main()