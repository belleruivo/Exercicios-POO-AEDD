# displayable_account.py
from account import Account
from display_strategy import DisplayStrategy

class DisplayableAccount:
    def __init__(self, account: Account, display_strategy: DisplayStrategy):
        self.account = account
        self.display_strategy = display_strategy

    def display(self):
        self.display_strategy.display(self.account)
