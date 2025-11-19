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