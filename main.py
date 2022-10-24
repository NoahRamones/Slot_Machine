#Creator: Noah Ramones
#Date: 10/24/22
#Program: Slot Machine

import random

#Global Variables
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# List for how many of each letter are allowed to be spun
symbol_count = {
   "A": 3,
   "B": 4,
   "C": 5,
   "D": 6
}

# List of the value of each symbol
symbol_value = {
   "A": 5,
   "B": 4,
   "C": 3,
   "D": 2
}

# Calculates winnings after spinning
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    #Checks the value of the symbol that is in the place of the column,
    # going through and checking each line
    for line in range(lines):
        # We do columns[0] because we need to look at the first column
        # because that is where the first symbol will be for each row
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                # We are breaking because if we found that one of the symbols DO NOT equal to all or any of the symbols
                # in the row, we will break out of the for loop
                break
        # else statement will tell us if we didn't break out of the for loop
        # Finds out how much user won from spin
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# Generates the values(random) for the columns and rows
def get_slot_machine_spin(rows, cols, symbols):
   all_symbols = []
   # .items gives you both the key and value associated with a dictionary
   for symbol, symbol_count in symbols.items():
       # for loop adds symbols to all_symbols list
       for _ in range(symbol_count):
           all_symbols.append(symbol)

   columns = []
   for _ in range(cols):
       # Picking random values for each row in our column
       column = []
       current_symbols = all_symbols[:] #copies all_symbols list but does not change and exactly equal it b/c of slice [:]
       for _ in range(rows):
           value = random.choice(current_symbols)
           current_symbols.remove(value)
           column.append(value)

       columns.append(column)
   return columns

# This prints out - aligns the rows and columns of the generated slot machine
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "" )
        print()

# Gets the amount that the user wants to deposit from input
def deposit():
   while True:
       amount = input("What would you like to deposit? $")
       if amount.isdigit():
           amount = int(amount)
           if amount > 0:
               break
           else:
               print("Amount must be greater than 0.")
       else:
           print("Please enter a number.")
   return amount

# Gets the number of lines from user input
def get_number_of_lines():
   while True:
       lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
       if lines.isdigit():
           lines = int(lines)
           if 1 <= lines <= MAX_LINES:
               break
           else:
               print("Enter a valid number of lines.")
       else:
           print("Please enter a number.")

   return lines

# Gets the bet from user input
def get_bet():
   while True:
       amount = input("How much would you like to bet on each line? $")
       if amount.isdigit():
           amount = int(amount)
           if MIN_BET <= amount <= MAX_BET:
               break
           else:
               print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
       else:
           print("Please enter a number.")
   return amount

# Big Function for majority of the program to work - while loop implemented
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: {balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet

# Main Function to be called
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


# CALL FUNCTION
main()

