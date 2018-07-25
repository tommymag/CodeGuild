# # Lab: Distance Converter

# ###### Delivery Method: Prompt Only

# --------------

# ##### Goal

# Write a function to convert between `mi`, `km`, `ft`, and `m`.

# --------------------

# ##### Instructions

# Ask the user for a distance, then the units of that distance, then the target units.
# Then print out the conversion as below.

def conversion():

    print("Enter a distance: ")
    length = int(input())
    print("Enter units: ")
    orig_unit = input()
    print("Enter target units: ")
    to_unit = input()

    if orig_unit == 'mi':
        if to_unit == 'km':
            answer = str(length * 1.60934) + "km"
        elif to_unit == 'm':
            answer = str(length * 1609.34) + "m"
        elif to_unit == 'ft':
            answer = str(length * 5280) + "ft"

    if orig_unit == 'km':
        if to_unit == 'mi':
            answer = str(length * 0.621371) + 'mi'
        elif to_unit == 'm':
            answer = str(length * 1000) + 'm'
        elif to_unit == 'ft':
            answer = str(length * 3280.84) + 'ft'

    if orig_unit == 'm':
        if to_unit == 'mi':
            answer = str(length * 0.000621371) + 'mi'
        elif to_unit == 'km':
            answer = str(length * 0.621371) + 'km'
        elif to_unit == 'ft':
            answer = str(length * 3280.84) + 'ft'

    if orig_unit == 'ft':
        if to_unit == 'mi':
            answer = str(length * 0.000189394) + 'mi'
        elif to_unit == 'km':
            answer = str(length * 0.0003048) + 'km'
        elif to_unit == 'm':
            answer = str(length * 0.3048) + 'm'

    print(answer)

conversion()



# DISTANCE CONVERTER
# LAB: DISTANCE CONVERTER
# DELIVERY METHOD: PROMPT ONLY
# GOAL
# Write a function to convert between mi, km, ft, and m.
#
# INSTRUCTIONS
# Ask the user for a distance, then the units of that distance, then the target units.
# Then print out the conversion as below.
#
# > Enter a distance:
# > 100
# > Enter units:
# > mi
# > Enter target units:
# > km
# > 100 mi is 160.93440000000115 km
# Support converting between mi, km, ft, and m.
#
# DOCUMENTATION
# Python Official: Built-In Functions
#
# Python Official: Operators
#
# ADVANCED
# Also support converting between in and cm.
#
# Also support converting between gal and L.
# Error if someone tries to convert between volume and distance. Use raise.
#
# SUPER ADVANCED
# Also support converting between all metric prefixes of meters.
# KEY CONCEPTS
# Variables
# Function definition
# User input
# Built-In functions
# Logic Problems
