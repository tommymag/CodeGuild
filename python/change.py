
quarters = 0
dimes = 0
nickels = 0
pennies = 0

change = int(input("How much change?: "))

while change > 0:
    if change - 25 >= 0:
        quarters += 1
        change -= 25
    elif change - 10 >= 0:
        change -= 10
        dimes += 1
    elif change - 5 >= 0:
        change -= 5
        nickels += 1
    elif change >= 0:
        change -= 1
        pennies += 1

print("You will receive {} quarters, {} dimes, {} nickels and {} pennies".format(quarters, dimes, nickels, pennies))


#
#
# print("You have {}Q, {}D, {}N and {}P".format(quartes, dimes, nickels, pennies))
#
#
# 99 if 99 - 25 > 0
#



    #     if change < 25:
    #         change // 10 = dimes
    #     elif change > 5:
    #         change // 5 = nickels
    # else:
    #     change // 25 = quarters
    # while change > 0 and change <25:
    #     change // 10 = dimes
    # elif change > 5:
    #         change // 5 = nickels











# # Lab: Change Return
#
# ###### Delivery Method: Doctests
#
# ------------------------------
#
# ##### Goal
#
# Write a python script that figures out how to divvy up an amount of change into the _fewest_ quarters, dimes, nickels, and pennies.
#
# ---------------------------------------------------------
#
# ##### Instructions
#
# Some supermarkets have automatic change dispensers.
#
# *   Ask for the amount of change to dispense _in cents_.
#     Assume that the amount input will be less than 100 cents.
#
# *   Calculate the number of quarters necessary first.
#
# *   Then calculate the number of dimes, nickels, and pennies.
#     If you do it in that order, you will minimize the number of coins.
#
# This is easiest done by updating a _running total_ of number of cents left to be put into coins.
#
# Also remember that the `//` operator divides and removes any remainder.

# ------------------

# get change from the user

# #  assign values
#
# quarter = 0
# dime = 0
# nickel = 0
# penny = 0
#
# change = int(input("How much change?: "))
#
# while change > 0:
#     if change >= 25:
#         change -= 25
#         quarter += 1
#     elif change >= 10:
#         change >= 10
#         dime += 1
#     elif changee >= 5:
#         change -= 5
#         nickel += 1
#     else:
#         penny += change
#         break

    # print('Your change is {} quarters, {} dimes, {} nickels, {} pennies.'.format(quarter, dime, nickel, penny))

#
#
#
#
# #### Documentation
#
# ##### [Python Official Docs: Operators](https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions)
#
#
# change_due = int(input("How much change is owed: "))
# q = 0
# d = 0
# n = 0
# p = 0
# while change_due > 0:
# #     Assume that the amount input will be less than 100 cents.
#
# # *   Calculate the number of quarters necessary first.
#     if change_due >= 25:
#         change_due -= 25
#         q += 1
#     elif change_due >= 10:
#         change_due>= 10:
#         d += 1
#     elif change_due >= 5:
#         change_due -= 5:
#         n += 1
#         else:
# else:
#     p += change_due
#     break
#
# print('Your change is {}q, {} d, {} n, {} p.'.format(q, d, n, p))
#
#
# # *   Then calculate the number of dimes, nickels, and pennies.
# #     If you do it in that order, you will minimize the number of coins.
#
# # This is easiest done by updating a _running total_ of number of cents left to be put into coins.
#
# # Also remember that the `//` operator divides and removes any remainder.
#
# # ------------------
#
# # #### Documentation
#
# # ##### [Python Official Docs: Operators](https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions)
#
# # -----------------
#
# # #### Advanced
#
# # * Expand this problem to work on an amount of cents greater than 100 and include bills.
# # * Print out the total number of coins and bills dispensed.
#
# # --------------------
# # #### Super Advanced
#
# # * Store how many of each coin is in the cash register, then allow the change algorithm to deal with when you don't have enough coins to optimally give change.
#
# # ------------------
#
# # #### Key Concepts
#
# # - Operators
# # - Variables
# # - Data Types
# - PEP8