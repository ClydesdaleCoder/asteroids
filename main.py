import sys
import pygame
from constants import*
from player import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    player = Player(x,y)
    asteroid_field = AsteroidField()
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for things in drawable:
            things.draw(screen)

        updatable.update(dt)
        for a in asteroids:
            if a.collision(player) == True:
                print ("Game Over!")
                sys.exit()
            for s in shots:
                if s.collision(a) == True: 
                    a.split(),s.kill()

        pygame.display.flip()
        dt =  clock.tick(60)/1000

    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__" :
    main()
