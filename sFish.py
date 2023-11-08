import pygame
import random

MIN_SPEED = 0.5
MAX_SPEED = 3

class sFish(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("../chomp/assets/sprites/green_fish.png").convert()
        #self.image = pygame.transform.flip(self.image, True, False)

        # scale image if need by getting and multiplying current size
        imgsize = self.image.get_size()
        newsize = (imgsize[0] * .5, imgsize[1] * .5)
        self.image = pygame.transform.scale(self.image, newsize)

        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.center = (x,y)

        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
    def update(self):
        self.x += self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

sfishes = pygame.sprite.Group()