# console_display.py
from display_strategy import DisplayStrategy
from account import Account

class ConsoleDisplay(DisplayStrategy):
    def display(self, account: Account):
        print(f"Nome: {account.name}, Saldo: {account.balance}")
