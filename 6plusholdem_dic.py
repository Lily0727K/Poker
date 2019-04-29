import random
import itertools
import pandas as pd

df = pd.read_csv("ID_to_Strength.csv")
ID_to_strength = {row[1]: row[2] for row in df.itertuples()}


def rank_of_five_card(card_list):
    ID = "".join(sorted(card_list))
    return ID_to_strength[ID]


def rank_of_seven_card(seven_card_list):
    five_card_list = itertools.combinations(seven_card_list, 5)
    best_rank_num = max(rank_of_five_card(five_card) for five_card in five_card_list)
    return best_rank_num


def main():
    rank_list = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6']
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

    print("****************")
    boards = list(itertools.combinations(deck, 5))
    boards = random.sample(boards, 10000)

    player_win = [0] * player_num
    for board in boards:
        player_rank = [rank_of_seven_card(board + hole_cards[player]) for player in range(player_num)]
        winning_player = [player_rank[player] == max(player_rank) for player in range(player_num)]
        winning_cnt = sum(winning_player)
        player_win = [player_win[player] + winning_player[player] / winning_cnt for player in range(player_num)]

    for player in range(player_num):
        print('player{} win: {:.2f}%'.format(player + 1, player_win[player] * 100 / len(boards)))

    cont = input("Continue?(Y:Yes, N:No):")
    if cont == "Y":
        main()


main()
