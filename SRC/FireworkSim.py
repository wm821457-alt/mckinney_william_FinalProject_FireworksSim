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

        self.life = 100
        self.age = 0
        self.alpha = 255
        self.dead = False

    def update(self):
        self.pos[0] += self.dx
        self.pos[1] += self.dy

        self.age += 1

        if self.age >= self.life:
            self.dead = True

        self.alpha = 255 * (1 - self.age / self.life)

    def draw(self, surface):
        if self.dead:
            return

        particle_surface = pygame.Surface(
            (self.size * 2, self.size * 2),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            particle_surface,
            (*self.color[:3], int(self.alpha)),
            (self.size, self.size),
            self.size
        )

        surface.blit(
            particle_surface,
            (int(self.pos[0] - self.size),
             int(self.pos[1] - self.size))
        )


class Firework():

    def __init__(self, pos):
        self.pos = pos
        self.particles = []

        colors = [
            (255, 0, 0),
            (255, 200, 0),
            (0, 200, 255),
            (200, 0, 255),
            (0, 255, 100)
        ]

        self.color = random.choice(colors)
        for count in range(40):
            particle = Particle(self.pos, self.color)
            self.particles.append(particle)

    def update(self):
        for particle in self.particles:
            particle.update()

        self.particles = [
            particle for particle in self.particles
            if not particle.dead
        ]