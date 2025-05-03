import pygame
from constants import *
from player import Player


def main():
    pygame.init()

    myclock = pygame.time.Clock()

    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player_1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player_1.update(dt)
        pygame.Surface.fill(screen, (0, 0, 0))
        player_1.draw(screen)
        amt_t = myclock.tick(60)

        dt = amt_t / 1000

        pygame.display.flip()


if __name__ == "__main__":
    main()
