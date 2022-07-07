import random
import math


# Lists of valid responses (test, do NOT ADD IN COMPONENT)
yes_no_list = ["yes", "no"]
equation_list = ["addition", "subtraction", "multiplication", "division", "xxx"]



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

# Testing to generate the numbers for the equation
for item in range (0, 12):
    chosen_num = random.randint(1, 100)
    table_num = random.randint(1, 12)


    choose_instruction = "Please choose addition, subtraction, multiplication, division or 'xxx' to exit "
    print()
    choose_error = ("{} or 'xxx' to end: ".format(choose_instruction))

    # ask user for choice and check it's valid
    choose = choice_checker(choose_instruction, equation_list, choose_error)
    if choose == "xxx":
        break

    # If the user chooses addition
    if choose_instruction == "addition":
        print("Question: {} + {}".format(chosen_num, chosen_num))

    # If the user chooses subtraction
    elif choose_instruction == "subtraction":
        print("Question: {} - {}".format(chosen_num, chosen_num))

    # If the user chooses multiplication
    elif choose_instruction == "multiplication":
        print("Question: {} * {}".format(chosen_num, table_num))
        
    # If the user chooses division
    elif choose_instruction == "division":
        print("Question: {} / {}".format(chosen_num, table_num))
