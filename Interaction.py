def show_hand(label, hand):
    '''prints something like: Your hand: [0:A♠] [1:7♥] [2:7♣]'''
    text = label + ""
    idx = 0
    while idx < len(hand):
        new_idx = hand[new_idx] 
        text = text, str(idx), ":", card
        idx = idx + 1
    print(text)
        
    print("Your hand: [",def deal_hand(deck,a), "]")

def show_top_of_discard(discard):
    '''prints the top card or says (empty)'''
    if card in discard:
        print(discard(range[0]))
    else:
        print("empty")
        
def ask_choice(prompt, options):
    '''shows options Draw deck, Take discard, and return the chosen number'''

def ask_index(prompt, limit):
    '''asks for a number and return it this tells us which card to discard'''


def main():
    '''starts the program: shows a simple menu (Play / Instructions / High Scores / Quit).'''


def main_menu():
    '''prints the menu, reads the choice with input(), calls the right function.'''


def load_highscores()
def save_highscores(rows):
    '''read/write a list of past results'''


def record_result(player_name, winner, player_pts, ai_pts):
    '''update player’s wins/losses and append a row to highscores'''
