import random
import math
import pygame

class Particle():

    def __init__(self, pos, color):
        self.pos = list(pos)
        self.color = pygame.Color(color)
        self.size = random.randint(3, 6)