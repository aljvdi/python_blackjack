# The Treasury the chips in front of the dealer (here, the dealer is the computer).
# It contains the player and the dealer balance, as well as the total chips in the treasury.

class Treasury:
    _player_balance: float
    _dealer_balance: float
    _total_chips: int

    def __init__(self, player_balance: float):
        self._player_balance = player_balance
        self._total_chips = 1000000 # A million by default.
        self._dealer_balance = self._total_chips * 0.1 # 10% of the casino's Treasury

    def does_player_have_enough_money(self) -> bool:
        """
        Check if player is able to play more or not
        """
        return self._player_balance > 1 # Means the player has enough fund to play (£1 is the minimum bet in most casinos)
    
    def does_dealer_have_enough_money(self) -> bool:
        """
        Check if the dealer's fund is enough to continue
        """

        return self._dealer_balance > 0 # Means the delaer has enough fund to play (otherwise, what a shame for a computer Xd)
    
    def can_player_bet(self, player_bet_amount: float) -> bool:
        """
        Check if player has enough money to bet
        """

        return player_bet_amount <= self._player_balance
    
    def get_player_balance(self) -> float:
        return self._player_balance
    
    def set_player_balance(self, amount: float) -> None:
        self._player_balance = amount

    def get_dealer_balance(self) -> float:
        return self._dealer_balance
    
    def set_dealer_balance(self, amount: float) -> None:
        self._dealer_balance = amount