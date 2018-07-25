#  make players and then team of players


class Player:
    def __init__(self, name, number, shoot2, shoot3, dunk, speed, strength):
        self.name = name
        self.number = number
        self.shoot2 = shoot2
        self.shoot3 = shoot3
        self.dunk = dunk
        self.speed = speed
        self.strength = strength
    def __str__(self):
        return "He is {} wearing number {}.  His rating at shooting 2's is {}.  3's are {}. His dunk rating is {}, speed {} and strength {}.".format(self.name, self.number, self.shoot2, self.shoot3, self.dunk, self.speed, self.strength)
    def __repr__(self):
        return str(self.dunk)


damian_lillard = Player("Damian Lillard", "0", 92, 89, 85, 93, 80)
jusuf_nurkic = Player("Jusuf Nurkic", "27", 80, 65, 92, 79, 90)
cj_mccollum = Player("CJ McCollum", "3", 90, 92, 75, 86, 83)

class Team:
    def __init__(self):
        self.roster = []
    def __str__(self):
        return "{}".format(self.roster)


# print(damian_lillard)
# print(jusuf_nurkic)
# print(cj_mccollum)

blazers = Team()
blazers.roster.append(damian_lillard)
blazers.roster.append(jusuf_nurkic)
blazers.roster.append(cj_mccollum)

print(blazers.roster)

