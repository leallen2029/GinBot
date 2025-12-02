import random


"""cards = ["2♠", "3♠", "4♠", "5♠", "6♠","7♠","8♠","9♠", "10♠", "J♠", "Q♠", "K♠", "A♠",
            "2♥", "3♥", "4♥", "5♥", "6♥","7♥","8♥","9♥", "10♥", "J♥", "Q♥", "K♥", "A♥",
            "2♦", "3♦", "4♦", "5♦", "6♦","7♦","8♦","9♦", "10♦", "J♦", "Q♦", "K♦", "A♦",
            "2♣", "3♣", "4♣", "5♣", "6♣","7♣","8♣","9♣", "10♣", "J♣", "Q♣", "K♣", "A♣"]"""

suits = "♠", "♥", "♦", "♣"
ranks = "A","2","3","4","5","6","7","8","9","10","J","Q","K",


def make_deck():
    """ this will be the central storage for the deck and be able to shuffle the deck before playing """
    
    deck = [r+s for r in ranks for s in suits]
    return(deck)

def shuffle_deck(deck):
    """shuffles deck using random.shuffle, stores new value of deck for next function"""
    random.shuffle(deck)
    
    return(deck)

def deal_hand(deck, a):
    '''this function gives you your drawn hand and sorts it from least to most value'''
    hand = []
    for _ in range(a):
        hand.append(deck.pop(0))

    # sort from least to most value using card_points
    hand.sort(key=card_points)

    return hand
    

def draw_from_stock(deck):
    return deck.pop()

def draw_from_discard(discard):
    return discard.pop()

def card_points(card):
    """Asigns each card with there gin rummy scoring: A = 1 & J/Q/K = 10"""
    rank = card[:-1]  # removes suit

    if rank == "A":
        return 1
    if rank in {"J", "Q", "K"}:
        return 10
    return int(rank)

def find_sets(hand):
    """Return all 3+ of a kind melds"""
    rank_groups = {}
    for card in hand:
        rank = card[:-1]
        rank_groups.setdefault(rank, []).append(card)

    melds = []
    for group in rank_groups.values():
        if len(group) >= 3:
            melds.append(group)
    return melds
def find_runs(hand):
    """Return runs 3+ same suit in a row"""
    suit_groups = {"♠": [], "♥": [], "♦": [], "♣": []}

    # separate by suit
    for card in hand:
        suit = card[-1]
        rank = card[:-1]
        suit_groups[suit].append((card, rank))

    all_runs = []

    # convert ranks to numbers
    rank_order = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    for suit, cards in suit_groups.items():
        # sort cards by numerical order
        sorted_cards = sorted(cards, key=lambda x: rank_order.index(x[1]))

        # build runs
        temp_run = [sorted_cards[0][0]] if sorted_cards else []

        for i in range(1, len(sorted_cards)):
            previous_rank = sorted_cards[i-1][1]
            current_rank = sorted_cards[i][1]

            if rank_order.index(current_rank) - rank_order.index(previous_rank) == 1:
                temp_run.append(sorted_cards[i][0])
            else:
                if len(temp_run) >= 3:
                    all_runs.append(temp_run)
                temp_run = [sorted_cards[i][0]]

        if len(temp_run) >= 3:
            all_runs.append(temp_run)

    return all_runs

def pick_melds_and_deadwood(hand):
    """Choose all runs + sets and uses runs first (longest melds),
        then sets.Returns (list_of_melds, leftover_cards) """
    hand_copy = hand[:]
    melds = []

    # get all potential melds
    possible_runs = find_runs(hand_copy)
    possible_sets = find_sets(hand_copy)

    # choose runs first
    for run in possible_runs:
        melds.append(run)
        for c in run:
            if c in hand_copy:
                hand_copy.remove(c)

    # then choose sets that still exist
    for s in possible_sets:
        if all(c in hand_copy for c in s):
            melds.append(s)
            for c in s:
                hand_copy.remove(c)

    leftover = hand_copy
    return melds, leftover


def deadwood_points(cards):
    return sum(card_points(c) for c in cards)

def knocks(hand, limit):
    melds, leftover = pick_melds_and_deadwood(hand)
    return deadwood_points(leftover) <= limit
