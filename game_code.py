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
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        symbols = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, symbol) for rank in ranks for symbol in symbols]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_to_players(self, num_players):
        hands = [[] for _ in range(num_players)]
        while self.cards:
            for hand in hands:
                if self.cards:
                    hand.append(self.cards.pop())
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
        self.players = [Player("Player 1"), Player("Player 2")]
        deck = Deck()
        deck.shuffle()
        player_hands = deck.deal_to_players(len(self.players))

        for player, hand in zip(self.players, player_hands):
            player.collect_cards(hand)

    def is_game_over(self):
        return any(not player.hand for player in self.players)

    def play_game(self):
        round_number = 1
        while not self.is_game_over():
            print(f"\n--- Round {round_number} ---")
            self.play_round()
            self.validate_card_counts()
            self.show_player_hands()

            if self.is_game_over():
                break
            round_number += 1

        self.declare_winner()

    def play_round(self):
        card1 = self.players[0].play_card()
        card2 = self.players[1].play_card()

        if not card1 or not card2:
            return  # Stop the game immediately if a player has no cards

        print(f"{self.players[0].name} plays {card1}")
        print(f"{self.players[1].name} plays {card2}")

        if card1.get_value() > card2.get_value():
            self.players[0].collect_cards([card1, card2])
        elif card1.get_value() < card2.get_value():
            self.players[1].collect_cards([card1, card2])
        else:
            self.handle_war([card1, card2])

    def handle_war(self, pile):
        print("It's a tie! This means war!")
        print("Each player places one card face down and one card face up.")

        # Ensure both players have enough cards for the war
        if len(self.players[0].hand) < 2 or len(self.players[1].hand) < 2:
            self.end_game_on_insufficient_cards(pile)
            return

        # Add one face-down card to the pile
        pile.append(self.players[0].play_card())
        pile.append(self.players[1].play_card())

        # Add one face-up card to the pile
        face_up_card1 = self.players[0].play_card()
        face_up_card2 = self.players[1].play_card()

        if not face_up_card1 or not face_up_card2:
            return

        pile.extend([face_up_card1, face_up_card2])

        print(f"{self.players[0].name} plays {face_up_card1} (face up).")
        print(f"{self.players[1].name} plays {face_up_card2} (face up).")

        if face_up_card1.get_value() > face_up_card2.get_value():
            print(f"{self.players[0].name} wins the war with {face_up_card1}!")
            self.players[0].collect_cards(pile)
            pile.clear()  # Clear the pile after collection
        elif face_up_card1.get_value() < face_up_card2.get_value():
            print(f"{self.players[1].name} wins the war with {face_up_card2}!")
            self.players[1].collect_cards(pile)
            pile.clear()  # Clear the pile after collection
        else:
            print("It's another tie! The war continues!")
            self.handle_war(pile)  # Reuse the same pile for recursion

    def end_game_on_insufficient_cards(self, pile):
        print("A player doesn't have enough cards for war! Adding remaining cards to the winner.")

        # Add remaining cards to the pile
        for player in self.players:
            if player.hand:
                pile.extend(player.hand)
                player.hand.clear()

        # Determine the winner
        winner = self.players[0] if not self.players[1].hand else self.players[1]
        winner.collect_cards(pile)
        pile.clear()

        print(f"{winner.name} wins the game with {len(winner.hand)} cards!")

    def declare_winner(self):
        winner = max(self.players, key=lambda player: len(player.hand))
        print(f"\n{winner.name} wins the game!")

    def show_player_hands(self):
        print(f"{self.players[0].name} has {len(self.players[0].hand)} cards.")
        print(f"{self.players[1].name} has {len(self.players[1].hand)} cards.")

    def validate_card_counts(self):
        total_cards = len(self.players[0].hand) + len(self.players[1].hand)
        if total_cards != 52:
            print(f"Warning: Total card count mismatch. Found {total_cards} cards (expected 52).")
            raise RuntimeError("Card duplication detected!")


def main():
    game = Game()
    game.play_game()


if __name__ == "__main__":
    main()
