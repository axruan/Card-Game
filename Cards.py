nums = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
suites = ["Hearts", "Spades", "Clubs", "Diamonds"]


class Cards:
    def __init__(self, num, suite):
        self.n = num
        self.s = suite

    def __str__(self):
        return "The ", self.n, "of ", self.s




class Deck:
    def __init__(self):
        self.deck = []

    def __str__(self):
        for i in range(len(self.deck)):
            self.printer = self.printer + "\n" + str(self.deck[i])
        return self.printer

    def addCard(self, card):
        self.deck.append(card)


dealDeck = Deck()

for i in range(len(suites)):
    for j in range(len(nums)):
        dealDeck.addCard(Cards(nums[j], suites[i]))

x = str(dealDeck)





