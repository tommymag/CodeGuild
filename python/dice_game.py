# Write a simple program that, when run, prompts the user for input then prints a result.
# Program should ask the user for the number of dice they want to roll as well as the number of sides per die.
# 1. Create a new file and save it as `dice_game.py`

# 1. [Compound statements](https://docs.python.org/3/reference/compound_stmts.html)
# 1. [Python Std. Library: Random Module random.randint()](https://docs.python.org/3/library/random.html#random.randint)


# - Importing
# - The Random Module
# - `for` looping
# - `input()` function
# - programmatic logic

from random import randint
print("Welcome to the dice game!")

user_amt = int(input("How many dice would you like to roll?: "))
sides = int(input("How many side to your die?: "))

for roll in range(user_amt):
    print("You rolled ", randint(1, sides))