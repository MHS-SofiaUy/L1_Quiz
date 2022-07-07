import random
# code

# Functions go here
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
            print ("Please answer yes / no")

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


# Lists of valid responses (test, do NOT ADD IN COMPONENT)
yes_no_list = ["yes", "no"]
equation_list = ["addition", "subtraction", "multiplication", "division", "xxx"]
GUESSES_ALLOWED = 3
response = ""

already_guessed = []
guesses_left = GUESSES_ALLOWED
play_again = "yes"

# Testing to generate the numbers for the equation
while play_again == "yes":
    chosen_num = random.randint(1, 100)
    chosen_num2 = random.randint(1, 100)
    table_num = random.randint(0, 12)
    table_num2 = random.randint(0, 12)

    choose_instruction = "Please choose addition, subtraction, multiplication, division or 'xxx' to exit "
    print()
    choose_error = ("{} or 'xxx' to end: ".format(choose_instruction))


    # ask user for choice and check it's valid
    choose = choice_checker(choose_instruction, equation_list, choose_error)
    if choose == "xxx":
        break

    # If the user chooses addition
    if choose == "addition":
        input("Question: {} + {}".format(chosen_num, chosen_num2))
        actual_ans = chosen_num + chosen_num2


    # If the user chooses subtraction
    elif choose == "subtraction":
        input("Question: {} - {}".format(chosen_num, chosen_num2))


    # If the user chooses multiplication
    elif choose == "multiplication":
        input("Question: {} * {}".format(table_num, table_num2))

        
    # If the user chooses division
    elif choose == "division":
        input("Question: {} / {}".format(chosen_num, table_num))

   
    # to get answer
    answer = ""

    # # when answer
    # while input != answer and guesses_left >=1:

    #     if input < answer:
    #         print ("sorry your answer is too low")

    #     elif input > answer:
    #         print ("sorry your answer is too high")

    #     elif input == answer:
    #         print ("you are correct")

    play_again = yes_no("Would you like to play again?")
