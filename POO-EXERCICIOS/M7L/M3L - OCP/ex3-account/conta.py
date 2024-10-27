class Conta:
    def __init__(self, saldo_inicial=0):
        if saldo_inicial < 0:
            print("O saldo inicial não pode ser negativo!")
            self.saldo = 0
        else:
            self.saldo = saldo_inicial

    def debito(self, valor):
        if valor > self.saldo:
            print("Quantia de débito excedeu o saldo da conta.")
        elif valor < 0:
            print("A quantia de débito não pode ser negativa.")
        else:
            self.saldo -= valor
            print(f"Débito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

    def get_saldo(self):
        return self.saldo