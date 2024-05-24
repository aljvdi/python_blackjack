# The cards is basically act as a dispenser. It gives card and keep track of them
from random import choices, choice

class Cards:
    _cards: list
    
    def __init__(self) -> None:
        self._cards: list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        pass

    def dispense(self, count: int = 1) -> list|str:    
        if count > 1:
            return choices(self._cards, k=count)

        return choice(self._cards)