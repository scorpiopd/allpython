from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit} "


c = Card("A", "hearts")
c1 = Card("b", "diamonds")

print(c, c1)


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for value in values for suit in suits]
        """""""""
        # another way to put values in self.cards 
        for suit in suits:
            for value in values:
                self.cards.append( Card (value,suit))
        """""
        #print(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards "

    def _deal(self, num):
        count = self.count()
        actual=min([count,num])
        if count == 0:
            raise ValueError ("all cards over ")
        cards=self.cards[-actual:]
        self.cards =self.cards[:-actual]
        return cards

        print(f" Going to remove {actual} cards")
    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self,hand_size):
        return self._deal(hand_size)
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
            shuffle(self.cards)


    def count(self):
           return len(self.cards)


d = Deck()
#d._deal(3)
d.shuffle()
card=d.deal_card()
print(card)
hand=d.deal_hand(50)
print(hand)



