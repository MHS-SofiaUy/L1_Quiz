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