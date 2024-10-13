from account import Account  
from bank import Bank       

def main():
    nome_conta = input("Digite o nome do titular da conta: ")
    saldo_conta = float(input("Digite o saldo da conta: "))
    
    nome_banco = input("Digite o nome do banco: ")

    conta = Account(nome_conta, saldo_conta)
    banco = Bank(nome_banco)
    
    conta.displayAccount()
    banco.displayBank()

if __name__ == "__main__":
    main()
