from random import randint, uniform
import pygame
from os.path import join

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
        self.direction = pygame.math.Vector2()
        self.speed = 300

        #cooldown
        self.can_shot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400
        
        
       
    def laser_timer(self):
        if not self.can_shot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shot = True


    def update(self, dt):
        # input
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt
        
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shot:
            Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        
        self.laser_timer()

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0,WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)))

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf,pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
        
       
        
    def update(self, dt):
        self.rect.centery -= 400*dt
        if self.rect.bottom < 0:
            self.kill()
        
            
class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.create_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(uniform(-0.5,0.5),1)
        self.speed = randint(400, 500)
        
        
        
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.create_time >= self.lifetime:
            self.kill()
            
def collisions():
    global running
    collision_sprites = pygame.sprite.spritecollide(player, meteor_sprites, True, pygame.sprite.collide_mask)
    if collision_sprites:
        running = False
    
    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()

def display_score():
    current_time = pygame.time.get_ticks() //100
    text_surf = font.render(str(current_time), True, (240,240,240))
    text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT - 50))
    pygame.draw.rect(screen, (240,240,240), text_rect.inflate(20,10).move((0,-8)), 5, 10) 
    screen.blit(text_surf, text_rect)

# general setup
pygame.init() 
WINDOW_WIDTH, WINDOW_HEIGHT= 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")
running = True
clock = pygame.time.Clock()

# import
meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
star_surf = pygame.image.load(join('images', "star.png")).convert_alpha()
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
font = pygame.font.Font(join('images', 'Oxanium-bold.ttf'), 40)


# sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)

# custom events -. meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


while running:
    dt = clock.tick() /1000

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x,y = (randint(0,WINDOW_WIDTH), randint(-200 ,-100))
            Meteor(meteor_surf, (x,y) , (all_sprites, meteor_sprites))

    # update
    all_sprites.update(dt)
    collisions()

    # draw the game
    screen.fill("#3a2e3f")
    all_sprites.draw(screen)
    
    display_score()
    
    
    pygame.display.update()

pygame.quit()