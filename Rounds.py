'''rounds'''

from SetUp import find_runs, make_deck, shuffle_deck, deal_hand, draw_from_stock, draw_from_discard, pick_melds_and_deadwood, deadwood_points
from Interaction import show_hand, show_top_of_discard, ask_choice, ask_index
from Computer import ai_draw_choice, ai_discard_index, ai_wants_to_knock
from Interaction import engine
from SetUp import organize_hand

def start_round():
    '''make/shuffle a deck, deal 10 to the player and 10 to the computer'''
    deck = make_deck()
    shuffle_deck(deck)
    
    player_hand = deal_hand(deck,10)
    ai_hand = deal_hand(deck,10)
    
    discard = [deck.pop()]
    
    #stores the values for the following variables into one variable
    state = {
    "deck": deck,
    "discard": discard,
    "player": player_hand,
    "ai": ai_hand
}

    
    return state

def player_turn(state):
    '''shows info, asks to draw from deck or discard (or try to knock),
    if draw, ask which card index to discard, update state'''
    player = state["player"]
    deck = state["deck"]
    discard = state["discard"]
    
    #shows the player what they need to know
    show_hand("Your Hand:", player)
    show_top_of_discard(discard)
    
    #gives choices for nect move
    choice = ask_choice("Draw or discard?", {"1": "Draw deck", "2": "Take discard", "3": "Knock"})
    
    if choice == "3": #knock
        melds, leftover = pick_melds_and_deadwood(player)
        if deadwood_points(leftover) <=10:
            return "knock"
        else:
            print("You cant knock, the deadwood is too high :(")
            
    if choice == "1": #discard
        card = draw_from_stock(deck)
        engine.clear_messages()
        engine.show_drawn_card(card)
        engine.show_message("Click a card below to discard", 200)
        engine.draw_hand(player)#draw normal hand only
        engine.show_drawn_card(card)
    else: 
        card = discard.pop()#gets top of discard
    
    player.append(card)
        
    index = ask_index("Which card would you like to discard?", len(player))
    discarded_card = player.pop(index)
    discard.append(discarded_card)
    organized = organize_hand(player)
    player[:] = organized
    
    engine.clear_messages()#clears text
    engine.clear_cards()#removes all card images from screen
    engine.show_message("Your Hand:", 50)
    engine.draw_hand(player)
    
    return None

def computer_turn(state):
    '''choose draw source, maybe knock?, choose a discard, updates state'''
    
    ai = state["ai"]
    discard = state["discard"]
    deck = state["deck"]

    upcard = discard[-1] if discard else None

   
    if ai_wants_to_knock(ai, 10):
        return "knock"

    # draw choice
    choice = ai_draw_choice(ai, upcard)

    if choice == "stock":
        ai.append(draw_from_stock(deck))
    else:
        ai.append(draw_from_discard(state["discard"]))

    
    index = ai_discard_index(ai)
    discarded_card = ai.pop(index)
    discard.append(discarded_card)
    return None

def round_over(state):
    '''return True if someone knocked or the stock ran out'''
    return len(state["deck"]) == 0

def score_round(state, who_knocked):
    '''computes deadwood for both; the knocker wins unless the other
    side has less deadwood (that’s an undercut—just say “computer wins”
    in that case)'''
    
    player = state["player"]
    ai = state["ai"]

    _, player_left = pick_melds_and_deadwood(player)
    _, ai_left = pick_melds_and_deadwood(ai)

    p_dead = deadwood_points(player_left)
    a_dead = deadwood_points(ai_left)

    if who_knocked == "player":
        if a_dead < p_dead:
            return "computer", p_dead, a_dead
        else:
            return "player", p_dead, a_dead

    else:
        if p_dead < a_dead:
            return "player", p_dead, a_dead
        else:
            return "computer", p_dead, a_dead

def play_round(player_name):
    '''call start_round, loop: player_turn; computer_turn until round_over,
    then call score_round and return the winner plus both deadwood totals'''
    
    state = start_round()
    
    knocker = None
    
    
    while not round_over(state): #for the turns
        result = player_turn(state)
        if result == "knock":
            knocker = "player"
            break
        
        result = computer_turn(state)
        if result == "knock":
            knocker = "computer"
            break
    if knocker is None:
        _, player_left = pick_melds_and_deadwood(state["player"])
        _, ai_left = pick_melds_and_deadwood(state["ai"])
        p_dead = deadwood_points(player_left)
        a_dead = deadwood_points(ai_left)
        winner = "player" if p_dead < a_dead else "computer"
        return winner, p_dead, a_dead
    
    return score_round(state, knocker)
    
    
