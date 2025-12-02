from SetUp import pick_melds_and_deadwood, deadwood_points, card_points

def get_rank(card):
    """Returns the rank part of a card string."""
    return card[:-1]


def get_suit(card):
    """Returns the suit part of a card string."""
    return card[-1]


def ai_draw_choice(ai_hand, upcard):
    """
    figures whether the Computer should draw from the stock or take the top card from the discard pile.

    Strategy:
      - If upcard is None, draw from stock.
      - If upcard matches a rank in computer's hand, take discard (helps make a set).
      - If upcard is cheaper than ai's worst (highest point) card, output discard
      - Else, draw from stock.
    """
    
    if upcard is None:
        return "stock"
    
    # asks if rank matches discard
    up_rank = get_rank(upcard)
    count = 0
    while count < len(ai_hand):
        card = ai_hand[count] # idx of the first one in the computer's hand
        
        if get_rank(card) == up_rank:
            return "discard"
        count = count + 1


    # if upcard is cheaper than AI's worst (highest point) card, take it
    up_value = card_points(upcard)
    max_points = 0
    count = 0
    while count < len(ai_hand):  
        card = ai_hand[count]
        value = card_points(card)
        if value > max_points:
            max_points = value
        count = count + 1
    if up_value < max_points:
        return "discard"
    

    return "stock"


def ai_discard_index(ai_hand):
    '''gives a strategy for which card to discard and which to keep,
    ensures that it will not seperate potential pairs'''
    # Counts how many cards of each rank while protecting pairs
    rank_counts = {}
    for card in ai_hand:
        g = get_rank(card)
        if g in rank_counts:
            rank_counts[g] += 1
        else:
            rank_counts[g] = 1

    # Picks the highest-value card that isn't a pair
    best_index = 0
    best_value = -1

    for index in range(len(ai_hand)):
        card = ai_hand[index]
        r = get_rank(card)
        value = card_points(card)

        # skip pairs
        if rank_counts[r] >= 2:
            continue

        # chooses the highest value card
        if value > best_value:
            best_value = value
            best_index = index

    return best_index



def ai_wants_to_knock(ai_hand, limit):
    """
    Decides if the AI should knock
      - use deadwood amount as total card_points in ai hand.
      - If dead <= limit, computer will knock.
    """

    # get all cards that aren't in a meld
    melds, leftover = pick_melds_and_deadwood(ai_hand)

    # calculates deadwood points
    dead = deadwood_points(leftover)

    # AI knocks if its deadwood is low enough
    return dead <= limit
        