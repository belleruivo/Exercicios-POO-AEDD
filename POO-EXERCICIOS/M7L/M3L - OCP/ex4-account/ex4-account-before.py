from abc import ABC, abstractmethod

# A classe Account permanece simples, sem lógica de exibição.
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

# Interface para exibição, permitindo múltiplas implementações.
class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, account: Account):
        pass

# Implementação para exibição no terminal.
class ConsoleDisplay(DisplayStrategy):
    def display(self, account: Account):
        print(f"Nome: {account.name}, Saldo: {account.balance}")

# Classe que usa a estratégia de exibição.
class DisplayableAccount:
    def __init__(self, account: Account, display_strategy: DisplayStrategy):
        self.account = account
        self.display_strategy = display_strategy

    def display(self):
        self.display_strategy.display(self.account)

def main():
    account = Account("João Silva", 1000.0)
    
    # Passa a estratégia de exibição para a classe DisplayableAccount.
    displayable_account = DisplayableAccount(account, ConsoleDisplay())
    displayable_account.display()

if __name__ == "__main__":
    main()
