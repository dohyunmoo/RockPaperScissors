import pygame
import pymunk
import utils

class Rock:
    def __init__(self, radius, x, y, x_speed, y_speed, space, collision_type, attribute) -> None:
        self.radius = radius
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.collision_type = collision_type
        self.attribute = attribute

        self.moment = pymunk.moment_for_circle(1, 0, radius)
        self.body = pymunk.Body(1, self.moment)
        self.body.position = x, y
        self.body.velocity = x_speed, y_speed
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.density = 1
        self.shape.elasticity = 1
        self.shape.friction = 0.7
        space.add(self.body, self.shape)

    def draw_object(self, screen):
        if self.attribute == "r":
            pygame.draw.circle(screen, pygame.Color("#FF0000"), self.body.position, self.radius)
        elif self.attribute == "p":
            pygame.draw.circle(screen, pygame.Color("#00FF00"), self.body.position, self.radius)
        elif self.attribute == "s":
            pygame.draw.circle(screen, pygame.Color("#0000FF"), self.body.position, self.radius)
    
    def obj_contact(self):
        pass

    def on_touch(self):
        pass

    def obj_move(self):
        self.body.position[0] += self.x_speed
        self.body.position[1] += self.y_speed

        if self.body.position[0] - self.radius < 0 or self.body.position[0] + self.radius > utils.SCREEN_SIZE[0]:
            self.x_speed *= -1
        if self.body.position[1] - self.radius < 0 or self.body.position[1] + self.radius > utils.SCREEN_SIZE[1]:
            self.y_speed *= -1
        