# Программу писал Я, Ден
# 11 февраля в 02:20 ночи
#
#
# Программа про новые блюда
#
# food1 = input('А какое твоё любимое блюдо пришло тебе в голову первым?\n')
# food2 = input('\nХорошо, а какое блюдо ты бы сьел затем?\n')
#
# new_food = food1 + food2
# print('\n\nОтлично, тогда, я думаю, что блюдо "', new_food, '" тебе тоже зайдёт', sep='+')
# print('\a')
# input('\n\nЖми ЭНТЕР, шобы дальше всё было')


# #Программа про чаевые и счёт
#
# score = int(input('Ну и на сколько ты посидел в этом баре?!\n'))
# tea1 = (score*15)//100
# tea2 = (score/100)*20
# print('''Кароч, если этот хер тебе понравился, то оставляй  {tea2} рублей.
# А если нет, то кинь ему на лицо хотя бы  {tea1}  рублей.
#
#       '''.format(tea1=tea1, tea2=tea2))
#
# input('\nХуяр в колокол, чтобы продолжить')


#Программа про покупку авто

price = int(input('Доброго времени суток, какой автомобиль вам приглянулся?! Сколько он стоит?\n'))
print('\n\n')

tax = price*0.05
reg_sbor = price*0.1
ag_sbor = 20000
delivery = 5000
new_price = price+tax+reg_sbor+ag_sbor+delivery

print('Отличынй выбор, итого к оплате, со всеми надбавками, будет', new_price, 'рублей.\n')

input('Ёбни по клаве, чтобы выйти из этой ЧУДЕСНОЙ программы')