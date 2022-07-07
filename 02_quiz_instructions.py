

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
    print ("- For each question, the user gets to choose which category the user wants to play with.")
    print ()
    print ("- After the user chooses the category of their choice, the computer will generate a random question from that category.")
    print ()
    print ("- When all the rounds are finished, or the user chooses to quit")
    print ("  The game will tally up the results and display the user's game statistics.")
    print ()
    print ("- We wish the user to have fun!~")
    return ""

# Main Routine goes here...

played_before = yes_no("Have you played this game before?")


if played_before == "no":
    instructions()

print("program continues")