card_strength = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
gt_max_card_strength = len(card_strength)
hand_type = ['High card','One pair','Two pair','Three of a kind','Full house','Four of a kind','Five of a kind']

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
    score = -1
    type = ''
    type_score = -1
    rank = -1

def create_hand(line):
    cards = line[:5]
    bid = int(line[6:])
    hand = Hand(cards, bid)
    return hand

def get_card_strength(card):
    return card_strength.index(card)

def get_score(cards, type_score):
    # type is worth morth than individual cards
    score = type_score * (gt_max_card_strength ** len(cards))
    # 1st card always worth more than 2nd, etc, etc
    for index, card in enumerate(cards):
        multiplier = gt_max_card_strength ** (len(cards) - 1 - index)
        score += get_card_strength(card)*multiplier
    return score

def get_joker_type(cards: str):
    if len(set(cards)) in [1,2]:
        return 'Five of a kind'
    if len(set(cards)) == 3:
        # can make 4 of a kind if there's 1 of something else
        if any(x != 'J' and cards.count(x) == 1 for x in cards):
            return 'Four of a kind'
        # otherwise we can make full house
        else:
            return 'Full house'
    if len(set(cards)) == 4:
        # if there's 2 of anything we can always make 3 of a kind
        return 'Three of a kind'
    if len(set(cards)) == 5:
        return 'One pair'

def get_type(cards: str):
    if 'J' in cards:
        return get_joker_type(cards)
    if len(set(cards)) == 1:
        return 'Five of a kind'
    if len(set(cards)) == 2:
        if cards.count(cards[0]) in [4,1]:
            return 'Four of a kind'
        else:
            return 'Full house'
    if len(set(cards)) == 3:
        if cards.count(cards[0]) == 2 or cards.count(cards[1]) == 2:
            return 'Two pair'
        else:
            return 'Three of a kind'
    if len(set(cards)) == 4:
        return 'One pair'
    if len(set(cards)) == 5:
        return 'High card'

with open('2023/Day07/input.txt') as f:
    lines = f.readlines()
    hands = list(map(create_hand, lines))
    for hand in hands:
        hand.type = get_type(hand.cards)
        hand.type_score = hand_type.index(hand.type)
        hand.score = get_score(hand.cards, hand.type_score)
    hands.sort(key=lambda x: x.score)
    
    total_winnings = 0

    for index, hand in enumerate(hands):
        hand.rank = index + 1
        total_winnings += hand.rank * hand.bid
        print(total_winnings)

    

