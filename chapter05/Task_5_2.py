# Task 5.2
# Program about hero and his specifications
#  User can customize hero

specification = {
    'Strength': 0,
    'health': 0,
    'wisdom': 0,
    'agility': 0}

points = 30

print('''
        Hello and Welcome
    Today you customize your hero

    Let's start:''')

while True:
    choice = input('''
1. Start to customize hero
2. Edit strength
3. Edit health
4. Edit wisdom
5. Edit agility

Remember, you can only distribute {} points\n'''.format(points))

    if choice == '1':
        for item in specification:
            while points >= 0:
                how_many = int(input("How many points do you want to bet " + item.lower() + '?\n'))
                if points + how_many < 0 or points - int(how_many) >30:
                    print("You can't do this. you don't have enough points")
                    print('You have left', points, 'points.')
                elif int(specification[item]) + int(points) + int(how_many) < 0:
                    print('Enter only positive values')
                    print('You have left', points, 'points.')
                else:
                    points = points - how_many
                    specification[item] = int(specification[item]) + int(how_many)
                    break
            print('You have left', points, 'points.')

    elif choice == '2':
        while points >= 0:
            print('Now strength have {} points'.format(specification['Strength']))
            how_many = input("How many points do you want to bet strength?\n")
            if points - int(how_many) < 0 or points - int(how_many) > 30:
                print("You can't do this. you don't have enough points")
                print('You have left', points, 'points.')
            elif int(specification['Strength']) + int(points) + int(how_many) < 0:
                print("You can 't reallocate more points than you have")
                print('You have left', points, 'points.')
            else:
                specification['Strength'] = int(specification['Strength']) + int(how_many)
                points = points - int(how_many)
                break

    elif choice == '3':
        while points >= 0:
            how_many = input("How many points do you want to bet health?\n")
            if points - int(how_many) < 0 or points - int(how_many) > 30:
                print("You can't do this. you don't have enough points")
                print('You have left', points, 'points.')
            elif int(specification['health']) + int(points) + int(how_many) < 0:
                print('Enter only positive values')
                print('You have left', points, 'points.')
            else:
                specification['health'] = int(specification['health']) + int(how_many)
                points = points - int(how_many)
                break

    elif choice == '4':
        while points >= 0:
            how_many = input("How many points do you want to bet wisdom?\n")
            if points - int(how_many) < 0 or points - int(how_many) > 30:
                print("You can't do this. you don't have enough points")
                print('You have left', points, 'points.')
            elif int(specification['wisdom']) + int(points) + int(how_many) < 0:
                print('Enter only positive values')
                print('You have left', points, 'points.')
            else:
                specification['wisdom'] = int(specification['wisdom']) + int(how_many)
                points = points - int(how_many)
                break

    elif choice == '5':
        while points >= 0:
            how_many = input("How many points do you want to bet agility?\n")
            if points - int(how_many) < 0 or points - int(how_many) > 30:
                print("You can't do this. you don't have enough points")
                print('You have left', points, 'points.')
            elif int(specification['agility']) + int(points) + int(how_many) < 0:
                print('Enter only positive values')
                print('You have left', points, 'points.')
            else:
                specification['agility'] = int(specification['agility']) + int(how_many)
                points = points - int(how_many)
                break

    else:
        print("Menu havan't this number")
        continue

    print('The hero looks like this:')
    print("Strength - [{}], health - [{}], wisdom - [{}], agility - [{}]".format(specification['Strength'],
                                                                                 specification['health'],
                                                                                 specification['wisdom'],
                                                                                 specification['agility']))
    print('You have {} points left'.format(points))
    print('\n')
    choice = input('Press "0" for quiet from program or press "Enter" if you want see main menu.\n')
    if choice == "0":
        break
    else:
        continue
