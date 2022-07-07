from multiprocessing.connection import answer_challenge
import random
import math


# Functions go here...
from tkinter import Y
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()


        if response == "yes" or response == "y" : 
            # response = "yes" 
            return "yes"

        elif response == "no" or response == "n": 
            # response = "no"
            return "no"
        
        else:
            print ("Please answer yes / no, if you're not sure I recommend you to press no")
  
def instructions ():
    print ("Welcome to uys0083's Trivia Game of Basic Math Equations!~")
    print ()
    print ("- In this game, the user will have a choice to answer a math equation of the following:")
    print ()
    print ("- Addition, Subtraction, Multiplication and Division!")
    print ()
    print ("- The user will select the amount of rounds they wish to play, or infinite mode if they wish to do so.")
    print ()
    print ("- After the user chooses the category of their choice, the computer will generate a random question from that category.")
    print ()
    print ("- For every question, the user is allowed to have 3 guesses.")
    print ()
    print ("- (Note that multiplication and division questions are tablelocked to 12.) ")
    print ()
    print ("- When all the rounds are finished, or the user chooses to quit")
    print ("  The game will tally up the results and display the user's game statistics.")
    print ()
    print ("- We wish the user to have fun!~")
    return ""


played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()

print("program continues")

# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        
        # If infinite mode not chosen, check response is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to start of loop
                if response <1:
                    print(round_error)
                    continue

            # If response is not an integer, go back to start of loop
            except ValueError:
                print(round_error)
                continue

        return response

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item in the list (or the first letter of an item), the full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item
        
        # output error if item not in list
        print(error)
        print()

# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
equation_list = ["addition", "subtraction", "multiplication", "division", "xxx"]

# Ask user if they have played before
# If 'yes', show instructions


# Ask user for # of rounds then loop...
rounds_played = 0

# Initialise rounds lost
rounds_lost = 0

game_summary = []

# ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # start of game play loop

    # rounds heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose_instruction = "Please choose addition, subtraction, multiplication, division or 'xxx' to exit "
    print()
    choose_error = ("{} or 'xxx' to end: ".format(choose_instruction))

    # ask user for choice and check it's valid
    choose = choice_checker(choose_instruction, equation_list, choose_error)
    if choose == "xxx":
        break


    # end game if exit code is typed
    if choose == "xxx":
        break


    # **** rest of loop / game ****
    print("You chose {}".format(choose))


    rounds_played += 1

    # End game if requested # of rounds has been played
    if rounds_played == rounds:
        break


answer = [] 
GUESSES_ALLOWED = 3
guess = ""

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0



# Testing to generate the numbers for the equation
for item in range (0, 12):
    chosen_num = random.randint(1, 100)
    chosen_num2 = random.randint(1, 100)
    table_num = random.randint(0, 12)
    table_num2 = random.randint(0, 12)
    div_num = random.randint (0, 144)

    # ask user for choice and check it's valid
    choose = choice_checker(choose_instruction, equation_list, choose_error)
    if choose == "xxx":
        break

    # If the user chooses addition
    if choose == "addition":
        print("Question: {} + {}".format(chosen_num, chosen_num2))
        input (guess)

    # If the user chooses subtraction
    elif choose == "subtraction":
        print("Question: {} - {}".format(chosen_num, chosen_num2))
        input (guess)

    # If the user chooses multiplication
    elif choose == "multiplication":
        print("Question: {} * {}".format(table_num, table_num2))
        input (guess)
        
    # If the user chooses division
    elif choose == "division":
        print("Question: {} / {}".format(div_num, table_num))
        input (guess)


guess = ""

while guess != answer and guesses_left >= 1:

    guess = int(input("Guess: ")) # replace this with function

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("You already guessed that number! Please try again. You *still* have {} guesses left.".format(guesses_left, already_guessed))
        continue

    guesses_left -=1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < answer:
            print("Your response is lower than the answer, sorry! Guesses left: {}".format(guesses_left, already_guessed))

        elif guess > answer:
            print("Your response is higher than the answer, sorry! Guesses left: {}".format(guesses_left, already_guessed))

    else:
        if guess < answer:
            print("Sorry, that's wrong!")

        elif guess > answer:
            print("Sorry, that's wrong!")
if guess == answer:
    if guesses_left == GUESSES_ALLOWED - 1:
        print("Amazing! You got it in one guess.")
    else:
        print("Your response is correct, well played!")

game_summary = []


# input rounds played/won for testing
rounds_lost = 0
rounds_won = 5
rounds_played = 5


# Game statistics
rounds_won = rounds_played - rounds_lost

# ***** Calculate Game Stats *****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

print()
print("***** Math Quiz History *****")
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the nearest whole number
print("***** Quiz Statistics *****")
print("Win: {}, ({:.0f}%) \nLoss: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose))

# End of game statements
print()
print('**** End Quiz Summary ****')
print("Won: {} \t|\t Lost: {}".format(rounds_won, rounds_lost))
print()
print ("Thanks for playing!")