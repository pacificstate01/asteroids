import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    Player.containers = (updatables,drawable)
    Asteroid.containers = (asteroids,updatables,drawable)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shot_group, updatables, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        # In your main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot(shot_group)
        screen.fill("black")
        updatables.update(dt)
        for ast in asteroids:
            for bullet in shot_group:
                if bullet.collision(ast):
                    bullet.kill()
                    ast.split()
        for col in asteroids:
            if player.collision(col):
                print("Game Over!")
                sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
