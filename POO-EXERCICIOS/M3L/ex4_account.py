'''
4. Crie uma versão nova da classe Account com um método chamado displayAccount,
que exiba o name e o balance de uma conta passada como parâmetro. Altere também
o main para, ao invés de imprimir diretamente o name e o balance da conta, use o
método displayAccount, passando a conta como parâmetro.
'''

class Account:
    # método init -> constructor, executado automaticamente quando a classe é instanciada
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def displayAccount(self):
        print(f"Nome: {self.name}, Saldo: {self.balance}")
        # poderia ser um return -> return f"Nome: {self.name}, Saldo: {self.balance}" 
        # print(conta.displayAccount())

def main():
    # objeto -> conta
    conta = Account("João Silva", 1000.0)
    conta.displayAccount()

if __name__ == "__main__":
    main()
