# Guess the word
#
# The computer makes a word and answers only "Yes" or "no".
#
# The player has 5 attempts to guess the maximum number of letters, and then the player must write the entire word

import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
word = random.choice(WORDS)

print('In guess word', len(word), 'letters\n')

try_i = 0

while try_i < 5:
    # if try_i == 5:
    #     break
    letter = input('Enter a letter\n')
    try_i += 1
    if letter.lower() in word:
        print('Yen\n')
    else:
        print('No\n')

guess = input('Enter the hidden word\n')

if guess.lower() == word:
    print('This is the correct answer')
else:
    print('You lose this game!')
