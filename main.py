import pygame
import pymunk
import random

import objects
import utils

pygame.init()

screen = pygame.display.set_mode(utils.SCREEN_SIZE)
pygame.display.set_caption("Rock Paper Scissors")
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 0)

def game():
    running = True

    ball_radius = 10

    balls = [objects.Rock(ball_radius, random.randint(0, 200), i*25, 20, 20, space, 1, "r") for i in range(1, 100)]
    special_ball = objects.Rock(ball_radius, -25, -25, 20, 20, space, 2, "p")

    handler = space.add_collision_handler(1, 2)
    handler.begin = utils.collision

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(utils.BACKGROUND_COLOR)

        [ball.draw_object(screen) for ball in balls]
        special_ball.draw_object(screen)

        space.step(1/60)
        pygame.display.flip()
        # clock.tick(60) # 60 FPS

    pygame.quit()

if __name__ == "__main__":
    game()
