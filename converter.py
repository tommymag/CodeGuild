# # Lab: Distance Converter

# ###### Delivery Method: Prompt Only

# --------------

# ##### Goal

# Write a function to convert between `mi`, `km`, `ft`, and `m`.

# --------------------

# ##### Instructions

# Ask the user for a distance, then the units of that distance, then the target units.
# Then print out the conversion as below.

# print("Enter a distance: ")
# length = int(input())
# print("Enter units: ")
# orig_unit = input()
# print("Enter target units: ")
# to_unit = input()
# something = ''
#
# def converter(length, orig_unit, to_unit):
#     if orig_unit == 'mi':
#         if to_unit == 'km':
#             something = length * 1.60934
#         elif to_unit == 'm':
#             something = length * 1609.34
#         elif to_unit == 'ft':
#             something = length * 5280
#
#
#     if orig_unit == 'km':
#         if to_unit == 'mi':
#             something = length * 0.621371
#         elif to_unit == 'm':
#             something = length * 1000
#         elif to_unit == 'ft':
#             something =  length * 3280.84
#
#     if orig_unit == 'm':
#         if to_unit == 'mi':
#             something = length * 0.000621371
#         elif to_unit == 'km':
#             something = length * 0.621371
#         elif to_unit == 'ft':
#             something = length * 3280.84
#
#     if orig_unit == 'ft':
#         if to_unit == 'mi':
#             something = length * 0.000189394
#         elif to_unit == 'km':
#             something = length * 0.0003048
#         elif to_unit == 'm':
#             something = length * 0.3048
#
#     return something
#
# print(converter(length, orig_unit, to_unit))
# print(something)


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
#
# def unit_convert(): # Distance conversion function assignment.
#     while True:
#         orig_value = float(input("Enter a distance: "))
#         input_unit = str(input("What unit are you starting with (mi, km, m, or ft)? "))
#         output_unit = str(input("What would you like to convert to (mi, km, m, or ft)? "))
#         # Create conditions for input and output for all scenarios
#         if input_unit == 'mi':
#             if output_unit == 'km': #miles to kilometers
#                 conv_fac = 1.609344 #conversion factor
#                 output_value = float(orig_value) * conv_fac
#                 print (f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'm': #miles to meters
#                 conv_fac = 0.000621371192 #conversion factor
#                 output_value = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'ft': #miles to feet
#                 conv_fac = 5280 #conversion factor
#                 output_value = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#         elif input_unit == 'km':
#             if output_unit == 'mi': #kilometers to miles
#                 conv_fac = .621371 #conversion factor
#                 output_value = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'm': #kilometers to meters
#                 conv_fac = 1000 #conversion factor
#                 output_uvalue = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'ft': #kilometers to feet
#                 conv_fac = 3280.84 #conversion factor
#                 output_value = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#         elif input_unit == 'm':
#             if output_unit == 'km': #meters to kilometers
#                 conv_fac = .001 #conversion factor
#                 output_unit = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'mi': #meters to miles
#                 conv_fac = .000621371 #conversion factor
#                 output_unit = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'ft': #meters to feet
#                 conv_fac = 3.28084 #conversion factor
#                 output_unit = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#         elif input_unit == 'ft':
#             if output_unit == 'km': #feet to kilometers
#                 conv_fac = .0003048000097536 #conversion factor
#                 output_unit = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'mi': #feet to miles
#                 conv_fac = 0.00018939394545454545809 #conversion factor
#                 output_unit = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'm': #feet to meters
#                 conv_fac = 0.3048000097535999986 #conversion factor
#                 output_unit = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#         else:
#             print("Something went wrong. Shall we try again?")
# unit_convert()