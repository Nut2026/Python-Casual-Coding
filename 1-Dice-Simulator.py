# Python-Casual-Coding 
# > Project No.1
# > > Dice-Simulator
# > > > Very first Python project

import random, traceback, os, re
from time import sleep

# Initialisations
count = 1
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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
            print('Invalid choice. Please use the digits on your number pad.')
    return dice_to_roll


def roll_dice():
    global count
    number = roll_number()
    print(f'\nThis is dice-rolling round {count}.')
    sleep(0.5)
    if number == 1:
        print('The result is...\n')
    elif number == 0:
        print('No dice are rolled!')
    else:
        print('The results are...\n')
    sleep(random.uniform(0.5, 3.5))
    for i in range(1, number+1):
        print(f'Dice {i}: ' + str(random.randint(1, 6)))
    count += 1
    print('\n')
    roll_ask()


def end_program():
    print('\nThanks for joining me! See you soon and enjoy your day!🎊\n')
    print('\n' + '🎲' * 15 + '\n')


def intro():
    print('\n' + '🎲' * 15)
    print('\nGreat to have you here!')
    roll = roll_ask()

def unexpected_error():
    """
    A message for contact details in case of bugs/errors.
    """
    print("\n❗" + "💬"*5)
    print("Message From Author:")
    sleep(1)
    print("Apologies for the error; it seems that there are bugs I have yet to handle.")
    sleep(0.5)
    print("Kindly report it at:")
    sleep(0.5)
    print(f"""
    - GitHub >> https://github.com/Nut2026/Python-Casual-Coding/issues
    """)
    sleep(0.2)
    print("Do attach a complete copy of the traceback, thank you!")
    print("I've tried to sanitise the directories, but in case some leaks, please don't hesitate to redact it.")
    sleep(0.1)
    print("We will be in touch shortly; I appreciate your time and patience.")
    print("\n—Nuz")
    print("💬"*5 + " ❗\n")

def run_program():
    try:
        start_simulator()
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt detected. Exiting safely...")
        end_program()
    except Exception:
        print("\n🚨🚨 A fatal error has occurred. 🚨🚨\n")
        tb = traceback.format_exc()
        # Replace project directory paths
        tb = tb.replace(str(BASE_DIR), "<PROJECT_DIR>")
        # Replace absolute paths
        tb = re.sub(r"[A-Z]:\\[^:\n]*", "<ABS_PATH>", tb)  # Windows
        tb = re.sub(r"/[^:\n]*", "<ABS_PATH>", tb)  # Unix/Linux
        print(tb) 
        unexpected_error()

# === Run Program (Dice-Simulator) ===
run_program()