# Create a program that uses a dictionary to store phonebook
# entries. Must have user interaction.
# Include ability to:
# 1. Search
# 2. Add Entry
# 3. Change Entry
# 4. Delete Entry
# 5. Exit Program

phone_book = {
    'Thomas Magnuson': '5033322579'
}


def phonebook():
    while True:
        menu = input("""
                       1. Search
                       2. Add Entry
                       3. Change Entry
                       4. Delete Entry
                       5. Exit Program
                       Please choose from menu: """)
        if menu == "1":
            name = input("What is the name?: ")
            try:
                print(phone_book[name])
            except KeyError:
                print("phonebook doesn't know {}".format(name))
            print("Anything Else?")
        elif menu == "2":
            name = input("Enter a name to add to your phonebook: ")
            number = input("Enter their number: ")
            phone_book[name] = number
            print(name + " added to phonebook with the number: " + number)
            print("Anything Else?")
            # print(phone_book) I would take this out.  It's just to test.
            pass
        elif menu == "3":
            name = input("Which name do you want to change?: ")
            name_change = input("What is their new name?: ")
            number = phone_book[name]
            del phone_book[name]
            phone_book[name_change] = number
            pass
        elif menu == "4":
            name = input("Which name would you like to delete?: ")
            del phone_book[name]
            pass
        elif menu == "5":
            quit()
phonebook()



