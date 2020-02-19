# Программа подбрасывает монетку 100 раз
# А затем выводит сколько раз выпало орёл и сколько решка

import random


toos = 0
eagle = 0
tails = 0
while toos !=100:
    coin=int(random.randint(1,2))
    if coin == 1:
        eagle += 1
    else:
        tails += 1
    toos += 1

print('Орлов -', eagle, 'раз',  sep=' ')
print('Решек -', tails, 'раз',  sep=' ')