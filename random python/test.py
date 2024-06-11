import random

class Cards:
  def __init__(self):
    self.count = 0
    self.cards = []
  
  def addCard(self, card):
    self.cards.append(card)
    self.count += 1

  def getCount(self):
    return self.count
  
  def removeCard(self, suit, name):
    flag = 0
    for card in self.cards:
      if card.suit == suit and card.name == name:
        flag = 1
        self.cards.remove(card)

    if flag:
      print('That card does not exist')

  def printCards(self):
    for card in self.cards:
      print('Card: ' + card.name + ' ' + card.suit)

  def getTopCard(self):
    return self.cards[-1]
  
  def getBottomCard(self):
    return self.cards[0]
  
  def shuffleCards(self):
    random.shuffle(self.cards)

class Card:
  def __init__(self, suit, name):
    self.suit = suit
    self.name = name

aCard = Card('hearts', 'queen')
bCard = Card('clubs', 'king')

cards = Cards()

cards.addCard(aCard)
cards.addCard(bCard)

cards.printCards()

cards.removeCard('hearts','queen')

cards.printCards()

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    return result

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = divide(total, len(numbers))  # Bug: passing len(numbers) instead of len(numbers) - 1
    return average

# Example usage:
data = [10, 20, 30, 40, 50]
print(len(data))
average = calculate_average([])
print("The average is:", average)

def calculate_average(numbers: list) -> float:
    return sum(numbers) / len(numbers) if numbers else None

# Example usage:
data = [10, 20, 30, 40, 50]
average = calculate_average([])
print("The average is:", average)