import pygame
from math import *
from game_parameters import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self ,x, y, angle):
        super().__init__()
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, BULLET_WIDTH, BULLET_HEIGHT)
        self.x = x
        self.y = y
        self.angle = angle

    def update(self, player):
        # Move the bullet up the screen
        self.x += BULLET_SPEED * cos(self.angle)
        self.y -= BULLET_SPEED * sin(self.angle) # note the negative


        # Update the rect position
        self.rect.x, self.rect.y = self.x, self.y

    def draw_bullet(self, screen):
        # Draw the bullet to the screen
        pygame.draw.rect(screen, BULLET_COLOR, self.rect)

bullets = pygame.sprite.Group()