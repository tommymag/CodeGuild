# user_word = input("What word would you like translated to Pig Latin? ")

# first_letter = user_word[0]
# suffix = user_word[1:]

# if first_letter in 'aeiou':
#     print(user_word + 'yay')
# elif first_letter in 'bcdfghjklmnpqrstvwxyz':
#     print(suffix + first_letter + 'ay')

# # Practice: Pig Latin

# ###### Delivery Method: Prompt Only

# ------------------------------

# #### Goal

# Create a program asks for a _single_ English word and translates it to **Pig Latin**.
# It prints out the input word and the resulting translation like the example below.

# ---------------------------------

# #### Instructions

# 1. If the first letter is a consonant, move it to the end.
# 1. Add "ay" to the end of that.
# 1. If the first letter is a vowel, just ad "yay" to the end.

# ```
# > Word? hat
# >
# > hat in Pig Latin is athay
# >
# > Word? apple
# >
# > apple in Pig Latin is appleyay
# ```

# -----------------------------------

# #### Advanced

# Properly maintain the position of capitalization and punctuation.

# ```
# > Word? Cat
# >
# > Cat in Pig Latin is Atcay
# >
# > Word? hat.
# >
# > hat. in Pig Latin is athay.
# ```

# --------------------------------------

# #### Super Advanced

# Handle words that start with multiple consonants by moving all of the consonants
#  to the end.

# ```
# > Word? string
# >
# > string in Pig Latin is ingstray
# ```

# here is how we did it in class

def pig_latin():
    word = input('What word would you like translated?: ')
    first_letter = word[0]
    left_over = word[1:]

    vowels = 'aeiou'

    if first_letter.lower() in vowels:
        return '{}yay'.format(word)
    else:
        return '{}{}ay'.format(left_over, first_letter)

print(pig_latin())
