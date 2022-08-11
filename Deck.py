import random


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """Create a deck using a Card class.
        Adding every combination of suit and number to the cards list"""
        self.suit = ['spades', 'hearts', 'bell', 'cross']
        self.number = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        for s in self.suit:
            for n in self.number:
                self.cards.append(Card(s, n).give_card())
        return self.cards

    def draw(self):
        """Function removes one card from a deck and returns it"""
        self.getted = self.cards.pop()
        return self.getted

    def show_deck(self):
        return self.cards

    def shufle(self):
        for idx in range(len(self.cards)-1, 0, -1):
            randidx = random.randint(0, idx)
            self.cards[idx], self.cards[randidx] = self.cards[randidx], self.cards[idx]
        return self.cards


class Card:
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number

    def give_card(self):
        return "{} of {}".format(self.number, self.suit)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.points = 0

    def show_player(self):
        return f"Player: {self.name}\nPoints: {self.points}"

    def show_hand(self):
        return f"{self.name}'s hand: {self.hand}"

    def hit(self, deck):
        """Function represents HIT in blackjack which is a simply drawing a card"""
        self.getcard = deck.draw()
        self.hand.append(self.getcard)
        return self.getcard

    def add_points(self):
        """Adds points to the players points amount according to the BlackJack rules"""
        self.value = 0
        self.splited = self.getcard.split(" ")
        if self.splited[2] in ['J', 'Q', 'K']:
            self.value += 10
        elif self.splited[2] == 'A':
            if self.points > 10:
                self.value += 1
            else:
                self.value += 11
        elif int(self.splited[2]) in range(2, 11):
            self.value += int(self.splited[2])
        self.points += self.value
        return self.value
