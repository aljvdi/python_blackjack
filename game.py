try:
    import models.treasury, models.engine, models.cards
    from colorama import Fore
    from os import system
    from time import sleep
    from pyfiglet import Figlet
except ImportError as e:
    print("Import Error:", e.args[0])
    print("Please make sure you have installed the required packages by running 'pip install -r requirements.txt'.")
    exit(1)

treasury = models.treasury.Treasury(player_balance=100) # the player enters with £100 by default.
dispenser = models.cards.Cards()
engine = models.engine.Engine()

def print_hand(is_dealer: bool, the_hand: list) -> None:
    """
    Print the player's hand
    """

    print(f"{"Player" if not is_dealer else "Dealer"}'s Hand: ", the_hand)

def set_balance(did_player_win: bool, blackjack: bool = False) -> None:
    """
    Set the balance of the player and the dealer
    """

    player_bet = player_bet * 1.5 if blackjack else player_bet # If the player has a Blackjack, the player will get 1.5 times the bet

    if did_player_win:
        treasury.set_player_balance(treasury.get_player_balance() + player_bet)
        treasury.set_dealer_balance(treasury.get_dealer_balance() - player_bet)
    else:
        treasury.set_player_balance(treasury.get_player_balance() - player_bet)
        treasury.set_dealer_balance(treasury.get_dealer_balance() + player_bet)

try:
    while treasury.does_dealer_have_enough_money() and treasury.does_player_have_enough_money():
        player_cards = []
        dealer_cards = []

        any_lost: bool = False # To keep track if any of them lost before checking the result

        system('clear') # Clear the "Table" for each new game
        print(Fore.CYAN + Figlet(font='slant').renderText("PY BlackJack") + Fore.RESET)
        print(Fore.CYAN + f"By: gh/@aljvdi | Version: 0.0.1\n" + Fore.RESET) # A little bit of self-promotion Xd

        print(Fore.YELLOW + f"Player Balance: £{treasury.get_player_balance():.2f}" + Fore.RESET)


        # Ask the player to bet
        while True:
            try:
                player_bet = float(input("Enter your bet: £"))
                if not treasury.can_player_bet(player_bet):
                    raise ValueError(f"You don't have enough money to bet, you have £{treasury.get_player_balance()}")
            except ValueError as e:
                print(Fore.RED + "Error:", e.args[0], Fore.RESET)
                continue
            else:
                break

        # Dispense the cards
        player_cards.extend(dispenser.dispense(2))
        dealer_cards.extend(['HIDDEN', dispenser.dispense()]) # The dealer's first card is hidden
        
        print_hand(False, player_cards)
        print_hand(True, dealer_cards) # The dealer's second card is hidden

        if engine.get_the_score(player_cards) == 21: # If the player has a Blackjack
            print(Fore.GREEN + "Whoala! Player wins with a Blackjack!" + Fore.RESET)
            set_balance(True, True)
            sleep(3)
            continue

        # Player's turn
        while engine.get_the_score(player_cards) < 21:
            while True:
                try:
                    player_choice = input("Do you want to hit or stand? (h/s): ").lower()
                    if player_choice not in ['h', 's']:
                        raise ValueError("Invalid choice.")
                except ValueError as e:
                    print(Fore.RED + "Error:", e, Fore.RESET)
                    continue
                else:
                    break

            if player_choice == 'h':
                player_cards.append(dispenser.dispense())
                print_hand(False, player_cards)
                score = engine.get_the_score(player_cards)
                if score > 21:
                    break
                elif score == 21:
                    any_lost = True
                    break
                continue
            elif player_choice == 's':
                break

        # Dealer's turn
        if dealer_cards[0] == 'HIDDEN':
            dealer_cards[0] = dispenser.dispense()
            print_hand(True, dealer_cards)
            sleep(1)
        
        while engine.get_the_score(dealer_cards) < 17 and engine.get_the_score(player_cards) <= 21 and not any_lost:
            dealer_cards.append(dispenser.dispense())
            print_hand(True, dealer_cards)
            sleep(0.8)
            if engine.get_the_score(dealer_cards) > 21:
                break
            elif engine.get_the_score(dealer_cards) == 21:
                any_lost = True
                break
            
            

        # Check the result
        winner, message = engine.check_the_result(player_hand=player_cards, dealer_hand=dealer_cards)

        if winner == "player":
            print(Fore.GREEN + message + Fore.RESET)
            set_balance(True, False)
        elif winner == "dealer":
            print(Fore.RED + message + Fore.RESET)
            set_balance(False, False)
        else:
            print(Fore.YELLOW + message + Fore.RESET)
        
        sleep(3)
        

    raise KeyboardInterrupt()


except KeyboardInterrupt:
    system('clear') # Clear the "Table" before exiting
    print("\nPlayer has left the game. Final Stats:", f"\nPlayer Wins: {engine._player_wins}", f"\nDealer Wins: {engine._dealer_wins}") # I know it's not a good practice to access the private variables, but I'm just showing you that I can access them (Its python after all, everything is public Xd)
    print((Fore.GREEN if treasury.get_player_balance() > 100 else (Fore.YELLOW if treasury.get_player_balance() == 100 else Fore.RED)) + f"\nPlayer Cashout: £{treasury.get_player_balance():,.2f}" + Fore.RESET) # If the player has more than £100, it will be green, otherwise, it will be red.
    print(Fore.YELLOW + f"Dealer Balance: £{treasury.get_dealer_balance():,.2f}" + Fore.RESET)
    exit(0)