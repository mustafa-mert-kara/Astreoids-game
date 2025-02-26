import pygame
from constants import *



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.mixer.quit()
    pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


if __name__=="__main__":
    main()