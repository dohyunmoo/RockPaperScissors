import pygame
import pymunk

WIDTH, HEIGHT = 1280, 720

SCREEN_SIZE = (WIDTH, HEIGHT)
BACKGROUND_COLOR = pygame.Color("#6375DA")

def collision1(arbiter, space, data):
    print("hello")
    return True

def collision2(arbiter, space, data):
    print("hello2")
    return True

def collision3(arbiter, space, data):
    print("hello3")
    return True

def draw(space, screen, draw_options):
    screen.fill(BACKGROUND_COLOR)
    space.debug_draw(draw_options)
    pygame.display.update()

def draw_boundaries(space, width, height):
    # center of the rectangles
    rects = [
        [(width/2, height + 10), (width, 20)],
        [(width/2, -10), (width, 20)],
        [(-10, height/2), (20, height)],
        [(width + 10, height/2), (20, height)]
    ]

    for coord, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = coord
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 1
        shape.friction = 0
        space.add(body, shape)
