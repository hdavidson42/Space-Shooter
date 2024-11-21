import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT= 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("test")
running = True

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
    
    # draw the game
    screen.fill("red")
    pygame.display.update()
    
pygame.quit()