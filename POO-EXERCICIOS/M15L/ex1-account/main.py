from abc import ABC, abstractmethod

class LimiteCreditoInterface(ABC):
    @abstractmethod
    def set_limite(self, limite):
        pass
    
    @abstractmethod
    def get_limite(self):
        pass

class JurosInterface(ABC):
    @abstractmethod
    def aplicar_juros(self):
        pass

class RendimentoInterface(ABC):
    @abstractmethod
    def aplicar_rendimento(self):
        pass

#from abc import ABC, abstractmethod
#from interfaces import LimiteCreditoInterface, JurosInterface, RendimentoInterface

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

    def set_limite(self, limite):
        self.limite = limite

    def get_limite(self):
        return self.limite

# Registrando a interface para ContaCorrente
LimiteCreditoInterface.register(ContaCorrente)

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo=0, taxa_juros=0.01):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        return "Saldo insuficiente para saque."

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."

    def aplicar_juros(self):
        self.saldo += self.saldo * self.taxa_juros
        return f"Juros aplicados. Novo saldo: R${self.saldo:.2f}"

# Registrando a interface para ContaPoupanca
JurosInterface.register(ContaPoupanca)

class ContaInvestimento(Conta):
    def __init__(self, titular, saldo=0, rendimento=0.05):
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
        return f"Rendimento aplicado. Novo saldo: R${self.saldo:.2f}"

# Registrando a interface para ContaInvestimento
RendimentoInterface.register(ContaInvestimento)

#from contas import ContaCorrente, ContaPoupanca, ContaInvestimento
#from interfaces import LimiteCreditoInterface, JurosInterface, RendimentoInterface

def operar_conta(conta):
    while True:
        print("\nOpções de operações:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        
        if isinstance(conta, RendimentoInterface):
            print("4 - Aplicar rendimento")
        elif isinstance(conta, JurosInterface):
            print("4 - Aplicar juros")
        
        print("0 - Sair")

        opcao = input("Escolha uma operação: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$"))
            print(conta.depositar(valor))
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$"))
            print(conta.sacar(valor))
        elif opcao == "3":
            print(conta.extrato())
        elif opcao == "4":
            if isinstance(conta, RendimentoInterface):
                print(conta.aplicar_rendimento())
            elif isinstance(conta, JurosInterface):
                print(conta.aplicar_juros())
        elif opcao == "0":
            break
        else:
            print("Opção inválida ou operação indisponível! Tente novamente.\n")

#from contas import ContaCorrente, ContaPoupanca, ContaInvestimento
#from interfaces import LimiteCreditoInterface, JurosInterface, RendimentoInterface

def criar_conta():
    print("Escolha o tipo de conta:")
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
            print("Por favor, insira um número válido.\n")

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
        while True:
            try:
                rendimento = float(input("Informe o rendimento da conta de investimento (exemplo: 0.05 para 5%): "))
                if rendimento < 0:
                    print("O rendimento não pode ser negativo!\n")
                else:
                    break
            except ValueError:
                print("Por favor, insira um valor numérico válido para o rendimento.\n")
        return ContaInvestimento(titular, saldo_inicial, rendimento)

def operar_conta(conta):
    while True:
        print("\nOpções de operações:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        
        if isinstance(conta, RendimentoInterface):
            print("4 - Aplicar rendimento")
        elif isinstance(conta, JurosInterface):
            print("4 - Aplicar juros")
        
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
        elif opcao == "4":
            if isinstance(conta, RendimentoInterface):
                print(conta.aplicar_rendimento())
            elif isinstance(conta, JurosInterface):
                print(conta.aplicar_juros())
        elif opcao == "0":
            break
        else:
            print("Opção inválida ou operação indisponível! Tente novamente.\n")

def main():
    print("Bem-vindo ao sistema bancário!\n")
    conta = criar_conta()
    if conta:
        operar_conta(conta)
    print("Obrigado por usar nosso sistema bancário. Até a próxima!")

if __name__ == "__main__":
    main()

