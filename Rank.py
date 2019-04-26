import itertools
import collections


def rank_of_five_card(card_list):
    rank_to_num = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
                   '2': 2}

    ranks = [rank_to_num[c[0]] for c in card_list]
    num_cnt = collections.Counter(ranks)
    num_cnt = sorted(num_cnt.items(), key=lambda x: -x[0] - x[1]*100)

    suits = [c[1] for c in card_list]
    suits_cnt = collections.Counter(suits)
    is_flush = len(suits_cnt) == 1
    is_flush_draw = suits_cnt.most_common()[0][1] == 4

    high = sum([item[0] * 100 ** (4-i) for i, item in enumerate(num_cnt)])

    if len(num_cnt) == 2:
        if num_cnt[0][1] == 4:
            rank_text, rank_num = 'four of a kind', 8
        else:
            rank_text, rank_num = 'full house', 7
    elif len(num_cnt) == 3:
        if num_cnt[0][1] == 3:
            rank_text, rank_num = 'three of a kind', 4
        else:
            rank_text, rank_num = 'two pair', 3
    elif len(num_cnt) == 4:
        rank_text, rank_num = 'one pair', 2
    else:
        num_list = sorted(list(num_cnt), reverse=True)
        is_straight = (num_list[0][0] - num_list[4][0] == 4) or (num_list[0][0] == 14 and num_list[1][0] == 5)
        if is_flush and is_straight:
            rank_text, rank_num = 'straight flush', 9
        elif is_flush:
            rank_text, rank_num = 'flush', 6
        elif is_straight:
            rank_text, rank_num = 'straight', 5
        elif is_flush_draw:
            rank_text, rank_num = 'flush draw', 1
        else:
            rank_text, rank_num = 'high card', 0
    high = rank_num * 100 ** 5 + high
    return rank_text, rank_num, high


def rank_of_seven_card(seven_card_list):
    best_rank_num = 0
    five_card_list = itertools.combinations(seven_card_list, 5)

    for five_card in five_card_list:
        ranks = rank_of_five_card(five_card)
        if ranks[2] > best_rank_num:
            best_rank_num = ranks[2]
            best_five_card = five_card
            best_rank_text = ranks[0]
    return best_five_card, best_rank_text, best_rank_num
