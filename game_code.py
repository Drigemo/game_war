import random

class Card:
    def __init__(self, rank, symbol):
        self.rank = rank
        self.symbol = symbol

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        symbols = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, symbol) for rank in ranks for symbol in symbols]

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self):
        return self.hand.pop(0) if self.hand else None

    def add_cards(self, cards):

        if isinstance(cards, list):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)



deck = Deck()
deck.shuffle()

print(deck.deal())  
print(deck.deal())  
