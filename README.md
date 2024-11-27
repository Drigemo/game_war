War Card Game Simulation

A Python implementation of the classic card game "War." This project simulates a two-player card game where players compete by playing cards from their deck, resolving ties with "war" scenarios, and collecting cards until one player wins all the cards.

How the Game Works

Setup:
A standard deck of 52 cards is shuffled and evenly distributed between two players.

Gameplay:
Each player plays the top card from their deck.
The player with the higher card value wins and collects both cards.
If there is a tie, a "war" occurs:
Each player places one card face down and one face up.
The player with the higher face-up card wins all the cards in the pile.
If another tie occurs, the process repeats recursively.
Special Case - Insufficient Cards for War:

If a player doesn't have enough cards to continue a war, all remaining cards are given to the opponent, and the game ends.
Game End:

The game ends when one player has all 52 cards.
Features
Realistic Gameplay:

Implements the standard rules of the War card game.
Handles tie scenarios (wars) and recursive ties effectively.
Robust Handling of Edge Cases:

Automatically ends the game if a player cannot continue a war due to insufficient cards.
Ensures no card duplication or loss during gameplay.
Randomized Card Shuffling:

Cards are shuffled after every collection to ensure unpredictability.
Comprehensive Validation:

Verifies the total card count (52) after every round to detect and prevent errors.
How to Run the Game
Prerequisites
Python 3.6 or higher must be installed on your system.
Steps to Run
Clone or download this repository to your local machine.
Navigate to the project directory.
Run the program using the command:
python game_code.py
Code Overview
Key Components
Classes:

Card: Represents a single card with a rank and a suit.
Deck: Manages the creation and shuffling of a deck of cards.
Player: Represents a player with their hand of cards and actions (e.g., play a card, collect cards).
Game: Implements the game logic, including playing rounds, handling wars, and determining the winner.
Functions:

play_round(): Plays a single round of the game.
handle_war(): Handles ties by initiating a "war."
end_game_on_insufficient_cards(): Handles cases where a player doesn’t have enough cards for a war.
validate_card_counts(): Ensures the total card count remains accurate.
