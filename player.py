from circleshape import CircleShape
from constants import *
from shot import Shot
import pygame
class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation=0
        self.firerate=0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    def rotate(self,dt):
        self.rotation+=dt*PLAYER_TURN_SPEED
    
    def update(self, dt):
        self.firerate-=dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            reverse=-1*dt
            self.rotate(reverse)
        if keys[pygame.K_d]:
            
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            reverse=-1*dt
            self.move(reverse)
        if keys[pygame.K_SPACE]:
            self.shoot()
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self,):
        if self.firerate>0:
            return
        self.firerate=PLAYER_SHOOT_COOLDOWN
        new_shot=Shot(self.position[0],self.position[1])
        new_shot.velocity=pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
        timer=pygame.time.Clock