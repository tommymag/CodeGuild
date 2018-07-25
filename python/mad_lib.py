noun1 = input("Give me a plural noun: ")
place = input("Give me a place: ")
verb = input("Give me a verb: ")
adjective1 = input("Give me an adjective: ")
adjective2 = input("Finally one more adjective: ")

print("I have eaten the '{}' that were in the '{}' and which you were probably saving for '{}'. Forgive me they were delicious so '{}'' and so '{}'.".format(noun1, place, verb, adjective1, adjective2))


# from random import shuffle
# def split_words(string):
#     word_list = string.split(', ')
#     shuffle(word_list)
#     return word_list

# playing = True
# x = 1
# while playing:
#     query = input("Press 1 to enter words, 2 to read story, 3 to exit: ")
#     if query == '1':
#         nouns = input('Enter three nouns seperated by commas: ')
#         adjective = input('Enter three adjective seperated by commas: ')
#         nouns_list = split_words(nouns)
#         nouns_list = split_words(nouns)
#     elif query == '2':
#     print('Hello: {}'.format(x))
#     x += 1

# nouns = input('Enter three nouns seperated by commas: ')
# adjective = input('Enter three adjective seperated by commas: ')

# nouns_list = split_words(nouns)
# print(nouns_list)

# story = 

# # Lab: madlib.py

# ------
# #### Goal

# Write a simple program that, when run, prompts the user for several inputs then
#  prints a [Mad Lib](https://en.wikipedia.org/wiki/Mad_Libs) as the result.

# -------
# #### Instructions

#   1. Search the interwebs for an example Mad Lib
#   1. Open Atom
#   1. Create a new file and save it as `madlib.py`

# Example:

# ```
# >>> Give me an antonym for 'data': nonmaterial
# >>> Tell me an adjective: Bearded
# >>> Give me a sciency buzzword: half-stack
# >>> A type of animal (plural): parrots
# >>> Some Sciency thing: warp drive
# >>> Another sciency thing: Trilithium crystals
# >>> Sciency adjective: biochemical
# ...
# >>> Nonmaterial Scientist Job Description:
# >>> Seeking a bearded engineer, able to work on half-stack projects with a team of parrots.
# >>> Key responsibilities:
# >>> - Extract patterns from non-material
# >>> - Optimize warp drive
# >>> - Transform trilithium crystals into biochemical material.
# ```
# ------


# #### Documentation

# 1. [Common string operations](https://docs.python.org/3.1/library/string.html)

# -------

# #### Advanced
# * Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.
# * Add randomness! Use the random module, rather than selecting which adjective goes where in the story.


# #### Super Advanced
# * Not satisfied yet? Make it a repeatable game. Once you're done prompting the user for words, prompt them for whether they'd like to hear the story. Use a while loop to keep asking if they'd like to hear the story again until the answer is 'no'. You could then ask them if they'd like to make another story, and so on.

# #### Key Concepts

# - Variables
# - String formatting¹
# - Handling user input