from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
            #self.position
            #self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, 'grey', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        a = uniform(20, 50)
        Asteroid(self.position, self.position, self.radius-ASTEROID_MIN_RADIUS).initiate(self.velocity.rotate(a)*1.5)
        Asteroid(self.position, self.position, self.radius-ASTEROID_MIN_RADIUS).initiate(self.velocity.rotate(-a)*1.5)

    def initiate(self, v):
        self.velocity = v
