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

# m = 0
# for x in [3, 5, 3]:
#    for y in range (10, 11):
#       m = m + x + y
# print(m)
#
#
#
# count = 20
# for x in range(0, 10):
#     count = count - 1
#     if x == 2:
#         break
# print(count)
#
#
# 0
#
# def greeting(name):
#     print('Hello, {}. How are you today?'.format(foo))
# my_name = input('What is your name?')
#
#
#


# target_word = input("enter possible palindrome: ")
# word_backward = ("".join(reversed(target_word)))
# print(target_word)
# print(word_backward)
# if word_backward == target_word:
#     print("Congratulations! You have a palindrome! ")
# else:
#     print("I'm so sorry. That's not a palindrome afterall.")

# # for string
# seqString = 'Python'
# print(list(reversed(seqString)))
#
# # for tuple
# seqTuple = ('P', 'y', 't', 'h', 'o', 'n')
# print(list(reversed(seqTuple)))
#
# # for range
# seqRange = range(5, 9)
# print(list(reversed(seqRange)))
#
# # for list
# seqList = [1, 2, 4, 3, 5]
# print(list(reversed(seqList)


#   Making text file of html :


# def list_creator(list_items, type='ul'):
#   lst = ''
#   for item in list_items:
#     lst += '<li>{}</li>'.format(item)
#   return '<{type}>{lst}</{type}>'.format(type=type, lst=lst)
#
# items = ['cats', 'dogs', 'ferret']
#
# with open('new.html', 'w') as f:
#   f.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Title</title></head><body>{}</body></html>\
# '.format(list_creator(items, 'ol')))

#
# '''Function definition and invocation.'''
#
# def happyBirthdayEmily():
#     print("Happy Birthday to you!")
#     print("Happy Birthday to you!")
#     print("Happy Birthday, dear Emily.")
#     print("Happy Birthday to you!")
#
# happyBirthdayEmily()
# happyBirthdayEmily()

# def happyBirthday(person):
#     print("Happy Birthday to you!")
#     print("Happy Birthday to you!")
#     print("Happy Birthday, dear " + person + ".")
#     print("Happy Birthday to you!")
#
# happyBirthday('Emily')
# happyBirthday('Andre')



# def mad_lib():
#     print("You are invited to a dinner party! Only problem is part of the invitation is sketch...\n" "Most of the important"
#           " words are smudged out.\n")
#     user_question = input("How about we fill in some options?: ")
#     if user_question == "y":
#         last_name = input("Eccentric last name of the hosting couple: ")
#         verb = input("Two verbs separated by commas: ")
#         plural_noun = input("Please give me a plural noun: ")
#         food = input("What are we eating?: ")
#         guest_of_honor = input("Who are we honoring?: ")
#         date = input("When is the party?: ")
#         location = input("Where is this bash taking place?: ")
#
#         print("Mr. and Mrs. {} cordially invite you for a night of {} and {} {}\n\n Serving: {} \n\n Honoring: {}
# \n\n Date: {} \n\n" "Location: {} \n\n Regrets only please \n\n Call: 867-5309 \n\n This party must be hosted by
# Tommy Tutone!!!".format(last_name,
#     verb, plural_noun, plural_noun, food, guest_of_honor, date, location,))
# mad_lib


def cost_to_paint():

    width = int(input("Overall, just how much wall are we talking here?? \nWidth: "))
    height = int(input("Height: "))
    pp = float(input("How much is a gallon of your paint going for?: "))

    gallons_needed = (width * height)/400

    gnr = gallons_needed.ceil()

    answer = str(gnr * pp)

    print(gr)

cost_to_paint()



















