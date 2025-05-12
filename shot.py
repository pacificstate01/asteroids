from circleshape import CircleShape
import pygame
from constants import *
from pygame.math import Vector2
class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.velocity= Vector2(0,0)
        
    def draw(self,screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), int(self.radius), 2)

    def update(self,dt):
        self.position += self.velocity * dt
        self.x = self.position.x
        self.y = self.position.y
