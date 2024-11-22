from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def saque(self, valor):
        pass

    @abstractmethod
    def deposito(self, valor):
        pass

    def extrato(self):
        return f"Titular: {self.titular}, Saldo: R${self.saldo:.2f}"
    
'''A classe abstrata Account padroniza o comportamento de diferentes contas bancárias ao definir 
métodos abstratos (saque e deposito) que obrigam as subclasses (ContaCorrente, ContaPoupança, 
ContaInvestimento) a implementá-los. Ela também inclui métodos concretos, como extrato, para 
reutilização de código. Cada subclasse pode adicionar funcionalidades específicas, garantindo
consistência e flexibilidade no design.'''

class ContaCorrente(Account):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def saque(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        else:
            return "Saldo insuficiente para saque."

    def deposito(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso!"

class ContaPoupança(Account):
    def __init__(self, titular, saldo, taxa_juros):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        else:
            return "Saldo insuficiente para saque."

    def deposito(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso!"

    def aplicar_juros(self):
        juros = self.saldo * self.taxa_juros / 100
        self.saldo += juros
        return f"Juros aplicados: R${juros:.2f}"

class ContaInvestimento(Account):
    def __init__(self, titular, saldo, tipo_investimento):
        super().__init__(titular, saldo)
        self.tipo_investimento = tipo_investimento

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        else:
            return "Saldo insuficiente para saque."

    def deposito(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso!"

    def aplicar_investimento(self):
        if self.tipo_investimento == "alto_rendimento":
            rendimento = self.saldo * 0.10
        elif self.tipo_investimento == "baixo_rendimento":
            rendimento = self.saldo * 0.03
        else:
            rendimento = 0

        self.saldo += rendimento
        return f"Rendimento de {self.tipo_investimento} aplicado: R${rendimento:.2f}"

