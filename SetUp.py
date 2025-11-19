
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
    """shuffles deck using random.shuffle, stores new value of deck for next function"""
    random.shuffle(deck)
    
    return(deck)
def deal_hand(deck,a):
    hand = []
    for _ in range(a):
        hand.append(deck.pop(0))
    return (hand)
     
def main ():
    deck = make_deck()
    shuffle_deck(deck)
    hand1 = deal_hand(deck,10)
    print ("Your Hand: ", hand1)
    
if __name__ == "__main__":
    main()

    
    


