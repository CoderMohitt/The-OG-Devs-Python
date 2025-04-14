#snake water and gun
#snake beats water, water beats gun, gun beats snake

import random

# comp_value = 'snake'
# user_input = 'water'

# print('computer win')

# print(random.random())
# print(random.random())
# print(random.random())
# print(random.random())

# print(random.randint(0, 7))
# print(random.randint(0, 7))
# print(random.randint(0, 7))
# print(random.randint(0, 7))
# print(random.randint(0, 7))
# print(random.randint(0, 7))
# print(random.randint(0, 7))

#snake beats water, water beats gun, gun beats snake

print('press 1 for snake, 2 for water and 3 for gun')

user_input = int(input('Enter Your Option : '))

if(user_input > 3 or user_input < 1):
    print('not a valid value')
else:
    comp_input = random.randint(1, 3)

    if(user_input == 1 and comp_input == 2):
        print('user won')
    elif(user_input == 2 and comp_input == 3):
        print('user won')
    elif(user_input == 3 and comp_input == 1):
        print('user won')
    elif(user_input == comp_input):
        print('its a tie')
    else:
        print('computer won')

    if(user_input == 1):
        user_input = 'snake'
    elif(user_input == 2):
        user_input = 'water'
    else:
        user_input = 'gun'

    if(comp_input == 1):
        comp_input = 'snake'
    elif(comp_input == 2):
        comp_input = 'water'
    else:
        comp_input = 'gun'

    print('your choice : ', user_input)
    print('computer choice : ', comp_input)

    print('here')


# Mansi Bisht
# Rahul Rawat
# Rajat
# Harsh Ghai
# Jyoti Sanwal
# Aarti Mehra
# Paras Prajapati
# Meenakshi Giri

