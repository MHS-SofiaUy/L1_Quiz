# quiz component 5 - correct incorrect answer

# To Do
# set up empty list called already_guessed
# when user guesses, add that guess to list
# for each guess, check that number is not in already_guessed

ANSWER = 10
GUESSES_ALLOWED = 3

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != ANSWER and guesses_left >= 1:

    guess = int(input("Guess: ")) # replace this with function

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("You already guessed that number! Please try again. You *still* have {} guesses left.".format(guesses_left, already_guessed))
        continue

    guesses_left -=1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < ANSWER:
            print("Your response is lower than the answer, sorry! Guesses left: {}".format(guesses_left, already_guessed))

        elif guess > ANSWER:
            print("Your response is higher than the answer, sorry! Guesses left: {}".format(guesses_left, already_guessed))

    else:
        if guess < ANSWER:
            print("Sorry, that's wrong!")

        elif guess > ANSWER:
            print("Sorry, that's wrong!")
if guess == ANSWER:
    if guesses_left == GUESSES_ALLOWED - 1:
        print("Amazing! You got it in one guess.")
    else:
        print("Your response is correct, well played!")