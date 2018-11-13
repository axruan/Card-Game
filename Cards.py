import random as r

nums = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
suites = ["Hearts", "Spades", "Clubs", "Diamonds"]
money = 1000
cardDrawn = 0


class Cards:

    def __init__(self, num, suite):
        self.n = num
        self.s = suite
        self.card = ""
        self.pt = 0

    def __str__(self):
        return "The " + str(self.n) + " of " + str(self.s)

    def drawCard(self, deck):
        self.card = deck[r.randint(0, len(deck))]
        return self.card

    def getPt(self):
        if self.n == "Ace":
            self.pt = 11
        elif self.n == "Jack" or self.n == "Queen" or self.n == "King":
            self.pt = 10
        else:
            self.pt = int(self.n)
        return self.pt


class Deck:
    def __init__(self):
        self.deck = []
        self.print = ""
        self.card = ""
        self.score = 0

    def addCard(self, card):
        self.deck.append(card)

    def __str__(self):
        for i in range(0, len(self.deck)):
            self.print = self.print + "\n" + str(self.deck[i])
        return self.print


    def addScore(self, card):
        self.score = self.score + card.pt
        return self.score


dealDeck = Deck()
playerDeck = Deck()
dealerDeck = Deck()
drawCard = Cards(0,0)

for i in range(len(suites)):
    for j in range(len(nums)):
        dealDeck.addCard(Cards(nums[j], suites[i]))

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

for i in range(0, 2):
    drawCard = drawCard.drawCard(dealDeck.deck)
    drawCard.getPt()
    playerDeck.addScore(drawCard)
    playerDeck.addCard(drawCard)
    drawCard = drawCard.drawCard(dealDeck.deck)
    drawCard.getPt()
    dealerDeck.addCard(drawCard)
    dealerDeck.addScore(drawCard)

p = str(playerDeck)
d = str(dealerDeck)

print("The player has:", p)
print("Player score:", playerDeck.score)
print("\nThe dealer has:", d)
print("Dealer score", dealerDeck.score)

choice = input("How much would you like to bet?")


input()







