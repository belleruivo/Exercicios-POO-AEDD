'''
4. Crie uma versão nova da classe Account com um método chamado displayAccount,
que exiba o name e o balance de uma conta passada como parâmetro. Altere também
o main para, ao invés de imprimir diretamente o name e o balance da conta, use o
método displayAccount, passando a conta como parâmetro.
'''

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def getName(self):
        return self.name
    
    def getBalance(self):
        return self.balance
    
    def setName(self, name):
        self.name = name
        
    def setBalance(self, balance):
        self.balance = balance
        
    def displayAccount(self):
        print(f"\nNome do Cliente: {self.name}")
        print(f"Saldo Disponível: R${self.balance}")