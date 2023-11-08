import pygame
import random
from game_parameters import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("../assets/sprites/puffer_fish.png").convert()
        self.image = pygame.transform.flip(self.image, True, False)

        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.center = (x,y)

        self.speed = random.uniform(ENEMY_SPEED_MIN, ENEMY_SPEED_MAX)
    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

enemies = pygame.sprite.Group()
