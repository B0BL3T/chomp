import pygame
import sys
import random


# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 900
screen_height = 600
tile_size = 64

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Using titles and blit to draw on surface')

# load tiles from assets folder into surfaces
def draw_background(screen):
    water = pygame.image.load("../assets/sprites/water.png").convert()
    sand = pygame.image.load("../assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()

    # use the png transparency
    water.set_colorkey((0,0,0))
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    # fill the screen with water
    for x in range(0,screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x,y))
        xpos = random.randint(0, screen_width)
        screen.blit(seagrass, (xpos, screen_height - 1.75 * tile_size))
        screen.blit(sand, (x, screen_height - tile_size))

# # draw sand at bottom
# for x in range(0, screen_width, tile_size):
#     screen.blit(sand, (x,screen_height - tile_size))
#
# for x in range(0, screen_width, tile_size):
#     xpos = random.randint(0, screen_width)
#     screen.blit(seagrass, (xpos, screen_height - 1.75 * tile_size))

background = screen.copy()
draw_background(background)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0,0))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()