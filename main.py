import pygame

import objects
import utils

pygame.init()

screen = pygame.display.set_mode(utils.SCREEN_SIZE)
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(utils.BACKGROUND_COLOR)

    pygame.display.flip()
    clock.tick(60) # 60 FPS

pygame.quit()
