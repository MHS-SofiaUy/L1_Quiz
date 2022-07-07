import random

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