# # Lab: Distance Converter

# ###### Delivery Method: Prompt Only

# --------------

# ##### Goal

# Write a function to convert between `mi`, `km`, `ft`, and `m`.

# --------------------

# ##### Instructions

# Ask the user for a distance, then the units of that distance, then the target units.
# Then print out the conversion as below.

print("Enter a distance: ")
length = int(input())
print("Enter units: ")
orig_unit = input()
print("Enter target units: ")
to_unit = input()
something = ''

def converter(length, orig_unit, to_unit):
    if orig_unit == 'mi':
        if to_unit == 'km':
            something = length * 1.60934
        elif to_unit == 'm':
            something = length * 1609.34
        elif to_unit == 'ft':
            something = length * 5280


    if orig_unit == 'km':
        if to_unit == 'mi':
            something = length * 0.621371
        elif to_unit == 'm':
            something = length * 1000
        elif to_unit == 'ft':
            something =  length * 3280.84

    if orig_unit == 'm':
        if to_unit == 'mi':
            something = length * 0.000621371
        elif to_unit == 'km':
            something = length * 0.621371
        elif to_unit == 'ft':
            something = length * 3280.84

    if orig_unit == 'ft':
        if to_unit == 'mi':
            something = length * 0.000189394
        elif to_unit == 'km':
            something = length * 0.0003048
        elif to_unit == 'm':
            something = length * 0.3048

    return something

print(converter(length, orig_unit, to_unit))
print(something)


# ```
# > Enter a distance:
# > 100
# > Enter units:
# > mi
# > Enter target units:
# > km
# > 100 mi is 160.93440000000115 km
# ```

# Support converting between `mi`, `km`, `ft`, and `m`.


# -------------------

# #### Documentation

# 1. [Python Official: Built-In Functions](https://docs.python.org/3.6/library/functions.html)

# 1. [Python Official: Operators](https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions)

# ----------------------


# ## Advanced

# *   Also support converting between `in` and `cm`.

# *   Also support converting between `gal` and `L`.
#     Error if someone tries to convert between volume and distance. Use `raise`.

# -------------------


# ## Super Advanced

# * Also support converting between all [metric prefixes](https://en.wikipedia.org/wiki/Metric_prefix) of meters.


# ------------------------
# #### Key Concepts

# - Variables
# - Function definition
# - User input
# - Built-In functions
# - Logic Problems
# Add Comment Col