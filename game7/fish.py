import pygame
import random
from game_parameters import *

class Fish(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("../assets/sprites/green_fish.png").convert()
        self.image = pygame.transform.flip(self.image, True, False)

        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.center = (x,y)

        self.speed = random.uniform(FISH_SPEED_MIN, FISH_SPEED_MAX)
    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

fishes = pygame.sprite.Group()
