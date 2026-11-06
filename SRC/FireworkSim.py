import random
import math
import pygame

class Particle():

    def __init__(self, pos, color):
        self.pos = list(pos)
        self.color = pygame.Color(color)
        self.size = random.randint(3, 6)

        self.speed = random.uniform(2, 6)
        self.angle = random.uniform(0, math.pi * 2)

        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed