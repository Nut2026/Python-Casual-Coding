# Python-Casual-Coding 
# > Project No.2
# > > Rock-Paper-Scissors

import random, traceback, os, re
from time import sleep

# Initialisations
match_count = 1
match_win_count = 0
match_draw_count = 0
match_lost_count = 0

def computer_choice():
    computer_choice_number = random.randint(1, 3)
    if computer_choice_number == 1:
        comp_emoji = '🗿'
    elif computer_choice_number == 2:
        comp_emoji = '📃'
    else:
        comp_emoji = '🪒'
    print(f'I Chose: {comp_emoji}\n')
    return comp_emoji


def user_choice():
    global choice
    if choice == 'r':
        user_emoji = '🗿'
    elif choice == 'p':
        user_emoji = '📃'
    else:
        user_emoji = '🪒'
    print(f'\nYou Chose: {user_emoji}')
    return user_emoji


def start():
    global choice
    global match_count
    global match_win_count
    global match_draw_count
    global match_lost_count
    round_count = 1
    user_win = 0
    comp_win = 0
    while round_count != 6:
        print(f"\nMatch {match_count}: Round {round_count}")
        choice = input(
            "\nChoose rock, paper, or scissors? ('r'/'p'/'s'): ").lower()
        if choice not in ('r', 'p', 's'):
            print("Invalid choice. Please enter 'r', 'p', or 's'.")
            start()
        else:
            user_emoji = user_choice()
            comp_emoji = computer_choice()
            if user_emoji == comp_emoji:
                print('Tie!')
            elif user_emoji == '🗿' and comp_emoji == '📃':
                print('Paper wraps rock. You lose!')
                comp_win += 1
            elif user_emoji == '🗿' and comp_emoji == '🪒':
                print('Rock smashes scissors. You win!')
                user_win += 1
            elif user_emoji == '📃' and comp_emoji == '🗿':
                print('Paper wraps rock. You win!')
                user_win += 1
            elif user_emoji == '📃' and comp_emoji == '🪒':
                print('Scissors cut paper. You lose!')
                comp_win += 1
            elif user_emoji == '🪒' and comp_emoji == '📃':
                print('Scissors cut paper. You win!')
                user_win += 1
            elif user_emoji == '🪒' and comp_emoji == '🗿':
                print('Rock smashes scissors. You lose!')
                comp_win += 1
            else:
                print('Unexpected outcome. You get a lucky win!')
                user_win += 1
        round_count += 1
    print(
        f"\n🎁 Result of match {match_count} 🎁\n\nYou: {user_win}\nMe: {comp_win}\n\n")
    if user_win > comp_win:
        print(f"You win match {match_count}! 🎉🎉")
        match_win_count += 1
    elif user_win < comp_win:
        print(
            f"You lose match {match_count}! Don't worry, you can always try again!")
        match_lost_count += 1
    else:
        print("We got a draw! Don't worry, we can always try again!")
        match_draw_count += 1
    match_count += 1
    print('\n')
    start_choice()

def intro():
    print('\n' + '🗿📃🪒' * 10 + '\n')
    print("Welcome to Rock Paper Scissors!\nEach match has five rounds. The one who wins the most rounds in that match is declared as the match winner!\n")

def outro():
    print(f'\n🎈Final Tally🎈\n🎡Total Matches Won: {match_win_count}\n🥖Total Matches Drawn: {match_draw_count}\n🛑Total Matches Lost: {match_lost_count}')
    print('\nThanks for joining me! See you soon! 🎊')
    print('\n' + '🗿📃🪒' * 10 + '\n')

def start_choice():
    global match_count
    global match_win_count
    global match_draw_count
    global match_lost_count
    start_input = input('Start a match or quit? (s/q): ').lower()
    if start_input == 's':
        start()
    elif start_input == 'q':
        outro()
    else:
        print('Invalid input. Please input \'s\' to start or \'q\' to quit the program.\n')
        start_choice()

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
        intro()
        start_choice()
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

# === Run Program (Rock-Paper-Scissors) ===
run_program()