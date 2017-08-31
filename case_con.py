# # Lab: Case Conversion

# Write a program that prompts the user for a word.
# Print out either  `snake_case` or `CamelCase` depending case convention it is!.

# ##### Instructions

# Use substring membership with the `in` operator

# 1. [PEP8](https://www.python.org/dev/peps/pep-0008/)
# 1. [Stack Overflow](http://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function-names)

# - Python social conventions for variable and function naming

case = input("What word would you like checked?: ")

for stuff in case:
    if stuff.isupper():
        print("This is CamelCase!")
        break
    elif stuff == "_":
        print("This is snake case")
        break