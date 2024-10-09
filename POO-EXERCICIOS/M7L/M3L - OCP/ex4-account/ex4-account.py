'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class DisplayableAccount(Account):
    def displayAccount(self):
        print(f"Nome: {self.name}, Saldo: {self.balance}")

def main():
    conta = DisplayableAccount("João Silva", 1000.0)
    conta.displayAccount()

if __name__ == "__main__":
    main()