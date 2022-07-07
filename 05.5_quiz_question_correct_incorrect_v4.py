import random
# from this import d
# code
# try get all division questions to integers

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


def int_check(question, low=None, high=None):

    situation = ""

    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"

    while True:
       
        try:
            response = int(input(question))

            # checks input is not too high or too low if both upper and lower bounds are specifies
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue

            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please print a number that is more than (or equal to) {}".format(low))
                    continue

            return response

        # checks input is an integer
        except ValueError:
            print("Please enter an integer")
            continue


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
    table_num = random.randint(1, 12)
    table_num2 = random.randint(1, 12)
    ans = table_num * table_num2

    choose_instruction = "Please choose addition, subtraction, multiplication, division or 'xxx' to exit "
    print()
    choose_error = ("{} or 'xxx' to end: ".format(choose_instruction))


    # ask user for choice and check it's valid
    choose = choice_checker(choose_instruction, equation_list, choose_error)
    if choose == "xxx":
        break

    # If the user chooses addition
    if choose == "addition":
        answer = int_check("Question: {} + {}  = ".format(chosen_num, chosen_num2))
        actual_ans = chosen_num + chosen_num2


    # If the user chooses subtraction
    elif choose == "subtraction":
        answer = int_check("Question: {} - {}  = ".format(chosen_num, chosen_num2))
        actual_ans = chosen_num - chosen_num2

    # If the user chooses multiplication
    elif choose == "multiplication":
        answer = int_check("Question: {} * {}  = ".format(table_num, table_num2))
        actual_ans = table_num * table_num2
        
    # If the user chooses division
    elif choose == "division":
        answer = int_check("Question: {} / {}  = ".format(ans, table_num2))
        actual_ans = ans / table_num2

    # compare user's input answer to the actual answer
    if answer == actual_ans:
        print("That's the correct answer. Well played.")
    else:
        print("User Response: {}".format(answer))
        print("Correct Answer: {}".format(actual_ans))
        print("No that's wrong!")

    play_again = yes_no("Would you like to play again? ")