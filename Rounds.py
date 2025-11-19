def start_round():
    '''make/shuffle a deck, deal 10 to the player and 10 to the computer'''


def player_turn(state):
    '''shows info, asks to draw from deck or discard (or try to knock),
    if draw, ask which card index to discard, update state'''


def computer_turn(state):
    '''choose draw source, maybe knock?, choose a discard, updates state'''


def round_over(state):
    '''return True if someone knocked or the stock ran out'''


def score_round(state, who_knocked):
    '''computes deadwood for both; the knocker wins unless the other
    side has less deadwood (that’s an undercut—just say “computer wins”
    in that case)'''


def play_round(player_name):
    '''call start_round, loop: player_turn; computer_turn until round_over,
    then call score_round and return the winner plus both deadwood totals'''
