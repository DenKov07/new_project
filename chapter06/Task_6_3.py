# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money
#
# # Внесены изменения:
# 1) У игрока конечное число попыток(10)

import random


def instruct():
    print('''Welcome to 'Guess My Number'!
    I'm thinking of a number between 1 and 100.
    Try to guess it in as few attempts as possible.\n''')


def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def main():
    instruct()

    # set the initial values
    the_number = random.randint(1, 100)
    guess = ask_number('Take a guess:', 1, 100)
    tries = 1

    # guessing loop
    while guess != the_number:
        while tries <= 9:
            if guess > the_number:
                print("Lower...")
                tries += 1
                guess = ask_number('Take a guess:', 1, 100)
            elif guess < the_number:
                print("Higher...")
                tries += 1
                guess = ask_number('Take a guess:', 1, 100)
            else:
                break
        else:
            print('You lose! Machines WON!!! HA-HA-HA! ')
            break
    print('What?! You win?! How?!')

    print("And it only took you", tries, "tries!\n")
    input("\n\nPress the enter key to exit.")


main()

