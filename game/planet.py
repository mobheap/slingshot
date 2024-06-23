import pygame
from pygame.locals import *

class Planet:
    def __init__(self, x, y, mass, image, size):
        self.x = x
        self.y = y
        self.mass = mass
        self.image = pygame.transform.scale(image, (size * 2, size * 2))
        self.size = size

    def draw(self, win):
        win.blit(self.image, (self.x - self.size, self.y - self.size))
