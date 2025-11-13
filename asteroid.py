import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x + self.radius / 2, self.position.y + self.radius / 2, new_radius)
            a1.velocity = velocity1
            a2 = Asteroid(self.position.x - self.radius / 2, self.position.y - self.radius / 2, new_radius)
            a2.velocity = velocity2
