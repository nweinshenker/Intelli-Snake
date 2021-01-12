import pygame
from pygame.constants import K_LEFT

# All the basic objects
from player import Player
from food import Food

from settings import *

def main():
    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    # Define the font styles for the game
    font_style = pygame.font.SysFont("arial", 30)
    score_font = pygame.font.SysFont("optima", 30)



    # Create a player object
    player = Player()
    food = Food()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(food)

    # Game loop
    running = True
    game_started= False
    while running:
        # keep loop running at the right speed
        while game_started == True:
            print("Here")
            screen.fill(BLUE)
            message = font_style.render("You've Lost the Game", True, BLUE)
            screen.blit(message, [WIDTH // 5, HEIGHT // 3])
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = True
                        game_started = False
                    if event.key == pygame.K_c:
                        main()

        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            
        # Update
        if (player.rect.x < 0):
            game_started = True
        all_sprites.update()
        print(f'X pos {player.rect.x}')
        # Draw / render
        screen.fill(BLACK)
        all_sprites.draw(screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()

    

if __name__ == "__main__":
    main()