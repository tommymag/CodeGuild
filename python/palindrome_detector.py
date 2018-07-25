# GOAL
# Write a program that, when given a word or phrase, returns True if it is a Palindrome, and returns 
# False if it is not.

# INSTRUCTIONS
# You will be writing a program that analyzes a string for whether it’s a palindrome.
# Reformat the string so that it only contains characters.
# If the string is a palindrome, return True, if not, return False.
# Hint: Utilize the ‘alien smiley’ [::-1] to reverse the string.

# DOCUMENTATION
# Python Official Docs: .replace()
# Python official docs: string constants

def word_check():
	while True:
		print("Welcome to The Pal Detector!!!\n")
		while True:
			try:
				urword = input("Is the word your Pal?: ")
				if len(urword) > 2:
					break
				else:
					raise ValueError
			except ValueError:
				print("\nTo have a Pal we will need more characters!\n")
		print(is_pal(urword))

		play_again = input("Would you like to detect again?: ").strip()
		if play_again[:1] == "n" or "N":
			break			

def is_pal(urword):
	list_of_chars = list(urword)
	if list_of_chars == list_of_chars[::-1]:
		return True
	return False

		# while True:
		# 	try:


		# if urword[::-1] == urword:

word_check()













