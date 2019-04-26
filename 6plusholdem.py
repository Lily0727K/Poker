import random
import itertools
import collections

rank_to_num = {'A': 9, 'K': 8, 'Q': 7, 'J': 6, 'T': 5, '9': 4, '8': 3, '7': 2, '6': 1}


def rank_of_five_card(card_list):
    ranks = [rank_to_num[c[0]] for c in card_list]
    num_cnt = collections.Counter(ranks)
    num_cnt = sorted(num_cnt.items(), key=lambda x: x[1] * 10 + x[0], reverse=True)
    suits = [c[1] for c in card_list]
    is_flush = len(set(suits)) == 1
    high = sum([item[0] * 10 ** (4 - i) for i, item in enumerate(num_cnt)])

    if len(num_cnt) == 2:
        if num_cnt[0][1] == 4:
            rank_num = 8  # four of a kind
        else:
            rank_num = 6  # full house
    elif len(num_cnt) == 3:
        if num_cnt[0][1] == 3:
            rank_num = 4  # three of a kind
        else:
            rank_num = 3  # two pair
    elif len(num_cnt) == 4:
        rank_num = 2  # one pair
    else:
        is_straight = (num_cnt[0][0] - num_cnt[4][0] == 4) or (num_cnt[0][0] == 9 and num_cnt[1][0] == 4)
        if num_cnt[0][0] == 9 and num_cnt[1][0] == 4:
            high = 43219
        if is_flush and is_straight:
            rank_num = 9  # straight flush
        elif is_flush:
            rank_num = 7  # flush
        elif is_straight:
            rank_num = 5  # straight
        else:
            rank_num = 1  # high card
    rank_num = rank_num * 10 ** 5 + high
    return rank_num


def rank_of_seven_card(seven_card_list):
    five_card_list = itertools.combinations(seven_card_list, 5)
    best_rank_num = max(rank_of_five_card(five_card) for five_card in five_card_list)
    return best_rank_num


def main():
    rank_list = list(rank_to_num)
    suit_list = ['s', 'd', 'c', 'h']
    deck = [r + s for r in rank_list for s in suit_list]

    hole_cards = []
    while True:
        player_num = input("How many players?:")
        try:
            player_num = int(player_num)
            if 2 <= player_num <= 10:
                break
        except ValueError:
            pass

    for player in range(player_num):
        while True:
            hand = tuple(input("player {}:".format(player + 1)).split())
            if hand[0] in deck and hand[1] in deck and hand[0] != hand[1] and len(hand) == 2:
                break
        deck.remove(hand[0])
        deck.remove(hand[1])
        hole_cards.append((hand[0], hand[1]))

    boards = list(itertools.combinations(deck, 5))
    boards = random.sample(boards, 1000)

    player_win = [0] * player_num
    for board in boards:
        player_rank = [rank_of_seven_card(board + hole_cards[player]) for player in range(player_num)]
        winning_player = [player_rank[player] == max(player_rank) for player in range(player_num)]
        winning_cnt = sum(winning_player)
        player_win = [player_win[player] + winning_player[player] / winning_cnt for player in range(player_num)]

    for player in range(player_num):
        print('player{} win: {:.2f}%'.format(player + 1, player_win[player] / 10))


main()
