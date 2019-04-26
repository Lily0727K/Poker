import random
import sys
import pygame
import pandas as pd
import Rank

rank_list = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
suit_list = ['s', 'd', 'c', 'h']
deck = []
for card_rank in rank_list:
    for card_suit in suit_list:
        deck.append(card_rank + card_suit)
card = pd.DataFrame(index=[1, 2, 3, 4, 5, 6, 7], columns=[1, 2, 3, 4, 5, 6, 7])
card.fillna("")


def print_card(screen, font_big, x, y, card):
    screen.fill((157, 204, 224))
    for r in range(7):
        for c in range(7):
            if x == c and y == r:
                sf_card = font_big.render(card.iloc[r, c], True, (255, 255, 255))
            else:
                sf_card = font_big.render(card.iloc[r, c], True, (0, 0, 0))
            screen.blit(sf_card, (72 * c, 72 * r))


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((504, 648))
    font_big = pygame.font.SysFont("Courier", 36)

    deck_shuffle = random.sample(deck, 49)
    for r in range(7):
        for c in range(7):
            card.iloc[r, c] = deck_shuffle[r * 7 + c]

    x = 3
    y = 3
    hand = [card.iloc[y, x]]

    while len(hand) < 7:
        print_card(screen, font_big, x, y, card)
        for i, h in enumerate(hand):
            sf_hand = font_big.render(h, True, (255, 0, 0))
            screen.blit(sf_hand, (72*i, 576))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x > 0 and card.iloc[y, x-1] not in hand:
                    x = x - 1
                    hand.append(card.iloc[y, x])
                if event.key == pygame.K_RIGHT and x < 6 and card.iloc[y, x+1] not in hand:
                    x = x + 1
                    hand.append(card.iloc[y, x])
                if event.key == pygame.K_UP and y > 0 and card.iloc[y-1, x] not in hand:
                    y = y - 1
                    hand.append(card.iloc[y, x])
                if event.key == pygame.K_DOWN and y < 6 and card.iloc[y+1, x] not in hand:
                    y = y + 1
                    hand.append(card.iloc[y, x])

    print_card(screen, font_big, x, y, card)
    best_hand = Rank.rank_of_seven_card(hand)[0]
    for i, h in enumerate(hand):
        if h in best_hand:
            sf_hand = font_big.render(h, True, (255, 0, 0))
        else:
            sf_hand = font_big.render(h, True, (0, 0, 0))
        screen.blit(sf_hand, (72 * i, 576))

    rank = Rank.rank_of_seven_card(hand)[1]
    sf_rank = font_big.render(rank, True, (255, 0, 0))
    center_x = screen.get_rect().width / 2 - sf_rank.get_rect().width / 2
    screen.blit(sf_rank, (center_x, 504))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    run_game()


run_game()
