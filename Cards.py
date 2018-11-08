import random as r

nums = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
suites = ["Hearts", "Spades", "Clubs", "Diamonds"]
money = 1000
cardDrawn = 0

class Cards:
    def __init__(self, num, suite):
        self.n = num
        self.s = suite

    def __str__(self):
        return "The " + str(self.n) + " of " + str(self.s)




class Deck:

    score = 0

    def __init__(self):
        self.deck = []
        self.print = ""
        self.card = ""

    def __str__(self):
        for i in range(0, len(self.deck)):
            self.print = self.print + "\n" + str(self.deck[i])
        return self.print

    def addCard(self, card):
        self.deck.append(card)

    def drawCard(self):
        self.card = self.deck[r.randint(0, len(self.deck))]
        c = str(self.card)
        print(c)


dealDeck = Deck()
playerDeck = Deck()

for i in range(len(suites)):
    for j in range(len(nums)):
        dealDeck.addCard(Cards(nums[j], suites[i]))

interface = input("""
=======================================================
 ____  ____   _____   ___  
|    ||    \ |     | /   \ 
 |  | |  _  ||   __||     |
 |  | |  |  ||  |_  |  O  |
 |  | |  |  ||   _] |     |
 |  | |  |  ||  |   |     |
|____||__|__||__|    \___/
=======================================================
Hello and welcome to Blackjack. The rules are simple!\n
You will start with $1000. Everytime you play, you will bet however much you want.
Blackjack pays out 3-2, s""")




