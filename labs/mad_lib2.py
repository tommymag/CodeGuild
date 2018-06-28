def mad_lib():
    print("You are invited to a dinner party! Only problem is part of the invitation is sketch...\n" "Most of the important"
          " words are smudged out.\n")
    user_question = input("How about we fill in some options?: ")
    if user_question in ["y"[:1], "Y"[:1], "ok", "OK", "Ok"]:
        last_name = input("Eccentric last name of the hosting couple: ")
        verb = input("Two verbs separated by commas: ")
        plural_noun = input("Please give me a plural noun: ")
        food = input("What are we eating?: ")
        guest_of_honor = input("Who are we honoring?: ")
        date = input("When is the party?: ")
        location = input("Where is this bash taking place?: ")
        print("Mr. and Mrs. {} cordially invite you for a night of {} and {} {}\n\n Serving: {} \n\n Honoring: {}\n\n Date: {} \n\n"
          "Location: {} \n\n Regrets only please \n\n Call: 867-5309 \n\n This party must be hosted by Tommy Tutone!!!"
              .format(last_name, verb, plural_noun, food, guest_of_honor, date, location))
    else:
        print("Fine then... You probably aren't fun at parties anyway!")
mad_lib()