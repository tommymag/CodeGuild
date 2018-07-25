

# Let’s convert a number grade to a letter grade, using if and elif statements and comparisons.

# Have the user enter a number representing the grade (0-100)
# Convert the number grade to a letter grade
# NUMERIC RANGES
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F


def grading_score():
    user_score = int(input("Hello student.\n\nWhat is the score you would like evaluated?: "))
    if user_score > 100:
        print("\nC'mon man!")
    elif 100 >= user_score >= 90:
        print("\nWay to go! That's an A!")
    elif user_score >= 80:
        print("\nYou get a B")
    elif user_score >= 70:
        print("\nYou got a C")
    elif user_score >= 60:
        print("\nYou get a D...")
    elif user_score < 60:
        print("\nYou get the F outta here!!!")
    else:
        print("WTH")
grading_score()













