import models.treasury, models.engine, models.cards
from colorama import Fore
from os import system
from time import sleep
from pyfiglet import Figlet

treasury = models.treasury.Treasury(player_balance=100) # the player enters with £100 by default.
dispenser = models.cards.Cards()
engine = models.engine.Engine()


try:
    while treasury.does_dealer_have_enough_money() and treasury.does_player_have_enough_money():
        player_cards = []
        dealer_cards = []

        any_lost: bool = False # To keep track if any of them lost before checking the result

        system('clear') # Clear the "Table" for each new game
        print(Fore.CYAN + Figlet(font='slant').renderText("PY BlackJack") + Fore.RESET)

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
        dealer_cards.extend(dispenser.dispense(2)) # The dealer gets two cards as well (one of them is hidden)
        
        print("Player's Hand: ", player_cards)
        print("Dealer's Hand: ", [dealer_cards[0], 'HIDDEN']) # The dealer's second card is hidden

        if engine.get_the_score(player_cards) == 21:
            print(Fore.GREEN + "Whoala! Player wins with a Blackjack!" + Fore.RESET)
            treasury.set_player_balance(treasury.get_player_balance() + (player_bet * 1.5))
            sleep(3)
            continue
        
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
                print("Player's Hand: ", player_cards)
                if engine.get_the_score(player_cards) > 21:
                    break
                elif engine.get_the_score(player_cards) == 21:
                    any_lost = True
                    break
                continue
            elif player_choice == 's':
                break

        while engine.get_the_score(dealer_cards) < 17 and engine.get_the_score(player_cards) <= 21 and not any_lost:
            dealer_cards.append(dispenser.dispense())
            print("Dealer's Hand: ", dealer_cards)
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
            treasury.set_player_balance(treasury.get_player_balance() + player_bet)
        elif winner == "dealer":
            print(Fore.RED + message + Fore.RESET)
            treasury.set_player_balance(treasury.get_player_balance() - player_bet)
        else:
            print(Fore.YELLOW + message + Fore.RESET)
        
        sleep(3)
        

    raise KeyboardInterrupt()


except KeyboardInterrupt:
    system('clear') # Clear the "Table" before exiting
    print("\nPlayer has left the game. Final Stats:", f"\nPlayer Wins: {engine._player_wins}", f"\nDealer Wins: {engine._dealer_wins}") # I know it's not a good practice to access the private variables, but I'm just showing you that I can access them (Its python after all, everything is public Xd)
    print((Fore.GREEN if treasury.get_player_balance() > 100 else Fore.RED) + f"\nPlayer Cashout: £{treasury.get_player_balance()}" + Fore.RESET) # If the player has more than £100, it will be green, otherwise, it will be red.
    exit(0)