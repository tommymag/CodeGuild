# Create a program that uses a dictionary to store phonebook
# entries. Must have user interaction.
# Include ability to:
# 1. Search
# 2. Add Entry
# 3. Change Entry
# 4. Delete Entry
# 5. Exit Program

# phone_book = {
#     'Thomas': {'Surname': 'Magnuson',
#                 'phone_number': '5033322579',
#                 'Phrase': 'Never give up!'},
#     'Kieran': {'Surname': 'Nareik',
#                 'phone_number': '8456331959',
#                 'Phrase': 'Good code is not written, it\'s re-written.'},
#     'Lambda': {'Surname': 'Yoga',
#                  'phone_number': '8454185633',
#                  'Phrase': 'I am a machine.'},
#     'Vu': {'Surname': 'Pham',
#             'phone_number': '5037891234',
#             'Phrase': 'Is it OK to talk to girl at grocery store?!'}
# }


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
                for key, value in phone_book[name].items():
                    if key == 'phone_number':
                        print(value[0:3] + "-" + value[3:6] + "-" + value[6:10])
                    else:
                        print(key + ': ' + value)
            except KeyError:
                print("Sorry... phonebook doesn't know {}".format(name))
            print("\nAnything else?")
        elif menu == "2":
            name = input("Enter a name to add to your phonebook: ")
            Surname = input("Family or last name: ")
            phone_number = input("Enter their number: ")
            Phrase = input("Phrase to remember them by: ")
            phone_book[name] = {'Surname': Surname, 'phone_number': phone_number, 'Phrase': Phrase}
            print(name + " added to phonebook with the number: " + phone_number + "\n")
            print("Anything Else?")
        elif menu == "3":
            while True:
                try:
                    name = input("Which name do you want to change?: ")
                    phone_book[name]
                    break
                except KeyError:
                    print("Who?!")
            name_change = input("What is their new name?: ")
            p_info = phone_book[name]
            del phone_book[name]
            phone_book[name_change] = p_info
            print("\nAnything else?")
        elif menu == "4":
            while True:
                try:
                    name = input("Which name would you like to delete?: ")
                    phone_book[name]
                    break
                except KeyError:
                    print("Who?!")
            del phone_book[name]
            print("{} has been deleted.\n".format(name))
            print("Anything else?")
        elif menu == "5":
            print("\nGoodbye!\n")
            quit()
phonebook()

















