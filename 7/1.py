with open("7/input.txt", "r") as f:
    strings = f.readlines()

NOT_SET = -1
HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
FULL_HOUSE = 4
FOUR_OF_A_KIND = 5
FIVE_OF_A_KIND = 6

letter_cards = ['T', 'J', 'Q', 'K', 'A']


def transform_cards_into_num_arr(full_card: str):
    res = []
    for b in full_card:
        if b.isnumeric(): res.append(int(b))
        else: res.append(10 + letter_cards.index(b))
    return res


def get_card_type(full_card: list):
    card = [i for i in full_card]
    if card[0] == card[1] == card[2] == card[3] == card[4]: return FIVE_OF_A_KIND
    for c in card:
        if card.count(c) == 4: return FOUR_OF_A_KIND
        elif card.count(c) == 3:
            while c in card: card.remove(c)
            if card[0] == card[1]: return FULL_HOUSE
            else: return THREE_OF_A_KIND
        elif card.count(c) == 2:
            while c in card: card.remove(c)
            if len(card) == 3 and (card[0] == card[1] or card[1] == card[2] or card[0] == card[2]) and not (card.count(card[0]) == 3): return TWO_PAIR
            elif len(card) == 3 and card.count(card[0]) == 3: return FULL_HOUSE
            else: return ONE_PAIR
    return HIGH_CARD


def sort_by_type(all_cards, all_bids):
    for i in range(len(all_cards)):
        for j in range(len(all_cards) - 1 - i):
            if all_cards[j][1] > all_cards[j + 1][1]:
                all_cards[j], all_cards[j + 1] = all_cards[j + 1], all_cards[j]
                all_bids[j], all_bids[j + 1] = all_bids[j + 1], all_bids[j]
            elif all_cards[j][1] == all_cards[j + 1][1]:
                for b in range(5):
                    if all_cards[j][0][b] > all_cards[j + 1][0][b]:
                        all_cards[j], all_cards[j + 1] = all_cards[j + 1], all_cards[j]
                        all_bids[j], all_bids[j + 1] = all_bids[j + 1], all_bids[j]
                        break
                    elif all_cards[j + 1][0][b] > all_cards[j][0][b]:
                        break
    return all_cards, all_bids


cards = []
bids = []
for string in strings:
    cards.append([string.split()[0], NOT_SET])
    bids.append(int(string.split()[-1]))

for i in range(len(cards)):
    cards[i][0] = transform_cards_into_num_arr(cards[i][0])
    cards[i][1] = get_card_type(cards[i][0])

cards, bids = sort_by_type(cards, bids)
s = 0
for k in range(len(cards)):
    s += bids[k] * (k + 1)
print(s)