import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 900
screen_height = 600

# Colors
blue = (0, 0, 255)
brown = (150, 75, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Blue Background with Brown Rectangle')

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the screen with blue
    screen.fill(blue)

    # Draw the brown rectangle at the bottom
    rectangle_height = 100
    pygame.draw.rect(screen, brown, (0,screen_height - rectangle_height, screen_width, rectangle_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()