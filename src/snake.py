import pygame
from settings import *


def main():
    pygame.init()
    
    # Set up of the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SNAKE")

    # Sets the number of frames per second the game should run
    clock = pygame.time.Clock()
    done = False

    while not done:
        clock.tick(FPS)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 

        # Draw the screen
        screen.fill(BLACK)
        pygame.display.flip()


    pygame.quit();        


if __name__ == '__main__':
    main()