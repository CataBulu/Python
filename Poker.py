import random

def draw_card(deck):
  hand = deck.pop()
  return [hand], deck

def create_deck():
  suits = ["♥", "♦", "♣", "♠"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  deck = []

  for suit in suits:
    for rank in ranks:
      deck.append((suit, rank))

  random.shuffle(deck)
  return deck

deck = create_deck()
while len(deck) > 0:
  input("Press Enter to draw the next card")
  hand, deck = draw_card(deck)
  print(hand[0])
print ("We are out of cards")

