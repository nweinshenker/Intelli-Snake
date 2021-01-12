import pygame
import sys
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.image.fill(BLUE)

    def update(self):
        x_change = 0 
        y_change = 0 

        keyInput = pygame.key.get_pressed()
        if (keyInput[pygame.K_UP]):
            y_change -= SNAKE_BLOCK
            x_change = 0
        if (keyInput[pygame.K_DOWN]):
            y_change += SNAKE_BLOCK
            x_change = 0
        if (keyInput[pygame.K_LEFT]):
            y_change = 0
            x_change -= SNAKE_BLOCK
        if (keyInput[pygame.K_RIGHT]):
            y_change = 0 
            x_change += SNAKE_BLOCK
        
        # No matter what make the snake move the original direction
        ##if (self.rect.x < 0 or
        ##    self.rect.x >= WIDTH or
        ##    self.rect.y < 0 or
        ##    self.rect.y >= HEIGHT):
        ##    sys.exit(0)
        self.rect.x += x_change
        self.rect.y += y_change

        
