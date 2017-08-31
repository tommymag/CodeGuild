# def coin_return(cents):
#     quarters = 0
#     dimes = 0
#     nickels = 0
#     if cents >= 25:
#         quarters = cents // 25
#         cents = cents % 25
#     if cents >= 10:
#         dimes = cents // 10
#         cents = cents % 10
#     if cents >= 5:
#         nickels = cents // 5
#         cents = cents % 5
# return "You need: {} quarters, {} dimes, {} nickels, {} pennies".format(quarters, dimes, nickels, cents)

# *   Ask for the amount of change to dispense _in cents_.

change_due = int(input("How much change is owed: "))
q = 0
d = 0
n = 0
p = 0
while change_due > 0:
#     Assume that the amount input will be less than 100 cents.
    
# *   Calculate the number of quarters necessary first.
    if change_due >= 25:
        change_due -= 25
        q += 1
    elif change_due >= 10:
        change_due>= 10:
        d += 1
    elif change_due >= 5:
        change_due -= 5:
        n += 1
        else:
else:
    p += change_due
    break

print('Your change is {}q, {} d, {} n, {} p.'.format(q, d, n, p))


# *   Then calculate the number of dimes, nickels, and pennies.
#     If you do it in that order, you will minimize the number of coins.

# This is easiest done by updating a _running total_ of number of cents left to be put into coins.

# Also remember that the `//` operator divides and removes any remainder.

# ------------------

# #### Documentation

# ##### [Python Official Docs: Operators](https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions)

# -----------------

# #### Advanced

# * Expand this problem to work on an amount of cents greater than 100 and include bills.
# * Print out the total number of coins and bills dispensed.

# --------------------
# #### Super Advanced

# * Store how many of each coin is in the cash register, then allow the change algorithm to deal with when you don't have enough coins to optimally give change.

# ------------------

# #### Key Concepts

# - Operators
# - Variables
# - Data Types
# - PEP8