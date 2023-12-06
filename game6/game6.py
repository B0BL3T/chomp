import pygame
import sys
import random
import time
from player import Player
from game_parameters import *
from utilities import draw_background, add_fish

# import the class Fish and fishes container from the module fish
from fish import Fish, fishes

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Using blit to draw tiles")

# Load the sound effects
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
tune = pygame.mixer.Sound("../assets/sounds/we_have_time.ogg")
clock = pygame.time.Clock()

pygame.mixer.Sound.play(tune, -1)

# initialize pygame clock
clock = pygame.time.Clock()

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
background = screen.copy()
draw_background(background)

# place fish off the right side of the screen in random positions
add_fish(5)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# initialize score and a custom font to display it
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)

def draw_welcome(screen):
    game_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 64)
    text = game_font.render("Welcome to Chomp", True, (155, 155, 155))
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - text.get_height() / 2))

draw_mess = True

if draw_mess:
    screen.blit(background, (0,0))

    draw_welcome(screen)

    pygame.display.flip()
    time.sleep(5)


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

    result = pygame.sprite.spritecollide(player, fishes, True)
    if result:
        score += len(result)
        # play chomp sound
        pygame.mixer.Sound.play(chomp)
        #add new fish
        add_fish(len(result))

    # if any fish have moved off the left side of the screen, remove them
    # and add a new fish off the right side of the screen

    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(SCREEN_WIDTH + TILE_SIZE * 2,
                    random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))

    # draw game objects
    fishes.draw(screen)
    player.draw(screen)

    #draw the score in the upper left corner
    text = score_font.render(f"{score}", True, (255, 69, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() -10, 0 ))

    # Update the display
    pygame.display.flip()

    clock.tick(60)
    if pygame.time.get_ticks() > 60000: # 1 min
        if score >= TO_WIN:
            won = "You Won!"
        else:
            won = "You Lost!"
        running = False

if won != "":
    res_text = custom_font.render(won, True, (255,69,0))
    screen.blit(res_text, ((SCREEN_WIDTH - text.get_width())/2, SCREEN_HEIGHT/2))
    pygame.display.flip()
    time.sleep(5)


# Quit Pygame
pygame.quit()
sys.exit()