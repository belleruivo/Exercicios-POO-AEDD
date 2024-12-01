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
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f"Conta de {conta.titular} adicionada com sucesso ao banco {self.nome}.")

    def buscar_conta(self, titular):
        for conta in self.contas:
            if conta.titular == titular:
                return conta
        print("Conta não encontrada.")
        return None

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada no banco.")
        else:
            print(f"\nContas no banco {self.nome}:")
            for conta in self.contas:
                print(f"- {conta.titular}: R${conta.saldo:.2f}")

def criar_conta():
    print("\nEscolha o tipo de conta:")
    print("1 - Corrente")
    print("2 - Poupança")
    print("3 - Investimento")
    
    while True:
        try:
            opcao = int(input("Digite sua opção: "))
            if opcao in [1, 2, 3]:
                break
            else:
                print("Escolha uma opção válida!\n")
        except ValueError:
            print("Escolha uma opção válida!\n")

    titular = input("\nInforme o nome do titular: ")

    while True:
        try:
            saldo_inicial = float(input("Informe o saldo inicial: R$"))
            if saldo_inicial < 0:
                print("O saldo inicial não pode ser negativo!\n")
            else:
                break
        except ValueError:
            print("Por favor, insira um valor numérico válido para o saldo.\n")

    if opcao == 1:
        while True:
            try:
                limite = float(input("Informe o limite de crédito da conta corrente: R$"))
                if limite < 0:
                    print("O limite de crédito não pode ser negativo!\n")
                else:
                    break
            except ValueError:
                print("Por favor, insira um valor numérico válido para o limite de crédito.\n")
        return ContaCorrente(titular, saldo_inicial, limite)
    
    elif opcao == 2:
        return ContaPoupanca(titular, saldo_inicial)
    
    elif opcao == 3:
        return ContaInvestimento(titular, saldo_inicial)

def operar_conta(conta):
    while True:
        print("\nOpções de operações:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("0 - Sair")

        opcao = input("Escolha uma operação: ")

        if opcao == "1":
            while True:
                try:
                    valor = float(input("Informe o valor do depósito: R$"))
                    if valor <= 0:
                        print("O valor do depósito deve ser positivo!\n")
                    else:
                        break
                except ValueError:
                    print("Por favor, insira um valor numérico válido para o depósito.\n")
            print(conta.depositar(valor))
        elif opcao == "2":
            while True:
                try:
                    valor = float(input("Informe o valor do saque: R$"))
                    if valor <= 0:
                        print("O valor do saque deve ser positivo!\n")
                    else:
                        break
                except ValueError:
                    print("Por favor, insira um valor numérico válido para o saque.\n")
            print(conta.sacar(valor))
        elif opcao == "3":
            print(conta.extrato())
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.\n")

def main():
    banco = Banco("Banco Central")
    while True:
        print("\nMenu do Banco:")
        print("1 - Criar Conta")
        print("2 - Operar Conta")
        print("3 - Listar Contas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            conta = criar_conta()
            if conta:
                banco.adicionar_conta(conta)
        elif opcao == "2":
            titular = input("Informe o nome do titular da conta: ")
            conta = banco.buscar_conta(titular)
            if conta:
                operar_conta(conta)
        elif opcao == "3":
            banco.listar_contas()
        elif opcao == "0":
            print("Saindo do sistema do banco.")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()