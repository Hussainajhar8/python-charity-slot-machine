import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": COLS*1,
    "B": COLS*2,
    "C": COLS*3,
    "D": COLS*4
}

symbol_value = {
    "A": 100,
    "B": 50,
    "C": 10,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    # print(all_symbols)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input(
            f"How many lines would you like to bet on (1 - {str(MAX_LINES)})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Lines must be between (1 - {str(MAX_LINES)})")
        else:
            print(f"Please enter a number between (1 - {str(MAX_LINES)})")
    return lines


def get_bet():
    while True:
        bet = input(
            f"How much would you like to bet on each line (${MIN_BET} - ${MAX_BET})? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be from (${MIN_BET} - ${MAX_BET})")
        else:
            print(f"Please enter a number from (${MIN_BET} - ${MAX_BET})")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"Invalid bet, not enough funds in balance, your current balance is: ${balance}")
        else:
            break

    print(
        f"Your are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    if winnings == 0:
        print("You didn't win anything, hopefully next time you do!", end="\n\n")
    else: 
        print(f"You won ${winnings}! Congratulations!")
        print(f"You won on lines:", *winning_lines, end="\n\n")
    return winnings - total_bet

def main():
    print('''
----  WELCOME TO THE CHARITY SLOT MACHINE  ----
DISCLAIMER WE DO NOT ENCOURAGE GAMBLING AT ALL, AS A MUSLIM ORGANISATION WE BELIEVE GAMBLING HAS BEEN MADE UNLAWFUL BY ALLAH THE AlMIGHTY AND HENCE WE DO NOT CONDONE IT AT ALL SINCE ITS HARMS ARE NUMEROUS.
ALL PROCEEDS FROM THIS SLOT MACHINE WILL GO TOWARDS CHARITY, SO PLEASE ONLY DEPOSIT AN AMOUNT YOU ARE WILLING TO DONATE, ANY EXTRA WINNINGS YOU EXIT THE GAME WITH WILL BE DONATED BY A GENEROUS INDIVIDUAL WHO WANTED TO ENCOURAGE OTHERS TO DONATE WITH A CHANCE OF MULTIPLYING THE GOOD!
---- ENJOY AND HAVE FUN! --- \n ''')
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}", end="\n\n")
        if balance == 0:
            print("Thank you for your donation! ByeBye.")
            break
        else:     
            answer = input("Press enter to play (q to quit). ")
            if answer == "q":
                break
            balance += spin(balance)
    
    if balance == 0:
        pass
    else:
        print(f"Thank you for your donation! The amount you've not played with is ${balance}")

main()
