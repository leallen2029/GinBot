
import random


"""cards = ["1♠", "2♠", "3♠", "4♠", "5♠", "6♠","7♠","8♠","9♠", "10♠", "J♠", "Q♠", "K♠", "A♠",
             "1♥", "2♥", "3♥", "4♥", "5♥", "6♥","7♥","8♥","9♥", "10♥", "J♥", "Q♥", "K♥", "A♥",
             "1♦", "2♦", "3♦", "4♦", "5♦", "6♦","7♦","8♦","9♦", "10♦", "J♦", "Q♦", "K♦", "A♦",
             "1♣", "2♣", "3♣", "4♣", "5♣", "6♣","7♣","8♣","9♣", "10♣", "J♣", "Q♣", "K♣", "A♣"]"""


def make_deck():
    """ this will be the central storage for the deck and be able to shuffle the deck before playing """
    
    suits = "♠", "♥", "♦", "♣"
    ranks = "1","2","3","4","5","6","7","8","9","10","J","Q","K","A"
    deck = [r+s for r in ranks for s in suits]

    return(deck)
def shuffle_deck(deck):
    random.shuffle(deck)
    print(deck)


def main ():
    make_deck()
    shuffle_deck()

if __name__ == "__main__":
    main()
h
    
    


