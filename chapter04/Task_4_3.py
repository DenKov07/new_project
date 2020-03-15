# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
# create tips
TIPS = ("The language we learn to program in",
        "What did we do with the letters of the words?!",
        "What do we say when we win CS: GO?",
        "The kid who got caught stealing - ",
        "What do we want to get to the question - ",
        "Strange musical instrument")
# create score
score = 0

# create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
    """
               Welcome to Word Jumble!
    
       Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")


while guess != correct or guess != '0':
    if guess == '?':
        score = 100
        score -= 25
        if score <= 0:
            print('Oh, you died)) Your score {}'.format(score))
            break

        if correct == (WORDS[0]):
            print(TIPS[0])
        elif correct == (WORDS[1]):
            print(TIPS[1])
        elif correct == (WORDS[2]):
            print(TIPS[2])
        elif correct == (WORDS[3]):
            print(TIPS[3])
        elif correct == (WORDS[4]):
            print(TIPS[4])
    else:
        print("Sorry, that's not it.")
    guess = input("Your guess: ")

if guess == correct:
    score = 100
    print("That's it!  You guessed it!\n")

print("Thanks for playing. Your score -", score)

input("\n\nPress the enter key to exit.")
