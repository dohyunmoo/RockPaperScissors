import pygame

class Object:
    def __init__(self, size) -> None:
        self.size = size
    
    def obj_contact(self):
        pass

    def on_touch(self):
        pass