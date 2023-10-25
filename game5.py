import pygame
import sys
import random
from fish import Fish, fishes
from player import Player
from game_parameters import *
from utilities import draw_background

# import the class Fish and fishes container from the module fish
from fish import Fish, fishes

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Using blit to draw tiles")

# initialize pygame clock
clock = pygame.time.Clock()

background = screen.copy()
draw_background(background)

# place fish off the right side of the screen in random positions
for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2),
    random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))

# spawn in player
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Screen dimensions
screen_width = 900
screen_height = 600
tile_size = 64


# load game font
custom_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 50)
text = (custom_font.render("Chomp", True, (255,69,0)))

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

    # Draw the text at the center of the display. Note that the text object is indeed a surface.
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, 0))

background = screen.copy()
draw_background(background)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # control player with arrow keys
        player.stop()  # always start from no motion state
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # move player up if event key is up
                player.move_up()
            if event.key == pygame.K_DOWN:  # move player down if event key is down
                player.move_down()
            if event.key == pygame.K_LEFT:  # move player left if event key is left
                player.move_left()
            if event.key == pygame.K_RIGHT:  # move player right if event key is right
                player.move_right()

    screen.blit(background, (0,0))

    # update game objects
    fishes.update()
    player.update()

    #if any fish

    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(SCREEN_WIDTH + TILE_SIZE * 2,
                    random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))

    # draw game objects
    fishes.draw(screen)
    player.draw(screen)

    # Update the display
    pygame.display.flip()

    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()