# Task_5_1
# Program print words without replay

import random

words = ('COW', 'HOME', 'TOWN', 'ROAD', 'SHOP', 'LIGHT')
printing = []

for word in words:
    choice = random.randrange(len(words))
    printing.append(words[choice])
    words = words[:choice] + words[(choice + 1):]

print(printing)
