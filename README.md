# Charity Slot Machine

## Purpose of the Game

The Charity Slot Machine is a simple Python console-based game designed to provide entertainment and raise funds for charity. The game is inspired by the classic slot machine mechanics, but with a charitable twist. All the proceeds from the game will be donated to charity, making it a fun and rewarding way to donate and contribute to a good cause.

**Disclaimer**: The creators of this game want to emphasize that they do not encourage gambling. As a Muslim organization, they believe that gambling is unlawful according to their religious beliefs. The game is intended solely for charity purposes, and players are encouraged to deposit only an amount they are willing to donate. Any extra winnings that players decide to exit the game with will be generously donated by someone who wants to encourage others to contribute to charity while having a chance of multiplying the good.

## How to Play

1. Upon starting the game, players will be prompted to deposit an amount they want to use for playing the game. The deposited amount will be the starting balance.

2. The game allows players to bet on multiple lines. The number of lines to bet on can be chosen by the player (within the range of 1 to 3).

3. For each line bet, the player is prompted to choose the bet amount (within the range of $1 to $100) on each line.

4. After placing the bet, the slot machine will spin, revealing symbols on each reel.

5. The game will check for winning combinations on the active lines based on the symbols obtained from the slot machine spin. Payouts are calculated based on the combination of symbols and the bet amount.

6. If the player wins, the winnings are added to the balance. If the player loses, the bet amount is subtracted from the balance.

7. The game continues until the player chooses to quit or runs out of balance.

## How the Game Works

### Symbols and Payouts

The slot machine consists of 3 rows and 3 columns, creating a 3x3 grid. The symbols used in the game are represented by uppercase letters: "A," "B," "C," and "D." Each symbol has its specific payout value:

- "A": Pays bet amount multiplied by 100
- "B": Pays bet amount multiplied by 50
- "C": Pays bet amount multiplied by 10
- "D": Pays bet amount multiplied by 2

### Lines and Bets

Players can choose to bet on multiple lines (up to a maximum of 3 lines) to increase their chances of winning. For each line, the player can choose a bet amount ranging from $1 to $100.

### Checking Winnings

After the slot machine spin, the game checks for winning combinations on the active lines. If all symbols on a line match, the player wins the corresponding payout based on the symbols' values and the bet amount.

### Ending the Game

Players can choose to quit the game at any time by pressing the "q" key when prompted to play. If the player decides to exit the game while still having a balance, the remaining balance will be donated to charity.

## Getting Started

To play the Charity Slot Machine, you need to have Python installed on your computer. If you don't have Python installed, you can download it from the official website (https://www.python.org/downloads/).

1. Clone or download the game code from the GitHub repository.

2. Open a terminal or command prompt and navigate to the directory containing the game files.

3. Run the game by executing the following command:

```
python slot_machine.py
```

4. Follow the on-screen instructions to deposit an amount, place bets, and enjoy playing the game.

Remember, the primary purpose of this game is to have fun while contributing to a charitable cause. Play responsibly and only deposit an amount you are comfortable donating to charity.

Enjoy the game, and thank you for supporting a good cause!
