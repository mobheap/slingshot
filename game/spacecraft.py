import pygame
import math
from pygame.locals import *

class Spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass, size, color):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass
        self.size = size
        self.color = color

    def move(self, planet, G):
        distance = math.sqrt((self.x - planet.x) ** 2 + (self.y - planet.y) ** 2)
        force = (G * self.mass * planet.mass) / distance ** 2

        acceleration = force / self.mass
        angle = math.atan2(planet.y - self.y, planet.x - self.x)

        acceleration_x = acceleration * math.cos(angle)
        acceleration_y = acceleration * math.sin(angle)

        self.vel_x += acceleration_x
        self.vel_y += acceleration_y

        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.size)
