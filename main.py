import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import  AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.mixer.quit()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    updatables=pygame.sprite.Group()
    drawables=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    Player.containers=(updatables,drawables)
    Asteroid.containers=(asteroids,updatables,drawables)
    AsteroidField.containers=(updatables)
    Shot.containers=(shots,drawables,updatables)

    field=AsteroidField()

    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(0)
        for drawable in drawables:            
            drawable.draw(screen)
        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                exit(0)

        pygame.display.flip()




        dt=clock.tick()/1000

if __name__=="__main__":
    main()