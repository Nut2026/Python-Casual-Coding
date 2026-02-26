# My First Python Project (rated difficulty: 2/10)

import random
import time

count = 1

def roll_ask():
    roll = input("Roll the dice? (y/n): ")
    if roll.lower() != 'y' and roll.lower() != 'n':
        print('Invalid choice. Please input \'y\' for \'yes\' or \'n\' for \'no\'.\n')
        roll_ask()
    elif roll.lower() == 'y':
        roll_dice()
    else:
        end_program()


def roll_number():
    while True:
        try:
            dice_to_roll = int(input('\nAwesome! How many dice do you wish to roll? (provide a number): '))
            break
        except ValueError:
            print('Invalid choice. Please use a digit on your number pad.')
    return dice_to_roll


def roll_dice():
    global count
    number = roll_number()
    print(f'\nThis is dice-rolling round {count}.')
    time.sleep(0.5)
    if number == 1:
        print('The result is...\n')
    elif number == 0:
        print('No dice are rolled!')
    else:
        print('The results are...\n')
    time.sleep(random.uniform(0.5, 3.5))
    for i in range(1, number+1):
        print(f'Dice {i}: ' + str(random.randint(1, 6)))
    count += 1
    print('\n')
    roll_ask()


def end_program():
    print('\nThanks for joining me! See you soon and enjoy your day!🎊\n')
    print('\n' + '🎲' * 15 + '\n')


def run_program():
    print('\n' + '🎲' * 15)
    print('\nGreat to have you here!')
    roll = roll_ask()


run_program()

# Code Organisation & Structure: 7/10
# Variable Naming: 8/10
# Error Handling: 6/10
# Code Style: 7/10
# Documentation: 4/10
# Overall Score: 6.5/10
# Code assistance & grading from GitHub Copilot.
