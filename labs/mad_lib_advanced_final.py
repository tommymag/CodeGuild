import random

def toms_mad_lib(person_in_room, nouns_string, adjective_string, plural_noun_string):

    # person_in_room = input("Give me the name of a person in the room: ")
    # nouns_string = input("Give me eight singular nouns with commas between them: ")
    # adjective_string = input("Give me three adjectives: ")
    verb_past_tense = input("Past tense verb please: ")
    # plural_noun_string = input("Now we need two plural nouns: ")
    # plural_noun_two = input("Another plural noun: ")
    number_one = input("Give me a basketball score: ")
    # adjective_two = input("Please provide an adjective: ")
    # adjective_three = input("Another adjective: ")
    # noun_two = input("Noun please: ")
    exclamation = input("Give me an exciting word!: ")
    # noun_three = input("Another noun please: ")
    person_in_room_two = input("The name of another person in the room: ")
    # noun_four = input("Another noun please: ")
    # noun_five = input("Another noun please: ")
    number_two = input("A number below five please: ")
    # noun_six = input("Another noun please: ")
    # noun_seven = input("Another noun please: ")
    # noun_eight = input("Another noun please: ")

    nouns_list = nouns_string.split(", ")
    # noun_1 = random.choice(nouns_list)
    # print(noun_1)
    # nouns_list.remove(noun_1)
    # print(nouns_list)

    list_for_mad_lib = []

    while len(nouns_list) > 0:
        noun_r = random.choice(nouns_list)
        # print(noun_r)
        list_for_mad_lib.append(noun_r)
        # print(list_for_mad_lib)
        nouns_list.remove(noun_r)
        # print(nouns_list)

    adjective_list = adjective_string.split(", ")

    list_for_adjectives = []

    while len(adjective_list) > 0:
        adjective_r = random.choice(adjective_list)
        list_for_adjectives.append(adjective_r)
        adjective_list.remove(adjective_r)

    plural_noun_list = plural_noun_string.split(", ")

    list_for_plural_nouns = []

    while len(plural_noun_list) > 0:
        plural_noun_r = random.choice(plural_noun_list)
        list_for_plural_nouns.append(plural_noun_r)
        plural_noun_list.remove(plural_noun_r)


    mad_lib = "Hi! This is, {} speaking to you from the broadcasting {} at the {} forum. In case you {} in late, the score between the Los Angeles {} and the Boston {} is a squeaker, 141 to {}. This has been the most {} game these {} eyes have seen in years. First, one team scores a {}, then {}!- the other team comes right back. Okay. Time-out is over. Los Angeles brings in the ball at mid-{}. {} dribbles down the {}, fakes the defender out of his {} and shoots a {}-handed shot. It goes right through the {}. He beat the {}! The game is over just as the {} goes off.".format(person_in_room, list_for_mad_lib[0], list_for_adjectives[0], verb_past_tense, list_for_plural_nouns[0], list_for_plural_nouns[1], number_one, list_for_adjectives[1], list_for_adjectives[2], list_for_mad_lib[1], exclamation, list_for_mad_lib[2], person_in_room_two, list_for_mad_lib[3], list_for_mad_lib[4], number_two, list_for_mad_lib[5], list_for_mad_lib[6], list_for_mad_lib[7])

    # print(len(list_for_adjectives))
    # print(len(list_for_plural_nouns))
    print(mad_lib)

toms_mad_lib(input("Give me the name of a person in the room: "), input("Give me eight singular nouns with commas between them: "), input("Give me three adjectives the same way you did nouns: "), input("Now we need two plural nouns (again seperated by comma): "))

# test list - ball, table, uniform, whiskey, dog, cat, car, gymnasium