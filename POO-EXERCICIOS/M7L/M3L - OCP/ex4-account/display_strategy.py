# display_strategy.py
from abc import ABC, abstractmethod
from account import Account

class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, account: Account):
        pass
