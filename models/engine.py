# Engine contains the game's algorithms and configs (such as can player play more? Did player win? Did dealer/casino win?)

class Engine:
    _scores: dict
    _player_wins: int
    _dealer_wins: int

    def __init__(self) -> None:
        self._scores = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10,
            # The reason I didn't add the ace here is because the ace counts as 1 and 11 at the same time and it's up to player to choose the amount
        }
        self._player_wins = 0
        self._dealer_wins = 0

    def get_the_score(self, cards: list) -> int:
        """
        Get the score of cards

        Rules:
            - The score should not exceed 21
            
        Parameters:
            cards (list): A list of cards (A.K.A. the hand)

        Returns:
            int: The total score of the cards
        """

        total_score = 0

        for card in cards:
            if card == 'A':
                # Ace can be 1 or 11, let's choose intelligently
                ace_value = 11 if total_score <= 10 else 1
                total_score += ace_value
            else:
                card_score = self._scores[card]
                total_score += card_score

        return total_score
    
    def check_the_result(self, player_hand: list, dealer_hand: list) -> tuple[str, str]:
        """
        Check the result of the game by comparing the player's hand and the dealer's hand.

        Args:
            player_hand (list): The list of cards in the player's hand.
            dealer_hand (list): The list of cards in the dealer's hand.

        Returns:
            tuple[str, str]: Who wins and the message
        """
        
        player_hand_score = self.get_the_score(cards=player_hand)
        dealer_hand_score = self.get_the_score(cards=dealer_hand)

        if player_hand_score > 21:
            self._dealer_wins += 1
            return "dealer", "Player busts. Dealer wins!"
        elif dealer_hand_score > 21:
            self._player_wins += 1
            return "player", "Dealer busts. Player wins!"
        elif player_hand_score > dealer_hand_score:
            self._player_wins += 1
            return "player", "Player wins!"
        elif dealer_hand_score > player_hand_score:
            self._dealer_wins += 1
            return "dealer", "Dealer wins!"
        else:
            return "push", "It's a push!" # Push means the player and the dealer have the same score
        

