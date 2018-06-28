# Write a function that returns the meal for any given hour of the day or night in respect to the following schedule:
#
# Breakfast: 7AM - 9AM
# Lunch: 12PM - 2PM
# Dinner: 7PM - 9PM
# Hammer: 10PM - 4AM

def HammerTime():
    user_var = input("What time is it?")
    if user_var in ["7AM", "8AM", "9AM"]:
        print("Breakfast")
    if user_var in ["10AM", "11AM"]:
        print("Wasn't breakfast enough?? It isn't lunch time yet!")
    if user_var in ["12PM", "1PM", "2PM"]:
        print("Lunch Time!")
    if user_var in ["3PM", "4PM", "5PM", "6PM"]:
        print("It isn't Dinner yet... Go back outside and play!")
    if user_var in ["7PM", "8PM", "9PM"]:
        print("Dinner is served!")
    if user_var in ["10PM", "11PM", "12AM", "1AM", "2AM", "3AM", "4AM"]:
        print("Hammer time!")
HammerTime()