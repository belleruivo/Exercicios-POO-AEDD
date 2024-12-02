from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    def extrato(self):
        return f"Extrato de {self.titular}: R${self.saldo:.2f}"

class ServicoTransacao:
    @staticmethod
    def transferir(conta_origem, conta_destino, valor):
        if conta_origem.saldo >= valor:
            conta_origem.sacar(valor)
            conta_destino.depositar(valor)
            return f"Transferência de R${valor:.2f} de {conta_origem.titular} para {conta_destino.titular} realizada com sucesso!"
        return "Saldo insuficiente para realizar a transferência."

class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=1000):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."

class ContaInvestimento(Conta):
    def __init__(self, titular, saldo=0, rendimento=0.02):
        super().__init__(titular, saldo)
        self.rendimento = rendimento

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."

    def aplicar_rendimento(self):
        self.saldo += self.saldo * self.rendimento
        return f"Rendimento de {self.rendimento * 100:.2f}% aplicado! Saldo atual: R${self.saldo:.2f}"

def criar_conta():
    print("\nEscolha o tipo de conta:")
    print("1 - Conta Corrente")
    print("2 - Conta Poupança")
    print("3 - Conta Investimento")
    
    while True:
        try:
            tipo = int(input("Digite sua escolha: "))
            if tipo in [1, 2, 3]:
                break
            print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

    titular = input("\nInforme o nome do titular: ")

    while True:
        try:
            saldo_inicial = float(input("Informe o saldo inicial: R$"))
            if saldo_inicial < 0:
                print("O saldo inicial não pode ser negativo.")
            else:
                break
        except ValueError:
            print("Por favor, insira um valor numérico válido para o saldo inicial.")

    if tipo == 1:
        while True:
            try:
                limite = float(input("Informe o limite de crédito: R$"))
                if limite < 0:
                    print("O limite de crédito não pode ser negativo.")
                else:
                    break
            except ValueError:
                print("Por favor, insira um valor numérico válido para o limite de crédito.")
        return ContaCorrente(titular, saldo_inicial, limite)
    elif tipo == 2:
        return ContaPoupanca(titular, saldo_inicial)
    elif tipo == 3:
        while True:
            try:
                rendimento = float(input("Informe o rendimento da conta (ex: 0.05 para 5%): "))
                if rendimento < 0:
                    print("O rendimento não pode ser negativo.")
                else:
                    break
            except ValueError:
                print("Por favor, insira um valor numérico válido para o rendimento.")
        return ContaInvestimento(titular, saldo_inicial, rendimento)

def operar_conta(conta):
    while True:
        print("\nOpções de operação:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Consultar Extrato")
        if isinstance(conta, ContaInvestimento):
            print("4 - Aplicar Rendimento")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                try:
                    valor = float(input("Informe o valor do depósito: R$"))
                    if valor <= 0:
                        print("O valor do depósito deve ser positivo.")
                    else:
                        break
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
            print(conta.depositar(valor))
        elif opcao == "2":
            while True:
                try:
                    valor = float(input("Informe o valor do saque: R$"))
                    if valor <= 0:
                        print("O valor do saque deve ser positivo.")
                    else:
                        break
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
            print(conta.sacar(valor))
        elif opcao == "3":
            print(conta.extrato())
        elif opcao == "4" and isinstance(conta, ContaInvestimento):
            print(conta.aplicar_rendimento())
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    conta = criar_conta()
    operar_conta(conta)

main()
