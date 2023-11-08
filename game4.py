import pygame
import sys
import random

# import the class Fish and fishes container from the module fish
from fish import Fish, fishes
from sFish import sFish, sfishes

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 900
screen_height = 600
tile_size = 64

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Using titles and blit to draw on surface')

# initialize pygame clock
clock = pygame.time.Clock()

# load game font
custom_font = pygame.font.Font("../chomp/assets/fonts/Black_Crayon.ttf", 50)

text = (custom_font.render("Chomp", True, (255,69,0)))

# load tiles from assets folder into surfaces
def draw_background(screen):
    water = pygame.image.load("../chomp/assets/sprites/water.png").convert()
    sand = pygame.image.load("../chomp/assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../chomp/assets/sprites/seagrass.png").convert()

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

    # Draw the text at the center of the display. Note that the text object is indeed a surface.
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, 0))

background = screen.copy()
draw_background(background)

for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, 2 * screen_width), random.randint(tile_size, screen_height - tile_size)))

for _ in range (5):
    sfishes.add(sFish(random.randint(-screen_width, 0), random.randint(tile_size, screen_height - tile_size)))



# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0,0))

    fishes.update()
    sfishes.update()

    #if any fish/sfish

    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, 2 * screen_width), random.randint(tile_size, screen_height - tile_size)))

    for sfish in sfishes:
        if sfish.rect.x > screen_width:
            sfishes.remove(sfish)
            sfishes.add(sFish(random.randint(-screen_width, 0), random.randint(tile_size, screen_height - tile_size)))

    fishes.draw(screen)
    sfishes.draw(screen)

    # Update the display
    pygame.display.flip()

    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()