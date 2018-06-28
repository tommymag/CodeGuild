# Print a welcome screen to the user.
# Use the random module’s random.choice() to choose a prediction.
# Prompt the user to ask the 8-ball a question “will I win the lottery tomorrow?”
# Display the result of the 8-ball.
# Below are some example ‘predictions’:
#
# It is certain
# It is decidedly so
# Without a doubt
# Yes definitely
# You may rely on it
# As I see it, yes
# Most likely
# Outlook good
# Yes
# Signs point to yes
# Reply hazy try again
# Ask again later
# Better not tell you now
# Cannot predict now
# Concentrate and ask again
# Don’t count on it
# My reply is no
# My sources say no
# Outlook not so good
# Very doubtful

import random

print("Welcome to the all-knowing, semi-automated, non magical 8-ball fortune teller!")

def MagicEightBall():
    user_question = input("What would you like to know?: ")
    options = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it",
             "As I see it, yes", "Most likely", "Outlook good" "Yes", "Signs point to yes", "Reply hazy try again",
             "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
             "Don’t count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
    print(random.choice(options))
MagicEightBall()











































