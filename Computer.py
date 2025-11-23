

def get_rank(card):
    """Gets the rank part of a card string."""
    return card[:-1]


def get_suit(card):
    """Gets the suit part of a card string."""
    return card[-1]


def card_points(card):
    """ Returns the point value for one card.
    A = 1 & J/Q/K = 10"""
    
    g = get_rank(card)
    if g == "A":
        return 1
    if g == "J" or g == "Q" or g == "K":
        return 10
    return int(g)

def ai_draw_choice(ai_hand, upcard):
    """
    whether the Computer should draw from the stock or take the top card from the discard pile.

    Strategy:
      - If upcard is None, draw from stock.
      - If upcard matches a rank in computer's hand, take discard (helps make a set).
      - If upcard is cheaper than ai's worst (highest point) card, output discard
      - Else, draw from stock.
    """
    
    if upcard is None:
        return "stock"
    
    # does rank match?
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
    # Count how many cards of each rank (protect pairs)
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

        # choose highest value card
        if value > best_value:
            best_value = value
            best_index = index

    return best_index



def ai_wants_to_knock(ai_hand, limit):
    """
    Decides if the AI should knock
      - Estimate deadwood as total card_points in ai hand.
      - If total <= limit + 3, computer will knock.
    """
    total = 0
    i = 0
    while i < len(ai_hand):
        total = total + card_points(ai_hand[i])
        i = i + 1

    return total <= limit + 3
        