# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money
#
# New updates:
# Player have 10 attempt

import random

print("\tWelcome to 'Guess My Number'!\n")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
print(the_number)
guess = int(input("Take a guess: "))
tries = 1
if guess == the_number:
    print('YOU WIN?! HOW?!')

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries += 1
    if tries > 10:
        print('You lose! Machines WON!!! HA-HA-HA! ')
        break
    elif guess != the_number:
        continue
    else:
        print('What?! You win?! How?!')

print("And it only took you", tries, "tries!\n\n\n")

input("Press the enter key to exit.")
