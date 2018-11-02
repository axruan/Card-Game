nums = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
suites = ["Hearts", "Spades", "Clubs", "Diamonds"]

class Cards:
    def __init__(self, num, suite):
        self.n = num
        self.s = suite

    def show(self):
        print("The ", self.n, "of ", self.s)


class Deck:
    def __init__(self):
        deck = []
        for i in range(len(suites)):
            for j in range(len(nums)):
                deck.append(Cards(nums[j-1], suites[i-1]))

    def __str__(self):
        return



