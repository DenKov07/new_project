# Who is your daddy?!)
# Program about
# Bloodline. You can find the father

son_father = [('Den', 'Konstantin'),
              ('Daniel', 'Pavel'),
              ('Vladimir', 'Viktor'),
              ('Konstantin', 'Feofan'),
              ('Viktor', 'Yiriy')]


while True:
    choice = input('''
            Hwo is your Daddy?!)
        I know your father. You can enter
        name, and i say, hwo is father.
        
    1. Get to know your father
    2. Added pair Son - Father in base
    3. Change pair Son - Father in base
    4. Delete pai Son - Father from base
    5. Show database\n
    ''')

    if choice == '1':
        input_son = input("Enter son's name\n")
        for pair in son_father:
            son, father = pair
            if input_son == son in pair:
                print("Father name's {}\n".format(father))
                choice = input("If it's the wrong pair, press 'n'\n")
                if choice.lower() == 'n':
                    continue
                else:
                    break
            elif input_son not in pair:
                continue
        else:
            print("This pair is not in the database\n")

    elif choice == '2':
        input_son = input("Enter son's name\n")
        input_father = input("Enter his father name\n")
        for pair in son_father:
                son, father = pair
                if input_son != son or input_father != father:
                    father = input_father
                    pair = (son, father)
                    son_father.append(pair)
                    print("Pair added in database\n")
                    break

                elif input_son == son and input_father == father:
                    print("This pair is already in base\n")
                    break

    elif choice == '3':
        input_son = input("Enter son's name\n")
        for pair in son_father:
            son, father = pair
            if input_son == son:
                print(pair)
                choice = input('You want change this pair? Press y or n.\n')
                if choice.lower() == 'n':
                    continue
                elif choice.lower() == 'y':
                    input_son = input("Enter changed son's name\n")
                    input_father = input("Enter changed father's name\n")
                    son_father.remove(pair)
                    for pair in son_father:
                        if input_son not in pair or input_father not in pair:
                            pair = (input_son, input_father)
                            son_father.append(pair)
                            print('Done. Pair changed\n')
                            break
                        else:
                            print('This pair already in database')
                            continue
                else:
                    print("Pres 'y' or 'n'!!!")
                    continue
        else:
            print('No pair in database')

    elif choice == '4':
        input_son = input("Enter son's name\n")
        for pair in son_father:
            for son in pair:
                if input_son == son:
                    print(pair)
                    choice = input('You want delete this pair? Press y or n or 0 if you want to get out\n')
                    if choice.lower() == 'n':
                        continue
                    elif choice.lower() == 'y':
                        son_father.remove(pair)
                        print('Pair deleted\n')
                        break
                    elif choice == 0:
                        break
                    else:
                        print("Pres 'y' or 'n'!!!")
                        continue
        else:
            print('No name in database')

    elif choice == '5':
        for pair in son_father:
            son, father = pair
            print(son, '=>>>', father)
        print('\n')
    else:
        break

    input('Press 0 for exit or press "Enter" to continue')

    if choice == '0':
        break
    else:
        continue

