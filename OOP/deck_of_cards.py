from random import shuffle

# card class that has suit and value
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

# deck class that holds 52 cards and deals cards out as well as shuffles a full deck
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', '2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(suit,value) for suit in suits for value in values]
    
    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"
    
    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    
    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self
    
