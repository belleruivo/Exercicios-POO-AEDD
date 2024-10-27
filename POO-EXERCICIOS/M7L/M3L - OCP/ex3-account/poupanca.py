from conta import Conta

class Poupanca(Conta):
    def debito(self, valor):
        if valor > self.saldo:
            print("Quantia de débito excedeu o saldo da conta.")
        elif valor < 0:
            print("A quantia de débito não pode ser negativa.")
        elif valor > 500:
            print("Débito excedeu o limite de R$500 para contas de poupança.")
        else:
            self.saldo -= valor
            print(f"Débito de R${valor:.2f} realizado com sucesso na conta de poupança. Saldo atual: R${self.saldo:.2f}")