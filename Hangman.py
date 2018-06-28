# Let’s write a program to play a game of hangman. In the data folder, you’ll find english.txt which contains a list of
# several thousand english words. Write a function load_words(path) which reads the text from this file and return a list
#  of strings which are greater than 5 letters. Randomly pick a word from that list and begin the game. Allow the user 10
# tries to guess the letters of the word. Keep track of the letters the user has already guessed.
#
# Show them a list of ‘blanks’ and ask them for a letter. If they guess a letter which is in the word, show the blanks with
#  the letters filled in. If they guess a letter which is not in the word, tell them and subtract 1 from their remaining
#  guesses. If they guess a letter they’ve guessed before, tell them and do not subtract 1 from their guesses.
#
# Be kind, if the user can’t guess the word in the number of allotted guesses, print the word and ask them if they’d like to play again.
#
# Feel free to customize the user interface, but provide these minimum features. Below is an example run of the program.
#
# _ _ _ _ _ _ _ _ _
# # of guesses remaining: 10
# already guessed:
#
# Guess a letter: a
# _ a _ _ _ _ a _ _
# # of guesses remaining: 10
# already guessed: a
#
# Guess a letter: a
# You've already guessed that
# _ a _ _ _ _ a _ _
# # of guesses remaining: 10
# already guessed: a
#
# Guess a letter: k
# _ a _ _ _ _ a _ _
# # of guesses remaining: 9
# already guessed: a, k
# Guess a letter:

import random

def load_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        wl = []
        for word in f.readlines():
            word = word.replace('\n', '')
            if len(word) > 5:
                wl.append(word)
        # for word in f.readlines():
        #     if word[:1] == a:
        #         wl.append(word)
    return wl

def to_select(word_list):
    return random.choice(word_list)

def dash_creator(word, guesses):
    blank = "_"
    new_word = ""
    for letter in word:
        if letter in guesses:
            new_word += letter
        else:
            new_word += blank
    return new_word

def main():
    word_list = load_words("english.txt")

    word = to_select(word_list)
    print(dash_creator(word, ["a", "e", "i", "o", "u", "y"]))

main()












































