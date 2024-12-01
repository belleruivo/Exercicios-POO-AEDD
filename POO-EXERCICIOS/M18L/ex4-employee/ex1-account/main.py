from abc import ABC, abstractmethod

class Saldo:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def adicionar(self, valor):
        self.saldo += valor

    def remover(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def consultar(self):
        return self.saldo


class Limite:
    def __init__(self, limite=0):
        self.limite = limite

    def ajustar_limite(self, novo_limite):
        self.limite = novo_limite

    def consultar_limite(self):
        return self.limite


class Conta(ABC):
    def __init__(self, titular, saldo_componente):
        self.titular = titular
        self.saldo_componente = saldo_componente

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    def extrato(self):
        saldo_atual = self.saldo_componente.consultar()
        return f"Extrato de {self.titular}: R${saldo_atual:.2f}"


class ContaCorrente(Conta):
    def __init__(self, titular, saldo_componente, limite_componente):
        super().__init__(titular, saldo_componente)
        self.limite_componente = limite_componente

    def sacar(self, valor):
        saldo_total = self.saldo_componente.consultar() + self.limite_componente.consultar_limite()
        if saldo_total >= valor:
            self.saldo_componente.remover(valor)
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo_componente.adicionar(valor)
        return f"Depósito de R${valor:.2f} realizado com sucesso."


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo_componente.remover(valor):
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo_componente.adicionar(valor)
        return f"Depósito de R${valor:.2f} realizado com sucesso."


class ContaInvestimento(Conta):
    def sacar(self, valor):
        if self.saldo_componente.remover(valor):
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo_componente.adicionar(valor)
        return f"Depósito de R${valor:.2f} realizado com sucesso."


# Funções principais para criar e operar as contas
def criar_conta():
    print("Escolha o tipo de conta:")
    print("1-Corrente")
    print("2-Poupança")
    print("3-Investimento")

    while True:
        try:
            opcao = int(input("Digite sua opção: "))
            if opcao in [1, 2, 3]:
                break
            else:
                print("Escolha uma opção válida!")
        except ValueError:
            print("Escolha uma opção válida!")

    titular = input("\nInforme o nome do titular: ")

    while True:
        try:
            saldo_inicial = float(input("Informe o saldo inicial: R$"))
            if saldo_inicial < 0:
                print("O saldo inicial não pode ser negativo!")
            else:
                break
        except ValueError:
            print("Por favor, insira um valor numérico válido para o saldo.")

    saldo_componente = Saldo(saldo_inicial)

    if opcao == 1:
        while True:
            try:
                limite = float(input("Informe o limite de crédito da conta corrente: R$"))
                if limite < 0:
                    print("O limite de crédito não pode ser negativo!")
                else:
                    break
            except ValueError:
                print("Por favor, insira um valor numérico válido para o limite.")
        limite_componente = Limite(limite)
        return ContaCorrente(titular, saldo_componente, limite_componente)

    elif opcao == 2:
        return ContaPoupanca(titular, saldo_componente)

    elif opcao == 3:
        return ContaInvestimento(titular, saldo_componente)


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
                        print("O valor do depósito deve ser positivo!")
                    else:
                        break
                except ValueError:
                    print("Por favor, insira um valor numérico válido para o depósito.")
            print(conta.depositar(valor))

        elif opcao == "2":
            while True:
                try:
                    valor = float(input("Informe o valor do saque: R$"))
                    if valor <= 0:
                        print("O valor do saque deve ser positivo!")
                    else:
                        break
                except ValueError:
                    print("Por favor, insira um valor numérico válido para o saque.")
            print(conta.sacar(valor))

        elif opcao == "3":
            print(conta.extrato())

        elif opcao == "0":
            break

        else:
            print("Opção inválida! Tente novamente.")


def main():
    conta = criar_conta()
    if conta:
        operar_conta(conta)


main()
