#
#  Wage problem from edx
#
# n = int(input("How many hours did you work this week?: "))
#
#
# if n < 0 or n > 168:
#     print("INVALID")
#
# if n <= 40:
#     print("You made", n * 8, "dollars this week!")
# elif n >= 41 and n <= 50:
#     print("You made", ((n-40) *9) + 320, "dollars this week!")
# elif n >= 51 or n <= 168:
#     print("You made", ((n-50) * 10) + 410, "dollars this week!")


# days problem from edx

# Write a program that asks the user to enter a positive integer n. Assuming that this integer is in seconds, your program should convert the number of seconds into days, hours, minutes, and seconds and prints them exactly in the format specified below. Here are a few sample runs of what your program is supposed to do:

# 369121517 = 4272 days 5 hours 45 minutes 17 seconds

# def time(days)

# n = int(input("How many seconds would you like calculated to time?: "))

# user_response = input("How many seconds would you like calculated to time?: ")
# given_seconds = int(user_response)
# # Calculate the days
# days = given_seconds//(24*60*60)
# seconds_1 = given_seconds % (24*60*60)    # remaining seconds after we get days
#
# # Calculate the hours
# hours = seconds_1//(60*60)          # get the hours out of seconds_1
# seconds_2 = seconds_1 % (60*60)     # remaining seconds after we get hours
#
# # Calculate the minutes
# minutes = seconds_2 // 60           # get the minutes
#
# # Finally calculate the remaining seconds after we get the minutes
# seconds = seconds_2 % 60
#
# print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")
#



# x=0
# count=0
# while x <= 101:
#     if x%5==0:
#         count = count+x
#     x=x+1
# print(count)

# x = 1
# count = 0
# while x < 1001:
#     count = count +x
# #     x = x + 3
# # print(count)
#
# count = 20
# for x in range(0,10):
#     count = count - 1
#     if x == 2:
#         break
# print(count)

#
# lst = []
#
# for i in range (1, 21):
#     lst.append(i)
#
# print (lst)
#
# lst2 = [i for i in range (1, 21)]
#
# print(lst2)

# def recur_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return (recur_fibo(n - 1) + recur_fibo(n - 2))
#
# print([recur_fibo(f) for f in range(35)])
#
# python -m doctest -v tsting.py
#
# filename.py
#

m = 0
for x in [3,5,3]:
   for y in range (10,11):
      m = m + x + y
print (m)



count = 20
for x in range(0,10):
    count = count - 1
    if x == 2:
        break
print(count)


0












