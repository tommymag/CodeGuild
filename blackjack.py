# # Practice: Blackjack
#
# Let's start modeling a game of [blackjack](https://en.wikipedia.org/wiki/Blackjack).
#
# `Card` class with a suit and a rank
# `Deck` class with a collection of cards
# `Hand` class with a collection of cards from a deck.
#
# Use multiple modules.
#
# In the `deck` module, implement methods that:
#
# * Return a shuffled deck
# * Cut the deck
# * Draw a card off the top of a deck
#
# In the `hand` module, implement methods that:
#
# * Add a card to a hand
# * Allow a user to type in a hand and have it be converted into a `Hand` object
#
# In the `game` module, implement top-level functions that:
#
# * Start a new game of Blackjack, or Quit
# * Score a hand
# * Bust if the score is over 21
#
# ## Scoring
#
# Cards have integer point values.
# Aces are 1 or 11, number cards are their number, face cards are all 10.
# A hand is worth the sum of all the points of the cards in it.
# An ace is worth 1 when the hand it's a part of would be over 21 if it was worth 11.
#
# ## Advanced
#
# *   Bring in your dealer hitting logic from the [21 practice problem](/practice/21.md) into a top-level function it's own module `dealer`.
#     Update it to take in a `Hand` instance and return whether to hit.
#
# *   Add a "card counting assistant" function in a module `advisor`.
#     Have it take in a deck and a hand and print out the probability that you will bust.
#     You can find the [expectation value](http://www.wikihow.com/Calculate-an-Expected-Value) of the score of your hand given one more card; basically the sum of the probability of the card multiplied by the resulting score of the hand with that card.
#
# *   Add in a UI so a single user can play versus the dealer.
#
# *   Allow multiple hands to be played with the same deck.

# class to make a card

# class to make a deck

# class for making a hand


import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

        for rank in values:
            for suit in suits:
                self.cards.append(Card(suit, rank))

        random.shuffle(self.cards)

    def __str__(self):
        return "{}".format(self.cards)


class Hand:
    def __init__(self):
        self.player_hand = []

    def deal(self, card):
        self.player_hand.append(card)




# my_card = Card('clubs', 'ace')
#
# print(my_card)

my_deck = Deck()
print(my_deck)

