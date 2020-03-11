# Игра наоборот
# Игра наоборот
# человек загадывает число, акомпьютер отгадывает

print('Hi, guess the number from 1 to 100. I will try to guess, but you need me to answer! \n'
      '"-" - If the guessed number is less than what I called  \n'
      '"+" - If the hidden number is greater than what I called \n'
      '"=" - If I answered correctly')

start = 0
end = 101
round = 0

while True:
    number = start + (end - start) // 2
    ans = input('This is ' + str(number) + '?\n')
    round += 1
    if ans == '=':
        print('I knew it')
        break
    elif ans == '-':
        end = number
    elif ans == '+':
        start = number
    else:
        print('Type only "+", "-" or "=", please')
        round -= 1

    if round > 10:
        print("I played this game")
        break


print('I spent', round, 'attempts. Play again?')
