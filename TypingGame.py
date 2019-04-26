import random
import sys
import pygame


def select_word(score):
    if score < 200:
        word_list = ["raise", "call", "fold", "check", "ante", "bluff", "fish", "flop", "flush",
                     "muck", "pair", "pot", "rake", "river", "tilt"]
    else:
        word_list = ["backdoor", "balancing", "bankroll", "blocker", "broadway", "connectors",
                     "isolation", "overbet", "passive", "rainbow", "rakeback", "satellite",
                     "shootout", "showdown", "staking", "straddle", "straight", "suited"]
    i = random.randint(0, len(word_list) - 1)
    return word_list[i]


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((720, 480))
    font_big = pygame.font.SysFont("comicsansms", 72)
    start_ticks = pygame.time.get_ticks()
    score = 0
    timer = 30 - int((pygame.time.get_ticks() - start_ticks) / 1000)
    word = select_word(score)

    while timer > 0:
        screen.fill((157, 204, 224))
        sf_word = font_big.render(word, True, (0, 0, 0))
        center_x = screen.get_rect().width / 2 - sf_word.get_rect().width / 2
        screen.blit(sf_word, (center_x, 200))
        timer = 30 - int((pygame.time.get_ticks() - start_ticks) / 1000)
        sf_timer = font_big.render(str(timer), True, (0, 0, 0))
        screen.blit(sf_timer, (0, 0))
        sf_score = font_big.render(str(score), True, (0, 0, 0))
        screen.blit(sf_score, (520, 0))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if chr(event.key) == word[0]:
                    word = word[1:]
                    score = score + 1
                    if word == "":
                        word = select_word(score)
                        score = score + 10

    screen.fill((157, 204, 224))
    title = "GTO Typing"
    sf_title = font_big.render(title, True, (0, 0, 0))
    screen.blit(sf_title, (0, 0))
    final_score = "Your score: " + str(score)
    sf_score = font_big.render(final_score, True, (0, 0, 0))
    screen.blit(sf_score, (0, 200))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


run_game()
