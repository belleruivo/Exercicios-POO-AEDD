# main.py
from account import Account
from console_display import ConsoleDisplay
from displayable_account import DisplayableAccount

def main():
    account = Account("João Silva", 1000.0)

    # Passa a estratégia de exibição para a classe DisplayableAccount.
    displayable_account = DisplayableAccount(account, ConsoleDisplay())
    displayable_account.display()

if __name__ == "__main__":
    main()
