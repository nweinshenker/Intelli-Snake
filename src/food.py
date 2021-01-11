import pygame
import random

# import basic settings of the game
from settings import *

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Random x and y coordinate
        self.rand_x, self.rand_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        self.is_cover = False
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (self.rand_x, self.rand_y)

    