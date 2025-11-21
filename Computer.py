from SetUp.py import ranks
o
def ai_draw_choice(ai_hand, upcard):
    '''returns 'stock' unless the upcard matches a rank
        you already have then discard'''
    
    if upcard in find_sets(hand) or find_runs(hand):
        draw_from_discard(discard)
    
    else:
        return
    

def ai_discard_index(ai_hand):
    '''returns the index of a card to throw away: pick
    the one with the highest card_points'''
    
def ai_wants_to_knock(ai_hand, limit):
    '''returns True if deadwood is small enough (use can_knock)'''
    counter = 0
    i = 0
    while i < len(ai_hand):
        counter = counter + card_points(ai_hand[i])
        i += 1
        


# Computer.py

from Setup import RANKS   # use the same RANKS list as in your setup file


def get_rank(card):
    """
    Return the rank part of a card string.
    Example: '10♣' -> '10', 'A♠' -> 'A'
    """
    return card[:-1]


def get_suit(card):
    """
    Return the suit part of a card string.
    Example: '10♣' -> '♣'
    """
    return card[-1]


def card_points(card):
    """
    Return the point value for one card.
    A = 1, J/Q/K = 10, numbers = their value.
    """
    r = get_rank(card)
    if r == "A":
        return 1
    if r == "J" or r == "Q" or r == "K":
        return 10
    return int(r)


def ai_draw_choice(ai_hand, upcard):
    """
    Decide whether the AI should draw from the stock ("stock")
    or take the top card from the discard pile ("discard").

    Strategy:
      - If upcard is None (no discard card), draw from stock.
      - If upcard matches a rank in AI's hand -> take discard (helps make a set).
      - If upcard is same suit and next/previous rank as one in AI's hand
        -> take discard (helps make a run).
      - Otherwise -> draw from stock.
    """
    if upcard is None:
        return "stock"

    up_rank = get_rank(upcard)
    up_suit = get_suit(upcard)
    up_index = RANKS.index(up_rank)

    # Check for same rank (sets)
    i = 0
    while i < len(ai_hand):
        card = ai_hand[i]
        if get_rank(card) == up_rank:
            return "discard"
        i = i + 1

    # Check for run neighbors (same suit, rank next to it)
    i = 0
    while i < len(ai_hand):
        card = ai_hand[i]
        if get_suit(card) == up_suit:
            card_rank = get_rank(card)
            card_index = RANKS.index(card_rank)
            if abs(card_index - up_index) == 1:
                return "discard"
        i = i + 1

    # Otherwise, stock is safer
    return "stock"


def ai_discard_index(ai_hand):
    """
    Decide which card the AI should discard.

    Strategy:
      - High point cards are bad.
      - Cards with fewer "neighbors" (same rank or close in suit) are bad.
      - For each card:
          score = card_points(card) - neighbor_count
        Higher score means worse card.
      - Discard the card with the highest score.
    """
    best_score = None
    best_i = 0

    i = 0
    while i < len(ai_hand):
        card = ai_hand[i]
        r = get_rank(card)
        s = get_suit(card)
        r_index = RANKS.index(r)

        # base score = its point value
        score = card_points(card)

        # count neighbors
        neighbors = 0
        j = 0
        while j < len(ai_hand):
            other = ai_hand[j]
            if other != card:
                # same rank helps sets
                if get_rank(other) == r:
                    neighbors = neighbors + 1
                # same suit and next/previous rank helps runs
                if get_suit(other) == s:
                    other_r = get_rank(other)
                    other_index = RANKS.index(other_r)
                    if abs(other_index - r_index) == 1:
                        neighbors = neighbors + 1
            j = j + 1

        # more neighbors = better card to keep, so subtract neighbors
        final_score = score - neighbors

        if best_score is None or final_score > best_score:
            best_score = final_score
            best_i = i

        i = i + 1

    return best_i


def ai_wants_to_knock(ai_hand, limit):
    """
    Decide if the AI should knock.

    Simple version:
      - Estimate deadwood as total card_points in AI hand.
      - If total <= limit + 3, AI will knock.
    """
    total = 0
    i = 0
    while i < len(ai_hand):
        total = total + card_points(ai_hand[i])
        i = i + 1

    return total <= limit + 3