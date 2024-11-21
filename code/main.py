from random import randint
import pygame
from os.path import join

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT= 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")
running = True
clock = pygame.time.Clock()

# plain surface
surf = pygame.Surface((100,200))
surf.fill("orange")
x = 100

# imports
path = join('images', "player.png")
player_surf = pygame.image.load(path).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
player_direction = pygame.math.Vector2(1, 0)
player_speed = 300

path = join('images', "star.png")
star_surf = pygame.image.load(path).convert_alpha()
star_positions = [(randint(0,WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)) for i in range (20)]

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT-20))



while running:
    dt = clock.tick() /1000
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
    
    # draw the game
    screen.fill("darkgray")
    for pos in star_positions:
        screen.blit(star_surf, pos)
    
    screen.blit(meteor_surf, meteor_rect)
    screen.blit(laser_surf, laser_rect)
    
    # player movement    
    player_rect.center += player_direction * player_speed * dt
    screen.blit(player_surf, player_rect)
    
    pygame.display.update()
    
pygame.quit()