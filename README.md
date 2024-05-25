# Python Blackjack Game

This is a simple text-based Blackjack game written in Python. The game is played against the computer, with the computer acting as the dealer.

## What is Blackjack?

Blackjack is a popular card game played in casinos around the world. The objective of the game is to have a hand value as close to 21 as possible without exceeding it. Each card has a value, with numbered cards worth their face value, face cards (Jack, Queen, King) worth 10, and the Ace worth either 1 or 11, depending on the player's choice.

In the game, players are dealt two cards initially, and they can choose to "hit" to receive another card or "stand" to keep their current hand. The dealer also receives two cards, one face-up and one face-down. Once all players have made their decisions, the dealer reveals their face-down card and draws additional cards until their hand value is 17 or higher.

If a player's hand value exceeds 21, they lose the round. If the dealer's hand value exceeds 21, the player wins the round. If neither player exceeds 21, the player with the highest hand value wins the round.

You can play multiple rounds of Blackjack until you decide to quit the game.

## Installation
```bash
git clone git@github.com:aljvdi/python_blackjack.git python_blackjack
cd python_blackjack

# install dependencies
pip install -r requirements.txt

# Either run the game directly
python game.py

# Or create an alias to run the game
echo "alias bj='python3 $(pwd)/game.py'" >> ~/.bashrc # if you are using bash
echo "alias bj='python3 $(pwd)/game.py'" >> ~/.zshrc # if you are using zsh
echo "alias bj='python3 $(pwd)/game.py'" >> ~/.bash_profile # if you are using macOS
echo "alias bj='python $(pwd)/game.py'" >> ~/.bash_aliases # if you are using Ubuntu

# Restart the terminal and run the game using the alias
```




## How to Play

1. Run the `game.py` file to start the game.
2. You will be dealt two cards, and the dealer will also have two cards, one face-up and one face-down.
3. The goal is to get a hand value as close to 21 as possible without going over.
4. You can choose to "hit" to receive another card, or "stand" to keep your current hand.
5. If your hand value exceeds 21, you lose the round.
6. Once you stand, the dealer will reveal their face-down card and draw additional cards until their hand value is 17 or higher.
7. If the dealer's hand value exceeds 21, you win the round.
8. If neither player exceeds 21, the player with the highest hand value wins the round.
9. You can play multiple rounds until you decide to quit the game.

Have fun playing Blackjack!

## License

This project is licensed under the [MIT License](LICENSE).