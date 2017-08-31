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

word = input("What is the single english word you would like checked?: ")

def word_check(word_arg):
    if "ie" in word_arg:
        print("This follows the rule, I before E!")
    elif "cei" in word_arg:
        print("This follows the rule, 'except after C!'")
    else:
        print("Cool word bro!")
word_check(word)