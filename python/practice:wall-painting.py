# All our friends are re-painting one wall of their rooms.
# They want us to figure out how much it’s going to cost.
# Assume one gallon of paint covers 400 square feet.

# Ask the user for:

# Width of the wall
# Height of the wall
# How much a gallon of paint costs
# Figure out then print how much it will cost to paint the wall with one coat.

import math

def cost_to_paint():

    width = int(input("Overall, just how much wall are we talking here?? \nWidth: "))
    height = int(input("Height: "))
    pp = float(input("How much is a gallon of your paint going for?: "))

    gallons_needed = math.ceil((width * height)/400)

    # print(gallons_needed)

    answer = "{:.2f}".format(gallons_needed * pp)


    print("$", answer)


#  need help with data type and rounding

cost_to_paint()

