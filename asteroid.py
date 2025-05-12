from circleshape import CircleShape
import pygame
import random
from constants import *
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), int(self.radius), 2)

    def update(self,dt):
        self.position += self.velocity * dt
        self.x = self.position.x
        self.y = self.position.y
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
    
        # Create two new velocity vectors
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2
        
        # Create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1
        
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel2
        
        # Return the new asteroids
        return [asteroid1, asteroid2]

        


