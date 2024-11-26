import random

class Card:
    def __init__(self, rank, symbol):
        self.rank = rank
        self.symbol = symbol

    def __str__(self):
        return f"{self.rank} of {self.symbol}"  

    def get_value(self):
        rank_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
        }
        return rank_values[self.rank]


class Deck:
    def __init__(self):
        print("Initializing deck...")
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        symbols = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, symbol) for rank in ranks for symbol in symbols]
        print(f"Deck initialized with {len(self.cards)} cards.")

    def shuffle(self):
        print("Shuffling deck...")
        random.shuffle(self.cards)
        print("Deck shuffled.")

    def deal(self):
        if self.cards:
            return self.cards.pop()
        return None

    def deal_to_players(self, num_players):
        print(f"Dealing cards to {num_players} players...")
        hands = [[] for _ in range(num_players)]
        while self.cards:
            for hand in hands:
                if self.cards:
                    hand.append(self.deal())
        print(f"Cards dealt. Each player has {len(hands[0])} cards.")
        return hands


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self):
        if self.hand:
            return self.hand.pop(0)
        return None

    def collect_cards(self, cards):
        if isinstance(cards, list):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)
        random.shuffle(self.hand)  


class Game:
    def __init__(self):
        print("Initializing game...")
        self.players = [Player("Player 1"), Player("Player 2")]
        deck = Deck()
        deck.shuffle()
        player_hands = deck.deal_to_players(len(self.players))

        for player, hand in zip(self.players, player_hands):
            player.collect_cards(hand)
        print("Game initialized. Players are ready.")

    def is_game_over(self):
        return any(not player.hand for player in self.players)

    def play_game(self):
        print("Game started.")
        round_number = 1
        while not self.is_game_over():
            print(f"\n--- Round {round_number} ---")
            self.play_round()
            print(f"{self.players[0].name} has {len(self.players[0].hand)} cards.")
            print(f"{self.players[1].name} has {len(self.players[1].hand)} cards.")
            round_number += 1

        winner = max(self.players, key=lambda player: len(player.hand))
        print(f"\n{winner.name} wins the game with {len(winner.hand)} cards!")

    def play_round(self):
        print("Starting a new round...")
        card1 = self.players[0].play_card()
        card2 = self.players[1].play_card()

        if not card1 or not card2:
            print("A player has run out of cards!")
            if not card1:
                print(f"{self.players[1].name} wins the game!")
            else:
                print(f"{self.players[0].name} wins the game!")
            return

        print(f"{self.players[0].name} plays {card1}")
        print(f"{self.players[1].name} plays {card2}")

        if card1.get_value() > card2.get_value():
            print(f"{self.players[0].name} wins this round!")
            self.players[0].collect_cards([card1, card2])
        elif card1.get_value() < card2.get_value():
            print(f"{self.players[1].name} wins this round!")
            self.players[1].collect_cards([card1, card2])
        else:
            print("It's a tie! This means war!")
            self.handle_war([card1, card2])

    def handle_war(self, pile):
        print("War! Each player places three cards face down and one card face up.")

        if len(self.players[0].hand) < 4 or len(self.players[1].hand) < 4:
            print("A player doesn't have enough cards for war! Game over.")
            if len(self.players[0].hand) < 4:
                print(f"{self.players[1].name} wins the game!")
            else:
                print(f"{self.players[0].name} wins the game!")
            return

        war_cards1 = []
        war_cards2 = []

        for _ in range(4):
            if self.players[0].hand:
                war_cards1.append(self.players[0].play_card())
            if self.players[1].hand:
                war_cards2.append(self.players[1].play_card())

        if not war_cards1 or not war_cards2:
            print("A player ran out of cards during war!")
            if not war_cards1:
                print(f"{self.players[1].name} wins the game!")
            else:
                print(f"{self.players[0].name} wins the game!")
            return

        pile.extend(war_cards1 + war_cards2)
        print(f"War cards added to the pile: {len(pile)} cards total.")

        if war_cards1[-1].get_value() > war_cards2[-1].get_value():
            print(f"{self.players[0].name} wins the war with {war_cards1[-1]}!")
            self.players[0].collect_cards(pile)
        elif war_cards1[-1].get_value() < war_cards2[-1].get_value():
            print(f"{self.players[1].name} wins the war with {war_cards2[-1]}!")
            self.players[1].collect_cards(pile)
        else:
            print("Another tie! Continue the war!")
            self.handle_war(pile)


def main():
    print("Welcome to the War Card Game!")

   
    game = Game()

    print("\nThe deck is shuffled, and cards are dealt to both players.")
    print(f"{game.players[0].name} starts with {len(game.players[0].hand)} cards.")
    print(f"{game.players[1].name} starts with {len(game.players[1].hand)} cards.")

    try:
        game.play_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Thanks for playing!")

    print("\nThank you for playing the War Card Game!")



if __name__ == "__main__":
    main()
