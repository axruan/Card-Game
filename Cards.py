# Alex Ruan
# CS550
# 15 November 2018
# Sources: Python documentation and various StackExchange threads
# Description: I created a small Blackjack game.

import random as r

# card class
class Cards:

    # initializes a card with a number and a suite
    def __init__(self, num, suite):
        self.n = num
        self.s = suite
        self.card = ""
        self.pt = 0

    # makes the card print out nicely
    def __str__(self):
        return "The " + str(self.n) + " of " + str(self.s)

    # gets and returns how much each card is worth
    def getPt(self):
        if self.n == "Ace":
            self.pt = 11
        elif self.n == "Jack" or self.n == "Queen" or self.n == "King":
            self.pt = 10
        else:
            self.pt = int(self.n)
        return self.pt


# deck class
class Deck:

    # initializes the deck
    def __init__(self):
        self.deck = []
        self.print = ""
        self.card = ""
        self.score = 0

    # adds a card to the deck
    def addCard(self, card):
        self.deck.append(card)

    # makes the deck print out nicely
    def __str__(self):
        for i in range(0, len(self.deck)):
            self.print = self.print + "\n" + str(self.deck[i])
        return self.print

    # adds the total score of the deck
    def addScore(self, card):
        self.score = self.score + card.pt
        return self.score

    # shuffles the deck
    def shuffle(self):
        r.shuffle(self.deck)


# creates the "hitting", or drawing a card
def hit2(deck1, deck2, who="dealer"):
    deck2.shuffle()
    card = deck2.deck[0]
    card.getPt()
    deck1.addScore(card)
    deck1.addCard(card)
    deck2.deck.remove(card)
    c = str(card)
    deck1.print = ""
    p = str(deck1)
    print("{} have drawn: ".format(who) + str(c) + "\n")
    print("The {} has:\n".format(who) + str(p) + "\n")
    print("Total score of {}:".format(who), deck1.score)


blackjackMessage = """
______ _            _    _            _    _
| ___ \ |          | |  (_)          | |  | |
| |_/ / | __ _  ___| | ___  __ _  ___| | _| |
| ___ \ |/ _` |/ __| |/ / |/ _` |/ __| |/ / |
| |_/ / | (_| | (__|   <| | (_| | (__|   <|_|
\____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_(_)
                       _/ |
                      |__/
"""

youWinMessage = """
__   __                     _       _
\ \ / /                    (_)     | |
 \ V /___  _   _  __      ___ _ __ | |
  \ // _ \| | | | \ \ /\ / / | '_ \| |
  | | (_) | |_| |  \ V  V /| | | | |_|
  \_/\___/ \__,_|   \_/\_/ |_|_| |_(_)
                                        """

youLoseMessage = """
__   __            _                _
\ \ / /           | |              | |
 \ V /___  _   _  | | ___  ___  ___| |
  \ // _ \| | | | | |/ _ \/ __|/ _ \ |
  | | (_) | |_| | | | (_) \__ \  __/_|
  \_/\___/ \__,_| |_|\___/|___/\___(_)

                                        """
interface = input("""
=======================================================
 _____       __
|_   _|     / _|
  | | _ __ | |_ ___
  | || '_ \|  _/ _ \
 _| || | | | || (_) |
 \___/_| |_|_| \___/

=======================================================

Instructions:
------------------

Hello and welcome to Blackjack. The rules are simple!

You will start with $1000. Everytime you play, you will bet however much you want.
Blackjack pays out 3-2, so if you bet $50 and win, you will win $75 instead of $50.

When the game starts, both you and the dealer (the computer) will draw two cards each.
The "score" of each card will be added up. Then, you will have the option to either
"hit" or "stand." Hitting will draw an additional card, while standing will end your turn.
When everyone is done drawing cards, your scores will be compared. The goal is to get
a score of 21, or blackjack. If you hit blackjack, you automatically win unless the
dealer also gets a blackjack. If you decide to continue hitting and you go over 21,
you "bust," or you lose your bet. If you have a higher score than the dealer, then
you win (and vice versa).

Scoring:
------------------
1 through 9: Worth their face value
10 through King: Worth 10
Ace: Worth 11

=======================================================

Press any key to start playing!
""")


nums = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
suites = ["Hearts", "Spades", "Clubs", "Diamonds"]
money = 1000
shouldGameStart = True
amount = 0
stop = False

dealDeck = Deck()
playerDeck = Deck()
dealerDeck = Deck()
drawCard = Cards(0, 0)

# creates a deck which everyone draws from
for i in range(len(suites)):
    for j in range(len(nums)):
        dealDeck.addCard(Cards(nums[j], suites[i]))


# the start of the game where each player draws two cards
for i in range(0, 2):
    dealDeck.shuffle()
    drawCard = dealDeck.deck[0]
    drawCard.getPt()
    playerDeck.addCard(drawCard)
    playerDeck.addScore(drawCard)
    dealDeck.deck.remove(drawCard)
    dealDeck.shuffle()
    drawCard = dealDeck.deck[0]
    drawCard.getPt()
    dealerDeck.addCard(drawCard)
    dealerDeck.addScore(drawCard)
    dealDeck.deck.remove(drawCard)

print("Your total amount is: $" + str(money) + "\n")

# asks user for how much money they would like to bet, if they don't enter a valid input it asks them to do it again
while True:
    try:
        amount = int(input("How much would you like to bet?\n"))
        if amount < 0 or amount > money:
            print("You don't have enough money!")
            raise ValueError
    except:
        print("Please enter a valid amount")
        continue
    else:
        break

p = str(playerDeck)
d = str(dealerDeck)
print("Your bet amount is: $" + str(amount) + "\n")
print("Your amount left is: $" + str(money-amount) + "\n"+'\n'+'\n')

print("The player has:", p)
print("Player score:", playerDeck.score)
print("\nThe dealer has: Hidden Card and", dealerDeck.deck[1])

# win/lose conditions
if dealerDeck.score == 21 or playerDeck.score > 21:
    print(youLoseMessage)
    shouldGameStart = False

# win/lost conditions
elif dealerDeck.score > 21 or playerDeck.score == 21:
    print(youWinMessage)
    money = money + 1.5 * amount
    print("You've won:", 1.5 * amount)
    print("You have:", money)
    shouldGameStart = False


# actual playing part of the game, asks if user wants to draw a card or stop their turn
while int(playerDeck.score) < 21 and shouldGameStart:
    if not stop:
        choice = input("Would you like to hit (h) or stop (s)?\n")
    if choice == "h":
        hit2(playerDeck, dealDeck, "player")
    elif choice == "s":
        stop = True
        if dealerDeck.score < 21:
            hit2(dealerDeck, dealDeck)

        if dealerDeck.score > 21:
            print(youWinMessage)
            money = money + 1.5 * amount
            print("You've won:", 1.5 * amount)
            break
        elif dealerDeck.score == 21:
            print(youLoseMessage)
            break
        elif dealerDeck.score < playerDeck.score:
            print(youWinMessage)
            money = money + 1.5 * amount
            print("You've won:", 1.5 * amount)
            break

    # win/lose condition
    if int(playerDeck.score) == 21:
        print(blackjackMessage)
        money = money + 1.5 * amount
        print("You've won:", 1.5 * amount)
        break
    elif int(playerDeck.score) > 21:
        print(youLoseMessage)
        break
