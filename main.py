import pygame
import pymunk
from pymunk import pygame_util
import random

import objects
import utils

pygame.init()

screen = pygame.display.set_mode(utils.SCREEN_SIZE)
pygame.display.set_caption("Rock Paper Scissors")
clock = pygame.time.Clock()

def game():
    space = pymunk.Space()
    space.gravity = (0, 0)

    draw_options = pymunk.pygame_util.DrawOptions(screen)

    ball_radius = 12

    balls = [objects.Rock(ball_radius, random.randint(0, utils.SCREEN_SIZE[0]), random.randint(0, utils.SCREEN_SIZE[1]), random.randint(-50, 50), random.randint(-50, 50), space, i, "r") for i in range(1, 200)]
    balls_2 = [objects.Rock(ball_radius, random.randint(0, utils.SCREEN_SIZE[0]), random.randint(0, utils.SCREEN_SIZE[1]), random.randint(-50, 50), random.randint(-50, 50), space, i, "p") for i in range(1, 200)]
    balls_3 = [objects.Rock(ball_radius, random.randint(0, utils.SCREEN_SIZE[0]), random.randint(0, utils.SCREEN_SIZE[1]), random.randint(-50, 50), random.randint(-50, 50), space, i, "s") for i in range(1, 200)]

    handler1 = space.add_collision_handler(1, 2)
    handler2 = space.add_collision_handler(1, 3)
    handler3 = space.add_collision_handler(2, 3)
    handler1.begin = utils.collision1
    handler2.begin = utils.collision2
    handler3.begin = utils.collision3

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        [ball.draw_object(screen) for ball in balls]
        [ball.draw_object(screen) for ball in balls_2]
        [ball.draw_object(screen) for ball in balls_3]

        utils.draw(space, screen, draw_options)
        utils.draw_boundaries(space, utils.WIDTH, utils.HEIGHT)
        space.step(1/60)

    pygame.quit()

if __name__ == "__main__":
    game()
