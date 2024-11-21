from random import randint
import pygame
from os.path import join

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT= 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")
running = True

# plain surface
surf = pygame.Surface((100,200))
surf.fill("orange")
x = 100

# importing an image
path = join('images', "player.png")
player_surf = pygame.image.load(path).convert_alpha()

path = join('images', "star.png")
star_surf = pygame.image.load(path).convert_alpha()
star_positions = [(randint(0,WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)) for i in range (20)]



while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
    
    # draw the game
    screen.fill("darkgray")
    for pos in star_positions:
        screen.blit(star_surf, pos)
    x += 0.1
    screen.blit(player_surf, (x,150))
    
        
    pygame.display.update()
    
pygame.quit()