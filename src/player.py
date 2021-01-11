import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        print(f'The horizontal position: {self.rect.x}')
        print(f' The vertical position: {self.rect.y}')
        keyInput = pygame.key.get_pressed()
        if (keyInput[pygame.K_UP]):
            self.rect.y -= 5
            if (self.rect.top <= 0):
                self.rect.top = HEIGHT
        if (keyInput[pygame.K_DOWN]):
            self.rect.y += 5
            if (self.rect.bottom >= HEIGHT):
                self.rect.bottom = 0
        if (keyInput[pygame.K_LEFT]):
            self.rect.x -= 5
            if (self.rect.left <= 0):
                self.rect.left = WIDTH 
        if (keyInput[pygame.K_RIGHT]):
            self.rect.x += 5
            if (self.rect.right >= WIDTH):
                self.rect.right = 0
    