# GinBot
Final project replicating Gin Rummy


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

README.md: A basic readme file including:
– team information
– a list of all files required/included in your project, and a description of their contents
– an explanation of how to run and interact with your project (similar to a user guide)
