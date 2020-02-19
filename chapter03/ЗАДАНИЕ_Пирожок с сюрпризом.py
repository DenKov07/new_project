# Программа про рандомный сюрприз в пирожках или типа того
# Писал код Ден


import random

surp=int(random.randint(1,5))
surp_1='пирожок с мясом'
surp_2='пирожок с капустой'
surp_3='пирожок с яблоком'
surp_4='пирожок с павидлом'
surp_5='пирожок с ничем'

if surp == 1:
    print('\nСегодня у тебя', surp_1, sep=' ')
elif surp == 2:
    print('\nСегодня у тебя', surp_2, sep=' ')
elif surp == 3:
    print('\nСегодня у тебя', surp_3, sep=' ')
elif surp == 4:
    print('\nСегоодня у тебя', surp_4, sep=' ')
elif surp == 5:
    print('\nСегодня у тебя', surp_5, sep=' ')

input('Нажми Enter для продолжения')
