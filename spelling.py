# # Lab: I before E except after C.
# From wikipedia:
# "The i before e except after c rule is not worth teaching. It applies only to words in which the ie or ei stands for a clear /ee/ sound and unless this is known, words such as 'sufficient', 'veil' and 'their' look like exceptions."
# Create a program that asks for a _single_ English word and checks if it follows the rule **"I before E except after C".**
# 1. Create a file named `spelling.py`
# 1. Write a function that searches for the index of any instances of `ie` in the string, then see if the preceding letter is `c`.
#### Documentation
# #### Advanced
# * Find a list of exceptions to use and check if the word given is an exception to the rule.
# #### Key Concepts
# - string lookup with `in`

exceptions = open("exception_list.txt", "r")

readable = exceptions.read()

exceptions.close()

useable = readable.split()

word = input("What is the single english word you would like checked?: ")

def word_check(word_arg):
    if word_arg in useable:
        print("This is an exception to the rule!")
    elif "ie" in word_arg and "cie" not in word_arg:
        print("This follows the rule, I before E!")
    elif "cei" in word_arg:
        print("This follows the rule, 'except after C!'")
    else:
        print("Cool word bro! FYI... did you mistake the word?")
word_check(word)

# turn a text file into a list of words python

# Kasey code:

# def i_b4_e(word):
#     word = word.lower()
#     with open('i_e_exceptions.txt', 'r') as file:
#         exceptions = file.read().replace('\n', ' ').split()
#     if 'i' in word and word not in exceptions:
#         for i in range(1, len(word)):
#             if word[i] == 'i' and (word[i-1] == 'e' or word[i+1] == 'e'):
#                 if word[i+1] == 'e' and word[i-1] == 'c':
#                     return False
#                 else:
#                     return True
#     else:
#         return True
#
#
# def c_grammar():
#     g_check = input('Enter a word: ')
#     if i_b4_e(g_check):
#         print('Good job!')
#     else:
#         print('Remember, i before e except after c, or when sounding like A, as in neighbour or weigh!')
#
# c_grammar()