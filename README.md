# GinBot
Final project replicating Gin Rummy

Team Information: B1 Landree and Madeleine

Files required/included in your project, and a description of their contents: 

Interaction.py:
Handles user interface through text.
Includes functions for:
	•	Showing the player’s hand with indices
	•	Showing the top of the discard pile
	•	Asking the user to choose actions
	•	Asking the user to choose a card index to discard

This file keeps all input/output code organized and easy to modify.

Main.py:
Our main calling file of the program.
	•	Displays the main menu (Play / Instructions / High Scores / Quit)
	•	Calls play_round() to start a game
	•	Calls functions for showing instructions and high scores
	•	Controls the overall flow of the project

Computer.py:
Controls the computer player’s strategy.
Includes functions for:
	•	Choosing to draw from the deck or the discard pile
	•	Choosing which card to discard (avoids breaking pairs, removes high-value cards)
	•	Deciding when the computer should knock

This creates a realistic, but beatable AI opponent.

GameGraphics.py: Turns code from the other files into a graphic expression of Gin Rummy, including imported card photos, sorted cards, and a green background.  

graphics.py: A simple object oriented graphics library

Rounds.py
Runs one full round of Gin Rummy.
Includes functions for:
	•	Setting up the round (deal cards, create discard pile)
	•	Player turn logic
	•	Computer turn logic
	•	Determining when the round is over
	•	Scoring the round and deciding a winner
	•	Running turns in a loop until the round ends

This file coordinates all other modules.

SetUp.py
Handles all card and scoring logic.
Includes functions for:
	•	Creating and shuffling the deck
	•	Dealing hands and drawing cards
	•	Calculating point values (A = 1, J/Q/K = 10, etc.)
	•	Detecting sets (3+ same rank)
	•	Detecting runs (3+ consecutive cards in a suit)
	•	Separating a hand into melds and deadwood
	•	Calculating deadwood points
	•	Checking whether a hand is allowed to knock

This file contains the most important rules of Gin Rummy.


~Basic Instructions and Calculations For Our Version of Gin Rummy~

Our Gin Rummy is a 2-player card game (one being you and the other being a computer algorithm). Each player tries to form melds (groups of cards that “fit together”) and get rid of deadwood (loose cards that don’t belong to any group). The lower your deadwood, the better.


Setup:
- A standard 52-card deck is used
- Each player is dealt 10 cards (you will always have 10 cards in your hand)
- The rest of the cards are placed face down as the stock.
- The top card of the stock is turned face up to start the discard pile.


Types of melds:

Sets:
- 3 or more cards of the same rank
- Examples: 7♠ 7♥ 7♦

Runs:
- 3 or more cards in number order, all in the same suit
-Examples: 4♥ 5♥ 6♥


Deadwood:
- Any card that is not part of a set or a run is called deadwood.
- Each deadwood card is worth points:
	- A = 1 point
	- 2–10 = face value
	- J, Q, K = 10 points
- Your deadwood total is the sum of these points.
- The goal of the game is to have as little deadwood as possible.


Round structure:
- On each turn, a player:
	- Draws one card:
		- Either from the stock (face-down deck), or from the discard pile (the top face-up card)

	- Discards one card:
		- They choose one card from their hand and put it face-up on the discard pile.


Knocking:
- You can knock at the end of your turn (instead of continuing to play) if your deadwood total is 10 or less.
- When you knock:
	- You reveal your hand.
	- Your sets and runs are counted as melds.
	- Your remaining cards count as deadwood.
    - The opponent also lays out their melds and deadwood.


Winning a round:
- After someone knocks, compare deadwood:
	- If the knocker has less deadwood, the person who knocked wins the round.
	- If the other player has equal or less deadwood, the knocker loses the round.


User manual: 

Once you run the game a screen will appear with :
Basic Rules
Highest Score
Play Game
Quit

	•	Click “Play Game” to start.
	•	You are given 10 cards; these are your randomly drawn starting cards.
	•	You will also see a card under “Take Discard,” and this is the top card of the discard pile, which you can choose to take instead of drawing from the deck.
	•	If you choose “Draw from Deck,” the card you draw will appear in the “Draw Deck” section.
	•	After drawing, you must choose one card to discard from your hand.
	•	You repeat this process (draw, then discard) while trying to form melds (groups of cards that belong together).
	•	Once your hand is good enough and your deadwood is low enough, you can click “Knock” to end the round.