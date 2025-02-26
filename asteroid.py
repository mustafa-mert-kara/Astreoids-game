from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self, dt):
        self.position+=self.velocity*dt
    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle=random.uniform(20,50)

            velocity1=self.velocity.rotate(new_angle)*1.2
            velocity2=self.velocity.rotate(-new_angle)

            split_asteroid1=Asteroid(self.position[0],self.position[1],self.radius-ASTEROID_MIN_RADIUS)
            split_asteroid2=Asteroid(self.position[0],self.position[1],self.radius-ASTEROID_MIN_RADIUS)
            
            split_asteroid1.velocity=velocity1
            split_asteroid2.velocity=velocity2
        